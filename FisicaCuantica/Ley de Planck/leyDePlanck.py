#Autor: Diego Javier Mena Amado 
## Que te diviertas...
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import scipy.constants
from pylab import plot,xlabel,ylabel,show
from sympy import *

#Ajuste de workstation
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.25)
t = np.arange(0, 0.99, 0.001)
a0 = 0.7
#s = a0*np.sin(2*np.pi*t)
#print (t,a0) #Depurando errores de divisiones por cero halladas
PLANCK =((t**5)*(np.exp(1/(t-a0)-1))**(-1))
l, = plt.plot(t, PLANCK, lw=2, color='red')

#Definimos limites de barrido
#plt.xlim((0.0008, 1))
#plt.ylim((0, 30))
plt.axis([0.01, 1, 0, 30])
x = np.linspace(0.01, 1, 1000)
y = np.linspace(0, 30, 1000)

#Asignamos nombres a nuestro sistema de coordenadas
xlabel("t")
ylabel("x(t)")

#Se añaden constantes debido a falta de comprension de libreria para constantes fisicas
k=1.38*10**(-23)
h=6.62*10**(-34)   #constante de Planck
c=3*10**8

#Se cargan los estilos para las curvas
style = {'family' : 'bold italic','color'  : 'blue','weight' : 'normal','size'   : 14}
style1 = {'family' : 'bold italic','color'  : 'green','weight' : 'normal','size'   : 14}     
style2 = {'family' : 'bold italic','color'  : 'red','weight' : 'normal','size'   : 14}
style3 = {'family' : 'bold italic','color'  : 'black','weight' : 'normal','size'   : 14}
style4 = {'family' : 'bold italic','color'  : 'purple','weight' : 'normal','size'   : 14}

#Se cargan los label's para identificar cada curva y sus desasrrolladores
plt.title('Fisica de Semiconductores', fontdict=style2)
plt.text(0.53, 28, r'$\  Diego \ Javier \ Mena $', fontdict=style3)
plt.text(0.23, 20, r'$\ Ley \ de \ Planck $', fontdict=style)
plt.text(0.52, 18, r'$\ Ley \ de \ Rayleigh-Jeans $', fontdict=style4)
plt.text(0.185, 25, r'$\ Limite \ de \ Wien $', fontdict=style3)

#Ecuación Ley de Planck
plt.plot(x, ((x**5)*(np.exp(1/x)-1))**(-1), 
         x, ((x**5)*(np.exp(1/(0.9*x))-1))**(-1), 
         x, ((x**5)*(np.exp(1/(0.8*x))-1))**(-1))


#Ecuación Rayleigh-Jeans
plt.plot(x, 1/(x**4), x,1/(0.9*x**4),x,1/(0.8*x**4) )

#Ecuación Limite de Wien
plt.plot(x,np.exp(((1)/(x)))*10**(-0.87))


#implementamos Slider para variaciones de Ley de Planck
axcolor = 'lightgoldenrodyellow'
axamp = plt.axes([0.25, 0.1, 0.65, 0.03], axisbg=axcolor)
samp = Slider(axamp, 'Amp', 0.1, 1.3, valinit=a0)


#Establecemos la funcion a variar con el slider
def update(val):
    amp = samp.val
    l.set_ydata(((t**5)*(np.exp(1/(t*amp))-1))**(-1))
    fig.canvas.draw_idle()
samp.on_changed(update)

#Creamos un boton reset para limpiar las variables color y amp
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    samp.reset()
button.on_clicked(reset)

#implementamos Cuadro Selector de Color
rax = plt.axes([0.025, 0.05, 0.15, 0.15], axisbg=axcolor)
radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)

def colorfunc(label):
    l.set_color(label)
    fig.canvas.draw_idle()
radio.on_clicked(colorfunc)

#Mostramos el Grafico
plt.show()