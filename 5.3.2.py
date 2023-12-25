import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D as ax

x = np.arange(-10,11,1)
y = np.arange(-10,11,1)
X, Y = np.meshgrid(x,y)

def fun1(x,y):
    return np.sqrt(np.abs(x)) + np.sqrt(np.abs(y))

def fun2(x,y):
    return x - y

def fun3(x,y):
    return 2*x + 3+y

def fun4(x,y):
    return x + y

def fun5(x,y):
    return 2 + 2*x + 2+y - x - y

fig, ax = plt.subplots(2, 3, figsize=(25,10), subplot_kw={'projection': '3d'}, sharex=True, sharey=True)
ax = ax.flatten()
Z1 = fun1(X,Y)
Z2 = fun2(X,Y)
Z3 = fun3(X,Y)
Z4 = fun4(X,Y)
Z5 = fun5(X,Y)

ax[0].plot_surface(X,Y,Z1, cmap='plasma')
ax[0].set_title('z = x^0.25 + y^0.25')

ax[1].plot_surface(X,Y,Z2, cmap='Spectral')
ax[1].set_title('z = x^2 - y^2')

ax[2].plot_surface(X,Y,Z3, cmap='OrRd')
ax[2].set_title('z = 2x + 3y')

ax[3].plot_surface(X,Y,Z4, cmap='RdPu')
ax[3].set_title('z = x^2 + y^2')

ax[4].plot_surface(X,Y,Z5, cmap='YlGn')
ax[4].set_title('z = 2 + 2x + 2y - x^2 - y^2')
plt.show()