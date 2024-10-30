## Authentication, Authorization

<img src="https://private-user-images.githubusercontent.com/40286378/351104905-057a58d8-537b-4dcb-96e6-ce195d1232bb.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjI1NjYyNjMsIm5iZiI6MTcyMjU2NTk2MywicGF0aCI6Ii80MDI4NjM3OC8zNTExMDQ5MDUtMDU3YTU4ZDgtNTM3Yi00ZGNiLTk2ZTYtY2UxOTVkMTIzMmJiLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA4MDIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwODAyVDAyMzI0M1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTI1Y2I5MmY0MGE3NTFmYWIxNTM2Y2U1Y2IzY2E5ZWM4N2JiMzk1NTcwNDNkYzExOTgxZDM2MDQ5OTEwOTFiYTUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.cNiuhO676QdXQ8IVbUPkQEF_N0K4BKIeVD-4JBrZK14" width=450>

1. Every time we nteract with the k8s cluster using the kubectl, the request for the resource is validated by the cluster.
2. Even through we are not manually sending these details, these are part of kube config which is ouw system.
3. If we want to use a different config file then , `kubectl get pods --kubeconfig config`
4. The default config file will be in `$HOME/.kube`
5. All the certificates of the cluster can be found at `/etc/kubernetes/pki` in the master node.