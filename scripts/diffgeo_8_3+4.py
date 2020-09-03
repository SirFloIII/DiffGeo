# -*- coding: utf-8 -*-
"""
Created on Tue May 26 13:12:13 2020

@author: Flo, Kathi, Ciara, Gamsi
"""

import sympy as sp
from sympy import diff, sqrt, sinh, cosh, tanh, cos, sin, log

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
t, u, v = sp.symbols("t u v", real = True)

f = lambda t : 1 / cosh(t)
g = lambda t : t - tanh(t)


#Uncomment the right line for the different examples:

# Example 3
sig = Vec3(g(u), f(u)*cos(v), f(u)*sin(v))

# Example 4
#  sigma:
# sig = Vec3(u*cos(v), u*sin(v), log(u))
#  tau:
# sig = Vec3(u*cos(v), u*sin(v), v)

sig_u = sig.diff(u)
sig_v = sig.diff(v)

sig_uu = sig.diff(u).diff(u)
sig_uv = sig.diff(u).diff(v)
sig_vv = sig.diff(v).diff(v)

c = sig_u.cross(sig_v)

NN = c / c.norm()

E = sp.simplify(sig_u.dot(sig_u))
F = sp.simplify(sig_u.dot(sig_v))
G = sp.simplify(sig_v.dot(sig_v))

L = sp.simplify(sig_uu.dot(NN))
M = sp.simplify(sig_uv.dot(NN))
N = sp.simplify(sig_vv.dot(NN))

K = sp.simplify((L*N-M*M)/(E*G-F*F))






















