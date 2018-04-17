import json
import websiteList


#this script creats a file that summerize all the data in all of the tests for
#each of the 500 websites. It counts how many errors, timeouts, other code or
#200 response code does each website have for all the tests.





documents = ["1st6pairs.txt", "1stPairPermu.txt", "2nd6PairPermu.txt", "3rd6accesses.txt", "2ndPairPermu.txt", "3rdPairPermu.txt"]
d = {}
outfile = "DataForEachUrl.txt"


for web in websiteList.websites:
    d[web] = {}
    d[web]["headed"] = {}
    d[web]["headed"]["timeout"] = 0
    d[web]["headed"]["200"] = 0
    d[web]["headed"]["Error"] = 0
    d[web]["headed"]["Other"] = 0
    d[web]["headless"] = {}
    d[web]["headless"]["timeout"] = 0
    d[web]["headless"]["200"] = 0
    d[web]["headless"]["Error"] = 0
    d[web]["headless"]["Other"] = 0

for doc in documents:
    with open(doc) as data_file:
        data = json.load(data_file)
    measurements = data["measurements"]
    for lst in measurements:
        target = d[lst[0]["url"]]
        for dct in lst:
            if dct["browser"] == "headed":
                if dct["Status"] == -1:
                    target["headed"]["timeout"] += 1
                elif dct["Status"] == 200:
                    target["headed"]["200"] += 1
                elif dct["Status"] == 0:
                    target["headed"]["Error"] += 1
                else:
                    target["headed"]["Other"] += 1
            else:
                if dct["Status"] == -1:
                    target["headless"]["200"] += 1
                elif dct["Status"] == 200:
                    target["headless"]["200"] += 1
                elif dct["Status"] == 0:
                    target["headless"]["Error"] += 1
                else:
                    target["headless"]["Other"] += 1


with open(outfile, 'w') as outfile:
    json.dump(d, outfile, indent = 4)
