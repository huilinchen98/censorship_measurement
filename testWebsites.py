'''This test measures the number of different response code for selenium and Urllib.
We group all the responses into 4 categories: 200, timeout, error and Other. 200 means
the status code we got is 200。 Other means we got the reponses code but it's not 200. Timeout
means the access exceeded the time limit we set. Error means the access throws eror by Selenium
or Urllib.

 We are using 2 kinds of recording Formats, called matched pairs and full randomization
 For the first, matched pairs, we randomized the sequence of using Selenium and urllib.
 We repeated this randomized pair 3 times. The second one, full randomization,
 we randomized the 6 accesses, 3 for urllib and 3 for Selenium.
 For each of the tests mentioned below we run it in both of these two formats to see
 if we find any major difference.

NOTE: since I didn't put the functions into a class, it might be easier to understand
if reading the functions from bottom to top. I'm sorry for the inconvience
'''



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



timeout = 15                 #the default timeout is 15 seconds
timeoutCode = -1
errorCode = 0
recordFormat = "Matched Pair"
fileName = '6th.txt'
result = []
#variables for Selenium
headError = 0
headTimeout = 0
head200 = 0
headOther = 0
#variables for Urllib
headlessError = 0
headless200 = 0
headlessOther = 0
headlessTimeout = 0

#class AppURLopener(urllib.FancyURLopener):
userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:57.0) Gecko/20100101 Firefox/57.0'   # this is the user agent we want for headless browser


'''We call this function to save information in dictionry for a single headed browser access, and return the dictionry
   See the function below for detailed comment.
'''
def infoForHeaded(url, d, driver):
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


'''We call this function to save information in a dictionary for a single headless browser access, and return the dictionry
'''
def infoForHeadless(url, d):
    try:
        d["url"] = url                #we add the information we want to save into dictionary
        d["time"] = time.time()
        d["browser"] = "headless"
        req = urllib.request.Request(url)
        req.add_header("User-Agent", userAgent)  #This line if optional. If you don't want to change the useragent, delete this
        code = urllib.request.urlopen(req).getcode()  #get the response code from headless browser
        d["Status"] = code    # add code to dictionary
        print(code)
        if code == 200:
            global headless200
            headless200 += 1   # update the global variable to see how many total number of each kind of response we have
        else:
            global headlessOther
            headlessOther += 1
    except IOError as ie:      # if the response code is not 200, (i.e. 404, 405) or an error occurs, urllib will throw ieError
                               # an error can occur when the website link is broken.
        print(ie)
        if "HTTP Error" in str(ie):
            code = int(re.findall('\d+', str(ie))[0])  #we catch the error message and extract the response code from it
            d["Status"] = code
            headlessOther += 1
            print(code)
        else:
            print("error")             #if it's an error, we save this access as error.
            d["Status"] = str(ie)
            global headlessError
            headlessError += 1


#time out hanlder, required for signal
def handler(signum, frame):
    raise Exception



def head(url, driver):
    try:
        d = {}
        d["url"] = url
        d["time"] = time.time()
        d["browser"] = "headed"
        signal.signal(signal.SIGALRM, handler)   #we use signal package to set timeout for a single access
        signal.alarm(timeout)
        infoForHeaded(url, d, driver)
    except Exception:                             #exception raised means that it's timeout
        d["Status"] = timeoutCode
        global headTimeout
        headTimeout += 1
        print("timtout")
    signal.alarm(0)                               #reset the signal if it's not timedout
    return d



def headless(url):
    try:
        d = {}
        d["url"] = url
        d["time"] = time.time()
        d["browser"] = "headless"
        signal.signal(signal.SIGALRM, handler)   #we use signal package to set timeout for a single access
        signal.alarm(timeout)
        infoForHeadless(url, d)
    except Exception:                            #exception raised means that it's timeout
        d["Status"] = timeoutCode
        global headlessTimeout
        headlessTimeout += 1
    signal.alarm(0)                               #reset the signal if it's not timedout
    return d


'''function for pair permutation
'''
def pairRecord():
    driver = Firefox()
    time.sleep(4)       #wait for 4 secons to open FirFox
    n = 0
    for url in websiteList.websites:    #For each website
        print(url)
        for i in range(3):
            block = []
            sequence = [0, 1]
            random.shuffle(sequence)    # we suffle the sequence list to determine which broswer we are runing first
            if sequence[0] == 0:        # if the first element is 0, we will run headed broswer first
                block.append(head(url, driver))   #block.append(...) meaning we will append the result (a dictionary) to a block
                block.append(headless(url))
            else:                       # else we will run headless first
                block.append(headless(url))
                block.append(head(url, driver))
            result.append(block)        #result list has all the blocks for 500 webistes, each block has 6 dictionaries containing information for each access
        n = n + 1
        if n % 20 == 0:                 # after running tests for every 20 websites, we reopen the brower.
            driver.quit()
            driver = Firefox()
            print(n)

'''function for pair permutation
'''
def fullRandom():
    driver = Firefox()
    time.sleep(4)
    n = 0
    for url in websiteList.websites:
        sequence = [0, 1, 2, 3, 4, 5]
        random.shuffle(sequence)         #we suffle the sequence list to determine which broswer we are runing first
        block = []
        for i in range(len(sequence)):
            if i != 0 and sequence[i - i] % 2 != 0 and sequence[i] % 2 != 0:
                #since urllib is really fast, we add a 1 second wait time after using it. We don't want 2 tests too close
                time.sleep(1)
            if sequence[i] % 2 == 0:     # if it's even number we run headed browser
                d = head(url, driver)    #block.append(...) meaning we will append the result (a dictionary) to a block
                block.append(d)
            else:                       # if it's odd number we run headless browser
                d = headless(url)
                block.append(d)
        result.append(block)           #result list has all the blocks for 500 webistes, each block has 6 dictionaries containing information for each access
        n += 1
        if n % 20 == 0:                 # after running tests for every 20 websites, we reopen the brower.
            driver.quit()
            driver = Firefox()
            print(n)


'''FIRST FUNCTION TO READ:
we try to figure which form of randomization of are using'''
if(recordFormat == "Matched Pair"):
    pairRecord()
else:
    fullRandom()



'''
after running the test, I'm writing the results into a file with json, and print
the results
'''
with open(fileName, "w") as outfile:
    output = {}
    output["measurements"] = result
    json.dump(output, outfile, indent = 4)




print("head200", head200)
print("headError" + headError)
print("headTimeout", headTimeout)
print("headOther", headOther)
print("headless200", headless200)
print("headlessError", headlessError)
print("headlessTimeout", headlessTimeout)
print("headlessOther", headlessOther)
print(recordFormat)
