import time
from selenium import webdriver
import requests
import urllib
from selenium.webdriver.common.keys import Keys

start = time.time()
f = open("checktime.txt", "w")
#driver = webdriver.Firefox("/usr/local/Cellar/geckodriver/0.18.0/bin/")

start = time.time()
web = "http://www.facebook.com/"
r = urllib.request.urlopen(web)
f.write(web + str(r.getcode()) + "\n")
