## Internal Pod Networking

1. The k8s config in this directory has 2 containers
2. Both the containers running in same pod
3. But User container is exposed and Auth container is not exposed
4. Since both the containers are in same pod, User can communicate with auth using `localhost`
5. Also is Auth is not exposed, separate service is not created

