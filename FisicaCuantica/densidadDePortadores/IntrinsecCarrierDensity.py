import numpy as np
import matplotlib.pyplot as plt

from matplotlib.widgets import Slider
import scipy.constants 	as sc
import math
#Constantes Nc(cm-3) Nv(cm-3) Eg(eV)

Si = [3.22e19,1.83e19,1.12]
Ge = [1.03e19,5.35e18,0.66]
GaAs = [4.21e17,9.52e18,1.42]
corte=1
#Configuracion ejes de grafica
x1=100
x2=100000
y1=1
y2=1e17

x = np.linspace(x1, x2, 10000)

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.25, top=0.9)
plt.axis([0.2, 2, y1, y2])
#plt.text(1.4,1, 'Danny Fabian Mora 20112005201\nDiego Javier Mena 20092005053', style='italic',bbox={'facecolor':'red','alpha':0.5, 'pad':10})
plt.xlabel("$Temperature (K)$")
plt.ylabel("$ni \ (cm-3)$")
plt.title("$Intrinsic \ Carrier \ Density $")
plt.grid(True)

#Ecuaciones

def si(x):
    nc=3.22*10**19
    nv=1.83*10**19
    eg=1.12*1.602*10**-19
    return ((math.sqrt(nc*nv))*(np.exp(-(eg)/(2*x*sc.k))))

def ge(x):
    nc=1.03*10**19
    nv=5.35*10**18
    eg=0.6*1.602*10**-19
    return ((math.sqrt(nc*nv))*(np.exp(-(eg)/(2*x*sc.k))))

def gaas(x):
    nc=4.21*10**17
    nv=9.52*10**18
    eg=1.42*1.602*10**-19
    return ((math.sqrt(nc*nv))*(np.exp(-(eg)/(2*x*sc.k))))

f1, = plt.plot(1000/x, ge(x), lw=1, color='blue')#Grafica la funcion 1
f2, = plt.plot(1000/x, si(x), lw=1, color='green')#Grafica la funcion 2
f3, = plt.plot(1000/x, gaas(x), lw=1, color='red')#Grafica la funcion 3

p1, = plt.plot(corte, ge(1000/corte), 'o',color='blue')
p2, = plt.plot(corte, si(1000/corte), 'o',color='green')
p3, = plt.plot(corte, gaas(1000/corte), 'o',color='red')

#Configuracion Slider [x,y,ancho,alto]
axdot = plt.axes([0.1, 0.1, 0.8, 0.05], axisbg='w')
sdot = Slider(axdot, 'Cursor', 0.2, 2, valinit=corte,color='#A5665D')#Longitud dinamica del Slider, esta coincide con el eje x de la grafica.

def update(val):  
    dot = sdot.val#Este valor es el punto en donde se ubica el slider.    
    p1.set_xdata(dot)
    p1.set_ydata(ge(1000/dot))      
    p2.set_xdata(dot)
    p2.set_ydata(si(1000/dot))
    p3.set_xdata(dot)
    p3.set_ydata(gaas(1000/dot))
    fig.canvas.draw()
sdot.on_changed(update)

plt.show()
