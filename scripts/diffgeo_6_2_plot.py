# -*- coding: utf-8 -*-
"""
Created on Thu May  7 13:06:54 2020

@author: Flo
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#def sigma(u,v):
#    return np.array((u - u**3/3 + u * v**2,
#                     v - v**3/3 + u**2 * v,
#                     u**2 - v**2))

#def sigma(u,v):
#    return np.array((u*np.cos(v),
#                     u*np.sin(v),
#                     np.log(u)))

def sigma(u,v):
    return np.array((u*np.cos(v),
                     u*np.sin(v),
                     v))



u = np.linspace(0, 1)
v = np.linspace(0, 2 * np.pi)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.axis("equal")

for uu in u:
    ax.plot(*sigma(uu, v), color = "r")
for vv in v:
    ax.plot(*sigma(u, vv), color = "g")
    

plt.show()