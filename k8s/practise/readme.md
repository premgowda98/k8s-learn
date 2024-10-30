## Practise

```yml
spec:
    containers:
    - name: mybackend
    image: "docker.io/premgowda98/backend:latest"
    ports:
    - containerPort: 8501
    imagePullPolicy: Always
    env:
    - name: PAYMENT_URL
        value: "localhost:8502"
    - name: mypayment
    image: "docker.io/premgowda98/payment:latest"
    ports:
    - containerPort: 8502
    imagePullPolicy: Always
    env:
    - name: BACKEND_URL
        value: "localhost:8501"
```

1. Containers within same spec will be inside the same pod
2. Hence call be called using `localhost`