## Service Mesh

1. Istio is a open source service mesh.
2. Service Mesh helps in micro-service inter communication
3. When service mesh is insalled it install a sidecar container in every pod
4. Very communication between the services will not be direct but through the *Envoy* proxy installed as sidecar
5. This support mTLS between the service communication
6. Also comes with monitoring, observability and traing out of the box.
7. L7 and L4 load balancer
8. Has Gateway and Virtual Service

## Ingress

1. In Ingress, the Controller was installed
2. And Ingress CRDs were installed in application namespace and this CRD was connected to Ingress Controller
3. This Controller routed the trafiic
4. But this does not have service to service communication
5. Supports only HTTP
6. L7 Load Balancer
7. Here Ingress Controller and Ingress CRD

## Gateway

1. Istio is making Gateway API as default traffic management
2. Support L4 and L7 load balancer
3. Here Gateway and HTTPRoute 

## Kubernetes Networking Policy

1. This can be used to allow/deny network communication between the applications
2. By default in K8s any pod can communicate with any pod.
3. But with Network Policy we can control this behaviour and they operate at L4 unlike Service Mesh which operates at L7, L4
