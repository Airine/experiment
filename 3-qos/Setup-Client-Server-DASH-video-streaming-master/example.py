import os
import logging

from pyvirtualdisplay import Display
from selenium import webdriver
from time import sleep

logging.getLogger().setLevel(logging.INFO)
# BASE_URL = 'http://10.10.10.22/dash/samples/dash-if-reference-player/t1.html'
BASE_URL = 'http://reference.dashif.org/dash.js/nightly/samples/dash-if-reference-player/index.html'

#BASE_URL = 'http://www.example.com/'


def chrome_example():
    display = Display(visible=0, size=(800, 1600))
    display.start()
    logging.info('Initialized virtual display..')

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')

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
    sleep(5)
    browser.save_screenshot('shd1.png')
    logging.info('Accessed %s ..', BASE_URL)

    logging.info('Page title: %s', browser.title)

    browser.quit()
    display.stop()


def firefox_example():
    display = Display(visible=0, size=(800, 600))
    display.start()
    logging.info('Initialized virtual display..')

    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference('browser.download.folderList', 2)
    firefox_profile.set_preference('browser.download.manager.showWhenStarting', False)
    firefox_profile.set_preference('browser.download.dir', os.getcwd())
    firefox_profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')

    logging.info('Prepared firefox profile..')

    browser = webdriver.Firefox(firefox_profile=firefox_profile)
    logging.info('Initialized firefox browser..')

    browser.get(BASE_URL)
    logging.info('Accessed %s ..', BASE_URL)

    logging.info('Page title: %s', browser.title)

    browser.quit()
    display.stop()


def phantomjs_example():
    display = Display(visible=0, size=(800, 600))
    display.start()
    logging.info('Initialized virtual display..')

    browser = webdriver.PhantomJS()
    logging.info('Initialized phantomjs browser..')

    browser.get(BASE_URL)
    logging.info('Accessed %s ..', BASE_URL)

    logging.info('Page title: %s', browser.title)

    browser.quit()
    display.stop()




if __name__ == '__main__':
    chrome_example()
    #firefox_example()
    #phantomjs_example()
