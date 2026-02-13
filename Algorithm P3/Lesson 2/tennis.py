import pandas as pd

df = pd.read_csv('play_tennis.csv')

print(df['play'])
counter = 0
for i in range(len(df['play'])):
    if df['play'][i] == "Yes":
        counter += 1
    print(df['play'][i])

posPlay = counter/len(df['play'])
posNotPlay = 1-counter/len(df['play'])
counter1 = 0
counter2 = 0
for i in range(len(df['temp'])):
    if df['temp'][i] == "Hot":
        if df['play'][i] == "Yes":
            counter1 += 1
    counter2 += 1

posHotPlay = counter1/counter2


def inHeader(condition1, condition2):
    if condition1 in df['outlook'].to_list():
        temp1 = "outlook"
    elif condition1 in df['temp'].to_list():
        temp1 = "temp"
    elif condition1 in df['humidity'].to_list():
        temp1 = "humidity"
    elif condition1 in df['wind'].to_list():
        temp1 = "wind"
    elif condition1 in df['play'].to_list():
        temp1 = "play"
    else:
        print("You are a retard")
        return None
    
    if condition2 in df['outlook'].to_list():
        temp2 = "outlook"
    elif condition2 in df['temp'].to_list():
        temp2 = "temp"
    elif condition2 in df['humidity'].to_list():
        temp2 = "humidity"
    elif condition2 in df['wind'].to_list():
        temp2 = "wind"
    elif condition2 in df['play'].to_list():
        temp2 = "play"
    else:
        print("You are a retard2")
        return None
    return [temp1, temp2]
    
def bayesTheorem(condition1, condition2):
    loc = inHeader(condition1, condition2)
    counter1 = 0
    counter2 = 0
    print(loc)
    for i in range(len(df[loc[0]])):
        if df[loc[0]][i] == condition1:
            if df[loc[1]][i] == condition2:
                counter1 += 1
        counter2 += 1
    return counter1/counter2

def considerPlay(list):
    temp1 = 1
    temp2 = 1
    for i in range(len(list)):
        temp1 = temp1*bayesTheorem(list[i], "Yes")
    for i in range(len(list)):
        temp2 = temp2*bayesTheorem(list[i], "No")
    if temp1 >= temp2:
        return "play"
    else:
        return "don't play"

print(considerPlay(["Hot", "Normal", "Sunny"]))