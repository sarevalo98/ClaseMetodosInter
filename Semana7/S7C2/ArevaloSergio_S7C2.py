# Ejercicio 1

import numpy as np
import matplotlib.pylab as plt


# Use esta funcion que recibe un valor x y retorna un valor f(x) donde f es la forma funcional que debe seguir su distribucion. 
def mifun(x):
    x_0 = 3.0
    a = 0.01
    return np.exp(-(x**2))/((x-x_0)**2 + a**2)
x1=np.linspace(-4,4,1000)
# Dentro de una funcion que reciba como parametros el numero de pasos y el sigma de la distribucion gausiana que va a usar para calcular el paso de su caminata, implemente el algortimo de Metropolis-Hastings. Finalmente, haga un histograma de los datos obtenidos y grafique en la misma grafica, la funcion de distribucion de probabilidad fx (Ojo, aca debe normalizar). Guarde la grafica sin mostrarla en un pdf. Use plt.savefig("histograma_"+str(sigma)+"_"+str(pasos)+".pdf"), donde sigma y pasos son los parametros que recibe la funcion. 
def funcion(N0,sigma):
    pasos=[]
    x= 8*np.random.random()-4
    pasos.append(x)
    for i in range(N0):
        x2=np.random.normal(pasos[i],sigma)
        alpha=mifun(x2)/mifun(pasos[i])
        if(alpha>1.0):
            pasos.append(x2)
        else:
            beta=np.random.uniform(low=0.0, high=1.0, size=1)
            if(beta<=alpha):
                pasos.append(x2)
            else:
                pasos.append(pasos[i])
    return pasos
def rectangulos(x0):
    suma=0
    h=(4-(-4))/(1000-1)
    suma= np.sum(mifun(x0)*h)
    return suma

plt.figure()
plt.hist(funcion(100000, 5), density=True,bins=25)
plt.plot(x1,mifun(x1)/rectangulos(x1))
plt.title("Primera condición")
plt.savefig("histograma_5_100000.pdf")

plt.figure()
plt.hist(funcion(100000,0.2), density=True,bins=25)
plt.plot(x1,mifun(x1)/rectangulos(x1))
plt.title("Segunda condición")
plt.savefig("histograma_0.2_100000.pdf")

plt.figure()
plt.hist(funcion(100000,0.01), density=True,bins=25)
plt.plot(x1,mifun(x1)/rectangulos(x1))
plt.title("Tercera condición")
plt.savefig("histograma_0.01_100000.pdf")

plt.figure()
plt.hist(funcion(1000, 0.1), density=True,bins=25)
plt.plot(x1,mifun(x1)/rectangulos(x1))
plt.title("Cuarta condición")
plt.savefig("histograma_0.1_1000.pdf")

plt.figure()
plt.hist(funcion(100000,0.1), density=True,bins=25)
plt.plot(x1,mifun(x1)/rectangulos(x1))
plt.title("Quinta condición")
plt.savefig("histograma_0.1_100000.pdf")
# Cuando haya verificado que su codigo funciona, use los siguientes parametros:
# sigma = 5, pasos =100000 
# sigma = 0.2, pasos =100000 
# sigma = 0.01, pasos =100000 
# sigma = 0.1, pasos =1000 
# sigma = 0.1, pasos =100000 
# este puede ser muy demorado dependiendo del computador: sigma = 0.1, pasos =500000 

# Al ejecutar el codigo, este debe generar 6 (o 5) graficas .pdf una para cada vez que se llama a la funcion.
