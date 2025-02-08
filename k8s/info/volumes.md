## Volumes


### emptyDir

1. Ephmeral type of volumes can be defined using emptyDir in spec
    1. These volumes exists only till the pod exists

### CSI (Container Storage Interface)

1. It bridges between kubernetes and the storage systems like AWS, Azure and others

### PVC

1. It sugests k8s to claim a volume using CSI
2. In the spec we can specify the storageClass we need, like managed in case if k8s hosted in cloud

### ConfigMaps

1. Are also volumes and they are read-only

### Secrets

1. Are also volumes, but encrypted
2. Datas are base64 encoded