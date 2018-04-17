import csv

f = open("top500.txt", "w")

with open("top500.domains.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        url = "http://www." + row["URL"]
        f.write("'" + url + "'" + ", ")
