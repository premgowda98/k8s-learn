## RBAC

To check access `kubectl auth can-i get pod`
To check the role `kubectl auth whoami`

### Steps to bind the role

#### Create Role

1. Create the user using proceducre inside *certificates/* directory
2. Once created, check this user has access to get pods `kubectl auth can-i get pods --as mycsr`.
3. **mycsr** is the name provided in *certificates/csr.yml*
4. There are 2 types of API groups
    1. Core Group
    2. Named Group
5. To get roles `kubectl get role`
6. Roles are namespace scoped

#### Create Binding

1. Apply *binding.yml*
2. `kubectl get rolebinding`
3. Now check `kubectl auth can-i get pods --as mycsr`.

1. Now in the kubeconfig the context can be created for the user.
2. `kubectl config get-contexts` displays all the context
3. We have copied the kube config to this directory and added the user and the context as well.
4. `kubectl --kubeconfig=sample-kube-config config get-contexts`
5. Now it will display 2 contexts
6. To set the context use `kubectl config set-context usercontext@mycsr`

## ClusterRoles

1. These roles are cluster scoped
2. Creating clusterroles and biniing is simillar to roles.

## Service Account

Used by applications. Example Prometheus, DataDog, Jenkins etc. can use service account to access the k8s resources.
Each SA is bound to kubernetes namespace and getsa a default SA

When ever the service account is created. Its token, secrets will be avaibale to each pod as mount at this location `/var/run/secrets/kubernetes.io/serviceaccount`.

This location can be found in MountSecerts field inside `kubectl describe <pod name>`

`kubectl get sa` displays all service accounts

Create new serviceaccount `kubectl apply -f sa.yml`
Create a token for ServiceAccount

## Image Pull Secrets

1. In order to pull docker images from private registry
2. `kubectl create secret docker-registry regcred --docker-server=docker.io --docker-username=premgowda --docker-password=password --docker-email=prem@gmail.com --dry-run=client -o yaml `
3. The value of the .dockerconfigjson field is a base64 representation of your Docker credentials.
4. But it can be decode using `echo "base64 string" | base64 -d`
5. And the output is 

```json
{"auths":{"docker.io":{"username":"premgowda","password":"password","email":"prem@gmail.com","auth":"cHJlbWdvd2RhOnBhc3N3b3Jk"}}}
```

This secret has to used when pulling images from private repository









