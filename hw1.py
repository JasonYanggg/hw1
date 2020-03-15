#!/usr/bin/python3
# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '106061233.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

i = 0
while (i < len(data)):
    if (data[i]["PRES"] == '-99.000' or data[i]["PRES"] == '-999.000'):
        del data[i]
    else:
        i = i + 1

def mean(id):
    global data, target_data
    averge = 0.0
    number = 0
    for row in data:
        if (row["station_id"] == id):
            averge += float(row["PRES"])
            number += 1
    if (number == 0):
        target_data.append([id, "None"])
    else:
        averge /= number
        target_data.append([id, averge])

target_data = []
mean("C0A880")
mean("C0F9A0")
mean("C0G640")
mean("C0R190")
mean("C0X260")
target_data.sort(key = lambda s: s[0], reverse = False)

#=======================================

# Part. 4
#=======================================
# Print result
print(target_data)
#========================================