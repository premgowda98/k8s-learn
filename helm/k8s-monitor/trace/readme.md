## Jaeger

Jaeger is an open-source, end-to-end distributed tracing system used for monitoring and troubleshooting microservices-based architectures. It helps developers understand how requests flow through a complex system, by tracing the path a request takes and measuring how long each step in that path takes.

### Core Concepts of Jaeger

1. Trace: A trace represents the journey of a request as it travels through various services. Think of it as a detailed map that shows every stop a request makes in your system
2. Span: Each trace is made up of multiple spans. A span is a single operation within a trace, such as an API call or a database query. It has a start time and a duration.
3. Tags are key-value pairs that provide additional context about a span. For example, a tag might indicate the HTTP method used (GET, POST) or the status code returned.
4. Logs: Logs in a span provide details about what’s happening during that operation. They can capture events like errors or important checkpoints.
5. Context Propagation: For Jaeger to trace requests across services, it needs to propagate context. This means each service in the call chain passes along the trace information to the next service.

### Components of Jaeger

1. Jaeger consists of several components:
2. Agent: Collects traces from your application.
3. Collector: Receives traces from the agent and processes them.
4. Query: Provides a UI to view traces.
5. Storage: Stores traces for later retrieval (often a database like Elasticsearch).

## Deployment

1. We will use ElasticSearch as the db for Jaeger
2. Get ElasticSearch CA Certificate
   ```bash
   kubectl get secret elasticsearch-master-certs -n logging -o jsonpath='{.data.ca\.crt}' | base64 --decode > ca-cert.pem
   ```
3. Create Namespace `kubectl create ns tracing`
4. Create ConfigMap `kubectl create configmap jaeger-tls --from-file=ca-cert.pem -n tracing`
5. Create secret for ElasticSearch TLS `kubectl create secret generic es-tls-secret --from-file=ca-cert.pem -n tracing` and also note the Password of ElasticSearch (Refer logs-EFK)
6. Helm install
   ```bash
    helm repo add jaegertracing https://jaegertracing.github.io/helm-charts

    helm repo update
   ```
7. Install jaeger with custom values `helm install jaeger jaegertracing/jaeger -n tracing --values jaeger-values.yml`
8. While deploying jaeger, also make sure to add *OTEL_EXPORTER_JAEGER_HOST* env variable in application deployment. **ex: jaeger-agent.tracing.svc**
9. About [Jaeger](https://www.jaegertracing.io/docs/1.6/getting-started/)
10. Inorder to change the jaeger-query from ClusterIP to Nodeport refere [this](https://github.com/jaegertracing/helm-charts/tree/main/charts/jaeger)


<img src="https://camo.githubusercontent.com/db26b242c4f2b85dcb6e981132c0d95463b6abd81a934be7f40da5c170ba4732/68747470733a2f2f7777772e6a616567657274726163696e672e696f2f696d672f6172636869746563747572652d76312e706e67">