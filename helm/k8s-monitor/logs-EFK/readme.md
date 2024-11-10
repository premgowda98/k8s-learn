## Logging

ELK Stack (Elastic Search, Fluentbit, Kibana)

1. ES for storage
2. Fluentbit to get the logs
   1. Fluentbit will be deloyed as daemon set in k8s
   2. Fluentbit vs Logstash
      1. Logstash is rich in fetaures
      2. Fluentbit is log forwareder
      3. Logstash is log aggregator
         1. Advantace filtering, labeling
3. Kibana for visualization

### Deployment

1. Create k8s namespace `kubectl create namespace logging`
2. Need to create Storage class
   1. If using Cloud then we have to just mention the storage class in helm and PV and PVC will be handled by K8s
   2. Since we are doing it locally, we have to create a Storage class and PV
   3. StorageClass is more like a template and PV is actuall pythical location  
   4. StorageClass config are in *storage-class.ynl*
   5. PV is in *pv.yml*
   6. Create a dir `/mnt/disks/elasticsearch` in one of worker node for ElsaticSearch data now i am choosing k8s-worker1
   7. `kubectl apply -f sc-pv.yml`
3. Install helm
   ```bash
   helm repo add elastic https://helm.elastic.co

   helm install elasticsearch \
   --set replicas=1 \
   --set persistence.enabled=false \
   --set persistence.existingClaim=elk-pv-claim \
   elastic/elasticsearch \
   -n logging
   ```
4. Imp points for aboce helm command
   1. We are setting persistence.enabled=false, so that we can use pre-existing PVC
   2. Also specifying the already created pvc-claim
   3. If we specify VolumeClaimTemplate when the PVC will be automatically provisioned
5. To unisntall `helm uninstall <name> -n <namespace>`
6. Get elastic login credentials
   ```bash
      # for username
      kubectl get secrets --namespace=logging elasticsearch-master-credentials -ojsonpath='{.data.username}' | base64 -d
      # for password
      kubectl get secrets --namespace=logging elasticsearch-master-credentials -ojsonpath='{.data.password}' | base64 -d
   ```
7. Install Kibanan `helm install kibana --set service.type=NodePort elastic/kibana -n logging`
8. Install fluentbit
    ```bash
    helm repo add fluent https://fluent.github.io/helm-charts
    helm install fluent-bit fluent/fluent-bit -f fluentbit-values.yaml -n logging
    ```
9. Include elasticsearch password in the fluentbit-values.yml
10. Accesss the UI of kibana which is at nodeport
