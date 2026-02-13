# factorial
import numpy as np
import math

def factorial(n):
    y = n
    for i in range(y-1):
        n = n * (y-i-1)
    return n

rng = np.random.default_rng(678956789)

rfloat = rng.integers(low=1, high=10000, size=100)/100

counter = 0
for i in range(100):
    if rfloat[i] >= 50.00:
        counter += 1

print(counter/100)
counter20 = 0
counter60 = 0
counter90 = 0
for i in range(100):
    if 1 < rfloat[i] and 20 > rfloat[i]:
        counter20 += 1
    if 30 < rfloat[i] and 60 > rfloat[i]:
        counter60 += 1
    if 70 < rfloat[i] and 90 > rfloat[i]:
        counter90 += 1

possibility = counter20*counter60*counter90

print(possibility)

mean = rfloat.sum()/100
temp = 0
for i in range(100):
    temp += pow(rfloat[i] - mean, 2)

std = math.sqrt(temp/100)
print(mean, std)

for i in range(100):
    for j in range(100):
        if rfloat[i] < rfloat[j]:
            temp = rfloat[i]
            rfloat[i] = rfloat[j]
            rfloat[j] = temp

if len(rfloat) // 2 == 1:
    print(rfloat[len(rfloat)/2])
else:
    print((rfloat[math.floor(len(rfloat)/2)]+rfloat[math.ceil(len(rfloat)/2)])/2)
