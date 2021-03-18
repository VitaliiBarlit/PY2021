# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 08:52:46 2019

@author: User
"""

import random as r


def ran():
    R = r.choice(range(100000,1000000,1))
    return R


def numstr(R):
    R0 = str(R)

    R1 = R0[:3]
    R2 = R0[3:]
    
    
    Y1 = int(R1[0])+int(R1[1])+int(R1[2])
    if Y1 > 9:
        Y1 = str(Y1)
        Y1 = int(Y1[0]) + int(Y1[1])
    
    Y2 = int(R2[0])+int(R2[1])+int(R2[2])
    if Y2 > 9:
        Y2 = str(Y2)
        Y2 = int(Y2[0]) + int(Y2[1]) 
    return Y1,Y2        


def circ():
    count = 0
    x = ran()
    z = numstr(x)    
    while z[0] != z[1]:
        x = ran()
        z = numstr(x)
        count += 1
    else:
        print(count,x)


X = [i for i in range(0,1000000,1)]

Num = 345678


def num(i:int):
    i1 = i//100000
    i2 = (i - i1*100000)//10000 
    i3 = (i - i2*10000 - i1*100000)//1000 
    i4 = (i - i3*1000 - i2*10000 - i1*100000)//100 
    i5 = (i - i4*100- i3*1000 - i2*10000 - i1*100000)//10 
    i6 = (i - i5*10 - i4*100- i3*1000 - i2*10000 - i1*100000)//1
    E1 = i1 + i2 + i3
    E2 = i4 + i5 + i6
#    while E1 > 9:
#        E1 -= 9
#    while E2 > 9:
#        E2 -= 9
    if E1 == E2:
        return i
    else:
        return None


def numlist(L:list):
    D = []

    for _ in L:
        x = num(_)
        if x != None:
            D.append(_)
    return D



List_of_lucky_tickets = [i for i in range(0,1000000,1)]

S = numlist(List_of_lucky_tickets)

print(len(S))



        
        
        
        
        
        
        
