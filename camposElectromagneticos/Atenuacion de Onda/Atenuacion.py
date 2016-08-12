# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as sp
import matplotlib.collections as collections
from matplotlib.widgets import Slider, Button, RadioButtons, Cursor

#Espacio para graficar
fig, axes = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
#Diferentes valores de Conductividad
s0=5.8e7
s1=3.8e7
s2=1.86e7
s3=3.54e7
s4=4.50e7
s5=1e5

#se asume que la razón (2a/b)=1
b0=5.8
b=b0/100
a=b/2
landa=np.arange(0.001, 0.99, 0.00001)#será la razón de (landa0/landac)<1
#Longitud de Onda en el vacío-landa0=c/f si n=1
landa0=landa*2*b

f=(sp.c)/landa0

# Longitud de Onda de Corte landac=2b
landac=2*b


#Conductividad del material: Sigma
Sigma=5.8e7
print('sigma is'+str(Sigma))
#constante de atenuacion kgi multiplicada por b**3/2 : Kgi
Kgi=(1/(np.sqrt(120*Sigma*landa0)))*((1+(landa**2))/(np.sqrt(1-(landa**2))))*2*np.sqrt(b)
#n = np.sqrt(1-b)#sacamos la raíz
l, = plt.plot(landa,Kgi, lw=2, color='blue', label='0' )
plt.xlabel('Longitud de Onda/Longitud de Onda de Corte')
plt.ylabel('Kgi*(b^(3/2))')
plt.grid('on')
plt.title('Dependencia de Kgi con la Razon Longitudes de Onda')
plt.grid('on')
plt.axis([0, 1, 0, 1e-4])

#Definimos el espacio que ocuparan los sliders
axcolor = 'Thistle'
amcolor = 'SeaShell'
avcolor='red'
axr = plt.axes([0.25, 0.1, 0.65, 0.03], axisbg=avcolor)

#Creamos los sliders que modificaran b y el radio al gusto del usuario
sb = Slider(axr, 'Longitud b (cm)', 1.5, 7.21, valinit=b0)

rax = plt.axes([0.01, 0.7, 0.105, 0.22], axisbg=amcolor)
radio = RadioButtons(rax, ('Cu', 'Cr', 'Zn','Al','Au'))
def hzfunc(label):
    hzdict = {'Cu':s0, 'Cr':s1, 'Zn':s2, 'Al':s3, 'Au':s4}
    
    global Sigma
    Sigma=hzdict[label]
   # print('sigma is'+str(Sigma))
    Kgi=(1/(np.sqrt(120*Sigma*landa0)))*((1+(landa**2))/(np.sqrt(1-(landa**2))))*2*np.sqrt(b) #hzdict[label]
    ydata = Kgi
    l.set_ydata(ydata)
    fig.canvas.draw_idle()
    
      
radio.on_clicked(hzfunc)


#Se Define la funcion que actualiza la zona de graficos al mover los sliders
def update(val):
    bb = sb.val

    b=bb/100
    Kgi=(1/(np.sqrt(120*Sigma*landa0)))*((1+(landa**2))/(np.sqrt(1-(landa**2))))*2*np.sqrt(b)
    l.set_xdata(landa)
    l.set_ydata(Kgi)


    fig.canvas.draw_idle()
sb.on_changed(update)


resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=amcolor, hovercolor='0.975')
def reset(event):
    sb.reset()

button.on_clicked(reset)



plt.show()