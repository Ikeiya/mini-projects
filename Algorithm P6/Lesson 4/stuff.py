import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import math
import seaborn as sb
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
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


cancer = cancer.dropna(axis=1, how="any")
correlation = cancer.corr(numeric_only=True)
cor_target = abs(correlation)
relevant = cor_target[cor_target>0.5]

columns = relevant.columns
relevantColumns = []


# for col in relevant.columns:
#     for j in range(len(relevant[col])):   
        
#         xM = []
#         yM = []
#         xB = []
#         yB = []
#         if pd.isnull(relevant[col].iloc[j]) == False and int(relevant[col].iloc[j]) != 1:
#             relevantColumns.append([col, j])
#             for i in range(len(result)-1):
#                 if result[i] == "M":
#                     xM.append(cancer[relevantColumns[-1][0]].iloc[i])
#                     yM.append(cancer[columns[relevantColumns[-1][1]]].iloc[i])
#                 if result[i] == "B":
#                     xB.append(cancer[relevantColumns[-1][0]].iloc[i])
#                     yB.append(cancer[columns[relevantColumns[-1][1]]].iloc[i])
#             plt.scatter(xM, yM, c="r")
#             plt.scatter(xB, yB, c="b")
#             plt.savefig(str(j)+'.png')
#             plt.clf()

print("OK", columns)
X = cancer[columns]
Y = result
Y = Y.replace(to_replace="B", value=0)
Y = Y.replace(to_replace="M", value=1)
print("EFNO", X, "SUTG", Y)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=34) # 70% training and 30% test

clf = DecisionTreeClassifier()
clf = clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

text_representation = tree.export_text(clf)
print(text_representation)

fig = plt.figure(figsize=(25,20))
_ = tree.plot_tree(clf,
                   feature_names=cancer[columns],
                   class_names=result,
                   filled=True)
# # dataplot = sb.heatmap(cancer, annot=True, fmt=".2f", annot_kws={"size":10}, linewidths=.7)
