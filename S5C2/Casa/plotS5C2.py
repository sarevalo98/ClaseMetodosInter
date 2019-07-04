import numpy as np
import matplotlib.pylab as plt

Datos= np.genfromtxt("euler.dat",delimiter=";")
x=Datos[:,0]
y=Datos[:,1]
plt.figure()
plt.plot(x,y)
plt.savefig("EulerS5C2PLOT.png")