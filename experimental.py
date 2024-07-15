# Here go adhoc snippets of code jus to quickly verify if a concept works.


import pandas as pd

import matplotlib.pyplot as plt
import numpy as np

#plot 1:
csv_file = pd.read_csv('data/aaplprices.csv')
x = csv_file.Volume

plt.subplot(2, 1, 1)
x.plot.bar()
#plt.plot(x)

# https://www.w3schools.com/python/matplotlib_subplot.asp

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2)
plt.plot(x,y)

plt.show()




'''
def plot_sin(ax):
    x = np.linspace(0, 10)
    y = np.sin(x)
    ax.plot(x, y)
    ax.set_title('Just a sine curve')

fig, ax = plt.subplots(2,2)
plot_sin(ax[0,0])
plt.show()
'''

'''import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 2)

ax[0, 0].plot(range(10), 'r') #row=0, col=0
ax[1, 0].plot(range(10), 'b') #row=1, col=0
ax[0, 1].plot(range(10), 'g') #row=0, col=1
ax[1, 1].plot(range(10), 'k') #row=1, col=1
plt.show()
'''


'''
f = open('goodlines.txt')
result = f.split(" ", 1)[0]
print(result)
'''


''' THIS WORKS FOR SINGLE STRINGS.
str = "dzs xd xx"
result = str.split(" ", 1)[0]
print(result)  # Output: "hello"

'''