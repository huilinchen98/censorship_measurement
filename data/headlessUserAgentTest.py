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
from seleniumrequests import Firefox

timeout = 15
timeoutCode = -1
errorCode = 0
recordFormat = "pairPermutation"
fileName = 'userAgentTest.txt'
result = []
changedError = 0
changedTimeout = 0
changed200 = 0
changedOther = 0
headlessError = 0
headless200 = 0
headlessOther = 0
headlessTimeout = 0
userAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:55.0) Gecko/20100101 Firefox/55.0"

def handler(signum, frame):
    raise Exception

def changedUrllib(url, d):
    try:
        req = urllib.request.Request(url)
        req.add_header("User-Agent", userAgent)
        code = urllib.request.urlopen(req).getcode()
        d["Status"] = code
        if code == 200:
            global changed200
            changed200 += 1
        else:
            global changedOther
            changedOther += 1
    except IOError as ie:
        print(ie)
        if "HTTP Error" in str(ie):
            code = int(re.findall('\d+', str(ie))[0])
            d["Status"] = code
            changedOther += 1
            print(code)
        else:
            print("error")
            d["Status"] = str(ie)
            global changedError
            changedError += 1





def changedUserAgent(url):
    try:
        d = {}
        d["url"] = url
        d["time"] = time.time()
        d["userAgent"] = userAgent
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(timeout)
        changedUrllib(url, d)
    except Exception:
        d["Status"] = timeoutCode
        global changedTimeout
        changedTimeout += 1
    signal.alarm(0)
    return d






def useUrllib(url, d):
    try:
        r2 = urllib.request.urlopen(url)
        code = r2.getcode()
        d["Status"] = code
        if code == 200:
            global changed200
            changed200 += 1

        else:
            global headlessOther
            headlessOther += 1
    except IOError as ie:
        print(ie)
        if "HTTP Error" in str(ie):
            code = int(re.findall('\d+', str(ie))[0])
            d["Status"] = code
            headlessOther += 1
            print(code)
        else:
            print("error")
            d["Status"] = str(ie)
            global headlessError
            headlessError += 1




def headless(url):
    try:
        d = {}
        d["url"] = url
        d["time"] = time.time()
        d["userAgent"] = "default"
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(timeout)
        useUrllib(url, d)
    except Exception:
        d["Status"] = timeoutCode
        global headlessTimeout
        headlessTimeout += 1
    signal.alarm(0)
    return d





def pairRecord():
    n = 0
    for url in websiteList.websites:
        print(url)
        for i in range(3):
            block = []
            sequence = [0, 1]
            random.shuffle(sequence)
            if sequence[0] == 0:
                block.append(changedUserAgent(url))
                block.append(headless(url))
            else:
                block.append(headless(url))
                block.append(changedUserAgent(url))
            result.append(block)
        n = n + 1
        if n % 20 == 0:
            print(n)

if(recordFormat == "pairPermutation"):
    pairRecord()
else:
    sixPairs()

with open(fileName, "w") as outfile:
    output = {}
    output["measurements"] = result
    json.dump(output, outfile, indent = 4)

print("head200: " + str(changed200))
print("headError: " + str(changedError))
print("headTimeout: " + str(changedTimeout))
print("headOther: " + str(changedOther))
print("headless200: " + str(headless200))
print("headlessError: " + str(headlessError))
print("headlessTimeout: " + str(headlessTimeout))
print("headlessOther: " + str(headlessOther))
print(recordFormat)
