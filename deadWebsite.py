import websiteList
import json
import websiteList

with open("data/DataForEachUrl.txt", "r") as inFile:
    data = json.load(inFile)


for url in websiteList.websites:
    if data[url]["headed"]["200"] == 0 and data[url]["headless"]["200"] == 0:
        print(url)
