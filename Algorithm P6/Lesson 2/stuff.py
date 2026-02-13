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
for column in relevant:
    if relevant[column].count("NaN") > 26:
        cancer.drop(column, axis=1)
dataplot = sb.heatmap(cancer, annot=True, fmt=".2f", annot_kws={"size":10}, linewidths=.7)
plt.show()