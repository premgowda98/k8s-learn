from fastapi import FastAPI
import uvicorn
import socket
import os

import http.client

class HTTPSConnectionManager:
    def __init__(self, host):
        self.host = host
        self.connection = None

    def __enter__(self):
        self.connection = http.client.HTTPConnection(self.host)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()

url = os.getenv("BACKEND_URL")

app = FastAPI()

@app.get("/")
def test():
    ip = socket.gethostbyname(socket.gethostname())
    return f"payment from {ip}"


@app.get("/backend")
def backend():
    with HTTPSConnectionManager(url) as conn:

        conn.request("GET", "/")

        response = conn.getresponse()

        data = response.read()
    return data.decode()


if __name__=="__main__":
    print(f"Backend URl is {url}")
    uvicorn.run("main:app", port=8502, host="0.0.0.0")