import numpy as np
import matplotlib.pylab as plt
import random
import matplotlib.pyplot as plt

datos=np.genfromtxt("Canal_ionico.txt", delimiter="	")
x=datos[:,1]
y=datos[:,0]

def funcion(x0,y0):
    r0=x0**2+y0**2
    return np.sqrt(r0)

def metro():
    sigma=0.5
    x1=[]
    y1=[]
    r=[]
    x0=np.random.uniform(low=min(x),high=max(x),size=1)
    y0=np.random.uniform(low=min(y),high=max(y),size=1)
    x1.append(x0)
    y1.append(y0)
    r0=funcion(x1[0],y1[0])
    r.append(r0)
    for i in range(100):
        x2=np.random.normal(x1[i],sigma)
        y2=np.random.normal(y1[i],sigma)
        alpha=funcion(x2,y2)/funcion(x1[i],y1[i])
        if(alpha>=1.0):
            r.append(funcion(x2,y2))
            x1.append(x2)
            x1.append(x2)
        else:
            beta=np.random.uniform(low=0,high=1.0,size=1)
            if(beta<=alpha):
                r.append(funcion(x2,y2))
                x1.append(x2)
                y1.append(y2)
            else:
                r.append(r[i])
                x1.append(x1[i])
                y1.append(y1[i])
    return r, x1, y1

erre=metro()[0]
x_1=metro()[1]
y_2=metro()[2]
for i in range(len(erre)):
    if(erre[i]==max(erre)):
        mex=x_1[i]
        mey=y_1[i]
plt.figure()
fig, ax = plt.subplots()
plt.axis('equal')
circle1 = plt.Circle((mex, myy), max(erre), color='r',fill=False)
ax.add_artist(circle1)
plt.scatter(x,y)
plt.savefig("Canal_ionico.png")
plt.close()