To build:
> docker build --platform linux/amd64 -t visr-test-backend .

To run locally:
docker run -d -p 0.0.0.0:8000:8000 visr-test-backend

To push image to DockerHub:
> docker tag visr-test-backend:latest docker.io/<username>/vist-test-backend:v2
> docker push docker.io/<username>/vist-test-backend:v3

