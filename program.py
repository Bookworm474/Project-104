from ast import mod
import csv
from collections import Counter
from statistics import mode

with open("data.csv", newline="") as f:
    reader = csv.reader(f)
    filedata = list(reader)
filedata.pop(0)
newdata = []

#Mean/average
sum = 0
for i in range(len(filedata)):
    n = filedata[i][2]
    newdata.append(float(n))
for i in newdata:
    sum = sum + 1
mean = sum / len(newdata)
print(mean)

#Median
length = len(newdata)
newdata.sort()
if length % 2 == 0:
    median1 = float(newdata[n//2])
    median2 = float(newdata[n//2-1])
    median = median1 + median2
else:
    median = float(newdata[n//2])
print(median)

#Mode
data = Counter.newdata()
mode_data_for_range = {
    "75-85":0,
    "85-95":0,
    "95-105":0,
    "105-115":0,
    "115-125":0,
    "125-135":0,
    "135-145":0,
    "145-155":0,
    "155-165":0,
    "165-175":0
}
for weight, occurrence in data.items():
    if 75 < float(weight) < 85:
        mode_data_for_range["75-85"] += occurrence
    elif 85 < float(weight) < 95:
        mode_data_for_range["85-95"] += occurrence
    elif 95 < float(weight) < 105:
        mode_data_for_range["95-105"] += occurrence
    elif 105 < float(weight) < 115:
        mode_data_for_range["105-115"] += occurrence
    elif 115 < float(weight) < 125:
        mode_data_for_range["115-125"] += occurrence
    elif 125 < float(weight) < 135:
        mode_data_for_range["125-135"] += occurrence
    elif 135 < float(weight) < 145:
        mode_data_for_range["135-145"] += occurrence
    elif 145 < float(weight) < 155:
        mode_data_for_range["145-155"] += occurrence
    elif 155 < float(weight) < 165:
        mode_data_for_range["155-165"] += occurrence
    elif 165 < float(weight) < 175:
        mode_data_for_range["165-175"] += occurrence
mode_range, mode_occurrence = 0
for range, occurrence in mode_data_for_range.items():
    if occurrence > mode_occurrence:
        mode_range, mode_occurrence = [int(range.split("-")[0]), int(range.split("-")[1])], occurrence
mode = float((mode_range[0] + mode_range[1]) / 2)
print(mode)