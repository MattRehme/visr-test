To test locally with Docker:

* Ensure Docker Desktop is running
> docker compose up --build                                              
* Connect to- http://localhost:8080/  



To push containers to DockerHub:

map-viewer> docker compose up --build
> docker tag backend <username>/backend:vX
> docker push <username>/backend:vX
> docker tag frontend <username>/frontend:vX
> docker push <username>/frontend:vX


