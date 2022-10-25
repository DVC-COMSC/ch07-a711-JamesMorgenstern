import numpy as np
import matplotlib.pyplot as plt

Math = [100, 90]
English = [90, 80]
Physics = [80, 80]
Computer = [80, 90]
x = np.arange(2) 
width = 0.2
labels = ['Math', 'English', 'Physics', 'Computer']
names = ['Bill', 'Mary']
fig, ax = plt.subplots()
m1 = ax.bar(x-width*1.5, Math, width)
e1 = ax.bar(x-width*0.5, English, width)
p1 = ax.bar(x+width*0.5, Physics, width)
c1 = ax.bar(x+width*1.5, Computer, width)
ax.legend(labels)
ax.set_title('Grouped graph for scores')
ax.bar_label(m1, padding=1)
ax.bar_label(e1, padding=1)
ax.bar_label(p1, padding=1)
ax.bar_label(c1, padding=1)
ax.set_xticks(x, names)

fig.savefig('A11.png')
