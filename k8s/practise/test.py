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

with HTTPSConnectionManager("localhost:8501") as conn:

    conn.request("GET", "/")

    response = conn.getresponse()

    data = response.read()

print(data.decode())