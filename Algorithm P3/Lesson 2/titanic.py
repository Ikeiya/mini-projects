import pandas as pd

df = pd.read_csv('titanic.csv')

 
def bayesTheorem(condition1, condition2, loc):
    counter1 = 0
    counter2 = 0
    for i in range(len(df[loc[0]])):
        if df[loc[0]][i] == condition1:
            if df[loc[1]][i] == condition2:
                counter1 += 1
        counter2 += 1
    return counter1/counter2

def considerPlay(list, loc):
    temp1 = 1
    temp2 = 1
    for i in range(len(list)):
        temp1 = temp1*bayesTheorem(list[i], 1, [loc[i], "Survived"])
    for i in range(len(list)-1):
        temp2 = temp2*bayesTheorem(list[i], 0, [loc[i], "Survived"])
    if temp1 >= temp2:
        return "survive"
    else:
        return "don't survive"

print(considerPlay(["Female", "3", "3"], ["Sex", "Age", "Pclass"]))