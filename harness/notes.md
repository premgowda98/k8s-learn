## Installation

1. Harnes has Open Source Version which an be self hosted
2. Install Harnes Manager through docker container
3. Harness also has free cloud tier
4. AroCD is more of CD toll which looks for changes in git and apply those changes
5. Harness is more compherensive toll, which has 
    1. Pipelines
    2. Environments -> namespace
    3. Services -> deployments
    4. Secrets -> secrets
    5. Connectors
6. Harness provides control on where to deply the changes
7. Harness uses ArgoCD for gitop tasks
8. ArgoCD architecture
    1. Application server
    2. Git Server
    3. Redis cache
    4. UI/CLI
9. Harness delegates are involved in running pipelines