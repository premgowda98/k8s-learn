## [Setup monitoring for K8s](https://github.com/iam-veeramalla/observability-zero-to-hero/blob/main/day-2/readme.md)


1. Add prometheus repo [Link](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack)
```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```
2. `helm repo list` will list all the repos
3. The repo info is stored at `.config/helm/repositories.yml`
4. Create k8s namespace `kubectl create ns monitoring`
5. Install prometheus to monitoring namespace
```bash
helm install monitoring prometheus-community/kube-prometheus-stack \
-n monitoring \
-f ./prometheus.yml
```
6. To view the grafana dashboard using port forward `kubectl port-forward service/monitoring-grafana -n monitoring 8080:80`
7. To view Prometheus UI `kubectl port-forward service/prometheus-operated -n monitoring 9090:9090`


### Generating custom metrics for prometheus

1. Service Monitor in K8s does the service discovery of this pods are exposing the `/metrics` endpoint
2. Build the docker image for code in *Instrumentation* folder
3. Push it to private repo *registry.premgowda.in*
4. Create a secret for k8s to pull from private rpository
5. [Docker Private Registry in K8s](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/) `kubectl create secret docker-registry regcred --docker-server=<your-registry-server> --docker-username=<your-name> --docker-password=<your-pword> --docker-email=<your-email>`
6. To view secret `kubectl get secret regcred --output=yaml` and to see full details `kubectl get secret regcred --output="jsonpath={.data.\.dockerconfigjson}" | base64 --decode`
7. Add this in container section in the deployment file 
    ```bash
      imagePullSecrets:
        - name: regcred
    ```
8. Run `kubectl apply -k ./k8s` to deploy using kustomize
9. Access the application `http://<any-node-ip>:<node-port>`
10. To get NodePort use `kubectl get svc`
11. Now Search for *http_requests_total* in prometheus
12. Good you are not be able to see anything, even though you exposed */metrics* in your application
13. This is because as of now their is no service discovery assigned for prometheus
14. Add serviceMonitor to the deployment, add it in service-a folder inside k8s and then do `kubectl apply -k servic-a`, this is applying through kustomization