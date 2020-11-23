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
    """
    i: the client id
    both dash and web browsing clients share the same function
    """
    return {
            "image": "aljoby/selenium_docker_new:dashClientImage",
            "container_name": "client_"+str(i),
            "ports" :[
                "4000:80"
            ],
            "volumes" :[
                path+"/clients/"+"client-"+str(i)+":/usr/src/app"
            ],
            "networks": {
                "default": {
                    "ipv4_address": new_ip(i)
                }
            }
    }

def generate_browser_client(i):
    return {
        "image": "myfi-browser:1.0",
        "container_name": "client_"+str(i),
        "volumes" :[
           path+"/clients/"+"client-"+str(i)+":/app"
        ],
        "networks": {
            "default": {
                "ipv4_address": new_ip(i)
            }
        }
    }

def generate_download_client(i):
    """
    i: the client id
    """
    return {
        "image": "mifi-downloader:1.0",
        "container_name": "client_"+str(i),
        "environment": {
            "LOGDIR": "client-"+str(i)
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
    settings = []
    with open(path+"/"+setting_file, "r") as file:
        settings = json.load(file)

    assert len(settings) == N

    for i in range(N):
        print(settings[i]["application"])
        client = None
        if settings[i]["application"] == "0":
            client = generate_dash_client(i)
        elif settings[i]["application"] == "1":
            client = generate_browser_client(i)
        else:
            client = generate_download_client(i)
        dc["services"]["client-"+str(i)] = client
    
    with open(path+"/"+"docker-compose.yml", 'w') as file:
        documents = yaml.dump(dc, file)

    os.system("mkdir clients")
    for i in range(N):
        directory = "clients/client-"+str(i)
        os.system("mkdir "+directory)
        
        # copy files
        if settings[i]["application"] == "0":
            os.system("cp example.py "+directory+"/example.py")
        elif settings[i]["application"] == "1":
            os.system("cp browser.py "+directory+"/browser.py")
            os.system("cp urls.txt "+directory+"/urls.txt")    
        
        with open(directory+"/setting.json", "w") as file:
            json.dump(settings[i], file)
