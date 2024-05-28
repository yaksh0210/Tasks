# COMMAND TO RUN THE TASK

### Build images

> 1) docker build -t container1 -f Dockerfile.network1 .
> 2) docker build -t container2 -f Dockerfile.network2 .
> 3) docker build -t container3 -f Dockerfile.network3 .


### Create networks

> 1) docker network create --subnet=172.19.0.0/16 net1
> 2) docker network create --subnet=172.20.0.0/16 net2
> 3) docker network create --subnet=172.21.0.0/16 net3

### Run containers

> 1) docker run --network=net1 --ip=172.18.0.2 --name=container1 -d container1
> 2) docker run --network=net2 --ip=172.19.0.2 --name=container2 -d container2
> 3) docker run --network=net3 --ip=172.20.0.2 --name=container3 -d container3

### Verifying ping process

> 1) docker exec container1 ping -c 4 172.19.0.2
> 2) docker exec container2 ping -c 4 172.20.0.2
> 3) docker exec container3 ping -c 4 172.21.0.2

