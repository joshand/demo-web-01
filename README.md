# demo-web-01

```
docker build . --tag demo-web-01
docker run -e IMG_SVR_IP=127.0.0.1 -e IMG_SVR_PRT=8080 -d -p 8000:5000 demo-web-01
```
