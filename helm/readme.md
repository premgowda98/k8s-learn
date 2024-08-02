## Helm Chart

<div style="display: flex; flex-direction: column; align-items: center; gap: 20px;">

<div style="display: flex; gap: 10px;">

<img src="https://ctf-cci-com.imgix.net/4mpa9wPxoZ8GeAFCpoaryl/9b70f6c2bcd6a93f4692ed3806c4e30e/2023-03-16-image2.png?ixlib=rb-3.2.1&w=2000&auto=format&fit=max&q=60&ch=DPR%2CWidth%2CViewport-Width%2CSave-Data" width=400>

<img src="https://assets.cloudacademy.com/bakery/media/uploads/entity/blobid1-ed9f8e01-0402-4fcd-887f-25b8f50888f2.png" width=400 style="background: white;">

</div>

<div>
<img src="../static/helm-arch.png" width=400 style="background: white;">
</div>

</div>


Helm is widely known as "the package manager for Kubernetes". 

### Install 

```bash
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

### Helloworld

```bash
helm create helloworld
```