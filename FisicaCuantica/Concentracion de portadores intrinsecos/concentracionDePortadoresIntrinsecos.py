# Autor: Diego Javier Mena

#Librerias necesarias para ejecutar el codigo
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
home.wm_title("Concentracion de portadores intrinsecos")
#Declaracion de limites    
f = Figure()
plota = f.add_subplot(111)
#Declaracion de Variables
a = num.linspace(200,700,5000)#Temperatura desde 200 hasta 700 kelvin
#Definicion de las funciones
mnSi=1.08*sc.m_e    
mnGaAs=0.068*sc.m_e
mnGe=0.55*sc.m_e
mnGaN=0.19*sc.m_e
mnGaP=0.9*sc.m_e
mnInP=0.07*sc.m_e

mpSi=1.1*sc.m_e  
mpGaAs=0.5*sc.m_e
mpGe=0.39*sc.m_e
mpGaN=0.8*sc.m_e
mpGaP=0.9*sc.m_e
mpInP=0.4*sc.m_e
#GaN
nc=2*((2*num.pi*mnGaN*sc.k*a)/(sc.h**2))**(3/2)/1e+6 #1+e6 para que sea en cm-3, es en m
nv=2*((2*num.pi*mpGaN*sc.k*a)/(sc.h**2))**(3/2)/1e+6
Eg=3.470-((7.70*10**(-4))*a**2/(a+600))  #GaN
b=num.sqrt(nc*nv)*num.exp(-Eg*sc.e/(2*(a)*sc.k))
#GaP
nc=2*((2*num.pi*mnGaP*sc.k*a)/(sc.h**2))**(3/2)/1e+6
nv=2*((2*num.pi*mpGaP*sc.k*a)/(sc.h**2))**(3/2)/1e+6
Eg=2.340-((6.20*10**(-4))*a**2/(a+460)) #GaP
c=num.sqrt(nc*nv)*num.exp(-Eg*sc.e/(2*(a)*sc.k))
#GaAs
nc=2*((2*num.pi*mnGaAs*sc.k*a)/(sc.h**2))**(3/2)/1e+6
nv=2*((2*num.pi*mpGaAs*sc.k*a)/(sc.h**2))**(3/2)/1e+6
Eg=1.519-((5.41*10**(-4))*a**2/(a+204)) #GaAS
d=num.sqrt(nc*nv)*num.exp(-Eg*sc.e/(2*(a)*sc.k))
#InP
nc=2*((2*num.pi*mnInP*sc.k*a)/(sc.h**2))**(3/2)/1e+6
nv=2*((2*num.pi*mpInP*sc.k*a)/(sc.h**2))**(3/2)/1e+6
Eg=1.425-((4.50*10**(-4))*a**2/(a+327)) #InP
e=num.sqrt(nc*nv)*num.exp(-Eg*sc.e/(2*(a)*sc.k))
#Si
nc=2*((2*num.pi*mnSi*sc.k*a)/(sc.h**2))**(3/2)/1e+6
nv=2*((2*num.pi*mpSi*sc.k*a)/(sc.h**2))**(3/2)/1e+6
Eg=1.170-((4.73*10**(-4))*a**2/(a+636)) #Si
g=num.sqrt(nc*nv)*num.exp(-Eg*sc.e/(2*(a)*sc.k))
#Ge
nc=2*((2*num.pi*mnGe*sc.k*a)/(sc.h**2))**(3/2)/1e+6
nv=2*((2*num.pi*mpGe*sc.k*a)/(sc.h**2))**(3/2)/1e+6
Eg=0.744-((4.77*10**(-4))*a**2/(a+235)) #Ge
h=num.sqrt(nc*nv)*num.exp(-Eg*sc.e/(2*(a)*sc.k))
#Se les asigna el label correspondiente a cada eje
plota.semilogy(a,b,color='y',label='GaN')
plota.semilogy(a,c,color='b',label='GaP')
plota.semilogy(a,d,color='g',label='GaAS')
plota.semilogy(a,e,color='black',label='InP')
plota.semilogy(a,g,color='r',label='Si')
plota.semilogy(a,h,color='cyan',label='Ge')
plota.set_xlabel("$T \ (K)$")
plota.set_ylabel("$ni \ (cm-3)$",rotation='vertical')
plota.axis([200,700,0,10**17])
plota.legend(loc=4)
# Muestra la grafica-------------------------------------------------
plota.set_title('Concentracion de portadores intrinsecos')
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
var.set("Utilice las flechas del teclado para desplazarce por la grafica")
def graficar(x):
    if state==0:
        #Ge
        nc=2*((2*num.pi*mnGe*sc.k*x)/(sc.h**2))**(3/2)/1e+6
        nv=2*((2*num.pi*mpGe*sc.k*x)/(sc.h**2))**(3/2)/1e+6
        Eg=0.744-((4.77*10**(-4))*x**2/(x+235)) #Ge
        y=num.sqrt(nc*nv)*num.exp(-Eg*sc.e/(2*(x)*sc.k))
    elif state==1:
        #Si
        nc=2*((2*num.pi*mnSi*sc.k*x)/(sc.h**2))**(3/2)/1e+6
        nv=2*((2*num.pi*mpSi*sc.k*x)/(sc.h**2))**(3/2)/1e+6
        Eg=1.170-((4.73*10**(-4))*x**2/(x+636)) #Si
        y=num.sqrt(nc*nv)*num.exp(-Eg*sc.e/(2*(x)*sc.k))
    elif state==2:
        #InP
        nc=2*((2*num.pi*mnInP*sc.k*x)/(sc.h**2))**(3/2)/1e+6
        nv=2*((2*num.pi*mpInP*sc.k*x)/(sc.h**2))**(3/2)/1e+6
        Eg=1.425-((4.50*10**(-4))*x**2/(x+327)) #InP
        y=num.sqrt(nc*nv)*num.exp(-Eg*sc.e/(2*(x)*sc.k))
    elif state==3:
        #GaAs
        nc=2*((2*num.pi*mnGaAs*sc.k*x)/(sc.h**2))**(3/2)/1e+6
        nv=2*((2*num.pi*mpGaAs*sc.k*x)/(sc.h**2))**(3/2)/1e+6
        Eg=1.519-((5.41*10**(-4))*x**2/(x+204)) #GaAS
        y=num.sqrt(nc*nv)*num.exp(-Eg*sc.e/(2*(x)*sc.k))
    elif state==4:
        #GaP
        nc=2*((2*num.pi*mnGaP*sc.k*x)/(sc.h**2))**(3/2)/1e+6
        nv=2*((2*num.pi*mpGaP*sc.k*x)/(sc.h**2))**(3/2)/1e+6
        Eg=2.340-((6.20*10**(-4))*x**2/(x+460)) #GaP
        y=num.sqrt(nc*nv)*num.exp(-Eg*sc.e/(2*(x)*sc.k))
    else:
        #GaN
        nc=2*((2*num.pi*mnGaN*sc.k*x)/(sc.h**2))**(3/2)/1e+6
        nv=2*((2*num.pi*mpGaN*sc.k*x)/(sc.h**2))**(3/2)/1e+6
        Eg=3.470-((7.70*10**(-4))*x**2/(x+600))  #GaN
        y=num.sqrt(nc*nv)*num.exp(-Eg*sc.e/(2*(x)*sc.k))
    n = num.linspace(x,x,2)
    plota.cla()
    plota.semilogy(a,b,color='y',label='GaN')
    plota.semilogy(a,c,color='b',label='GaP')
    plota.semilogy(a,d,color='g',label='GaAS')
    plota.semilogy(a,e,color='black',label='InP')
    plota.semilogy(a,g,color='r',label='Si')
    plota.semilogy(a,h,color='cyan',label='Ge')
    plota.set_xlabel("$T \ (K)$")
    plota.set_ylabel("$ni \ (cm-3)$",rotation='vertical')
    plota.legend(loc=4)
    plota.axis([200,700,0,10**17])
    # Muestra la grafica-------------------------------------------------
    plota.set_title('Concentracion de portadores intrinsecos')
    f.tight_layout()
    plota.grid(True)
    plota.scatter([x, ], [y, ], 50, color='red')
    canvas.draw()
    var.set("Valores sobre la curva\t ni= "+str(y)+" con T= "+str(x))
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
        if x>=700:
            x=700
        else:
            x = x + 10
        graficar(x)
    #Flecha Izquierda
    elif event.key==L:
        global a
        global b
        global x 
        if x<=200:
            x=200
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