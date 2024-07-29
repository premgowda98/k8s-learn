## Scheduler

1. Scheduler on the control plane, will decide about placement of pod in a node
2. Once request got from the client, it logs in etcd and then communicate kubectl to create the pods
3. In fact scheduler is itself a pod `kubectl get pod -n kube-system | grep sched`
4. Maunal scheduling can be done using **nodeName**
    1. In this case, even if the scheduler is down, the pod gets scheduled
    2. This is because we are doing manual scheduling

## Static pods

1. Pods running on the control plane
2. These pods are not controlled by **scheduler**
3. The configurtaion of teh static pods are presetn in `/etc/kubernetes/manifests` folder in master node
    1. These contians `etcd.yaml  kube-apiserver.yaml  kube-controller-manager.yaml  kube-scheduler.yaml`

## Labels and Selectors

1. Labels can be at 3 levels
    1. Deployment level
    2. Pod level (Within template)
2. Selector
    1. Will match the label of the pod with the deployment
    2. 2 Types
        1. matchLabels
        2. matchExprssions -> In, NotIn, Exists, DoesNotExist

`kubectl get pods --selector env=demo`


