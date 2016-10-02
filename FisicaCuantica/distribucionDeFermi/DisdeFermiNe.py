#!/usr/bin/python
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.widgets as Cursor
import scipy.constants as cte
from sympy import *
from matplotlib.widgets import Cursor
import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk1
else:
    import tkinter as Tk1

from Tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

matplotlib.use('TkAgg')

T1=0.01
T2=300
T3=3000
T4=5000
N1=0.45

#EFF=0.3
E=np.linspace(0, 2, 5000)
select=0

root = Tk()
root.title("FERMI-DIRAC")

font = {'family' : 'serif',
        'color'  : 'blue',
        'weight' : 'normal',
        'size'   : 16,
        }

mlabel = Label(root, text="SELECCIONE EL SEMICONDUCTOR", font="Helvetica 16 bold italic", fg="blue").pack()

v = StringVar()
 
def imprimir(valor):
    
    valor=int(valor)
    if valor==1:
        nombre="Germanio"
        valor=0.66        
         
    else: 
        if valor ==2:
            nombre="Silicio"
            valor=1.169
            
             
        else:
            if valor==3:
                nombre="Arseniuro de Galio"
                valor=1.519
                 
                 
    selection = "Ha elegido simular " + nombre
    label.config(text = selection)
    plt.clf()                
    plt.ion()    
   

    NE1=(1/(np.exp((E-(valor))/(T1*0.0000138))+1))*((3*N1*(E**0.5))/(2*(valor**0.75)))    
    plt.plot(E,NE1)
    
    NE2=1/(np.exp((E-(valor))/(T2*0.0000138))+1)*((3*N1*(E**0.5))/(2*(valor**0.75)))    
    plt.plot(E,NE2)
    
    NE3=1/(np.exp((E-(valor))/(T3*0.0000138))+1)*((3*N1*(E**0.5))/(2*(valor**0.75)))     
    plt.plot(E,NE3)
    
    NE4=1/(np.exp((E-(valor))/(T4*0.0000138))+1)*((3*N1*(E**0.5))/(2*(valor**0.75)))
    plt.plot(E,NE4)
    
    

    plt.grid(True) 
    plt.ylim(-0.2, 1.2)

    plt.xlabel(r'$E(eV)$', fontsize=20)
    plt.ylabel(r'$N(E)$', fontsize=20)
    plt.title(r'$Funcion\ de\ distribucion\ de\ FERMI-DIRAC\ para\ el\ $'+nombre, fontdict=font)
    plt.text(1.5,1.05,'T1=0K',color='b')
    plt.text(1.5,0.95,'T1=300K',color='g')
    plt.text(1.5,0.85,'T2=3000K',color='r')
    plt.text(1.5,0.75,'T3=5000K',color='c')   
    plt.text(0.5,0.9, 'Danny Fabian Mora 20112005201\nDiego Javier Mena 20092005053', style='italic',bbox={'facecolor':'red','alpha':0.5, 'pad':10})

    plt.show()

def sel():
   
   EF=v.get()
   print EF
   imprimir(EF)
         

Radiobutton(root, text="Germanio [Ge]", indicatoron = 0, width = 50, variable=v, value=1, command=sel).pack(anchor=W)
Radiobutton(root, text="Silicio [Si]", indicatoron = 0, width = 50, variable=v, value=2, command=sel).pack(anchor=W)
Radiobutton(root, text="Arseniuro de galio [GaAs]", indicatoron = 0, width = 50, variable=v, value=3, command=sel).pack(anchor=W)
label = Label(root)
label.pack()

mainloop()
