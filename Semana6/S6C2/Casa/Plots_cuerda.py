import numpy as np
import matplotlib.pylab as plt

Datos= np.genfromtxt("datos.dat",delimiter=";")
x=Datos[:,0]
a=Datos[:,1]
Datos2= np.genfromtxt("datos2.dat",delimiter=";")
x2=Datos2[:,0]
a2=Datos2[:,1]
Datos3= np.genfromtxt("datos3.dat",delimiter=";")
x3=Datos3[:,0]
a3=Datos3[:,1]
plt.figure()
plt.plot(x,a,label="Inicial",c="red")
plt.plot(x2,a2,label="arrAf",c="blue")
plt.plot(x3,a3,label="arrf",c="green")
plt.xlabel("X")
plt.ylabel("A")
plt.legend()
plt.savefig("ArevaloSergioS6C2.pdf")