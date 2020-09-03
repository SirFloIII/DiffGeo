# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 01:19:47 2020

@author: Flo
"""

import sympy as sp
from sympy import diff, sqrt

class Vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __add__(self, other):
        return Vec3(self.x + other.x,
                    self.y + other.y,
                    self.z + other.z)
        
    def __mul__(self, scalar):
        return Vec3(scalar * self.x,
                    scalar * self.y,
                    scalar * self.z)
    
    __rmul__ = __mul__
    
    def __truediv__(self, scalar):
        return Vec3(self.x / scalar,
                    self.y / scalar,
                    self.z / scalar)
    
    def diff(self, var):
        return Vec3(diff(self.x, var),
                    diff(self.y, var),
                    diff(self.z, var))
        
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other):
        return Vec3(self.y * other.z - self.z * other.y,
                    self.z * other.x - self.x * other.z,
                    self.x * other.y - self.y * other.x)
        
    def norm(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)

sp.init_printing(forecolor = 'White')
u, v = sp.symbols("u v", real = True)

sig = Vec3(u - u**3/3 + u * v**2,
           v - v**3/3 + u**2 * v,
           u**2 - v**2)

sig_u = sig.diff(u)
sig_v = sig.diff(v)

sig_uu = sig.diff(u).diff(u)
sig_uv = sig.diff(u).diff(v)
sig_vv = sig.diff(v).diff(v)

c = sig_u.cross(sig_v)

NN = c / c.norm()

E = sig_u.dot(sig_u)
F = sig_u.dot(sig_v)
G = sig_v.dot(sig_v)

L = sig_uu.dot(NN)
M = sig_uv.dot(NN)
N = sig_vv.dot(NN)

print("\\begin{align*}")
for l in "EFGLMN":
    print(l, "&=", sp.latex(sp.simplify(sp.factor(sp.expand(sp.simplify(eval(l)))))), "\\\\")
print("\\end{align*}")
























