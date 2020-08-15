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
    -o parent=enp0s5 macvlanet
```

```bash
docker run --rm -dit \
    --network macvlanet \
    --name alpinetest \
    --ip 192.168.1.200 \
    alpine:latest \
    ash
```

