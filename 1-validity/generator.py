import argparse
import yaml
import os

dc = {
    "version": "2.0",
    "services": {},
    "networks": {
        "default": {
            "external":{
                "name": "macvlanet"
            }
        }
    }
}

parser = argparse.ArgumentParser(description='Generate docker-compose.yml from arguments.')
parser.add_argument("path", type=str, help="the full path of working directory")
parser.add_argument("N", type=int, help="number of containers")
args = parser.parse_args()
path = args.path
N = args.N

def new_ip(i):
    return '192.168.1.'+str(i+2)

def generate_dash_client(i):
    return {
            "image": "myfi-tester:1.0",
            "environment": {
                "LOGDIR": "tester"+str(i)
            },
            "volumes" :[
                path+":/app"
            ],
            "networks": {
                "default": {
                    "ipv4_address": new_ip(i)
                }
            }
    }
    

if __name__ == "__main__":

    for i in range(N):
        dc["services"]["tester"+str(i)] = generate_dash_client(i)
    
    with open(path+"/"+"docker-compose.yml", 'w') as file:
        documents = yaml.dump(dc, file)

    for i in range(N):
        os.system("mkdir tester"+str(i))
