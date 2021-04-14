## Application with example helm
### Python/Flask application

Project structure:
```
.
├── _helm
    └── flask-helm
├── app
    └── app.py
    └── wsgi.py
├── nginx
    └── default.conf
├── docker-compose.yaml
├── Dockerfile
├── requirements.txt
```

## Deploy with docker-compose

```
$ docker-compose up -d
Starting flask_helm_web_1 ... done
Starting flask_helm_nginx_1 ... done
```

## Expected result

Listing containers must show one container running and the port mapping as below:
```
$ docker ps
CONTAINER ID   IMAGE                                 COMMAND                  CREATED          STATUS          PORTS                                                                                                                                  NAMES
a57753c23e10   flask_helm_nginx                      "/docker-entrypoint.…"   41 minutes ago   Up 30 seconds   0.0.0.0:80->80/tcp                                                                                                                     flask_helm_nginx_1
b882bda83119   flask_helm_web                        "gunicorn -w 4 -t 60…"   42 minutes ago   Up 31 seconds   0.0.0.0:8000->8000/tcp  
```

After the application starts, navigate to `http://127.0.0.1:8000` in your web browser or run:
```
$ curl 127.0.0.1:8000
Flask application running properly!
```

Stop and remove the containers
```
$ docker-compose down
```

## Deploy with kubernetes

```
$ helm install flask-helm _helm/flask-helm/ --values _helm/flask-helm/values.yaml
```
