## Deployment

1. Using deployment, replicaset can be managed
2. In replicaset, if we change an image version it will try to create all at once, which can cause some downtime to application
3. Whereas in Deploytment, the updates will be done in rooling fashion, where each pod will be updated sequentially
4. Rollback is easy
5. A single Deployment in Kubernetes is designed to manage a set of identical Pods.

1. `kubectl describe deployment`
2. `kubectl rollout history deploy/nginx-deploy` will list out the hostory of rollouts
3. `kubectl rollout undo deploy/nginx-deploy`

Quick way to generate a template 
`kubectl create deploy deploy/new-nginx --image=nginx --dry-run=client -o yaml > dp-temp.yml`