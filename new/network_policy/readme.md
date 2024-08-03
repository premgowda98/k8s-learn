## Network Policy

Network policy helps is controlling the network incoming (ingress) and outgoing (egress) between resources

CNI provids th networking for resources inside kuberenetes

Type of CNI
1. Weave-net
2. Flannel
3. Calico
4. Cillium

## Example

<img src="https://private-user-images.githubusercontent.com/40286378/353423860-c7d2c77f-e12d-488b-8158-f7d2b3d4d10a.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjI2MDY4MjIsIm5iZiI6MTcyMjYwNjUyMiwicGF0aCI6Ii80MDI4NjM3OC8zNTM0MjM4NjAtYzdkMmM3N2YtZTEyZC00ODhiLTgxNTgtZjdkMmIzZDRkMTBhLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA4MDIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwODAyVDEzNDg0MlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWQyYjY1MWY2ZTAzNmI3ODc3ODFkMjFlNzNlY2FlNDM3NTcwMzU0OWEwZDZhZjExZjFjYWM1Njc5OWQ5YzFhMTcmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.Zb2ggIZbm9HlB41rmYzw-oJj-9aaPnq-YWY5Ld0XbWM" width=500>

1. Application is present inside the mainfest.yml
2. Now log into frontend and try to ping the backend and database.
3. In order to ping the db, install telnet. `apt-get update && apt-get install telnet`
4. ping db `telbet db 3306`

### Apply networking

1. `kubectl explain networkpolicy`
2. In podSelector use the labels of the srvice associated with the pod.
3. `kubectl get netpol`
4. After applying the network policy, try to ping database from the frontend, and you should not be able to ping it.
