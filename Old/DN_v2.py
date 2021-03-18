# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 09:58:22 2019

@author: User
"""



import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('classic')

fig, ax = plt.subplots()


plt.rcParams.update({'font.size': 18,'figure.dpi': 100.0,'axes.labelsize': 11.0,'grid.linewidth': 1})

legend = ax.legend(loc='lower center', shadow=True, fontsize='x-large')
legend.get_frame().set_facecolor('C0')

ax.set_xlabel("Angle of rotation , deg", fontsize=24)
ax.set_ylabel("Power, dBm", fontsize=24)

for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(24)

ax2 = plt.subplot(111)

ax2.xaxis.set_ticks_position('both')
ax2.yaxis.set_ticks_position('both')

for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(24)

x1 = [-49.2,-49.6,-49.8,-49.5,-47.9,-45.8,-43.6,-41.3,
      -39.2,-37.6,-36.0,-34.6,-33.5,-32.7,-32.0,-31.5,
      -31.2,-31.1,-31.3,-31.6,-32.2,-33.0,-34.1,-35.5,
      -37.0,-38.9,-40.9,]

x2 = [-41.8,-41.0,-40.1,-39.3,-38.3,-37.4,-36.5,-35.5,
      -34.6,-33.8,-33.1,-32.5,-32.0,-31.6,-31.3,-31.2,
      -31.2,-31.5,-32.0,-32.7,-33.6,-34.7,-36.2,-37.9,
      -39.7,-41.8,-43.8,]

x3 = [-43.1,-42.2,-41.0,-39.9,-38.7,-37.6,-36.4,-35.3,
      -34.2,-33.2,-32.4,-31.7,-31.0,-30.5,-30.2,-30.0,
      -30.0,-30.3,-30.8,-31.6,-32.6,-33.8,-35.3,-37.1,
      -38.9,-40.8,-42.7,]

y1 = [64,62,60,58,56,54,52,50,48,46,44,42,40,38,36,34,
      32,30,28,26,24,22,20,18,16,14,12,]


kwargs = dict(fontsize=24)


plt.figure(1)
plt.title("Beam(upper) (01.03.2019)", **kwargs)
plt.plot(y1,x1,'--',label='1f',lw=3)
plt.plot(y1,x2,'.-.',color='k',label='3f',lw=3)
plt.plot(y1,x3,label='3f',lw=3)
plt.grid(True,ls='solid',lw=1.5)
plt.legend(fontsize=18,frameon=True);
plt.show()

import matplotlib
matplotlib.axes.Axes.plot
matplotlib.pyplot.plot
matplotlib.axes.Axes.legend
matplotlib.pyplot.legend
