## Workload API

### Pods

1. Basic resource
2. 1 or more container
3. We cannot create this resource directly, it should be created by other resources
4. Once deleted cannot be brought back since it is not created/managed by other resource
5. When you look closely at the resource config, their is no **template** and we directly specify the **spec**.

### Replicasets

1. Ia type of resource where it is a contract between the user and kubernetes to maintain the application
2. Even if the pod fails, it will keep on trying to bring it up to abide to the contract
3. Here the container specs are wrapped inside the **template**.
4. RS has the repsobility of how to create/manage pod
5. `kubectl tree -n drivebill-dev rs drivebill-api-deployment-54775888d6` shows the hierarchy
6. `kubectl tree -n drivebill-dev deployment drivebill-api-deployment`
7. Even if one pod is deleted, RS creates another pod to maintain the defined state in the configuration
8. RS only maints the state of the template like replicas, but if we updated the spec of the container like changing the image name 
this will not trigger the RS sicne it only handles the template and not spec itself.
9. But if we want the image to be updated, then we can delete a pod, so when creating a new pod, it uses new image specified.

### Deployments

1. Configuration is same as RS
2. This solves the problem of Replicaset point 8
3. The way it does is different, it will create a new replica set and pods. Once completed it removes the old replicaset, behaving like rollling update
4. A Stateless applications has to be created with deployment resource. Because, if we specify the cvolume for this type of resource with n number of pods, then all 
the pods share the same volume. 
5. This Could be a potential problem.

### StatefulSets

1. Similar to Deployment
2. When creating volume in this resource type, their is no nedd to specify the PVC
3. This as **volumeClaimTemplates** inside which PVC can be defined.
4. This resource type will not manage pods using replicasets as in deployments, rather it directly manages the pods and their nummbers
5. Pods are numbered and they are created/deleted in order

### DaemonSets

1. Will make run sure that one pod is running in each node.

### Jobs

1. Used for short running workloads
2. RestratPolicy can be specified
3. It runs and shutdowns when the pod return exit code 0

### CronJobs

1. Can run preodically
2. It include schedule, jobTemplate


