#Ejercicio 0
#Lean el capitulo 5 del Landau (ver el programa del curso).
import numpy as np
import random
import matplotlib.pylab as plt
#Ejercicio 1
# Usando los generadores de numeros aleatorios de numpy (https://docs.scipy.org/doc/numpy-1.15.1/reference/routines.random.html):
# a) Genere 1000 numeros aleatorios que sigan una distribucion uniforme y esten entre -10 y 10. Haga un histograma y guardelo sin mostrarlo en un archivo llamado uniforme.pdf
xu=np.random.uniform(-10,10,1000)
plt.figure()
plt.hist(xu,bins=15)
plt.title("Distribucion uniforme")
plt.savefig("uniforme.pdf")
# a) Genere 1000 numeros aleatorios que sigan una distribucion gausiana centrada en 17 y de sigma 5. Haga un histograma y guardelo sin mostrarlo en un archivo llamado gausiana.pdf
xg= np.random.normal(17, 5, 100)
plt.figure()
plt.hist(xg,bins=10)
plt.title("Distribucion Gausiana")
plt.savefig("gausiana.pdf")
# Ejercicio 2
# Escriba un programa en Python que: 
# Genere puntos aleatorios distribuidos uniformemente dentro de un cuadrado de lado 30.5. Grafique sus puntos y guarde la grafica sin mostrarla en un archivo llamado cuadrado.pdf. 
# Genere puntos aleatorios distribuidos uniformemente dentro de circulo de radio 23. Grafique sus puntos y guarde la grafica sin mostrarla en un archivo llamado circulo.pdf. 
x=np.random.uniform(-30,30,10000)
y=np.random.uniform(-30,30,10000)

condicion=np.where(x**2+y**2<23**2)
xcon=x[condicion]
ycon=y[condicion]
plt.figure()
plt.scatter(x,y)
plt.scatter(xcon,ycon)
plt.title("Circulo")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("circulo.pdf")

x1=np.random.uniform(-10,40.5,1000)
y1=np.random.uniform(-10,40.5,1000)
xcua=np.random.uniform(0,30.5,1000)
ycua=np.random.uniform(0,30.5,1000)

plt.figure()
plt.scatter(x1,y1)
plt.scatter(xcua,ycua)
plt.title("Cuadrado")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("cuadrado.pdf")
# Ejercicio 3 
# Lean sobre caminatas aleatorias.


# Ejercicio 4
# Tome los puntos distribuidos aleatoriamente dentro del cuadrado y haga que cada punto siga una caminata aleatoria de 100 pasos. 
# La magnitud de los pasos de esta caminata debe seguir una distribucion gaussiana centrada en el punto y de sigma igual a 0.25
# Implemente condiciones de frontera periodicas: si un punto se "sale" de cuadrado por un lado, "entra" por el otro  
def caminata1(a0,b0,s0):
    xcua2=a0
    ycua2=b0
    sigma= s0
    for i in range(100):
        newxcua=np.random.normal(xcua2,sigma)
        newycua=np.random.normal(ycua2,sigma)
        xcua2=newxcua
        ycua2=newycua
        for k in range(len(a0)):
            if xcua2[k]>30.5:
                xcua2[k]= xcua2[k]-30.5
            if ycua2[k]>30.5:
                ycua2[k]= ycua2[k]-30.5
            if xcua2[k]<0:
                xcua2[k]=30.5-(abs(xcua2[k]))
            if ycua2[k]<0:
                ycua2[k]=30.5-(abs(ycua2[k]))
    return xcua2,ycua2
# Grafique la distribucion final de puntos y guarde dicha grafica sin mostrarla en un archivo llamado DistCaminata.pdf
# Grafique la caminata de UNO de sus puntos y guarde dicha grafica sin mostrarla en un archivo llamado puntoCaminata.pdf
plt.figure()
plt.scatter(caminata1(xcua,ycua,0.25)[0],caminata1(xcua,ycua,0.25)[1],label="Caminados")
plt.scatter(xcua,ycua,label="Originales")
plt.title("Sigma=0.25")
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("DistCaminata.pdf")

def caminata2(a0,b0,s0):
    xcua2=a0
    ycua2=b0
    arrx=[]
    arry=[]
    sigma= s0
    for i in range(100):
        newxcua=np.random.normal(xcua2,sigma)
        newycua=np.random.normal(ycua2,sigma)
        xcua2=newxcua
        ycua2=newycua
        for k in range(len(a0)):
            if xcua2[k]>30.5:
                xcua2[k]= xcua2[k]-30.5
            if ycua2[k]>30.5:
                ycua2[k]= ycua2[k]-30.5
            if xcua2[k]<0:
                xcua2[k]=30.5-(abs(xcua2[k]))
            if ycua2[k]<0:
                ycua2[k]=30.5-(abs(ycua2[k]))
        arrx.append(xcua2[1])
        arry.append(ycua2[1])
    return arrx,arry
plt.figure()
plt.plot(caminata2(xcua,ycua,0.25)[0],caminata2(xcua,ycua,0.25)[1],label="Caminados")
plt.title("Sigma=0.25")
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("puntoCaminata.pdf")
# Repita el proceso para sigma = 0.00025 y sigma= 2.5. Grafique la caminata de UNO de sus puntos para los distintos sigmas y guardela sin mostrarla en sigmaCaminata.pdf
plt.figure()
plt.subplot(1,2,1)
plt.plot(caminata2(xcua,ycua,0.00025)[0],caminata2(xcua,ycua,0.00025)[1],label="Caminados")
plt.title("Sigma=0.00025")
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")

