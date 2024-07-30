## Scaling

<img src="https://private-user-images.githubusercontent.com/40286378/348567613-684d96ca-60b7-4496-a180-dd1ab977a9bb.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjIzMTYwNTIsIm5iZiI6MTcyMjMxNTc1MiwicGF0aCI6Ii80MDI4NjM3OC8zNDg1Njc2MTMtNjg0ZDk2Y2EtNjBiNy00NDk2LWExODAtZGQxYWI5NzdhOWJiLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA3MzAlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNzMwVDA1MDIzMlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTI0MjBjNjY2MDk0ZjdjNzRjNjkwMjgxZGQyMzA0ZTJkYzg2NjQ2OTU5ZTAzZTJkNmU0NWZkNWUwM2Q3YWZkMWEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.HDkPOWI4FX3a9E6O7QDJprEAsj-dZgf-YniSUr4wMUc" width=500> 

> Note : Only HPA comes with k8s by default, rest as to be setup manually and some are though cloud providers.

### HPA (Horizontal Pod Autoscalling)

1. If the resource consumed is more due to high traffic on the pod, it automatically schedules more pods on the same node.
2. For HPA to work, metrics-serbver has to be installed.
3. `kubectl explain hpa`
4. Command to increae load manually `kubectl run -i --tty load-generator --rm --image=registry.k8s.io/busybox:1.28 --restart=Never -- /bin/sh -c "while sleep 0.01; do wget -q -O- http://php-apache; done"`
5. To see the stat use `kubectl get hpa` or `kubectl get hpa --watch`

### Vertical Pod Autoscalling

1. Here if the trafiic on the pod is incresed, teh resource allocation will be incresed say from 1GB memory to 2GB memory



