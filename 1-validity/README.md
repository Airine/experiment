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
    --gateway=192.168.1.1 \
    --aux-address="pi=192.168.1.241" \
    -o parent=enp0s25 macvlanet
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

```
apt install -y net-tools iproute2 iputils-ping iperf3 gnupg1 apt-transport-https dirmngr
export INSTALL_KEY=379CE192D401AB61
export DEB_DISTRO=$(lsb_release -sc)
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys $INSTALL_KEY
echo "deb https://ookla.bintray.com/debian ${DEB_DISTRO} main" | tee  /etc/apt/sources.list.d/speedtest.list
apt update
apt install -y speedtest

```

