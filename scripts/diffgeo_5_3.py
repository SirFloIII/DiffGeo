# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 01:19:47 2020

@author: Flo
"""

import sympy as sp
from sympy import sin, cos, sinh, cosh, diff

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

    def diff(self, var):
        return Vec3(diff(self.x, var),
                    diff(self.y, var),
                    diff(self.z, var))
        
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z


sp.init_printing(forecolor = 'White')

u, v, t = sp.symbols("u v t")

sig0 = Vec3( cosh(u) * cos(v),
             cosh(u) * sin(v),
             u )

sig1 = Vec3(-sinh(u) * sin(v),
             sinh(u) * cos(v),
            -v )

sigt = sig0 * cos(t) + sig1 * sin(t)

sigt_u = sigt.diff(u)
sigt_v = sigt.diff(v)

E = sigt_u.dot(sigt_u)
F = sigt_u.dot(sigt_v)
G = sigt_v.dot(sigt_v)

print(sp.latex(sp.simplify(E)))
print(sp.latex(sp.simplify(F)))
print(sp.latex(sp.simplify(G)))























