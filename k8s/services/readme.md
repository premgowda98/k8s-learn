## Services

1. Services will let us to control the communication betweeen the users and also between the pods
2. 4 Types
    1. Cluster IP
    2. Node Port
    3. LoadBalancer
    4. External Names
3. Endpoints are the IP address of the pods
4. Service discovery -> through labels of the pods

### Nodeport

<img src="https://private-user-images.githubusercontent.com/40286378/345119908-8aa9c482-be3a-450a-95b7-0a0c0e80403e.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjIxNjgzMzMsIm5iZiI6MTcyMjE2ODAzMywicGF0aCI6Ii80MDI4NjM3OC8zNDUxMTk5MDgtOGFhOWM0ODItYmUzYS00NTBhLTk1YjctMGEwYzBlODA0MDNlLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA3MjglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNzI4VDEyMDAzM1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTg0MmRjOGUwMTMzMDMxMGQ4ZDlkM2U5NGM1NzFhYWU1YmVjNzAxMWYwMTU0NDI0YThmZTExMzJlNDhkMWQ5YTAmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.2P-hKwsvgYaisDXuv4FjAKkgheCeP7PoN-y1g9cs48o" width=350 height=250>


1. Can have ports from 30,000–32,767 which contains 2,768 ports
2. The website can be accessed at the IP address of the node (Even master node ip works).
3. Can aslo be accessed using cluster-ip
4. Also through `http://localhost:8001/api/v1/namespaces/<namespace>/services/<service-name>:<port>/proxy/`
5. When running as nodeport each, application can be accesed using node ip, pod ip, clusterip
6. How excatly Nodeport works
    1. Deployment exposes port 3000 inside the container (application listens on this port).
    2. Service maps port 80 (external service port) to targetPort 3000 (the port on the container).
    3. NodePort is assigned automatically (or specified) in the range 30000-32767.
    4. Within Kubernetes (internal access): Pods or services inside the cluster access the service by calling http://<service-name>:80, and traffic is forwarded to the container's 3000 port.
    5. External access: Outside the cluster, you access the service via http://<worker-node-ip>:<NodePort>, and the traffic is forwarded to port 80 (on the service) and then to the container's 3000 port.



### Cluster IP

This is the default used by k8s
In This type, application can be accessed using only cluster ip and not node ip