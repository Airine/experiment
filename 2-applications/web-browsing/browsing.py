import datetime
import requests
from urllib import request, parse
import time


def get_news():
    url = ('http://newsapi.org/v2/top-headlines?'
        'country=sg&'
        'page=1&'
        'pageSize=30&'
        'apiKey=254959c602364221be3657dce3e13a8b')
    return requests.get(url).json()


def get_related(term):
    url = ('http://newsapi.org/v2/everything?'
        'q='+term+'&'
        'sortBy=popularity&'
        'page=1&'
        'apiKey=254959c602364221be3657dce3e13a8b')
    return requests.get(url).json()


def get_rt_urllib(url):
    start_time = time.time()
    res = request.urlopen(url)
    return time.time()-start_time

def get_response_time(url):
    try:
        r = requests.get(url, timeout=6)
        r.raise_for_status()
        # respTime = str(round(r.elapsed.total_seconds(),2))
        respTime =  r.elapsed.total_seconds()
        # currDate = datetime.datetime.now()
        # currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
        # print(currDate + " " + str(respTime))
        return respTime
    except requests.exceptions.HTTPError as err01:
        print ("HTTP error: ", err01)
    except requests.exceptions.ConnectionError as err02:
        print ("Error connecting: ", err02)
    except requests.exceptions.Timeout as err03:
        print ("Timeout error:", err03)
    except requests.exceptions.RequestException as err04:
        print ("Error: ", err04)
    return -1

if __name__ == "__main__":
    url = 'https://lifehacker.com/how-to-get-your-mac-ready-to-upgrade-to-big-sur-1845644605'
    print(get_response_time(url))
    print(get_rt_urllib(url))
    # res = get_news()
    # res = get_related("cov-19")
    # with open('cov-19.txt', 'w+') as f:
    #     for article in res['articles']:
    #         url = article['url']
    #         if get_response_time(url) != -1: 
    #             f.write(url+'\n')
            # print(article['url'], get_response_time(article['url']))
