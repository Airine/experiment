FROM ubuntu:latest

WORKDIR /app

RUN apt-get update && apt-get install -y \
    bmon \
    python3 \
    python3-pip \
    && pip3 install speedtest-cli

CMD /bin/bash ./start.sh
