import numpy as np
import matplotlib.pylab as plt

Datos= np.genfromtxt("runge.dat",delimiter=";")
x=Datos[:,0]
y=Datos[:,1]
z=Datos[:,2]
plt.figure()
plt.plot(x,y,label="Velocidad",c="blue")
plt.plot(x,z,label="Posición",c="red")
plt.xlabel("t")
plt.ylabel("y(x)")
plt.legend()
plt.savefig("ArevaloSergioResorte.png")