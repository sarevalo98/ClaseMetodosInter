import numpy as np
import matplotlib.pylab as plt

Datos= np.genfromtxt("datos.dat",delimiter=";")
t=Datos[:,0]
v=Datos[:,1]
Datos2= np.genfromtxt("datos2.dat",delimiter=";")
t2=Datos2[:,0]
v2=Datos2[:,1]
plt.figure()
plt.plot(t,v,label="Original",c="red")
plt.plot(t2,v2,label="Final",c="blue")
plt.xlabel("t")
plt.ylabel("v")
plt.legend()
plt.savefig("ArevaloSergio.png")