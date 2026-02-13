import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.cluster import KMeans 
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import MinMaxScaler

iris = pd.read_csv("IRIS.csv")
x = iris.iloc[:, [0, 1, 2, 3]].values

iris.info()
iris[0:10]

def initiate_centroids(k, dset):
    centroids = dset.sample(k)
    return centroids

def pythagorean(data, centroid):
    determine = 1000000000000
    cluster = 0
    for i in range(len(centroid.iloc[:,0])):
        if np.sqrt((centroid.iloc[i,0]-data[0])**2+(centroid.iloc[i,1]-data[1])**2) < determine:
            cluster = i
            determine = np.sqrt((centroid.iloc[i,0]-data[0])**2+(centroid.iloc[i,1]-data[1])**2)
    return cluster

def initiate_centroids(k, dset):
    centroids = dset.sample(k)
    return centroids

k=5
centroids = initiate_centroids(k, iris)

xCent = centroids.iloc[:,0]
yCent = centroids.iloc[:,1]

IrisSetosa = []
IrisVersicolor = []
IrisVirginica = []

for i in range(len(iris)-1):
    if iris["species"][i] == "Iris-setosa":
        IrisSetosa.append(iris.iloc[i])
    if iris["species"][i] == "Iris-versicolor":
        IrisVersicolor.append(iris.iloc[i])
    if iris["species"][i] == "Iris-virginica":
        IrisVirginica.append(iris.iloc[i])

plt.scatter(tempx, tempy)
plt.scatter(xCent, yCent, marker="*", color="black")
plt.show()