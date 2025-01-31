## Private Registry

1. `sudo apt install apache2-utils -y`
2. `htpasswd -Bc registry.password username` inside auth folder
3. For self signed Certificate
    1. cretae openssl.conf
```bash
    [req]
default_bits        = 2048
prompt               = no
default_keyfile      = server.key
distinguished_name   = req_distinguished_name
x509_extensions      = v3_ca

[req_distinguished_name]
countryName          = IN
stateOrProvinceName  = Karnataka
localityName         = Bengaluru
organizationName     = Drivebill
commonName           = 192.168.0.112

[v3_ca]
subjectAltName       = @alt_names

[alt_names]
IP.1 = 192.168.0.112

```
    2. `openssl req -x509 -newkey rsa:2048 -keyout registry.key -out registry.crt -days 365 -config openssl.conf`
    3. `openssl rsa -in server.key -out server.key.nopass` this removes the key phrase from .key file which is required by docker registry
    3. Copy the .crt file to this location `/usr/local/share/ca-certificates/`
    4. Then do `sudo update-ca-certificates`

```bash
services:
  registry:
    image: registry:2
    container_name: registry
    ports:
      - "5000:5000"
    volumes:
      - ./data:/var/lib/registry
      - ./auth:/auth
      - ./certs/registry.crt:/etc/ssl/certs/registry.crt
      - ./certs/registry.key:/etc/ssl/private/registry.key
    restart: always
    environment:
      REGISTRY_HTTP_ADDR: 0.0.0.0:5000
      REGISTRY_AUTH: htpasswd
      REGISTRY_AUTH_HTPASSWD_REALM: Registry
      REGISTRY_AUTH_HTPASSWD_PATH: /auth/registry.password
      REGISTRY_HTTP_TLS_CERTIFICATE: /etc/ssl/certs/registry.crt
      REGISTRY_HTTP_TLS_KEY: /etc/ssl/private/registry.key
      REGISTRY_STORAGE_DELETE_ENABLED: 'true'

  registry-ui:
    image: joxit/docker-registry-ui:main
    restart: always
    ports:
      - 5001:80
    environment:
      - SINGLE_REGISTRY=true
      - REGISTRY_TITLE=Docker Registry UI
      - DELETE_IMAGES=true
      - SHOW_CONTENT_DIGEST=true
      - NGINX_PROXY_PASS_URL=https://registry:5000
      - SHOW_CATALOG_NB_TAGS=true
      - CATALOG_MIN_BRANCHES=1
      - CATALOG_MAX_BRANCHES=1
      - TAGLIST_PAGE_SIZE=100
      - REGISTRY_SECURED=false
      - CATALOG_ELEMENTS_LIMIT=1000
    container_name: registry-ui
```