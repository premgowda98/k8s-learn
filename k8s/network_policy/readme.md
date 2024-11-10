## Network Policy

Network policy helps is controlling the network incoming (ingress) and outgoing (egress) between resources

CNI provids the networking for resources inside kuberenetes

Type of CNI
1. Weave-net
2. Flannel
3. Calico
4. Cillium

## Example

<img src="https://private-user-images.githubusercontent.com/40286378/353423860-c7d2c77f-e12d-488b-8158-f7d2b3d4d10a.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjI2MDY4MjIsIm5iZiI6MTcyMjYwNjUyMiwicGF0aCI6Ii80MDI4NjM3OC8zNTM0MjM4NjAtYzdkMmM3N2YtZTEyZC00ODhiLTgxNTgtZjdkMmIzZDRkMTBhLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA4MDIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwODAyVDEzNDg0MlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWQyYjY1MWY2ZTAzNmI3ODc3ODFkMjFlNzNlY2FlNDM3NTcwMzU0OWEwZDZhZjExZjFjYWM1Njc5OWQ5YzFhMTcmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.Zb2ggIZbm9HlB41rmYzw-oJj-9aaPnq-YWY5Ld0XbWM" width=500>

1. Application is present inside the mainfest.yml
2. By default all the pods inside k8s can communicate with each other
3. Now log into frontend and try to ping the backend and database.
4. In order to ping the db, install telnet. `apt-get update && apt-get install telnet`
5. ping db `telbet db 3306`

### Apply networking

1. `kubectl explain networkpolicy`
2. In podSelector use the labels of the srvice associated with the pod.
3. `kubectl get netpol`
4. After applying the network policy, try to ping database from the frontend, and you should not be able to ping it.

## Ingress vs Nodeport

Yes, you can use a `NodePort` service in Kubernetes to access your pods, but `Ingress` provides more flexibility and additional features that `NodePort` doesn't offer. Let me explain the differences between the two and why `Ingress` is still required in many use cases.

### 1. **NodePort:**
   - A **NodePort** is a type of Kubernetes service that exposes a pod to external traffic by opening a specific port on each node in your cluster. 
   - When you create a `NodePort` service, Kubernetes assigns a port (usually in the range `30000-32767` by default) on each node's IP address, which routes traffic to the pod.
   - You can access your service externally by sending traffic to any of the node IPs on that assigned port.
   - **Limitations** of NodePort:
     - **Port range**: NodePorts are bound to a specific port range (`30000-32767`), so you're limited to a small set of ports (though this range can be customized).
     - **Manual management of external traffic**: You need to know the IP addresses of your nodes. If you're using a cloud provider, nodes may have dynamic IP addresses, making it hard to expose the service.
     - **Scaling issues**: If you have a large number of services or need to expose many applications, you could run out of available NodePort ports or find it hard to manage.
     - **Lack of routing**: With NodePort, you don’t have any advanced routing, load balancing, or URL path-based routing. All traffic to the NodePort goes to the same service.

### 2. **Ingress:**
   - **Ingress** is a Kubernetes resource that provides HTTP/HTTPS routing to services based on URLs, hostnames, or even paths. It allows you to define sophisticated routing rules and manage access to multiple services using a single entry point.
   - **Ingress Controller**: To use Ingress, you need to deploy an **Ingress Controller** (such as NGINX, Traefik, or HAProxy). The Ingress controller acts as a reverse proxy and routes traffic based on the Ingress rules you define.
   - **Benefits of Ingress**:
     - **Single entry point**: With Ingress, you can expose multiple services under a single external IP address (or hostname) and route traffic to the appropriate service based on the request's URL or hostname.
     - **Path-based routing**: You can create rules to route traffic to different services based on the URL path (e.g., `myapp.example.com/api` routes to one service, and `myapp.example.com/admin` routes to another).
     - **TLS termination**: Ingress controllers often support TLS termination, meaning you can configure HTTPS with a single SSL certificate, reducing the need to configure individual certificates on each service.
     - **Load balancing**: Ingress controllers can perform load balancing across multiple pods of a service, which NodePort doesn’t do by itself.
     - **URL rewrites**: Advanced routing capabilities like URL rewriting and forwarding to other services or external URLs.

### When to Use **NodePort** vs. **Ingress**:
- **NodePort** is simpler to set up and works well if you only need to expose a single service and you don’t need sophisticated routing, load balancing, or SSL/TLS termination. It’s often used in small clusters or during development.
- **Ingress** is ideal if you need to expose multiple services behind a single entry point (e.g., a single domain), need path-based or host-based routing, want centralized SSL/TLS management, or require load balancing and advanced routing features.

### Key Differences:

| Feature                        | NodePort                                | Ingress                                    |
|---------------------------------|-----------------------------------------|--------------------------------------------|
| **Access Type**                 | Exposes on a static port across all nodes in the cluster. | Exposes services via HTTP/HTTPS and routes based on rules. |
| **Port Management**             | Limited to a small range of ports (`30000-32767`). | No limitation on number of services exposed; relies on a single entry point. |
| **Routing**                     | Direct access via the Node's IP and port. | Path and hostname-based routing. |
| **Load Balancing**              | No built-in load balancing (each node is independent). | Load balancing through the Ingress controller. |
| **TLS/SSL Termination**         | Not supported by default (but can be done via other means like a reverse proxy). | Built-in support for TLS/SSL termination. |
| **Use Case**                    | Single service exposure, usually in small or development environments. | Exposing multiple services, production environments, complex routing, SSL/TLS management. |

### Why is **Ingress** Still Required?

- **Scalability**: If you need to manage many services (e.g., multiple microservices), using a `NodePort` for each one could become unwieldy. Ingress provides a more scalable solution by allowing you to route multiple services through a single entry point.
- **Routing Flexibility**: If you need to expose multiple services and route traffic based on domain names, paths, or specific HTTP request attributes, `Ingress` is the way to go.
- **Simplified Management**: Ingress controllers handle many of the complexities, like SSL termination, centralized access control, and advanced routing, making it easier to manage traffic to your Kubernetes services.
- **Better Performance**: Ingress controllers often implement advanced load balancing algorithms and optimizations, ensuring better traffic distribution across your pods.

### Conclusion:
While you **can** use `NodePort` to expose services, especially for simple use cases or small setups, **Ingress** is typically preferred for production-grade applications because it offers far more control, flexibility, and scalability for handling external access to Kubernetes services.


## CNI (Container Network Interface)

