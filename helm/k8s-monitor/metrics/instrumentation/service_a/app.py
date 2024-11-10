import os
import logging
import random
import time
import asyncio
from fastapi import FastAPI, Request, Response, HTTPException
from prometheus_client import Counter, Histogram, Summary, Gauge, generate_latest, REGISTRY
import requests
from dotenv import load_dotenv

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Logger configuration
logger = logging.getLogger('app')
logging.basicConfig(level=logging.INFO)

# Prometheus metrics
http_request_counter = Counter(
    'http_requests_total',
    'Total number of HTTP requests',
    ['method', 'path', 'status_code']
)

request_duration_histogram = Histogram(
    'http_request_duration_seconds',
    'Duration of HTTP requests in seconds',
    ['method', 'path', 'status_code'],
    buckets=[0.1, 0.5, 1, 5, 10]  # Define buckets for histogram
)

request_duration_summary = Summary(
    'http_request_duration_summary_seconds',
    'Summary of the duration of HTTP requests in seconds',
    ['method', 'path', 'status_code'],
)

# Gauge for async task duration
gauge = Gauge(
    'node_gauge_example',
    'Example of a gauge tracking async task duration',
    labelnames=['method', 'status']
)

# Configure the OpenTelemetry Tracer
def configure_tracer():
    # Set the tracer provider globally
    trace.set_tracer_provider(
        TracerProvider(
            resource=Resource.create({SERVICE_NAME: "fastapi-jaeger-service"})
        )
    )

    # Create the Jaeger exporter
    jaeger_exporter = JaegerExporter(
        agent_host_name=os.getenv('OTEL_EXPORTER_JAEGER_HOST'),  # Jaeger agent host
        agent_port=os.getenv('OTEL_EXPORTER_JAEGER_PORT', 6831)  # Jaeger agent default port
    )

    # Add the Jaeger exporter to the tracer provider
    trace.get_tracer_provider().add_span_processor(
        BatchSpanProcessor(jaeger_exporter)
    )

configure_tracer()
FastAPIInstrumentor.instrument_app(app)
RequestsInstrumentor().instrument()

# Function to simulate async task duration
async def simulate_async_task():
    random_time = random.random() * 5  # Random time between 0 and 5 seconds
    await asyncio.sleep(random_time)

# Middleware for metrics tracking
@app.middleware("http")
async def add_metrics(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    method = request.method
    path = str(request.url.path)
    status_code = response.status_code

    # Track request metrics
    http_request_counter.labels(method=method, path=path, status_code=status_code).inc()
    request_duration_histogram.labels(method=method, path=path, status_code=status_code).observe(duration)
    request_duration_summary.labels(method=method, path=path, status_code=status_code).observe(duration)
    return response

# Example route to check service health
@app.get("/")
async def root():
    return {"status": "🏃- Running"}

@app.get("/healthy")
async def healthy():
    return {"name": "👀 - Observability 🔥- Prem Gowda", "status": "healthy"}

@app.get("/serverError")
async def server_error():
    raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/notFound")
async def not_found():
    raise HTTPException(status_code=404, detail="Not Found")

# Route to log messages
@app.get("/logs")
async def logs():
    logger.info("Here are the logs")
    logger.info("Please have a look")
    logger.info("This is just for testing")
    return {"objective": "To generate logs"}

# Simulate a crash by raising an exception
@app.get("/crash")
async def crash():
    logger.error("Intentionally crashing the server...")
    raise Exception("Crash simulated")

# Async example task with gauge
@app.get("/example")
async def example(request: Request):
    end_gauge = gauge.labels(method=request.method, status="completed").set(0)
    await simulate_async_task()
    end_gauge.set(1)
    return {"message": "Async task completed"}

@app.get("/external")
def request_call():
    url = "https://jsonplaceholder.typicode.com/posts/1"  # Example external API (JSONPlaceholder)
    
    # Make a synchronous GET request using the requests library
    response = requests.get(url)
    
    # If the request was successful, return the response data
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data", "status_code": response.status_code}

# Prometheus metrics route
@app.get("/metrics")
async def metrics():
    return Response(content=generate_latest(REGISTRY), media_type="text/plain")

# Start the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3001)