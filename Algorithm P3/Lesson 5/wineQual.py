import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import math
from mpl_toolkits.mplot3d import Axes3D
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv('winequality-red2.csv')

# # print(df["fixed acidity"])
# # df.to_csv("winequality-red2.csv", index=False)

# print(df.columns.values.tolist())

# n = len(df["fixed acidity"])

# x = df["residual sugar"]
# y = df["total sulfur dioxide"]
# z = df["quality"]

# fig = plt.figure(figsize=(10,10))
# ax = Axes3D(fig, auto_add_to_figure=False)
# fig.add_axes(ax)

# # cmap = ListedColormap(sns.color_palette("husl", 256).as_hex())

# sc = ax.scatter(x, y, z, s=40, c=x, marker='o', alpha=1)
# ax.set_xlabel('Residue Sugar')
# ax.set_ylabel('Total Sulfur Dioxide')
# ax.set_zlabel('Quality')
# plt.legend(*sc.legend_elements(), bbox_to_anchor=(1.05, 1), loc=2)
# plt.savefig("scatter2", bbox_inches='tight')

print(df["quality"].max())

quality = []
qualityCount = []
qualityVal = []
for i in range(df["quality"].max()):
    quality.append(i+1)
    qualityCount.append(len(df[df["quality"]==i+1]))

for i in range(len(df["quality"])):
    if df["quality"][i] >= 6:
        qualityVal.append(1)
    else:
        qualityVal.append(0)

df = df.assign(booleanQuality = qualityVal)

# badDf = df[df["booleanQuality"] == "Bad"]
# goodDf = df[df["booleanQuality"] == "Good"]
feature = np.array(df.iloc[:,:10])
result =  np.array(df.iloc[:,12])



featureTr, featureRs, resultTr, resultRs =  train_test_split(feature, result, test_size=0.3, random_state=928)
knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(featureTr ,resultTr)
accuracy = accuracy_score(knn.predict(featureRs), resultRs)
print(accuracy)

# scores = []
# temp = 0
# for i in range(math.floor(len(featureTr)*0.8)-1):
#     print(i)
#     temp = 0
#     for j in range(5):
#         featureTr2, featureRs2, resultTr2, resultRs2 = train_test_split(featureTr, resultTr, test_size=0.2, random_state=928+j)
#         knn = KNeighborsClassifier(n_neighbors = i+2)
#         knn.fit(featureTr2, resultTr2)
#         score = accuracy_score(knn.predict(featureRs2), resultRs2)
#         temp += score
#     scores.append(temp/5)

# print(scores, max(scores), scores.index(max(scores)))

featureTr, featureRs, resultTr, resultRs =  train_test_split(feature, result, test_size=0.3, random_state=928)
knn = KNeighborsClassifier(n_neighbors = 73)
knn.fit(featureTr ,resultTr)
accuracy = accuracy_score(knn.predict(featureRs), resultRs)
print(accuracy)

truePos = 0
trueNeg = 0
falsePos = 0
falseNeg = 0

predict = knn.predict(featureRs)

for i in range(len(resultRs)):
    if predict[i] == 1 and resultRs[i] == 1:
        truePos += 1
    if predict[i] == 0 and resultRs[i] == 0:
        trueNeg += 1
    if predict[i] == 1 and resultRs[i] == 0:
        falsePos += 1
    if predict[i] == 0 and resultRs[i] == 1:
        falseNeg += 1

hm = sns.heatmap([[truePos, falsePos],[falseNeg, trueNeg]], annot=True, cmap='Blues', fmt='g')

print(truePos, trueNeg, falsePos, falseNeg)

plt.show()
# fig = plt.figure(figsize = (10, 5))

# creating the bar plot
# plt.bar(quality, qualityCount, color ='maroon', 
#         width = 0.4)

# plt.xlabel("Quality")
# plt.ylabel("Amount of wine per quality")
# plt.title("List of shit wine")
# plt.show()