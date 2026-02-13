import math
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm, pylab

def graphing():
    graph = True
    graphInput = []
    x = []
    y = []
    print("'Plot' to plot graph")
    while graph:
        graphInput.append(input("f(x): "))
        if graphInput[-1] == "Plot":
            graphInput.pop()
            for i in range(len(graphInput)):
                fig, ax = plt.subplots()
            ax.plot(x, graphInput[i], label="plot "+i)
            plt.show()
            break

# graphing()

X = np.linspace(100, 2*np.pi, 100)
Y = (X)**2+X+1
Z = np.sin(X)
fig, ax = plt.subplots()
ax.plot(X, Y)
ax.plot(X, Z)
plt.show()