# Improvement of Service Quality

Dynamic Adaptive Streaming over HTTP (DASH) provides adaptive streaming of videos. Segmented media contents are encoded in various bit rates, and are adjusted subject to the network condition. Therefore, the real-time video quality directly reflects the available quality of connection.

## Getting Started

### Set up DASH server



### Generate clients

Run the command below to generate the `docker-compose.yml` and the client folders.

```bash
python3 generator.py `pwd` 10 settings.json
```

If already exist or out of date, run `./clear_data.sh` to clean.

### Run the contianers

