import numpy as np
import matplotlib.pylab as plt

Datos= np.genfromtxt("runge.dat",delimiter=";")
x=Datos2[:,0]
y=Datos2[:,1]
plt.figure()
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y(x)")
plt.savefig("ArevaloSergioResorte.pdf")