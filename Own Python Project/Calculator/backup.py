#calculator, pip install matplotlib
import math
import matplotlib.pyplot as plt

#Settings variables
calculator = True
radian = False


def setStr(input1):   
    token = [[]]
    for i in range(len(input1)):
        #When the i position of input and the one before is a number, or i position of input is a .
        if (input1[i].isnumeric() or input1[i] == ".") and (input1[i-1].isnumeric() or input1[i-1] == "."):
            #add the number to the former number
            token[-1].append(input1[i])
        #remove space from the input
        elif input1[i] == " ":
            continue
        #When i position is a negative, where the number before is not a number or - is not the first number
        elif input1[i] == "-"  and (input1[i-1].isnumeric() == False or i == 0)  and input1[i-1] != ")":
            token.append(["-1"])
            token.append(["*"])
        elif input1[i-1].isnumeric() == True and input1[i] == "(":
            token[-1].append(input1[i])
            token.append(["*"])
        elif input1[i].isalpha() == True and input1[i-1].isalpha() == True:
            token[-1].append(input1[i])
        else:
            token.append([input1[i]])
    for i in range(len(token)):
        token[i] = ''.join(token[i])
    if token[0] == '':
        token.pop(0)
    print(token)
    return token

def settings():
    print("'Radian' to set to radian\n'Degree' to set to degree")
    input1 = input("Enter command here: ")
    if input1 == "Radian":
        radian = True
    if input1 == "Degree":
        radian = False

def apps():
    print("things")

def graphing():
    graph = True
    graphInput = []
    print("'Plot' to plot graph")
    while graph:
        graphInput.append(input("f(x): "))
        if graphInput[-1] == "Plot":
            graphInput.pop()
        elif graphInput[-1] == "Exit":
            calculator()
            
graphing()
i = 0
deleteArray = []
status = True
ans = 0

def addition(a, b):
    return str(a+b)

def subtraction(a, b):
    return str(a-b)

def multiplication(a, b):
    return str(a*b)

def division(a, b):
    return str(a/b)

def factorial(a):
    return str(math.factorial(a))

def sin(a):
    if radian == False:
        a= a*math.pi/180
    return str(math.sin(a))

def stupidSin(a):
    if radian == False:
        a = a*math.pi/180
    return str(a-((a**3)/6)+((a**5)/120)-((a**7)/5040)+((a**9)/362880))

def cos(a):
    if radian == False:
        a = a*math.pi/180
    return str(math.cos(a))

def stupidCos(a):
    if radian == False:
        a = a*math.pi/180
    return str(1-((a**2)/2)+((a**4)/24)-((a**6)/720)+((a**8)/40320))

def tan(a):
    if radian == False:
        a = a*math.pi/180
    return str(math.tan(a))

def stupidTan(a):
    return str(sin(a)/cos(a))

def cosec(a):
    return str(1/float(sin(a)))

def sec(a):
    return str(1/float(cos(a)))

def cot(a):
    return str(1/float(tan(a)))

def asin(a):
    if radian == False:
        return str(math.asin(a)*180/math.pi)
    else:
        return str(math.asin(a))

def acos(a):
    if radian == False:
        return str(math.acos(a)*180/math.pi)
    else:
        return str(math.acos(a))

def atan(a):
    if radian == False:
        return str(math.atan(a)*180/math.pi)
    else:
        return str(math.atan(a))

def sqrt(a, b):
    return str(a**(1/b))

def power(a, b):
    return str(a**b)

def log(a, b):
    return str(math.log(b, a))

def fetusDeletus(token, numToDelete, positionToDelete):
    for i in range(0, numToDelete+1):
        print("pop",token)
        token.pop(positionToDelete)
    return token

def priority0(token):
    for i in range(len(token)):
        if token[i] == "pi":
            token[i] = "3.1415926539"
        if token[i] == "e":
            token[i] = "2.7182818285"
        if token[i] == "ans" or token[i] == "Ans" or token[i] == "ANS":
            token[i] = ans
        return token

