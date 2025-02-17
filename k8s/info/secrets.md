## Scerets Management

1. Kubeernets native secrets has encrypted in base64
2. They are not very safe and hard to manage
3. Insted Vault Secrets Operator or External Secrets Operator can be used to inject secrets.
4. VSO vs ESO
    1. Former is by Harshicorp Vault and tightly coupled
    2. Latter supports many key vault sytems like AKS, Vault etc.

### ESO

1. 2 CRDs needed
    1. SecretStore
        1. Providers are specified here like AWS Secret Manager, Azure KV, HarshiCorp Vault
    2. ExternalSecret
        1. SecretRef from here need to point to SecretStore
        2. Target Secret has to be created.
        3. Also Specifies how often should secrets be pulled
    3. The above 2 are Namespace Scoped, if CLuster Scoped is required use ClusterSecretStore and ClusterExternalSecret
2. Synchronizes the secrets from external API to kubernetes