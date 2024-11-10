## Volumes

<img src="https://private-user-images.githubusercontent.com/40286378/355082705-dfe93e1e-e5d2-447a-a3da-ee2391b1b73a.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjQ1NjI5MDYsIm5iZiI6MTcyNDU2MjYwNiwicGF0aCI6Ii80MDI4NjM3OC8zNTUwODI3MDUtZGZlOTNlMWUtZTVkMi00NDdhLWEzZGEtZWUyMzkxYjFiNzNhLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA4MjUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwODI1VDA1MTAwNlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTBjNGU0YWY5ODllZjQxYzMzNmUxZjFjNWFmZjIyMzFhNGFlNWE5YTk0YzU5ZTMxNTRiYzE4ZDU1NTU2MGIzNWImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.SOuR4o4y2SZPZlNp3tYBNqJs1D7AMKSEnboRwjmcS64" width=500>

1. PVC - Persistent volume claim
2. The PVC should be matched with policies of PV
3. With this method, it cannot be used for multi node clusters
4. For this we need to use StorageClass


Absolutely! Let's start with a quick overview of **StorageClass** and **PersistentVolume** (PV), then move to **PersistentVolumeClaim** (PVC) and how they all work together in Kubernetes, especially in the context of local storage.

### **1. What is a StorageClass?**
A **StorageClass** in Kubernetes provides a way to define different types of storage that can be dynamically provisioned. It abstracts the underlying storage infrastructure, allowing you to use different kinds of storage backends (like AWS EBS, GCE Persistent Disks, NFS, or local disks) without directly managing the provisioning process.

Think of a **StorageClass** as a template for how Kubernetes will provision storage. For example, it specifies which provisioner to use and what options are required (like the volume type or performance settings).

#### Key Concepts:
- **Provisioner**: The provisioner is the component that determines how the storage is created. For example, `kubernetes.io/aws-ebs` is used to create AWS EBS volumes, and `kubernetes.io/no-provisioner` can be used for **local storage** where you manually create PersistentVolumes.
- **Parameters**: StorageClasses often contain parameters to configure the underlying storage (e.g., IOPS settings for block storage, performance tiers, etc.).
- **ReclaimPolicy**: Defines what happens to the storage when the PVC is deleted. Typically, this is either `Retain`, `Recycle`, or `Delete`.

#### Example of a **StorageClass** for local storage:

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: local-storage
provisioner: kubernetes.io/no-provisioner  # No dynamic provisioning; uses manually created PVs
volumeBindingMode: WaitForFirstConsumer  # Wait until a pod is scheduled to bind to the volume
```

- **`provisioner: kubernetes.io/no-provisioner`**: This tells Kubernetes not to dynamically provision storage. Instead, you manage the actual local storage resources (e.g., disks, directories) on the nodes.
- **`volumeBindingMode: WaitForFirstConsumer`**: This ensures that the PV will not be bound to a pod until the pod is scheduled onto a node, ensuring the local storage is correctly matched to the node the pod will run on.

You can create this StorageClass first (if it doesn't exist) to use local storage.

### **2. What is a PersistentVolume (PV)?**
A **PersistentVolume** (PV) is a representation of actual physical storage in your Kubernetes cluster. The PV is provisioned by an administrator and describes the storage resource that exists within the cluster.

- **Manual vs Dynamic Provisioning**: If you're using a **StorageClass** with dynamic provisioning (like `kubernetes.io/aws-ebs`), Kubernetes automatically creates the PV for you. For **local storage**, you'll need to manually create the PV because it doesn't automatically provision local disks.
  
#### Example of a **PersistentVolume** for local storage:

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: elasticsearch-pv
spec:
  capacity:
    storage: 10Gi  # Size of the volume
  volumeMode: Filesystem
  accessModes:
    - ReadWriteOnce  # Only one pod can write to this volume
  persistentVolumeReclaimPolicy: Retain  # Keep the data when the PVC is deleted
  storageClassName: local-storage  # Refers to the StorageClass you created earlier
  local:
    path: /mnt/disks/elasticsearch  # Path to the local storage directory on the node
  nodeAffinity:
    required:
      nodeSelectorTerms:
        - matchExpressions:
            - key: kubernetes.io/hostname
              operator: In
              values:
                - <node-name>  # Specify the node where the local disk is available
```

