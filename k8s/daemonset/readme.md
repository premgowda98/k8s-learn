## Daemonset

1. Replicaset will create n pods across different nodes, not distributed evenly
2. Daemonset will create 1 pod in each and every node. avaliable
3. Uses
    1. Monitoring agent
    2. Logging agent
    3. kube-proxy
    4. Networking
4. `kubectl explain daemonset`
56. But this pod will not be deployed on master node / control panel beacuse of **taints**

`kubectl get ds --all-namespaces`

## [Cronjob](https://www.hostinger.in/tutorials/cron-job)

`kubectl explain cronjob`

<img src="https://www.hostinger.com/tutorials/wp-content/uploads/sites/2/2021/09/crontab-syntax.webp">

## Job

`kubectl explain cronjob`

Runs only once