def priority1(token):
    i = 0
    status = True
    while status:
        newToken = []
        if token[i] == "(":
            temp = i
        elif token[i] == ")":
            if token[temp-1].isalpha() == True:
                if token[temp-1] == "sin":
                    for j in range(i-temp-1):
                        newToken.append(token[temp+j+1])
                    token[i] = sin(float(run(newToken)[0]))
                elif token[temp-1] == "cos":
                    for j in range(i-temp-1):
                        newToken.append(token[temp+j+1])
                    token[i] = cos(float(run(newToken)[0]))
                elif token[temp-1] == "tan":
                    for j in range(i-temp-1):
                        newToken.append(token[temp+j+1])
                    token[i] = tan(float(run(newToken)[0]))
                elif token[temp-1] == "cosec" or token[i-3] == "csc":
                    for j in range(i-temp-1):
                        newToken.append(token[temp+j+1])
                    token[i] = cosec(float(run(newToken)[0]))
                elif token[temp-1] == "sec":
                    for j in range(i-temp-1):
                        newToken.append(token[temp+j+1])
                    token[i] = sec(float(run(newToken)[0]))
                elif token[temp-1] == "cot":
                    for j in range(i-temp-1):
                        newToken.append(token[temp+j+1])
                    token[i] = cot(float(run(newToken)[0]))
                elif token[temp-1] == "asin":
                    for j in range(i-temp-1):
                        newToken.append(token[temp+j+1])
                    token[i] = asin(float(run(newToken)[0]))
                elif token[temp-1] == "acos":
                    for j in range(i-temp-1):
                        newToken.append(token[temp+j+1])
                    token[i] = acos(float(run(newToken)[0]))
                elif token[temp-1] == "atan":
                    for j in range(i-temp-1):
                        newToken.append(token[temp+j+1])
                    token[i] = atan(float(run(newToken)[0]))
                elif token[temp-1] == "sqrt":
                    for j in range(i-temp-1):
                        newToken.append(token[temp+j+1])
                    token[i] = sqrt(float(run(newToken)[0]), 2)
                elif token[temp-1] == "log":
                    for j in range(i-temp-1):
                        newToken.append(token[temp+j+1])
                    token[i] = log(10, float(run(newToken)[0]))
                elif token[temp-1] == "ln":
                    for j in range(i-temp-1):
                        newToken.append(token[temp+j+1])
                    token[i] = log(math.e, float(run(newToken)[0]))
                token = fetusDeletus(token, (i-temp), temp-1)
                i = -1
            else:
                for j in range(i-temp-1):
                    newToken.append(token[temp+j+1])
                token[i] = bracketRun(newToken)[0]
                token = fetusDeletus(token, (i-temp-1), temp)
                i = -1
        print("bracket", token)
        i = i + 1
        if i>len(token)-1:
            i = 0
            print("bracket final", token)
            return token

def priority2(token): 
    i = 0
    status = True
    status2 = True
    position = -1
    while status2:
        print("multi", token)
        if token[i] == "^":
            token[i+1] = power(float(token[i-1]), float(token[i+1]))
            position = i-1
            i = 0
        if token[i] == "*":
            token[i+1] = multiplication(float(token[i-1]), float(token[i+1]))
            position = i-1
            i = 0
        elif token[i] == "/":
            token[i+1] = division(float(token[i-1]), float(token[i+1]))
            position = i-1
            i = 0
        if position != -1:
            token = fetusDeletus(token, 1, position)
            position = -1
        i = i+1
        if i>len(token)-1:
            i = 0
            print("final multiply", token)
            return token
    
def priority3(token):
    i = 0
    status = True
    position = -1
    while status:
        print("add", token)
        if token[i] == "+":
            token[i+1] = addition(float(token[i-1]), float(token[i+1]))
            position = i-1
            i = 0
        elif token[i] == "-":
            token[i+1] = subtraction(float(token[i-1]), float(token[i+1]))
            position = i-1
            i = 0
        if position != -1:
            token = fetusDeletus(token, 1, position)
            position = -1
        i = i+1
        if i>len(token)-1:
            print("final addition", token)
            return token

def run(token):
    token = setStr(token)
    token = priority0(token)
    token = priority1(token)
    token = priority2(token)
    token = priority3(token)
    return token

def bracketRun(token):
    token = setStr(token)
    token = priority2(token)
    token = priority3(token)
    return token

def calculator():
    print("Directly enter equation to enter equation\n'Help' to recieve all commands\n'Settings' to enter settings\n'Apps' to enter apps\n'Quit' to quit calculator")
    while calculator:
        token = input("Enter equation or command:")
        if token == "Quit":
            calculator = False
            break
        if token == "Settings":
            print(settings())
        if token == "Apps":
            print(apps())
        else:
            ans = run(token)[0]
            print("Final answer is: ", ans)
        