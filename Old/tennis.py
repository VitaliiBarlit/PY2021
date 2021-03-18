# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 13:44:13 2018
@author: User
"""

import numpy as np

def summa(N,n):
    k = [i for i in range(1,N-n+2)]
    M = np.sum(k)
    return M
  
S = summa(3,2)
print(S)
input('Press Enter...')
#def factorial(n):
#    if n == 0:
#        return 1
#    else:
#        return n * factorial(n-1)
#
#n = 5
#a = 1
#b = 1
##def binom(n,a,b):
#k = [i for i in range(n+1)]
#m = factorial(k)


