import numpy as np
import matplotlib.pylab as plt

Datos= np.genfromtxt("datos.dat",delimiter=";")
x=Datos[:,0]
y=Datos[:,1]
plt.figure()
plt.plot(x,y)
plt.savefig("GraficaS5C2PLOT.pdf")
