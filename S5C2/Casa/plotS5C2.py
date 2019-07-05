import numpy as np
import matplotlib.pylab as plt

Datos= np.genfromtxt("euler.dat",delimiter=";")
x=Datos[:,0]
y=Datos[:,1]
plt.figure()
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y(x)")
plt.savefig("EulerS5C2PLOT.pdf")

Datos2= np.genfromtxt("runge.dat",delimiter=";")
x_2=Datos2[:,0]
y_2=Datos2[:,1]
plt.figure()
plt.plot(x_2,y_2)
plt.xlabel("x")
plt.ylabel("y(x)")
plt.savefig("RungeS5C2PLOT.pdf")