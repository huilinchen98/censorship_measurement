import timeOutList
import urllib
import time
import requests
import signal
import re
import json
import signal
import websiteList

headless = {}
timeout = 60
userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:57.0) Gecko/20100101 Firefox/57.0'

def handler(signum, frame):
    raise Exception


def useUrllib(url):
    try:
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(timeout)
        req = urllib.request.Request(url)
        req.add_header("User-Agent", userAgent)  #This line if optional. If you don't want to change the useragent, delete this
        code = urllib.request.urlopen(req).getcode()
    except Exception as ie:
        print(ie)
    signal.alarm(0)




for i in range(100):
    url = websiteList.websites[i]
    headlessStart = time.time()
    useUrllib(url)
    headlessEnd = time.time()
    headless[url] = headlessEnd - headlessStart
    print(headlessEnd - headlessStart)

with open("timeOutForVPN.txt", "w") as outfile:
    json.dump(headless, outfile, indent = 4)
    print(sum([headless[url] for url in headless])/len(headless), "avg time out")
