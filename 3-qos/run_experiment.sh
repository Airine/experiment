#!/bin/bash
./clear_data.sh
python3 generator.py `pwd` experiment.csv
sudo docker-compose up --remove-orphans