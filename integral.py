# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 13:51:24 2019

@author: User
"""

import sympy as sp
from scipy.integrate import quad
import math as m
import numpy as np


x = sp.Symbol('x')
sp.integrate(3.0*x**2 + 1, x)

def f(x):
    return m.e**(-x) * m.sin(3 * x) 


print(f(5))
i,err = quad(f,0,2*m.pi) # solution, accuracy 

print(i)
print(err)

y = sp.Symbol('y')
sp.integrate(sp.exp(-x) * sp.sin(3.0*x),x)


def ff(x):
    return np.exp(-x) * np.sin(3.0*x)


ii,error = quad(ff,0,2*np.pi)
print(ii)
print(error)
