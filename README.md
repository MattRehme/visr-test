To test locally with Docker:

* Ensure Docker Desktop is running
> docker compose up --build                                              
* Connect to- http://localhost:8080/  



To push containers to DockerHub:

map-viewer> docker compose up --build
> docker tag map-viewer-backend <username>/map-viewer-backend:v1
> docker push <username>/map-viewer-backend:v1
> docker tag map-viewer-frontend <username>/map-viewer-frontend:v1
> docker push <username>/map-viewer-frontend:v1


