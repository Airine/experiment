# Validity and Effectiveness

We evaluate the effectiveness of our smart contract and WiFi controller with iPerf, which actively measures the maximum achievable bandwidth on IP networks. Emulated users submit demand for bandwidth and data burst. We then check if the received quality of connection matches the results directly derived from our allocation and pricing mechanisms.

To emulate the user, we use docker with macvlan. 

- Docker

- Macvlan

## Getting Started

### 1. Created Docker Network

```bash
docker network create -d macvlan \
    --subnet=192.168.1.0/24 \
    --gateway=192.168.1.241 \
    --aux-address="router=192.168.1.1" \
    -o parent=enp38s0 macvlanet
```

Then, run `docker network ls`. If `maclanet` shows up, the network was created successfully.

```bash
docker run --rm -dit \
    --network macvlanet \
    --name alpine-test \
    --ip 192.168.1.200 \
    alpine:latest \
    ash
```

or

```bash
docker run --rm -it \
	--network macvlanet \
	--name ubuntu-test \
	--ip 192.168.1.201 \
	ubuntu:latest \
	bash
```

### 2. Build the docker image

```bash
sudo docker build --tag mifi-downloader:1.0 .
```

### 3. Test with `docker run`

```bash
sudo docker run --rm -it --network macvlanet \             
    --name ubuntu-test \
    --ip 192.168.1.200 \
    -v /home/aaron/Documents/GitHub/wifi-lab/mifi-experiment/1-validity:/app \
    --env LOGDIR=tester1 \
    mifi-downloader:1.0
```

### 4. Run the experiment

```bash
sudo docker-compose up
```
