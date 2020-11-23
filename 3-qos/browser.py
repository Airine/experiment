import logging
import json
from time import sleep, time
from urllib import request
import requests


logging.getLogger().setLevel(logging.INFO)

def get_response_time(url):
    try:
        r = requests.get(url, timeout=6)
        return r.elapsed.total_seconds()
    except Exception as e:
        logging.error(e)
    return -1

def web_browsing(t):
    with open('urls.txt', 'r') as file:
        urls = file.readlines()
        start_time = time()
        with open('log.txt','w+') as f:
            total_resp_time = 0
            n_url = 0
            while time() - start_time < t:
                if len(urls) < 1:
                    break
                url = str(urls.pop()).strip('\n')
                resp_time = get_response_time(url)
                f.write(str(n_url)+','+str(resp_time)+'\n')
                total_resp_time += resp_time
                n_url += 1
                # sleep(2)
            avg_resp_time = total_resp_time/n_url
            f.write('avg,'+str(avg_resp_time)+'\n')


def request_bandwidth(data):
    params = json.dumps(data).encode('utf8')
    req = request.Request('http://192.168.1.241:5000/', data=params, headers={'content-type': 'application/json'})
    res = request.urlopen(req)
    logging.info(res.read().decode('utf8'))


if __name__ == '__main__':
    exp_time = 30
    with open('setting.json', 'r') as file:
        data = json.load(file)
        request_bandwidth(data)

        sleep(5) # sleep for 5 seconds to synchronize
        
        web_browsing(30)