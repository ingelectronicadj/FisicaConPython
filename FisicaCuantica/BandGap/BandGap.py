from __future__ import print_function
from scipy.optimize import newton	
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import sys
from numpy.random import randn


GaAs = [1.519,5.405*10**(-4),204.0]
Si = [1.17,4.73*10**(-4),636.0]
Ge = [0.7437,4.774*10**(-4),235.0]
Tabla = [GaAs,Si,Ge]
T = range(0,1000,10)
EgGaAs = []
EgSi = []
EgGe = []
incremento1 = 300
incremento2 = 300
incremento3 = 300
contador=2


fig , ax= plt.subplots(figsize=(20,10))
plt.subplots_adjust(left=0.1, bottom=0.2)


for i in T:
	EgGaAs.append(GaAs[0]- (GaAs[1])*i**2/(i + GaAs[2]))
	EgSi.append(Si[0]- (Si[1])*i**2/(i + Si[2]))
	EgGe.append(Ge[0]- (Ge[1])*i**2/(i + Ge[2]))

plt.plot(T,EgGaAs, color="red",  linewidth=1, linestyle="-")
plt.plot(T,EgSi, color="blue",  linewidth=1, linestyle="-")
plt.plot(T,EgGe, color="green",  linewidth=1, linestyle="-")
punto1, = plt.plot(incremento1, EgGaAs[incremento1/10], 'ro')
punto2, = plt.plot(incremento2, EgSi[incremento2/10], 'bo')
punto3, = plt.plot(incremento3, EgGe[incremento3/10], 'go')
plt.axvline(x=300,linewidth=1,color="black")

leyenda1=ur'Temperatura =  %f'%(incremento1)
leyenda2=ur'Temperatura =  %f'%(incremento2)
leyenda3=ur'Temperatura = %f'%(incremento3)
leyenda4=ur'Energia =  %f'%(EgGaAs[incremento1/10])
leyenda5=ur'Energia = %f'%(EgSi[incremento1/10])
leyenda6=ur'Energia =  %f'%(EgGe[incremento1/10])
ax.legend([leyenda1,leyenda2,leyenda3,leyenda4,leyenda5,leyenda6],bbox_to_anchor=(0.28,0.32))
fig.canvas.draw()

def press(event):
    print('press', event.key)
    sys.stdout.flush()
    if event.key == 'm':
	if (contador == 0):
		global incremento1, punto1, contador
		incremento1 = incremento1 + 10
		punto1.set_xdata(incremento1)
		punto1.set_ydata(EgGaAs[incremento1/10])
	if (contador == 1):
		global incremento2, punto2, contador
		incremento2 = incremento2 + 10
		punto2.set_xdata(incremento2)
		punto2.set_ydata(EgSi[incremento2/10])
	if (contador == 2):
		global incremento3, punto3, contador
		incremento3 = incremento3 + 10
		punto3.set_xdata(incremento3)
		punto3.set_ydata(EgGe[incremento3/10])
			
    if event.key == 'n':
	if (contador == 0):
		global incremento1, punto1, contador
		incremento1 = incremento1 - 10
		punto1.set_xdata(incremento1)
		punto1.set_ydata(EgGaAs[incremento1/10])
	if (contador == 1):
		global incremento2, punto2, contador
		incremento2 = incremento2 - 10
		punto2.set_xdata(incremento2)
		punto2.set_ydata(EgSi[incremento2/10])
	if (contador == 2):
		global incremento3, punto3, contador
		incremento3 = incremento3 - 10
		punto3.set_xdata(incremento3)
		punto3.set_ydata(EgGe[incremento3/10])

    if event.key == 'j':
	if (contador == 0):
		global incremento1, punto1, contador, seleccion
		contador = 1
		seleccion.remove()
		seleccion = plt.text(0,0.3,'Grafica seleccionada: 2',color='blue')
	if (contador == 1):
		global incremento2, punto2, contador, seleccion
		contador = 2
		seleccion.remove()
		seleccion = plt.text(0,0.3,'Grafica seleccionada: 3',color='green')
	if (contador == 2):
		global incremento2, punto2, contador, seleccion
		contador =0
		seleccion.remove()
		seleccion = plt.text(0,0.3,'Grafica seleccionada: 1',color='red')
    leyenda1=ur'Temperatura GaAs =  %f'%(incremento1)
    leyenda2=ur'Temperatura Si =  %f'%(incremento2)
    leyenda3=ur'Temperatura Ge = %f'%(incremento3)
    leyenda4=ur'Energia GaAs =  %f'%(EgGaAs[incremento1/10])
    leyenda5=ur'Energia Si = %f'%(EgSi[incremento2/10])
    leyenda6=ur'Energia Ge=  %f'%(EgGe[incremento3/10])
    ax.legend([leyenda1,leyenda2,leyenda3,leyenda4,leyenda5,leyenda6],bbox_to_anchor=(0.28,0.32))	
    fig.canvas.draw()



fig.canvas.mpl_connect('key_press_event', press)
plt.xlabel("$Temperatura (K)$")
plt.ylabel("$Energia (eV)$")
plt.title("$BandGap$")
plt.text(700, 1.3,'Presione "m" para avanzar por la grafica')
plt.text(700, 1.35,'Presione "n" para retroceder por la grafica')
plt.text(700, 1.4,'Presione "j" para cambiar de grafica')
plt.text(700, 1.5, 'Danny Fabian Mora 20112005201\nDiego Javier Mena 20092005053', style='italic',bbox={'facecolor':'red','alpha':0.5, 'pad':10})

the_table = plt.table(cellText=Tabla,
                  colWidths = [0.1]*5,
                  rowLabels=['GaAs','Si','Ge'],
                  colLabels=["Eg(eV)", r"a",r"b"],
                  loc='lower center')

plt.text(300,1.2,"1.17eV")
plt.text(300,1.5,"1.519eV")
plt.text(300,0.8,"0.66eV")

plt.show()
