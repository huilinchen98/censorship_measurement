import timeOutList
from seleniumrequests import Firefox
import urllib
import time
import signal
import re
import json
import signal

headed = []
headless = []
timeout = 60

def handler(signum, frame):
    raise Exception

def record(url, driver):
    try:
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(timeout)
        response = driver.request('GET', url)
        code = int(re.findall('\d+', str(response))[0])
    except Exception as ie:
        print(ie)
    signal.alarm(0)


def useUrllib(url):
    try:
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(timeout)
        r2 = urllib.request.urlopen(url)
        code = r2.getcode()
    except Exception as ie:
        print(ie)
    signal.alarm(0)





driver = Firefox()
for url in timeOutList.timeOutList:
    print(url)
    headStart = time.time()
    record(url, driver)
    headEnd = time.time()
    headed.append(headEnd - headStart)
    print(headEnd - headStart)
    headlessStart = time.time()
    useUrllib(url)
    headlessEnd = time.time()
    headless.append(headlessEnd - headlessStart)
    print(headlessEnd - headlessStart)

with open("timelist.txt", "w") as outfile:
    output = {}
    output["headed"] = headed
    output["headless"] = headless
    json.dump(output, outfile, indent = 4)
