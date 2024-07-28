## Implementing Independent Pod Communication

1. Here 3 Pods will be created Auth, User and Tasks
2. Independent pods will not be able to reach by service but only by cluster
3. Create different deployments for user and auth 
4. Create different service for user and auth 
5. The `LoadBalancer` type in service object will expose port to public.
6. Inorder to communicate with different pods, change this to `ClusterIP` type in service object.
7. **Note**: Change this to only auth service, since we don't want that to be publicy exposed

#### Okay, Now how to connect to auth service from user service.

1. We cannot connect with `localhost` since containers are in different pods
2. Two ways to slove this problem
    1. Manual Way
        1. First apply deployments of auth 
            ```bash
            kubectl apply -f=auth-deployment.yaml,auth-service.yaml
            ```
        2. Get Cluster IP of auth service
            ```bash
            kubectl get services
            ```
        3. Copy ClusterIP and paste it in user-deployment env variable.
    2. Automated Way
        1. Every time service is created, Kuberentes will automatically exposes those ClusterIP as environment variables
        2. So inside the application (code) we can use
            ```nodejs
            process.env.AUTH_SERVICE_SERVICE_HOST
            ```
        3. Here first we have capticalise the service name and then add `_SERVICE_HOST`
    3. 3rd Way
        1. Kubernetes mains DNS names inside a cluster `kubectl get namespaces`
        2. We can acces this qith this url `<service-name>.default`
        3. So now in our user deployment file, under env varibales for value we can use `auth-service.default`