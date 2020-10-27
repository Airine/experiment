import argparse
import yaml
import os
import json

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
parser.add_argument("setting", type=str, help="file name of the setting json file")
args = parser.parse_args()
path = args.path
N = args.N
setting_file = args.setting

def new_ip(i):
    return '192.168.1.'+str(i+2)

def generate_dash_client(i):
    return {
            "image": "aljoby/selenium_docker_new:dashClientImage",
            "container_name": "dash_client_"+str(i),
            "ports" :[
                "4000:80"
            ],
            "volumes" :[
                path+"/containers/"+"container-data"+str(i)+":/usr/src/app"
            ],
            "networks": {
                "default": {
                    "ipv4_address": new_ip(i)
                }
            }
    }
    

if __name__ == "__main__":
    settings = []
    with open(path+"/"+setting_file, "r") as file:
        settings = json.load(file)

    assert len(settings) == N

    for i in range(N):
        dc["services"]["dashClient"+str(i)] = generate_dash_client(i)
    
    with open(path+"/"+"docker-compose.yml", 'w') as file:
        documents = yaml.dump(dc, file)

    os.system("mkdir containers")
    for i in range(N):
        directory = "containers/container-data"+str(i)
        os.system("mkdir "+directory)
        os.system("cp example.py "+directory+"/example.py")
        with open(directory+"/setting.json", "w") as file:
            json.dump(settings[i], file)
