import numpy as np
import matplotlib.pylab as plt

Datos= np.genfromtxt("datos.dat",delimiter=";")
x=Datos[:,0]
a=Datos[:,1]
Datos2= np.genfromtxt("datos2.dat",delimiter=";")
x2=Datos2[:,0]
a2=Datos2[:,1]
plt.figure()
plt.plot(x,a,c="green")
plt.plot(x2,a2,label="arrf",c="green")
plt.title("Extremos fijos")
plt.xlabel("X")
plt.ylabel("A")
plt.savefig("ExtremosFijos.png")

Datos3= np.genfromtxt("datos3.dat",delimiter=";")
x3=Datos3[:,0]
a3=Datos3[:,1]
Datos4= np.genfromtxt("datos4.dat",delimiter=";")
x4=Datos4[:,0]
a4=Datos4[:,1]
plt.figure()
plt.plot(x3,a3,c="green")
plt.plot(x4,a4,c="green")
plt.title("Extremo suelto")
plt.xlabel("X")
plt.ylabel("A")
plt.savefig("ExtremosFijoYsuelto.png")

Datos5= np.genfromtxt("datos5.dat",delimiter=";")
x5=Datos5[:,0]
a5=Datos5[:,1]
Datos6= np.genfromtxt("datos6.dat",delimiter=";")
x6=Datos6[:,0]
a6=Datos6[:,1]
plt.figure()
plt.plot(x5,a5,c="green")
plt.plot(x6,a6,c="green")
plt.title("SEN()")
plt.xlabel("X")
plt.ylabel("A")
plt.savefig("FuncionSen.png")