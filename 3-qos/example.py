import os
import logging
import json
from urllib import request, parse

from pyvirtualdisplay import Display
from selenium import webdriver
from time import sleep

logging.getLogger().setLevel(logging.INFO)

BASE_URL = 'http://172.28.176.237/dash.js/samples/dash-if-reference-player/index.html'


def chrome_example():
    display = Display(visible=0, size=(800, 1310))
    display.start()
    logging.info('Initialized virtual display..')

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--autoplay-policy=no-user-gesture-required')

    chrome_options.add_experimental_option('prefs', {
        'download.default_directory': os.getcwd(),
       'download.prompt_for_download': False,
    })
    logging.info('Prepared chrome options..')

    #new
    chrome_driver = '/usr/bin/chromedriver'
    chrome_user_dir = '/usr/src/app/chrome_user_dir_real/'
    chrome_options.add_argument('--user-data-dir=' + chrome_user_dir)
    chrome_options.add_argument('--ignore-certificate-errors')
    f= open("guru99.txt","w+")

    browser = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
    logging.info('Initialized chrome browser..')

    browser.get(BASE_URL)
    sleep(20)
    browser.save_screenshot('shd1.png')
    logging.info('Accessed %s ..', BASE_URL)

    logging.info('Page title: %s', browser.title)

    browser.quit()
    display.stop()


def request_bandwidth():
    with open("setting.json", "r") as file:
        data = json.load(file)
        params = json.dumps(data).encode("utf8")
        req = request.Request("http://192.168.1.241:5000/", data=params, headers={'content-type': 'application/json'})
        res = request.urlopen(req)
        print(res.read().decode('utf8'))


if __name__ == '__main__':
    request_bandwidth()
    sleep(5)
    chrome_example()