import numpy as np 
import matplotlib.pylab as plt

datos= np.genfromtxt("datosderiv.dat"delimiter=";")
Xcos=datos[0,:]
Yder=datos[1,:]
plt.figure()
plt.plot(Yder,label="Derivada cos(x)",c="red")
plt.plot(Xcos,label="cos(x)",c="blue")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("S5C1PLOT.pdf")