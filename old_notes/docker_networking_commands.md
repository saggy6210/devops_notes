https://codingcompiler.com/docker-interview-questions-answers/

Docker Network:

> Create & run a ngnix container and run in detach(background) mode: 
docker container run -p 80:80 -d --name webhost nginx

> get Logs 
docker container logs mywebhost

> To get process ID
docker container top mywebhost

> Get list of docker containers 
docker container ls

> Get docker container ip address:
docker container inspect --format '{{.NetworkSettings.IPAddress}}

> Create & run mysql container
docker container run -d -p 3306:3306 --name db -e MYSQL_RANDOM_ROOT_PASSWORD=y mysql
docker container logs db
docker ps

> Create & run apache tomcat server
docker run -d -p 8080:80 --name webhost1 httpd

> Get container configuration details 
docker container inspect mysql

> Login into container with interactive mode
docker container -it exec mysql bash

> to get private IP address of ngnix server with inspect command
docker inspect --format="{{ .NetworkSettings.IPAddress }}" mywebhost

> To get port getting used
docker container port mywebhost

> Create network
docker network create my_net

> Create new nginx server withing network by using existing image
docker container run -d --name new_webhost --network my_net nginx

> Connect & discoonect to network
docker network connect my_net mywebhost
docker network disconnect my_net mywebhost

> ping from one container to another, got error as ping does not exist
docker container exec -it mywebhost ping new_webhost
OCI runtime exec failed: exec failed: container_linux.go:344: starting container process caused "exec: \"ping\": executable file not found in $PATH": unknown

> Solution: 
1. docker container exec -it mywebhost bash -c "echo $PATH"
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

2. docker container exec -it mywebhost bash
$apt -get update
$apt-get install iputils-ping

then try again : docker container exec -it mywebhost ping new_webhost

> Docker Compose template:

version: '1.0'

services:
  servicename:
    image: 
	command:
	environement:
  
  servicename2:
  
  volumes:
  networks:
------------------------------------------------------------------------------------------------------------------------------------------------------------------

Docker
https://www.toptal.com/docker/interview-questions

1. What is Docker?
Docker is an open-source lightweight containerization technology.

2. Explain Docker Swarm?

Docker Swarm is native gathering for docker which helps you to a group of Docker hosts into a single and virtual docker host

3. What is Docker hub?

Docker hub is a cloud-based registry that which helps you to link to code repositories. 

4. What is Hypervisor?

The hypervisor allows you to create a virtual environment in which the guest virtual machines operate. It controls the guest systems and checks if the resources are allocated to the guests as necessary.

5. What is CNM?

CNM stands for Container Networking Model.


6. What is the default Docker network driver, and how can you change it when running a Docker image?
Docker provides different network drivers like bridge, host, overlay, and macvlan. bridge is the default.

docker network create network-name

7. What is Docker Swarm and which network driver should be used with it?

Docker Swarm is an open-source container orchestration tool that is integrated with the Docker engine and CLI. If you want to use Docker Swarm, you should use the overlay network driver. Using an overlay network enables the Swarm service by connecting multiple docker host daemons together.


8. What is the difference between CMD & entrypoint? Done
CMD sets default command and/or parameters, which can be overwritten from command line when docker container runs.

ENTRYPOINT configures a container that will run as an executable.

9. What is the difference between ADD & COPY instruction? Done
COPY only lets you copy in a local file or directory from your host (the machine building the Docker image) into the Docker image itself.
ADD: you can use a URL instead of a local file / directory. Secondly, you can extract a tar file from the source directly into the destination. Resources from remote URLs are not decompressed.

10. What is docker compose?  Done
Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration.


11. what is use of docker save & docke load command ?  Done
docker save – Save one or more images to a tar archive. Contains all parent layers, and all tags + versions.
FROM busybox
CMD echo $((40 + 2))
docker save calc > calc.tar
tree calc

docker load – Load an image or repository from a tar archive. It restores both images and tags
docker load < calc.tar

12. What are a Docker container’s possible states, and what do they mean? done
created:  A container that has been created (e.g. with docker create) but not started
restarting:  A container that is in the process of being restarted
running:  A currently running container
paused:  A container whose processes have been paused
exited: A container that ran and completed ("stopped" in other contexts, although a created container is technically also "stopped")
dead:  A container that the daemon tried and failed to stop (usually due to a busy device or resource used by the container)

Status codes:

200 – no error
400 – bad parameter
500 – server error

13. Difference between RUN & CMD? done
RUN lets you execute commands inside of your Docker image. These commands get executed once at build time and get written into your Docker image as a new layer.

CMD lets you define a default command to run when your container starts.

14. difference between dockerfile and docker image? 
A Dockerfile is a file that you create which in turn produces a Docker image when you build it.
A Dockerfile is a recipe for creating Docker images
A Docker container is a running instance of a Docker image
