## Harness

1. Harness has Open Source Version which an be self hosted
2. Install Harness Manager through docker container
3. Harness also has free cloud tier
4. AroCD is more of CD toll which looks for changes in git and apply those changes
5. Harness is more comprehensive toll, which has 
    1. Pipelines
    2. Environments -> namespace
    3. Services -> deployments
    4. Secrets -> secrets
    5. Connectors
6. Harness provides control on where to deploy the changes
7. Harness uses ArgoCD for git-ops tasks
8. ArgoCD architecture
    1. Application server
    2. Git Server
    3. Redis cache
    4. UI/CLI
9. Harness delegates are involved in running pipelines


### Key Concepts

1. Deployment
2. Service
    1. Represents a micro service
    2. Includes ServiceDefinition which contains
        1. Artifacts
        2. Manifests
        3. Variables
        4. Can be propagate and override a Service in subsequent stages
    3. Service Instance
        1. Number of instances of Service running
        2. Example, replicas of 3 in k8s will have 3 pods
3. Pipeline
    1. Pipeline is a series of Stages where each Stage deploys a Service to an Environment.
    2. Stage
        1. A Stage is a subset of a Pipeline that contains the logic to perform one major segment of the deployment process. Stages are based on the different milestones of your release process, such as dev, qa, and prod releases, and approvals.
    3. Steps
        1. Steps perform the operations like applying a manifest, asking for approval, rollback, and so on.
4. Environment
    1. Targets like dev, prod
5. Connectors
    1. Connectors contain the information necessary to integrate and work with 3rd party tools such as Git providers, artifact repos, and target infrastructure.
    2. Harness uses Connectors at Pipeline runtime to authenticate and perform operations with a 3rd party tool.
6. Delegates
    1. Is a software service you install in your environment that connects to the Harness Manager and performs tasks using your container orchestration platforms.
    2. The Delegate uses the credentials set up in the Connectors used by the Pipeline to perform deployment tasks.

### Setup

1. Prerequisites
    1. K8s Cluster
    2. K8s Manifestation
2. Install Delegates
    1. The Harness Delegate is a lightweight worker process that is installed on your infrastructure and communicates only via outbound HTTP/HTTPS to the Harness Platform.
3. Install harness cli and connect to api-key
4. Connectors
    1. K8s Connector, Github Connector
    2. Each github connector can be attached to the account or a specific repo
    3. If account is specified any repo can be pulled
5. Services
    1. Includes the service name
    2. Service Definition
        1. k8s, aws lambda, shell
        2. Includes manifests
        3. Artifacts -> registry
6. Environment
    1. Includes production or Pre Production
    2. Infrastructure Definition includes the the namespace of the k8s, vms, shell, aws lambda
        1. Requires k8s connector 
7. Pipeline
    1. Can specify pipeline with multiple stages
    2. Deploy stage can takes k8s, lambda, shell 
        1. Service has to be selected
        2. Environment has to be chosen
