## Replication Controller

1. To get the current version of replication controller use `kubectl explain rc`
3. `kubectl get pods -o wide` to see where the pods are allocated
2. `kubectl get rc` to get the replication present
3. `kubectl delete rc/nginx-rc`

## Replicaset

Replication controller is the legacy version, the new verison is replicationset

1. To get the current version of replication controller use `kubectl explain rs`
2. With replication controller, only pods created by it can be managed.
3. But using replication sewt we can manage the pods which are not created by it.
    1. The other pods can be selected using selector, using match labels.
4. `kubectl delete rs/nginx-rs`
5. Other way to edit replicas is `kubectl scale --replicas=3 -f rs.yml`