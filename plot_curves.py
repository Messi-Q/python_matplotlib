# -*- coding: utf-8 -*-
"""
@author: Messi-Q
"""
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (7, 5)
plt.tight_layout()

epoch = []
number = []

input_epoch = "./data/epoch.txt"
f_epoch = open(input_epoch, "r")
epochs = f_epoch.readlines()
for line in epochs:
    epoch.append(float(line.strip()))

input_number = "./data/number.txt"
f_number = open(input_number, "r")
numbers = f_number.readlines()
for line in numbers:
    number.append(float(line.strip()))

lw = 1
plt.plot(epoch, number, color='steelblue', linestyle='-', marker='o')

font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 19,
         }
ax = plt.gca()
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
ax.spines['top'].set_linewidth(1.5)

plt.xlabel('Epoch', font1)
plt.ylabel('Accuracy', font1)
plt.tick_params(labelsize=16)

font2 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 17,
         }

plt.legend(['Paper number'], loc="lower right",
           prop=font2, edgecolor='black', bbox_to_anchor=(0.97, 0.03), shadow=True)
plt.xlim((2014, 2021))
plt.ylim((-1, 100))
# plt.savefig('model.png')
plt.title('Papers')
plt.show()