plt.subplot(1,2,2)
plt.plot(caminata2(xcua,ycua,2.5)[0],caminata2(xcua,ycua,2.5)[1],label="Caminados")
plt.title("Sigma=2.5")
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("sigmaCaminata.pdf")
# Repita el proceso para condiciones abiertas: si un punto se "sale" del cuadrado deja de ser considerado en la simulacion.

# Si le queda tiempo puede:

##################################################################################################################################################################
############################################################ Ejercicio  ##########################################################################
##################################################################################################################################################################

#difusion: una gota de crema en un Cafe.
#
#Condiciones iniciales:
#Cafe: 10000 particulas distribuidas uniformemente dentro de un circulo de radio igual a raiz de 230
x=np.random.uniform(-30,30.5,10000)
y=np.random.uniform(-30,30.5,10000)

condica = np.where(x**2+y**2<230)

xca = x[condica]
yca = y[condica]
#Crema: 100 particulas distribuidas uniformemente dentro de un circulo de radio igual a raiz de 2
#

x2=np.random.uniform(-30,30.5,10000)
y2=np.random.uniform(-30,30.5,10000)

condicre = np.where(x2**2+y2**2<2)

xcre = x2[condicre]
ycre = y2[condicre]


#Nota: si su codigo se esta demorando mucho en correr, puede usar 1000 particulas de cafe en vez de 10000.
#
# 1) Haga una grafica de las condiciones iniciales donde los dos tipos de particulas tengan distintos colores. Guarde dicha grafica sin mostrarla en CafeLecheIni.pdf
#
plt.figure()
plt.scatter(xca,yca)
plt.scatter(xcre,ycre)
plt.savefig("CafeLecheIni.pdf")
#2) Todas las particulas deben hacer una caminata aleatoria de 1000 pasos. Los pasos en las coordenadas x y deben seguir una distribucion gausiana de sigma 2.5. Si va a usar coordenadas polares elija un sigma apropiado.
#
def caminata3(a0,b0):
    xcua2=a0
    ycua2=b0
    sigma=2.5
    for i in range(1000):
        newxca=np.random.normal(xcua2,sigma)
        newyca=np.random.normal(ycua2,sigma)
        xcua2=newxca
        ycua2=newyca
    return xcua2,ycua2
    

#3) Condiciones de frontera: implemente unas condiciones tales que si la particulas "sale" del circulo, usted vuelva a dar el paso. Si no puede implementar solo las condiciones antes descritas, debe al menos escribir comentarios explicando que hace cada linea de codigo de las condiciones propuestas (comentado abajo)
sigma=2.5
indexcafe=np.where((caminata3(xca,yca)[0]*caminata3(xca,yca)[0]+caminata3(xca,yca)[1]*caminata3(xca,yca)[1])>230)
indexcrema=np.where((caminata3(xcre,ycre)[0]*caminata3(xcre,ycre)[0]+caminata3(xcre,ycre)[1]*caminata3(xcre,ycre)[1])>230)
while(len(indexcafe[0])>1):
	caminata3(xca,yca)[0][indexcafe]=xca[indexcafe] + np.random.normal(0,sigma)
	caminata3(xca,yca)[1][indexcafe]=yca[indexcafe] + np.random.normal(0,sigma)
	indexcafe=np.where((caminata3(xca,yca)[0]*caminata3(xca,yca)[0]+caminata3(xca,yca)[1]*caminata3(xca,yca)[1])>=230)
while(len(indexcrema[0])>1):
	caminata3(xcre,ycre)[0][indexcrema]=xcre[indexcrema] + np.random.normal(0,sigma)
	caminata3(xcre,ycre)[1][indexcrema]=ycre[indexcrema] + np.random.normal(0,sigma)
	indexcrema=np.where((caminata3(xcre,ycre)[0]*caminata3(xcre,ycre)[0]+caminata3(xcre,ycre)[1]*caminata3(xcre,ycre)[1])>=230)
# 4) Haga una grafica de las posiciones finales de las particulas despues de la caminata donde los dos tipos de particulas tengan distintos colores. Guarde dicha grafica sin mostrarla en CafeLecheFin.pdf
#
plt.figure()
plt.scatter(caminata3(xca,yca)[0],caminata3(xca,yca)[1])
plt.scatter(caminata3(xcre,ycre)[0],caminata3(xcre,ycre)[1])
plt.savefig("CafeLecheFin.pdf")

#Una posible implementacion de condiciones de frontera. Trate de hacer la suya propia sin usar esta. 
#Si usa esta (obtiene menos puntos) debe comentar cada una de las lineas explicando en palabras que hace el codigo. Debe tambien naturalmente usar los nombres de variables que uso en el resto de su codigo propio.
#indexcafe=np.where((xcafenuevo*xcafenuevo+ycafenuevo*ycafenuevo)>230)
#indexcrema=np.where((xcremanuevo*xcremanuevo+ycremanuevo*ycremanuevo)>230)
#while(len(indexcafe[0])>1):
#	xcafenuevo[indexcafe]=xcafe[indexcafe] + np.random.normal(0,sigma)
#	ycafenuevo[indexcafe]=ycafe[indexcafe] + np.random.normal(0,sigma)
#	indexcafe=np.where((xcafenuevo*xcafenuevo+ycafenuevo*ycafenuevo)>=230)
#while(len(indexcrema[0])>1):
#	xcremanuevo[indexcrema]=xcrema[indexcrema] + np.random.normal(0,sigma)
#	ycremanuevo[indexcrema]=ycrema[indexcrema] + np.random.normal(0,sigma)
#	indexcrema=np.where((xcremanuevo*xcremanuevo+ycremanuevo*ycremanuevo)>=230) 
