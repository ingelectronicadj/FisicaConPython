import numpy             as np
import matplotlib.pyplot as plt
import scipy.constants   as sc
from matplotlib.widgets import Slider
plt.subplots_adjust(left=0.1, bottom=0.25)
semic=['Ge', 'Si', 'GaAs']

Ego=[0.7437,1.170,1.519]
a=[4.774,4.73,5.405]
b=[235,636,204]


Eg=[0.66,1.12,1.42]
Egg=[0,0,0]

ni=[2.4*10**13,1.45*10**10,1.79*10**6]

mn_mp=[0,0,0]
mn_mp[0]=(((ni[0]*np.exp(Eg[0]*sc.e/(2*sc.k*300)))/2.0)*(((sc.h**2)/(2*sc.pi*sc.k*300))**(3/2.0)))
mn_mp[1]=(((ni[1]*np.exp(Eg[1]*sc.e/(2*sc.k*300)))/2.0)*(((sc.h**2)/(2*sc.pi*sc.k*300))**(3/2.0)))
mn_mp[2]=(((ni[2]*np.exp(Eg[2]*sc.e/(2*sc.k*300)))/2.0)*(((sc.h**2)/(2*sc.pi*sc.k*300))**(3/2.0)))

N=1000
x=np.linspace(0.5,4,N)

Egg[0]=Ego[0]-((a[0]*10**-4)*(1000/x)**2)/((1000/x)+b[0])
Ni_0=2*((2*sc.pi*sc.k/(sc.h**2))**(3/2.0))*((1000/x)**(3/2.0))*mn_mp[0]*np.exp(-Egg[0]*sc.e/(2*(1000/x)*sc.k))

Egg[1]=Ego[1]-((a[1]*10**-4)*(1000/x)**2)/((1000/x)+b[1])
Ni_1=2*((2*sc.pi*sc.k/(sc.h**2))**(3/2.0))*((1000/x)**(3/2.0))*mn_mp[1]*np.exp(-Egg[1]*sc.e/(2*(1000/x)*sc.k))

Egg[2]=Ego[2]-((a[2]*10**-4)*(1000/x)**2)/((1000/x)+b[2])
Ni_2=2*((2*sc.pi*sc.k/(sc.h**2))**(3/2.0))*((1000/x)**(3/2.0))*mn_mp[2]*np.exp(-Egg[2]*sc.e/(2*(1000/x)*sc.k))

g1, =plt.semilogy(x,Ni_0,'r')
g1, =plt.semilogy(x,Ni_1,'b')
g1, =plt.semilogy(x,Ni_2,'g')

plt.semilogy([10/3.0,10/3.0],[10**5,10**19])
plt.text(3.38,2.235e+13,'$2.235*10^{13}$',fontsize=12)
plt.text(3.38,2.7e+10,'$1.45*10^{10}$',fontsize=12)
plt.text(3.38,1.73e+6,'$1.705*10^{6}$',fontsize=12)

plt.text(3.38,3.6e+14,'$Ge$',fontsize=12)
plt.text(3.38,1.6e+11,'$Si$',fontsize=12)
plt.text(3.38,1.6e+7,'$GaAs$',fontsize=12)

#plt.text(2.03,1.5e+19, 'Danny Fabian Mora 20112005201\nDiego Javier Mena 20092005053', style='italic',bbox={'facecolor':'red','alpha':0.5, 'pad':10})
plt.plot(10/3.0,2.235e+13,'ro', markersize=4)
plt.plot(10/3.0,1.45e+10,'bo', markersize=4)
plt.plot(10/3.0,1.79e+6,'go', markersize=4)

dot1, = plt.plot(x[N/2],Ni_0[N/2],'ro', markersize=18)
dot2, = plt.plot(x[N/2],Ni_1[N/2],'bo', markersize=18)
dot3, = plt.plot(x[N/2],Ni_2[N/2],'go', markersize=18)

axcolor = 'lightgoldenrodyellow'
axp1=plt.axes([0.1, 0.15, 0.65, 0.03], axisbg=axcolor)
punto1 = Slider(axp1, '11', 0, 1000, valinit=N/2)
axp2=plt.axes([0.1, 0.1, 0.65, 0.03], axisbg=axcolor)
punto2 = Slider(axp2, '22', 0, 1000, valinit=N/2)
axp3=plt.axes([0.1, 0.05, 0.65, 0.03], axisbg=axcolor)
punto3 = Slider(axp3, '33', 0, 1000, valinit=N/2)


def update(val):
	
	a = punto1.val
	b=punto2.val
	c=punto3.val

	dot1.set_data(x[a],Ni_0[a])
	dot2.set_data(x[b],Ni_1[b])
	dot3.set_data(x[c],Ni_2[c])
punto1.on_changed(update)
punto2.on_changed(update)
punto3.on_changed(update)


plt.ylim(10**6,10**19)
plt.grid()
plt.show()


