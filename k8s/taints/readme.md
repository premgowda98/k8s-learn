## Taints and Toleration

1. Taints is on Nodes and toleration is on pods
2. Example
    1. If a Node has **taint** called gpu=true
    2. Then only pods having **toleration** of having gpu=true will get deployed
3. 3 effects in toleration
    1. NoSchedule
        1. This means that no new pod will be able to schedule onto node1 unless it has a matching toleration.
    2. PreferNoschedule
        1. Soft version of *NoSchedule*
    3. NoExecute
        1. Affects already running pods
        2. Pods that do not tolerate the taint are eviced immediately
4. Command to taint `kubectl taint nodes k8s-worker1 gpu=true:NoSchedule` . View taints `kubectl describe node/k8s-worker1 | grep Taints`
5. Command to remove taint `kubectl taint nodes k8s-worker1 gpu=true:NoSchedule-`
6. Toleration can be specified  in the PodSpec
7. If pods are manually scheduled, then taints will not work.

By default no pods will get scheduled on the control-plane because it will have a taint.
If we remove this taint, then we can deploy pods on that node as well

## NodeSelector

Opposite of taints, will get deployed if labels match