import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import math
import seaborn as sb

cancer = pd.read_csv("Cancer_Data.csv")

def sigmoid(x):
    return 1/(1+math.exp(x))

flag = 0
for i in range(len(cancer["id"])):
    for i1 in range(len(cancer["id"])):
        if i != i1:
            if cancer["id"][i] == cancer["id"][i1]:
                flag = 1

print(flag)

result = cancer["diagnosis"]
cancer = cancer.drop(columns=["id", "diagnosis"], axis=1)

print("stuff", cancer)

cancer = cancer.dropna(axis=1, how="any")
correlation = cancer.corr(numeric_only=True)
cor_target = abs(correlation)
relevant = cor_target[cor_target>0.5]
print(relevant)

columns = relevant.columns
relevantColumns = []

for col in relevant.columns:
    for j in range(len(relevant[col])):
        if pd.isnull(relevant[col].iloc[j]) == False and relevant[col].iloc[j] != 1:
            relevantColumns.append([col, j])

print(relevantColumns)

xM = []
yM = []
xB = []
yB = []

for i in range(len(result)):
    if result[i] == "M":
        xM.append(cancer[relevantColumns[0][0]].iloc[i])
        yM.append(cancer[columns[relevantColumns[0][1]]].iloc[i])
    if result[i] == "B":
        xB.append(cancer[relevantColumns[0][0]].iloc[i])
        yB.append(cancer[columns[relevantColumns[0][1]]].iloc[i])


plt.scatter(xM, yM, c="r")
plt.scatter(xB, yB, c="b")

# dataplot = sb.heatmap(cancer, annot=True, fmt=".2f", annot_kws={"size":10}, linewidths=.7)
plt.show()