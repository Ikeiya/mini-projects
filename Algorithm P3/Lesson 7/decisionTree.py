import pandas as pd
import numpy as np
import math

class node:
    def __init__(self, value, feature = None    , trueBr = None, falseBr = None, result = None):
        self.value = value
        self.feature = feature
        self.trueBr = trueBr
        self.falseBr = falseBr
        self.result = result


df = pd.read_csv('drug200.csv')
print(np.array(np.where(df["BP"].unique() == df["BP"][8]))[0][0])
print(df["BP"].unique())
entropyVal = []
for i in range(len(df["BP"].unique())):
    entropyVal.append([])
    for j in range(len(df["Drug"].unique())):
        entropyVal[i].append(0)
    for j in range(len(df["BP"])):
        if df["BP"][j] == df["BP"].unique()[i]:
            entropyVal[i][np.array(np.where(df["Drug"].unique() == df["Drug"][j]))[0][0]] += 1

for i in range(len(entropyVal)):
    temp = []
    for j in range(len(entropyVal[i])):
        temp.append(entropyVal[i][j]/sum(entropyVal[i]))
    entropyVal[i] = temp
    print(entropyVal[i])
    temp = 0
    for j in range(len(entropyVal[i])):
        if entropyVal[i][j] != 0:
            temp -= entropyVal[i][j]*math.log(entropyVal[i][j], 2)
            print(entropyVal[i][j]*math.log(entropyVal[i][j], 2), math.log(entropyVal[i][j], 2))
    entropyVal[i] = temp

print(sum(entropyVal))