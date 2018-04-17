import requests
import csv
import urllib
import time
import json
import re
import websiteList
import random
import signal
import selenium
from selenium import webdriver
from seleniumrequests import Chrome
from seleniumrequests import Firefox



timeout = 30
timeoutCode = -1
errorCode = 0
recordFormat = "Chrome/Firefox"
fileName = 'MixBrowserTest.txt'
result = []
headError = 0
headTimeout = 0
head200 = 0
headOther = 0
headlessError = 0
headless200 = 0
headlessOther = 0
headlessTimeout = 0

#class AppURLopener(urllib.FancyURLopener):
userAgent = 'Mozilla/5.0jalivneislgneixngoenfhskeigneox.gww)(uexpeuxigbe,xkgpwexitnex)'
def record(url, d, driver):
    try:
        response = driver.request('GET', url)
        code = int(re.findall('\d+', str(response))[0])
        #print(code)
        d["Status"] = code
        print(code)
        if code == 200:
            global head200
            head200 += 1
        else:
            global headOther
            headOther += 1
    except IOError as ie:
        d["Status"] = str(ie)
        global headError
        headError += 1
        #driver.close()



def handler(signum, frame):
    raise Exception


def head(url, driver):
    try:
        d = {}
        d["url"] = url
        d["time"] = time.time()
        d["browser"] = "headed"
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(timeout)
        record(url, d, driver)
    except Exception:
        d["Status"] = timeoutCode
        global headTimeout
        headTimeout += 1
        print("timtout")
    signal.alarm(0)
        #driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + Keys.NUMPAD2)
    return d


def pairRecord():
    n = 0
    for url in websiteList.websites:
        for i in range(2):
            if i == 1:
                driver = Chrome()
            else:
                driver = Firefox()
            result.append(head(url, driver))
            driver.quit()
        n = n + 1
        if n % 20 == 0:
            print(n)



pairRecord()


with open(fileName, "w") as outfile:
    output = {}
    output["measurements"] = result
    json.dump(output, outfile, indent = 4)

print("head200: " + str(head200))
print("headError: " + str(headError))
print("headTimeout: " + str(headTimeout))
print("headOther: " + str(headOther))
print("headless200: " + str(headless200))
print("headlessError: " + str(headlessError))
print("headlessTimeout: " + str(headlessTimeout))
print("headlessOther: " + str(headlessOther))
print(recordFormat)
