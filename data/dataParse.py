import json


#it counts how many error, timeout, 200, or other code does a single test have
#and print it outf


with open("chrome/chrome1.txt") as data_file:
    data = json.load(data_file)

result = []
headError = 0
headTimeout = 0
head200 = 0
headOther = 0
headlessError = 0
headless200 = 0
headlessOther = 0
headlessTimeout = 0

measurements = data["measurements"]
for lst in measurements:
    for dct in lst:
        if dct["browser"] == "headed":
            if dct["Status"] == -1:
                headTimeout += 1
            elif dct["Status"] == 200:
                head200 += 1
            elif type(dct["Status"]) == str:
                headError += 1
            else:
                headOther += 1
        else:
            if dct["Status"] == -1:
                headlessTimeout += 1
            elif dct["Status"] == 200:
                headless200 += 1
            elif type(dct["Status"]) == str:
                headlessError += 1
            else:
                headlessOther += 1

print("head200: " + str(head200))
print("headOther: " + str(headOther))
print("headError: " + str(headError))
print("headTimeout: " + str(headTimeout))
print("headless200: " + str(headless200))
print("headlessOther: " + str(headlessOther))
print("headlessError: " + str(headlessError))
print("headlessTimeout: " + str(headlessTimeout))
