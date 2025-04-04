## Certificates

[Resource](https://youtu.be/puiM8HZ3v_8?list=PLZorYoZY3amclAf4Wg9n7PJQbGsq5cSDw)

1. Just like certificate for https connection between the client and server.
2. Certificates are required for communication between client, api server and again from api server to other componenets like kubelete, etcd, scheduler, control manager.

### Steps for adding certificate to the cluster

1. The user has to run the following commands.
2. `openssl genrsa -out adam.key 2048` to generate a key
3. `openssl req -new -key adam.key -out adam.csr -subj "/CN=adam"` to generate a CSR (Certificate signing request)
4. Create a certificate yaml file. `kubectl explain CertificateSigningRequest`
5. In the **request** field inside spec, paste the **CSR**.
6. But this should be base64 encoded. To encode to base64, `cat adam.csr | base64 | tr -d "\n"`
7. Apply the yaml file `kubectl apply -f csr.yml` Here we are requesting certificate for client `kubernetes.io/kube-apiserver-client`
8. View certificate `kubectl get csr`
9. `kubectl describe csr/mycsr`
10. To approve the certificate `kubectl certificate approve mycsr`
    1. I am able to to this because, i am kubernetes admin.
    2. If I create a user using roles in k8s, then they will not be able to approve this request
11. Now we need to get the certificate for the user and then again decode and give it to the user who requested the certificate. Then they can use this to connect to the cluster using kubectl. `kubectl get csr mycsr -o yaml > issuedcert.yml`
12. Copy the key from request field and then `echo "paste value" | base64 -d` and share this to the user
13. Also using the certificate create, user.crt which will be required when setting context and running commands.
14. `kubectl get csr mycsr -o jsonpath='{.status.certificate}' | base64 --decode | tr -d "\n" > mycsr.crt`
15. This certificate will be valid only for 1 day, because in csr.yml when we requested for acess using CSR and key we set those to 86400.  

