## Services

### ClusterIP

1. Only pods inside the container can communicate and no external traffic can send request to pod.

### NodePort

1. Port will be open on all the nodes in the cluster no matter where the pod is running
2. Not to be used, since conflicts can occur, if 2 pods using same IP

### LoadBalancer

1. When specifid it creates a external LoadBalancer, example like creating load balancer on aws/azure
2. In local kubernetes cluster, this will be empty waiting to create loadbalancer.
3. In this case **MetalLB** load balancer can used

### Ingress

1. Works with COntroller and inress CRDs for application to be exposed
2. Will have single load balancer created externally
3. Request Flow External LB -> Ingress Service -> IngressController -> App Service -> App Pod
4. The IngressController will know the IP address of the app service, since we will be deploying Ingress resource
5. This Ingress resource will communicate to the IngressController

### Gateways

Gateway API is a collection of resources that model service networking in kubernetes

1. Unlike Ingress which is a single resource, gateways are multiple resources
2. Gateway resource should mention which GatewayClass to use.
3. Gateway has a Route resource which is like Ingress Resource which will have destination rules
4. 3 Main Components
    1. Gateway Classes -> simmilar to IngressClass (Nginx, Trafeik) and StorageClass
    2. Gateway -> Describes how traffic can be translaed to services within cluster, simillar to Ingress like LoadBalacner
    3. Routes -> Defines protocol specific rules for mapping requests from a gateway to kubernetes service
5. Gateway Classes must be installed, but on cloud it will be pre installed and we just need CRDs to use them
