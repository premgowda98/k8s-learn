## Scaling

<img src="https://private-user-images.githubusercontent.com/40286378/348567613-684d96ca-60b7-4496-a180-dd1ab977a9bb.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjIzMTYwNTIsIm5iZiI6MTcyMjMxNTc1MiwicGF0aCI6Ii80MDI4NjM3OC8zNDg1Njc2MTMtNjg0ZDk2Y2EtNjBiNy00NDk2LWExODAtZGQxYWI5NzdhOWJiLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA3MzAlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNzMwVDA1MDIzMlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTI0MjBjNjY2MDk0ZjdjNzRjNjkwMjgxZGQyMzA0ZTJkYzg2NjQ2OTU5ZTAzZTJkNmU0NWZkNWUwM2Q3YWZkMWEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.HDkPOWI4FX3a9E6O7QDJprEAsj-dZgf-YniSUr4wMUc" width=500> 

> Note : Only HPA comes with k8s by default, rest as to be setup manually and some are though cloud providers.

### HPA (Horizontal Pod Autoscaling)

1. If the resource consumed is more due to high traffic on the pod, it automatically schedules more pods on the same node.
2. Metrics server is need for hpa to work `kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml`
3. To make metrics work without tls, run the following command
   ```bash
   kubectl edit deployment metrics-server -n kube-system
   ```
   and add the following line in the container args
   ```yaml
   - --kubelet-insecure-tls
   ```
    and save the file.
4. For HPA to work, metrics-serbver has to be installed.
5. `kubectl explain hpa`
6. Command to increae load manually `kubectl run -i --tty load-generator --rm --image=registry.k8s.io/busybox:1.28 --restart=Never -- /bin/sh -c "while sleep 0.01; do wget -q -O- http://php-apache; done"`
7. To see the stat use `kubectl get hpa` or `kubectl get hpa --watch`

### How HPA Interacts with Resource Configuration

HPA makes scaling decisions based primarily on resource configurations in your Deployment:

1. **Resource Metrics Monitoring**:
   - HPA uses the metrics-server to collect CPU utilization data
   - It calculates utilization based on the **request** values, not limits
   - Example: For a pod with `requests: cpu: 200m`, HPA monitors percentage of 200m used

2. **Scaling Decisions**:
   - If HPA target is 50% CPU utilization and requests are 200m:
     - Target consumption = 100m CPU per pod
     - If actual usage exceeds 100m, HPA scales up
     - If actual usage drops below 100m (and stays down), HPA eventually scales down

3. **Scaling Calculation**:
   - `desired replicas = ceil(current replicas * (current utilization / target utilization))`
   - Example: If 1 pod is using 180m CPU (90% of request) with 50% target:
     - 1 * (90% / 50%) = 1.8, rounded up to 2 pods

4. **Request vs Limit Roles**:
   - **Requests**: Used by HPA for scaling decisions and by scheduler for pod placement
   - **Limits**: Enforce maximum resource usage but don't influence HPA directly
   - The gap between request and limit gives pods room to handle load spikes while HPA is catching up

5. **Memory Configuration**:
   - While our example focuses on CPU, HPA can also scale based on memory usage
   - Memory-based autoscaling works the same way, comparing actual memory usage against the requested amount

6. **Best Practices**:
   - Set realistic request values that represent actual application needs
   - Configure limits higher than requests to allow for temporary spikes
   - Choose your target utilization percentage based on application behavior
     - CPU-bound apps might use 50-70%
     - Less predictable apps might use lower targets like 30-40%

Understanding this relationship helps you fine-tune your autoscaling behavior to match your application's needs.

### Vertical Pod Autoscaling

1. Here if the traffic on the pod is increased, the resource allocation will be increased say from 1GB memory to 2GB memory



