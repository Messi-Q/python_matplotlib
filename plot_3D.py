# -*- coding: utf-8 -*-
"""
@author: Messi-Q
"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(5.8, 5.4))
ax = Axes3D(fig)

# timestamp NN
ax.bar([1, 2, 3, 4], [49.77, 44.59, 51.91, 45.62], 1, zdir='y', color='orangered', alpha=1)
ax.bar([1, 2, 3, 4], [50.79, 59.23, 50.32, 54.41], 2, zdir='y', color='black', alpha=0.86)
ax.bar([1, 2, 3, 4], [52.06, 59.91, 49.41, 54.15], 3, zdir='y', color='dodgerblue', alpha=0.82)
ax.bar([1, 2, 3, 4], [74.21, 75.97, 68.35, 71.96], 4, zdir='y', color='khaki', alpha=0.9)
ax.bar([1, 2, 3, 4], [78.68, 78.91, 71.29, 74.91], 5, zdir='y', color='navy', alpha=0.94)
ax.bar([1, 2, 3, 4], [83.45, 83.82, 75.05, 79.19], 6, zdir='y', color='orange', alpha=1)

font = {'family' : 'Times New Roman',
'weight' : 'normal',
'size'   : 16.8,
}

ax.set_xlabel('X', font)
ax.set_ylabel('Y', font)
ax.set_zlabel('Z', font)
ax.grid(True)
# ax.set_yticks(np.linspace(0, 7, 7))
ax.set_xticks(np.arange(1, 5, 1))
# plt.axis('equal')
# plt.text(60, .025, r'$mu=100, sigma=15$')
# plt.axis([0, 11, 1, 4, 0, 1])
ax.set_xlim3d(0.5, 4.5)
ax.set_ylim3d(1, 6)
ax.set_zlim3d(0, 100)
plt.tick_params(labelsize=17)
plt.show()
# fig.savefig("3D_Figure.pdf", format='pdf', dpi=1000)
