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
a = open(input_epoch, "r")
epochs = a.readlines()
for line in epochs:
    epoch.append(float(line.strip()))

input_number = "./data/number.txt"
b = open(input_number, "r")
b_read = b.readlines()
for line in b_read:
    number.append(float(line.strip()))

width = 0.45
plt.bar(epoch, number, width, label="num", color="steelblue")

plt.xlabel('Years')
plt.ylabel('Number of papers')
plt.title('Papers')
plt.legend(loc="upper right")
plt.show()
