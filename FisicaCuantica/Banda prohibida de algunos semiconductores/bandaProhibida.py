# Autor: Diego Javier Mena Amado

#Librerias necesarias para ejecutar el cdigo
import numpy as num
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plot
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler
import scipy.constants as sc
import matplotlib.patches as mpatches

import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

home = Tk.Tk()
home.wm_title("Banda prohibida de los semiconductores")
#Declaracion de limites    
f = Figure()
plota = f.add_subplot(111)
#Declaracion de Variables
a = num.arange(0.1, 1000, 0.1)#Temperatura
#Definicion de las funciones
b=3.470-((7.70*10**(-4))*a**2/(a+600))  #GaN
c=2.340-((6.20*10**(-4))*a**2/(a+460)) #GaP
d=1.519-((5.41*10**(-4))*a**2/(a+204)) #GaAS
e=1.425-((4.50*10**(-4))*a**2/(a+327)) #InP
g=1.170-((4.73*10**(-4))*a**2/(a+636)) #Si
h=0.744-((4.77*10**(-4))*a**2/(a+235)) #Ge

#Se les asigna el label correspondiente a cada eje
plota.plot(a,b,color='y',label='GaN')
plota.plot(a,c,color='b',label='GaP')
plota.plot(a,d,color='g',label='GaAS')
plota.plot(a,e,color='black',label='InP')
plota.plot(a,g,color='r',label='Si')
plota.plot(a,h,color='cyan',label='Ge')
plota.set_xlabel('Temperatura (Kelvin)')
plota.set_ylabel('Eg(eV)',rotation='horizontal')
plota.axis([200, 1000,0.5,3.5])
plota.legend(loc=1)
# Muestra la grafica-------------------------------------------------
plota.set_title('Banda prohibida de los semiconductores')
f.tight_layout()
plota.grid(True)

canvas = FigureCanvasTkAgg(f,master=home)
canvas.show()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

toolbar = NavigationToolbar2TkAgg(canvas, home)
toolbar.update()
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
#Proceso de seleccion del teclado
R = "right"
L = "left"
U = "up"
D = "down"
x = 300
state=0
var = Tk.StringVar()
label = Tk.Label(home, textvariable=var, fg="black", bg="white",  font = "Helvetica 14 bold italic")
var.set("Utilice las flechas horizontales del teclado para desplazarce por la grafica")
def graficar(x):
        if state==5:
            y=0.744-((4.77*10**(-4))*x**2/(x+235)) #Ge
        elif state==4:
            y=1.170-((4.73*10**(-4))*x**2/(x+636)) #Si
        elif state==3:
            y=1.425-((4.50*10**(-4))*x**2/(x+327)) #InP
        elif state==2:
            y=1.519-((5.41*10**(-4))*x**2/(x+204)) #GaAS
        elif state==1:
            y=2.340-((6.2*10**(-4))*x**2/(x+460))  #GaP
        else:
            y=3.470-((7.7*10**(-4))*x**2/(x+600))  #GaN
        n = num.linspace(x,x,2)
        plota.cla()
        plota.plot(a,b,color='y',label='GaN')
        plota.plot(a,c,color='b',label='GaP')
        plota.plot(a,d,color='g',label='GaAS')
        plota.plot(a,e,color='black',label='InP')
        plota.plot(a,g,color='r',label='Si')
        plota.plot(a,h,color='cyan',label='Ge')
        plota.set_xlabel('Temperatura (Kelvin)')
        plota.set_ylabel('Eg(eV)',rotation='horizontal')
        plota.axis([200, 1000,0.5,3.5])
        plota.legend(loc=1)
        # Muestra la grafica-------------------------------------------------
        plota.set_title('Banda prohibida de los semiconductores')
        f.tight_layout()
        plota.grid(True)
        plota.scatter([x, ], [y, ], 50, color='red')
        canvas.draw()
        var.set("Valores sobre la curva\t Eg= "+str(y)+" con T= "+str(x))
def on_key_event(event):
    #Flecha de abajo
    if event.key==D:
        global state
        global a
        global b
        global x 
        x = x
        if state==5:
            state=0
        else:
            state=state+1
        graficar(x)
    #Flecha de arriba
    elif event.key==U:
        global state
        global a
        global b
        global x 
        x = x
        if state==0:
            state=5
        else:
            state=state-1
        graficar(x)
    #Flecha derecha
    elif event.key==R:
        global a
        global b
        global x 
        if x>=1000:
            x=1000
        else:
            x = x + 10
        graficar(x)
    #Flecha Izquierda
    elif event.key==L:
        global a
        global b
        global x 
        if x<=0:
            x=0
        else:
            x = x - 10
        graficar(x)
    else:
        pass
    key_press_handler(event, canvas, toolbar)
plot.text(4*10**(-6),1*10**(6) , r'$\ Area $')
canvas.mpl_connect('key_press_event', on_key_event)
label.pack(side="bottom", ipady=20)
#Continue el proceso
Tk.mainloop()
