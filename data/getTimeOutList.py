import json
import websiteList

##it puts all the urls that ever get timeout in to a file


docs = ['useragent/1st.txt', 'useragent/2nd.txt']
f = open("timeoutList.txt", "w")

with open('useragent/1st.txt') as data_file:
    data = json.load(data_file)
measurements = data["measurements"]

urls = []

for lst in measurements:
    for dct in lst:
        if dct["Status"] == -1 and dct["url"] not in urls:
            urls.append(dct["url"])
            print(dct["url"])
            f.write(dct["url"] + ", ")


with open('useragent/2nd.txt') as data_file:
    data = json.load(data_file)
measurements = data["measurements"]
for lst in measurements:
    for dct in lst:
        if dct["Status"] == -1 and dct["url"] not in urls:
            urls.append(dct["url"])
            print(dct["url"])
            f.write("'" + dct["url"] + "'" + ", ")
