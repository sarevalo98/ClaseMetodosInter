import numpy as np
import matplotlib.pylab as plt

Datos= np.genfromtxt("datos.dat",delimiter=";")
t=Datos[:,0]
v=Datos[:,1]

plt.figure()
plt.plot(t,v)
plt.xlabel("t")
plt.ylabel("v")
plt.savefig("ArevaloSergio.pdf")