- **`path: /mnt/disks/elasticsearch`**: Specifies the local disk path on the node.
- **`nodeAffinity`**: Ensures the PV is bound to a specific node (since it's a local disk on that node).
- **`storageClassName: local-storage`**: Ensures that the PV uses the `local-storage` StorageClass.

This PV needs to be created **before** the PVC, as the PVC will bind to an available PV that matches the `storageClassName` and other criteria (like node affinity).

### **3. What is a PersistentVolumeClaim (PVC)?**
A **PersistentVolumeClaim** (PVC) is a request for storage by a user. It is like a "claim" on the physical storage resources, specifying how much storage is needed, and the `StorageClass` to use.

When you create a PVC, Kubernetes will look for a matching PV that satisfies the request. If it finds a match, it binds the PVC to that PV.

#### Example of a **PVC**:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: elasticsearch-pvc
spec:
  accessModes:
    - ReadWriteOnce  # This PVC will be used by one pod at a time
  resources:
    requests:
      storage: 10Gi  # The amount of storage requested
  storageClassName: local-storage  # Matches the PV StorageClass
```

- **`accessModes: ReadWriteOnce`**: This means only one pod can write to this volume.
- **`resources.requests.storage: 10Gi`**: This specifies the amount of storage you need for your application.
- **`storageClassName: local-storage`**: Ensures the PVC is matched with a PV that uses the `local-storage` StorageClass.

**Important Note**: When you use Helm to install Elasticsearch, the chart will automatically create a **PVC** for you as part of the `volumeClaimTemplate`. You don't usually need to manually define a PVC unless you have custom storage requirements.

### **4. Flow of Storage in Kubernetes**
1. **Create a StorageClass**: This defines the type of storage you want to use (in this case, local storage).
2. **Create a PersistentVolume (PV)**: The PV represents the actual local storage (disk or directory) on a node.
3. **Create a PersistentVolumeClaim (PVC)**: This is a request for storage, and the PVC binds to a matching PV.
4. **Helm Chart for Elasticsearch**: When deploying with Helm, the chart will automatically create the PVC based on the `volumeClaimTemplate` and the `storageClassName` you provide.

### **5. Example of How to Use This in Your Case**
1. **Create the `StorageClass`** for local storage (if it doesn't exist).
2. **Create the `PersistentVolume` (PV)** that points to a directory on your node (e.g., `/mnt/disks/elasticsearch`).
3. **Run the Helm command** to install Elasticsearch. It will create a **PVC** that requests storage from the local PV.

Here’s the full process for local storage:

### Step-by-Step:

#### 1. Create the StorageClass for Local Storage:

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: local-storage
provisioner: kubernetes.io/no-provisioner
volumeBindingMode: WaitForFirstConsumer
```

```bash
kubectl apply -f local-storageclass.yaml
```

#### 2. Create the PersistentVolume:

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: elasticsearch-pv
spec:
  capacity:
    storage: 10Gi
  volumeMode: Filesystem
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: local-storage
  local:
    path: /mnt/disks/elasticsearch  # Update this path as per your system
  nodeAffinity:
    required:
      nodeSelectorTerms:
        - matchExpressions:
            - key: kubernetes.io/hostname
              operator: In
              values:
                - <node-name>
```

```bash
kubectl apply -f local-pv.yaml
```

#### 3. Install Elasticsearch with Helm (using local storage):

```bash
helm install elasticsearch \
  --set replicas=1 \
  --set volumeClaimTemplate.storageClassName=local-storage \
  --set persistence.labels.enabled=true \
  elastic/elasticsearch -n logging
```

This command will deploy Elasticsearch with **local storage** using the previously created `StorageClass` and `PersistentVolume`.

### **Conclusion:**
- **StorageClass** defines how Kubernetes provisions storage (for local storage, you'll typically use `kubernetes.io/no-provisioner`).
- **PersistentVolume (PV)** defines the actual storage on the node.
- **PersistentVolumeClaim (PVC)** is the request for storage, which binds to an available PV.

By following these steps, you'll have **local storage** set up for your Elasticsearch instance without using cloud-based storage like AWS EBS.

Let me know if you need further clarification on any of these concepts or steps!