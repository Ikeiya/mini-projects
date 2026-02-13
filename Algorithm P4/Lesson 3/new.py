import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# data = np.random.rand(300,3)
# for i in range(len(data)):
#     data[i] = data[i]*100

# df = pd.DataFrame(data)
iris = pd.read_csv("IRIS.csv")
df = iris.iloc[:, [0, 1, 2, 3]].values

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
            

k=5
centroids = initiate_centroids(k, df)

xdf = np.array(df.iloc[:,0])
ydf = np.array(df.iloc[:,1])

xCent = centroids.iloc[:,0]
yCent = centroids.iloc[:,1]


for i in range(len(data)):
    data[i][2] = pythagorean(data[i], centroids)

print(data[10])

for i in range(k):
    tempx = []
    tempy = []
    for j in range(len(data)):
        if data[j][2] == i:
            tempx.append(data[j][0])
            tempy.append(data[j][1])
    plt.scatter(tempx, tempy)
plt.scatter(xCent, yCent, marker="*", color="black")
plt.show()