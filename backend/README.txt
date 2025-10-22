To run locally:
> docker build -t visr-test-backend . && docker run -d -p 0.0.0.0:8000:8000 visr-test-backend


To push image to DockerHub:
> docker tag visr-test-backend:latest docker.io/mattrncar/vist-test-backend:v2
> docker push docker.io/mattrncar/vist-test-backend:v2

