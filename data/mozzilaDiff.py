import json
import websiteList


#this script creats a file that summerize all the data in all of the tests for
#each of the 500 websites. It counts how many errors, timeouts, other code or
#200 response code does each website have for all the tests.





documents = ["6th(01234).txt", "20string.txt"]
d = {}


for web in websiteList.websites:
    d[web] = {}
    d[web]["1234"] = 0
    d[web]["useragent2"] = 0

with open("mozzilaTest/4.txt") as data_file:
    data = json.load(data_file)
measurements = data["measurements"]
for lst in measurements:
    target = d[lst[0]["url"]]
    for dct in lst:
        if dct["browser"] == "headless":
            if dct["Status"] == 200:
                target["1234"] += 1

with open("mozzilaTest/50.txt") as data_file:
    data = json.load(data_file)
measurements = data["measurements"]
for lst in measurements:
    target = d[lst[0]["url"]]
    for dct in lst:
        if dct["browser"] == "headless":
            if dct["Status"] == 200:
                target["useragent2"] += 1

for web in websiteList.websites:
    if d[web]["1234"] > d[web]["useragent2"]:
        print(web)


with open("differforMozi", 'w') as outfile:
    json.dump(d, outfile, indent = 4)
