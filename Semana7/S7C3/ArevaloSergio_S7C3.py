#Ejercicio 1 Terminar lo que hizo en clase + dos preguntas adicionales (en mayusculas en el texto)

import numpy as np
import matplotlib.pylab as plt


# 1) lea los datos de resorte.dat y almacenelos.
# 
datos= np.genfromtxt("resorte.dat")
t=datos[:,0]
a=datos[:,1]

# Los datos corresponden a las posiciones en x de un oscilador (masa resorte) en funcion del tiempo. La ecuacion de movimiento esta dada por 

# Donde a, gamma, y omega son parametros.

# 2) Implemente un algoritmo que le permita, por medio de estimacion bayesiana de parametros, encontrar los parametros correspondientes a los datos d. Para esto debe:

# 2a.) definir una funcion que reciba los parametros que se busca estimar y los datos de tiempo y retorne el modelo  
def resort(a0,gamma0,t0,omega0):
    xt=a0*np.exp(-gamma0*t0)*np.cos(omega0*t0)
    return xt

# 2b.) Definir una funcion que retorne la funcion de verosimilitud
def vero(a_obs, a_new):
    chi = (1.0/2.0)*sum((a_obs-a_new)**2)
    chi2= np.exp(-chi)
    return chi2
# 2c.) Caminata

#condiciones iniciales
aini=7.5
gammaini=0.6
omegaini=18.2

#numero de pasos
iteraciones=100000
sigma=0.1
def funcion(N0, a0, g0, o0):
    As=[]
    Gs=[]
    Os=[]
    Ls=[]
    As.append(a0)
    Gs.append(g0)
    Os.append(o0)
    yin=resort(As[0],Gs[0],t,Os[0])
    Ls.append(vero(a,yin))
    for i in range(N0):
        a2=np.random.normal(As[i],sigma)
        g2=np.random.normal(Gs[i],sigma)
        o2=np.random.normal(Os[i],sigma)
        yin=resort(As[i],Gs[i],t,Os[i])
        y2=resort(a2,g2,t,o2)
        l2=vero(a,y2)
        lvie=vero(a,yin)
        alpha=l2/lvie
        if(alpha>=1.0):
            As.append(a2)
            Gs.append(g2)
            Os.append(o2)
            Ls.append(l2)
        else:
            beta=np.random.uniform(low=0.0, high=1.0, size=1)
            if(beta<=alpha):
                As.append(a2)
                Gs.append(g2)
                Os.append(o2)
                Ls.append(l2)
            else:
                As.append(As[i])
                Gs.append(Gs[i])
                Os.append(Os[i])
                Ls.append(Ls[i])
    return As , Gs , Os , Ls

numero=np.argmax(funcion(100000, 7.5, 0.6, 18.2)[3])
Amplis = funcion(100000, 7.5, 0.6, 18.2)[0]
Gams = funcion(100000, 7.5, 0.6, 18.2)[1]
Omes = funcion(100000, 7.5, 0.6, 18.2)[2]

# 2d.) Seleccione los mejores parametros E IMPRIMA UN MENSAJE QUE DIGA: "LOS MEJORES PARAMETROS SON a=... gamma=... Y omgega=..."
print("LOS MEJORES PARAMETROS SON a= ",Amplis[numero],"gamma= ",Gams[numero],"Y omega= ",Omes[numero])
# 2f.) Grafique sus datos originales y su modelo con los mejores parametros. Guarde su grafica sin mostrarla en Resorte.pdf
plt.figure()
plt.plot(t,a,label="Original",c="red")
plt.plot(t,resort(Amplis[numero],Gams[numero],t,Omes[numero]),label="Mejores parametros",c="blue")
plt.legend()
plt.xlabel("Tiempo")
plt.ylabel("Posición")
plt.savefig("Resorte.pdf")
# 3) SABIENDO QUE omega=np.sqrt(k/m), IMPRIMA UN MENSAJE DONDE EXPLIQUE SI PUEDE O NO DETERMINAR k Y m DE MANERA INDIVIDUAL USANDO EL METODO ANTERIOR. JUSTIFIQUE BIEN SU RESPUESTA (PUEDE ADEMAS HACER PRUEBAS CON EL CODIGO PARA RESPONDER ESTA PREGUNTA).
print("Si seria posible. Sin embargo estos corresponden a valores que me generan otro valor el cual utilizo, por lo que la constantes del resorte y la masa de este tendrian valores ideales para condiciones ya dadas o encontradas de Gamma y amplitud.")


