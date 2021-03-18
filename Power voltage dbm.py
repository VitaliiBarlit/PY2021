# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 16:00:27 2019

@author: User
"""

import numpy as np



#def vltg():       # Voltage #
#    U = float(input('Voltage value: '))
#    N = 10*np.log10(np.power(U,2)/50 * 1000)
#    n1 = pow(10,N/10)/1000
#    
#    print(U,'V',round(N,2),'dBm',round(n1,5),'W')

#vltg()


def comparison(i:float):
    if i >= 1:
        return round(i,2)
    elif i < 1 and i >= (pow(10,-3)):
        return '{}*10e-3'.format(round((i*pow(10,3))),2)
    elif i < (pow(10,-3)) and i >= (pow(10,-6)):
        return '{}*10e-6'.format(round((i*pow(10,6))),2)
    elif i < (pow(10,-6)) and i >= (pow(10,-9)):
        return '{}*10e-9'.format(round((i*pow(10,9))),2)
    elif i < (pow(10,-9)) and i >= (pow(10,-12)):
        return '{}*10e-12'.format(round((i*pow(10,12))),2)
    elif i < (pow(10,-12)) and i >= (pow(10,-15)):
        return '{}*10e-15'.format(round((i*pow(10,15))),2)
    elif i < (pow(10,-15)) and i >= (pow(10,-18)):
        return '{}*10e-18'.format(round((i*pow(10,18))),2)


#z = pow(10,-9)
#print(comparison(z))


A = float(input('Value: '))
B = (input('Unit of measurement: ')).lower()


def tr(A,B):
    if B == 'v':
        N = 10*np.log10(np.power(A,2)/50.0 * 1000.0)
        P = pow(A,2)/50.0
        print('\n',N,'dBm','\n',comparison(P),'W')
    elif B == 'w':
        U = np.sqrt(A*50.0)
        N = 10*np.log10(A * 1000.0)
        print('\n',N,'dBm','\n',comparison(U),'V')
    elif B == 'dbm':
        P = pow(10.0,A/10.0)/1000.0
        U = np.sqrt(P*50.0)
        print('\n',comparison(P),'W','\n',comparison(U),'V')
    else:
        B = (input('Unit of measurement: ')).lower()
        tr(A,B)


tr(A,B)
