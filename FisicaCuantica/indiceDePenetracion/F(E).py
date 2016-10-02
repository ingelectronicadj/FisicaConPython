# NOTA: Cambiar Ef para otro material, el muestreo de T, incluso se puede llevar a un for si se desea, tambien cambiar rangos

import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as sc
# Inicializacion del tiempo
T = 0;
Ef=7 #7ev para el cobre
T1=0
# Definicion de variables
E = np.arange(0.1, 20, 0.01)  
#Simulacion
while(1):
    #definir intervalo de 0 a 5000 kelvin y luego se reinicia
    if (T == 0):
        simu = True
    if (T == 5000):
        simu = False
    #limpiar la grafica  
    plt.hold(False)  
    # Funcion a simular
    A=1/(1+np.exp((E-Ef)/(sc.k/sc.e*T1)))
    B=1/(1+np.exp((E-Ef)/(sc.k/sc.e*T))) 
    # Grafica de la funcion de contorno
    plt.plot( E,A, 'r') 
    plt.hold(True) #para no desaparecer la de T=0
    plt.plot( E,B, 'b')
    plt.text(9.5,0.9, 'Danny Fabian Mora 20112005201\nDiego Javier Mena 20092005053', style='italic',bbox={'facecolor':'red','alpha':0.5, 'pad':10})

    plt.title('F(E)')
    plt.xlabel('T=' + str(T) )
    plt.axis([0, 20,-0.1,1.1])
    if (simu):
        T = T + 100
    else:
        T = 0
    # Pausa
    plt.pause(0.05)
    
