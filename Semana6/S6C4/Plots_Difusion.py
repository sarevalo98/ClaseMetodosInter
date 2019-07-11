import numpy as np
import matplotlib.pylab as plt

Datos= np.loadtxt("placa.txt")
plt.figure()
plt.imshow(Datos)
plt.savefig("PlacaT.png")