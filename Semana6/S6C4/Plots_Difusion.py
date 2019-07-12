import numpy as np
import matplotlib.pylab as plt

Datos= np.loadtxt("placa.txt")
plt.figure()
plt.imshow(Datos)
plt.savefig("PlacaInicial.png")

Datos2= np.loadtxt("placa2.txt")
plt.figure()
plt.imshow(Datos2)
plt.savefig("Placa100.png")

Datos3= np.loadtxt("placa3.txt")
plt.figure()
plt.imshow(Datos3)
plt.savefig("Placa2500.png")