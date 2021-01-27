import os
import logging
import json
from urllib import request

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep, time

logging.getLogger().setLevel(logging.INFO)

BASE_URL = 'http://172.28.176.237/dash.js/samples/dash-if-reference-player/index.html'


def dash(t):
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

    dc = DesiredCapabilities.CHROME
    dc['goog:loggingPrefs'] = { 'browser':'ALL' }
    logging.info('Prepared desired capabilities..')

    #new
    chrome_driver = '/usr/bin/chromedriver'
    chrome_user_dir = '/usr/src/app/chrome_user_dir_real/'
    chrome_options.add_argument('--user-data-dir=' + chrome_user_dir)
    chrome_options.add_argument('--ignore-certificate-errors')

    browser = webdriver.Chrome(chrome_driver, chrome_options=chrome_options, desired_capabilities=dc)
    logging.info('Initialized chrome browser..')

    browser.get(BASE_URL)
    sleep(t)
    # browser.save_screenshot('shd1.png')
    logging.info('Accessed %s ..', BASE_URL)

    logging.info('Page title: %s', browser.title)

    logging.info('Processing log..')
    init_delay = None
    start = None
    current_quality = 1
    switches = 0
    chunks = 1
    total_quality = 0
    stalls = 0

    with open('log.txt','w+') as f:
        for entry in browser.get_log('browser'):
            msg = ' '.join(entry['message'].split(' ')[2:])

            if not init_delay:
                if '[PlaybackController]' in msg:
                    if 'play ' in msg:
                        start = int(msg.split(' ')[-2])
                    elif 'playing' in msg:
                        init_delay = (int(msg.split(' ')[-2]) - start)/1000
            
            if '[ScheduleController][video] OnFragmentLoadingCompleted' in msg:
                chunks += 1
                total_quality += current_quality
                f.write('\n' + str(chunks) + ',' + msg[msg.find('Range:')+6:-2] + ',' + str(current_quality) + ',' + str(switches) + ',')

            if '[PendingIndexMetrics]' in msg:
                switches += 1
                current_quality = int(msg.split(' ')[-1])
            if '[IndexMetrics]' in msg:
                current_quality = int(msg.split(' ')[-1])
            
            if '[Metrics]' in msg:
                f.write(','.join(msg.split(' ')[-5:])+',')

            if '[HttpMetrics]' in msg:
                f.write(','.join([i.strip('"') for i in msg.split(' ')[-3:]])+',')
            
            if 'stalled' in msg:
                stalls += 1
        
            # f.write(' '.join(msg.split(' ')[2:])+'\n')
        avg_quality = total_quality/chunks

        # average quality, number of switches, number of stalls, initial delay
        f.write('\n'+str(avg_quality)+','+str(switches)+','+str(stalls)+','+str(init_delay)+'\n')
        qoe = 0.25 * avg_quality - 0.25 * switches - 0.25 * stalls - 0.25 * init_delay
        f.write('QoE:'+str(qoe))
        n_qoe = 0.7 * avg_quality * chunks / 35 - 0.05 * switches - 0.1 * stalls - 0.15 * init_delay
        f.write('\nNew QoE:'+str(n_qoe))

    browser.quit()
    display.stop()

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

        sleep(30) # sleep for 10 seconds to synchronize
        
        dash(30)