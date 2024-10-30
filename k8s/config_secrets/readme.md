## Config Maps and Secrets

1. Instead of adding env var in the container pod spec. WE can create config map and then inject that to the pod.
2. `kubectl explain cm`
3. Creating config map. `kubectl create cm <name> --form-literal=firstname=prem --form-literal=jhbj=jvjvjg`
4. 