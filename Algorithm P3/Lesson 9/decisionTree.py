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
entropyVal = [[]]

parameters = df.columns
print("stuff", parameters)

for h in range(len(parameters)-3):
    entropyVal.append([])
    for i in range(len(df[parameters[h+1]].unique())):
        entropyVal[h].append([])
        for j in range(len(df["Drug"].unique())):
            print("val", entropyVal, h, i)
            entropyVal[h][i].append(0)
        for j in range(len(df[parameters[h+1]])):
            if df[parameters[h+1]][j] == df[parameters[h+1]].unique()[i]:
                entropyVal[h][i][np.array(np.where(df["Drug"].unique() == df["Drug"][j]))[0][0]] += 1
    for i in range(len(entropyVal[h])):
        temp = []
        tempTotal = sum(entropyVal[h][i])
        if i == 0:
            total = 0
            for j in range(len(entropyVal[h])):
                total += sum(entropyVal[h][j])
        for j in range(len(entropyVal[h][i])):
            temp.append(entropyVal[h][i][j]/tempTotal)
        entropyVal[h][i] = temp
        temp = 0
        for j in range(len(entropyVal[h][i])):
            if entropyVal[h][i][j] != 0:
                temp -= entropyVal[h][i][j]*(math.log(entropyVal[h][i][j], 2))
        entropyVal[h][i] = temp*tempTotal/total
        print("end", entropyVal)
