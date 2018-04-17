import json
files = ['week1test/1st6ac.txt', 'week1test/2nd6ac.txt', 'week1test/3rd6ac.txt',
        'useragent/2nd.txt', 'useragent/3rd.txt']

num2 = 0
num3 = 0

# we are trying to compare which one is better way of randomizing the accesses.
# we are comparing the number of different status code received according to the weith
d = {}
for i in range(6):
    d[i] = []


for fl in files:
    with open(fl) as data_file:
        data = json.load(data_file)

    measurements = data["measurements"]
    for lst in measurements:
        headlessValues = set()
        headlessIndices = [i for i, x in enumerate(lst) if x["browser"] == "headless"]
        for i in range(6):
            if i in headlessIndices:
                headlessValues.add(lst[i]["Status"])
        if len(headlessValues) == 2:
            num2 += 1
        if len(headlessValues) == 3:
            num3 += 1
        d[headlessIndices[2] - headlessIndices[0]].append(len(headlessValues))

        headedValues = set()
        headedIndices = [i for i, x in enumerate(lst) if x["browser"] == "headed"]
        for i in range(6):
            if i in headedIndices:
                headedValues.add(lst[i]["Status"])
        if len(headedValues) == 2:
            num2 += 1
        if len(headedValues) == 3:
            num3 += 1
        d[headedIndices[2] - headedIndices[0]].append(len(headedValues))

results = []
width = []
for i in range(6):
    if len(d[i]) != 0:
        width.append(i)
        results.append(sum(d[i])/len(d[i]))
print("width 2", len(d[2]))
print("width 3", len(d[3]))
print("width 4", len(d[4]))
print("width 5", len(d[5]))

print(width, results)
print("num of 2 responses", num2)
print("num of 3 responses", num3)
