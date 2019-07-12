import numpy as np
import matplotlib.pylab as plt

Datos= np.loadtxt("placa.txt")
Datos2= np.loadtxt("placa2.txt")
Datos3= np.loadtxt("placa3.txt")
plt.figure()
plt.subplot(1,3,1)
plt.imshow(Datos)
plt.title("Placa inicial")
plt.colorbar()

plt.subplot(1,3,2)
plt.imshow(Datos2)
plt.title("Placa en T=100")
plt.colorbar()

plt.subplot(1,3,3)
plt.imshow(Datos3)
plt.title("Placa en T=2500")
plt.colorbar()
plt.savefig("PlacaFija.png")