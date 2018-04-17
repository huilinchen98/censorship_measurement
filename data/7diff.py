import json
import websiteList

doc = 'useragent/1st.txt'

with open(doc) as data_file:
    data = json.load(data_file)
measurements = data["measurements"]

for lst in measurements:
    headed = 0
    headless = 0
    for dct in lst:
        if dct["browser"] == "headless":
            headless = dct["Status"]
        else:
            headed = dct["Status"]
    if headless == 200 and headed != 200:
        print(lst[0]["url"])
