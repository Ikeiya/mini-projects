import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

trainData = pd.read_csv('train.csv')
testData = pd.read_csv('test.csv')

trainSalePrice = trainData["SalePrice"].tolist()
trainLotArea = trainData["LotArea"].tolist()

del trainSalePrice[1::2]
del trainLotArea[1::2]

testSalePrice = trainData["SalePrice"].tolist()
testLotArea = trainData["LotArea"].tolist()

del testSalePrice[::2]
del testLotArea[::2]

gradient = []

for i in range(len(trainSalePrice)):
    gradient.append(trainSalePrice[i]/trainLotArea[i])

gradient = np.mean(gradient)

print(gradient)

plt.scatter(np.array(testLotArea), np.array(testSalePrice), alpha=0.5)
plt.plot(np.array(trainLotArea), gradient * np.array(trainLotArea), '-')
plt.show()

testSum = 0
trainSum = 0
# for loop for iteration 
for i in range(len(testLotArea)): 
    testSum += abs(testSalePrice[i] - (gradient * testLotArea[i])) 
  
testError = testSum/len(testLotArea) 

for i in range(len(trainLotArea)): 
    trainSum += abs(trainSalePrice[i] - (gradient * trainLotArea[i])) 
  
trainError = trainSum/len(testLotArea) 

print(testError/np.mean(testSalePrice)*100, trainError/np.mean(trainSalePrice)*100)

area = input("enter area")

print("price is: ", int(area)*int(gradient)*0.59, " to ", int(area)*int(gradient)*1.41)