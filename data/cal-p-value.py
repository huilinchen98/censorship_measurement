import pvalue
import json


"""
defining a test_stats function
"""
def test_stats(x, y):
	output = 0
	for i in range(6):
		if x[i] == 1:
			#if it's a headed
			if y[i] == 1:
				output += 1
		else:
			if y[i] == 1:
				output -= 1
	return output

#we are calculating the pvalue for 500 group in 1 file
files = ["week1test/1st6ac.txt"]

for file in files:
	with open(file) as data_file:
		data = json.load(data_file)
	measurements = data["measurements"]
	for lst in measurements:
		#for each group, we create x_value list and y_value list
		x_value = []
		y_value = []
		for d in lst:
			if d["browser"] == "headless":
				#if it's headless browser, we append 0 to x_value list, otherwise 1
				x_value.append(0)
			else:
				x_value.append(1)
			if d["Status"] == 200:
				#if it's a 200 response code, we append 1, otherwise 0
				y_value.append(1)
			else:
				y_value.append(0)

		p = pvalue.full_test(x_value, y_value, test_stats)
		if p <= 0.05:
			# if confidence is enough, we print out the url and confidence
			print(lst[0]["url"], p)

