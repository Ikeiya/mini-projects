import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

df = pd.read_csv('C:\\Users\\Ikeiya\\Desktop\\Fourier Transform\\temp\\diabetes.csv')

x1 = []
y1 = []
x2 = []
y2 = []

for i in range(len(df)):
    if df["Outcome"][i] == 0:
        y1.append(df["Insulin"][i])
        x1.append(df["Glucose"][i])
    else:
        y2.append(df["Insulin"][i])
        x2.append(df["Glucose"][i])

y3 = 0
x3 = 300

def betterSortThanPython(temp,k):
    for i in range(len(temp)):
        for j in range(len(temp)):
            temp2 = None
            if j+1 < k:
                if temp[j][1] < temp[j+1][1]:
                    temp2 = temp[j]
                    temp[j] = temp[j+1]
                    temp[j+1] = temp2
    return temp


def findDistance(x1,y1,k):
    temp = []
    for i in range(k):
        temp.append([0, 1000])
    for i in range(len(df)):
        if math.sqrt((df["Insulin"][i]-y1)**2+(df["Glucose"][i]-x1)**2) < math.sqrt((df["Insulin"][temp[0][0]]-y1)**2+(df["Glucose"][temp[0][0]]-x1)**2):
            temp[0] = [i, math.sqrt((df["Insulin"][i]-y1)**2+(df["Glucose"][i]-x1)**2)]
        temp = betterSortThanPython(temp,k)
    return temp

counter = 0
for i in range(len(findDistance(x3,y3,round(math.sqrt(len(df)))))):
    if df["Outcome"][findDistance(x3,y3,round(math.sqrt(len(df))))[i][0]] == 0:
        counter += 1

if counter/len(findDistance(x3,y3,round(math.sqrt(len(df))))) < 0.5:
    print("Diabetes")
else:
    print("Not diabetes")

plt.scatter(x1, y1, color="blue")
plt.scatter(x2, y2, color="red")
plt.scatter(x3, y3, color="lime")
plt.show()

