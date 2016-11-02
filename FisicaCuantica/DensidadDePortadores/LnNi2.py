#Librerias
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from scipy import constants as constantes
import sys as cr
import math

#Inicializar los Ejes
fig, ax = plt.subplots(figsize=(15,8))
plt.subplots_adjust(left=0.1, bottom=0.25)
plt.grid()
plt.xlim(1, 20)
plt.ylim(30, 60)

plt.title(r'$Logarithm \ Intrinsic \ Carrier \ Density  $')
plt.ylabel(r'Ln $n_{i}$')
plt.xlabel(r'$T$')

T = np.linspace(1,1000,10000) 

#Densidades
NcSi=12*((2*np.pi*(0.33*constantes.electron_mass)*constantes.k*T)/(constantes.h**2))**(3/2)
NcGe=2*((2*np.pi*(0.22*constantes.electron_mass)*constantes.k*T)/(constantes.h**2))**(3/2)
NcGaAs=2*((2*np.pi*(0.072*constantes.electron_mass)*constantes.k*T)/(constantes.h**2))**(3/2)
NvSi=2*((2*np.pi*(0.56*constantes.electron_mass)*constantes.k*T)/(constantes.h**2))**(3/2)
NvGe=2*((2*np.pi*(0.31*constantes.electron_mass)*constantes.k*T)/(constantes.h**2))**(3/2)
NvGaAs=2*((2*np.pi*(0.5*constantes.electron_mass)*constantes.k*T)/(constantes.h**2))**(3/2)


#logaritmo natural de la densidad intrinseca para cada componente
lnniSi=-(1/2*constantes.k)*((NcSi-NvSi)/T)+ np.log(np.sqrt(NcSi*NvSi))
lnniGe=-(1/2*constantes.k)*((NcGe-NvGe)/T)+ np.log(np.sqrt(NcGe*NvGe))
lnniGaAs=-(1/2*constantes.k)*((NcGaAs-NvGaAs)/T)+ np.log(np.sqrt(NcGaAs*NvGaAs))


#Graficas
plt.plot(T,lnniSi,color='b',lw=3)
plt.plot(T,lnniGe,color='g',lw=3)
plt.plot(T,lnniGaAs,color='r',lw=3)

#Valor Inicial
punto1, = plt.plot(T[100],lnniSi[100],"b",marker='o')
punto2, = plt.plot(T[100],lnniGe[100],"g",marker='o')
punto3, = plt.plot(T[100],lnniGaAs[100],"r",marker='o')

#datos iniciales
plt.legend([punto1,punto2,punto3], ['Ln(Ni) para el Silicio %f'%lnniSi[2000],'Ln(Ni) para el Germanio %f'%lnniGe[2000],'Ln(Ni) para el Arsenuro de Galio %f'%lnniGaAs[2000]],bbox_to_anchor=(0.9, 0.7), bbox_transform=plt.gcf().transFigure)

#Slider para la ubicacion de los puntos
eje1 = plt.axes([0.15, 0.14, 0.75, 0.03])
Slid1 = Slider(eje1, '$Temperatura$ $(°K)$', 0, 20, valinit=10)
eje2 = plt.axes([0.15, 0.10, 0.75, 0.03])
Slid2 = Slider(eje2, '$Temperatura$ $(°K)$', 0, 20, valinit=10)
eje3 = plt.axes([0.15, 0.06, 0.75, 0.03])
Slid3 = Slider(eje3, '$Temperatura$ $(°K)$', 0, 20, valinit=10)


#Actualizacion de datos: movimiento de los puntos de acuerdo al slider
def update1(val):
    temp1=Slid1.val
    temp2=Slid2.val
    temp3=Slid3.val
    punto1.set_ydata(lnniSi[temp1*10])
    punto1.set_xdata(T[temp1*10])
    plt.legend([punto1,punto2,punto3], ['Ln(Ni) para el Silicio %f'%lnniSi[temp1*10],'Ln(Ni) para el Germanio %f'%lnniGe[temp2*10],'Ln(Ni) para el Arsenuro de Galio %f'%lnniGaAs[temp3*10]],bbox_to_anchor=(0.9, 0.7), bbox_transform=plt.gcf().transFigure)
    
def update2(val):
    temp1=Slid1.val
    temp2=Slid2.val
    temp3=Slid3.val
    punto2.set_ydata(lnniGe[temp2*10])
    punto2.set_xdata(T[temp2*10])
    plt.legend([punto1,punto2,punto3], ['Ln(Ni) para el Silicio %f'%lnniSi[temp1*10],'Ln(Ni) para el Germanio %f'%lnniGe[temp2*10],'Ln(Ni) para el Arsenuro de Galio %f'%lnniGaAs[temp3*10]],bbox_to_anchor=(0.9, 0.7), bbox_transform=plt.gcf().transFigure)

def update3(val):
    temp1=Slid1.val
    temp2=Slid2.val
    temp3=Slid3.val
    punto3.set_ydata(lnniGaAs[temp3*10])
    punto3.set_xdata(T[temp3*10])
    plt.legend([punto1,punto2,punto3], ['Ln(Ni) para el Silicio %f'%lnniSi[temp1*10],'Ln(Ni) para el Germanio %f'%lnniGe[temp2*10],'Ln(Ni) para el Arsenuro de Galio %f'%lnniGaAs[temp3*10]],bbox_to_anchor=(0.9, 0.7), bbox_transform=plt.gcf().transFigure)

Slid1.on_changed(update1)
Slid2.on_changed(update2)
Slid3.on_changed(update3)

plt.show()
