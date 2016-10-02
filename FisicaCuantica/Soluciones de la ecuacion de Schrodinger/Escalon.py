import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.animation as animation
import scipy.constants   as sc
from matplotlib.widgets import Slider, Button, RadioButtons
from matplotlib.figure import Figure

from matplotlib import colors
from Tkinter import *

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
figure = Figure()
canvas = FigureCanvas(figure)

 
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.25)
#Valor del potencial en eV:
Vo=1

#Ancho del potencial en metros:
a=1.5*10**-9 #Del orden de los nanometros

#Valores de energia de la particula en eV:
En=np.linspace(0.01,1.5,1000)


T=[]
R=[]

for E in En:
    if E<=Vo:
        T.append(0.0)
        R.append(1.0)
    else:
        x=4*np.sqrt(E**2-E*Vo)/((E**(1/2.0)+np.sqrt(E-Vo))**2)
        T.append(x)
        R.append(1-x)


a0 = 1
f0 = 1.5*10**-9
l, = plt.plot(En,T, lw=2, color='red')
ll, = plt.plot(En,R, lw=2, color='blue')
dot, = plt.plot(En[300],T[300],'bo', markersize=18)
dot2, = plt.plot(En[300],R[300],'ro', markersize=18)
plt.text(0.8,1.1, 'Danny Fabian Mora 20112005201\nDiego Javier Mena 20092005053', style='italic',bbox={'facecolor':'red','alpha':0.5, 'pad':10})
plt.axis([0, 1.5, -0.3, 1.3])



axcolor = 'lightgoldenrodyellow'


axamp = plt.axes([0.1, 0.15, 0.65, 0.03], axisbg=axcolor)
axpunto=plt.axes([0.1, 0.05, 0.65, 0.03], axisbg=axcolor)

samp = Slider(axamp, 'Vo', 0.01, 1.5, valinit=a0)
punto = Slider(axpunto, 'Posicion', 0, 1000, valinit=300)

def update(val):
	
	Vo=samp.val
	p=punto.val
	T=[]
	R=[]
	
	for E in En:
	    if E<=Vo:
		T.append(0.0)
		R.append(1.0)
	    else:
		x=4*np.sqrt(E**2-E*Vo)/((E**(1/2.0)+np.sqrt(E-Vo))**2)
		T.append(x)
		R.append(1-x)

	l.set_ydata(T)
	ll.set_ydata(R)
	dot.set_data(En[int(p)],T[int(p)])
	dot2.set_data(En[int(p)],R[int(p)])
	fig.canvas.draw_idle()

samp.on_changed(update)
punto.on_changed(update)
plt.plot(En,T,color=plt.cm.gist_rainbow(50))
plt.plot(En,R,color=plt.cm.gist_rainbow(150))
plt.show()
