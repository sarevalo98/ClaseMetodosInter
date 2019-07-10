import numpy as np
import matplotlib.pylab as plt

Datos= np.genfromtxt("datos.dat",delimiter=";")
x=Datos[:,0]
a=Datos[:,1]
Datos3= np.genfromtxt("datos3.dat",delimiter=";")
x3=Datos3[:,0]
a3=Datos3[:,1]
plt.figure()
plt.plot(x,a,c="green")
plt.plot(x3,a3,label="arrf",c="green")
plt.xlabel("X")
plt.ylabel("A")
plt.legend()
plt.savefig("ArevaloSergioS6C2.pdf")