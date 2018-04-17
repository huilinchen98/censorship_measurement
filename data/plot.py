import json
import matplotlib.pyplot as plt
import numpy as np
import copy
import timeOutList

with open("timeOutForVPN.txt") as data_file:
    data = json.load(data_file)


headed = data['headed']
headless = data['headless']

numbers = range(len(headed))
deepcopy = copy.deepcopy(headed)
headed.sort()
outputHeadless = [None]*31
urlsForHeaded = [None]*31
urlsForHeadless = [None]*31


for i in range(len(timeOutList.timeOutList)):
    headedTime = deepcopy[i]
    for j in range(len(headed)):
        if headed[j] == headedTime:
            urlsForHeaded[j] = timeOutList.timeOutList[i]
#print(urlsForHeaded + "\n")

for i in range(len(headless)):
    headedTime = deepcopy[i]
    for j in range(len(headed)):
        if headed[j] == headedTime:
            outputHeadless[j] = headless[i]


for i in range(len(timeOutList.timeOutList)):
    headlessBeforeSort = headless[i]
    for j in range(len(headed)):
        if outputHeadless[j] == headlessBeforeSort:
            print(outputHeadless[j])

#print(urlsForHeadless)
#print(headless)
#print(outputHeadless)

x = range(31)
y = range(60)
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(np.array(numbers), np.array(headed), c = "b")
ax1.scatter(np.array(numbers), np.array(outputHeadless), c =  "r")
plt.show()


#plt.plot(np.array(numbers), np.array(headed), 'ro')
#plt.axis([0, len(headed), 0, 65])
#plt.show()

#plt.plot(np.array(numbers), np.array(outputHeadless), 'ro')
#plt.axis([0, len(headless), 0, 65])
#plt.show()
