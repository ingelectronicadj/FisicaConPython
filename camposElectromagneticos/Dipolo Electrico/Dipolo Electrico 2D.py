
import numpy as np
import matplotlib.pyplot as plt

theta=(np.arange(0,2*np.pi,0.01))
r = 1*(pow(np.sin(theta),2))
r2 = 1.5*(pow(np.sin(theta),2))
r3 = 2*(pow(np.sin(theta),2))
r4= 2.5*(pow(np.sin(theta),2))
r5= 3*(pow(np.sin(theta),2))
r6 = 3.5*(pow(np.sin(theta),2))

a1 = plt.subplot(111, polar=True)
a1.plot(theta,r, color='r', linewidth=3)
a1.set_rmax(4.0)
a1.grid(True)
a2 = plt.subplot(111, polar=True)
a2.plot(theta,r2, color='g', linewidth=3)
a2.set_rmax(4.0)
a2.grid(True)
a3 = plt.subplot(111, polar=True)
a3.plot(theta,r3, color='y', linewidth=3)
a3.set_rmax(4.0)
a3.grid(True)
a4= plt.subplot(111, polar=True)
a4.plot(theta,r4, color='b', linewidth=3)
a4.set_rmax(4.0)
a4.grid(True)
a5 = plt.subplot(111, polar=True)
a5.plot(theta,r5, color='black', linewidth=3)
a5.set_rmax(4.0)
a5.grid(True)
a6 = plt.subplot(111, polar=True)
a6.plot(theta,r6, color='c', linewidth=3)
a6.set_rmax(4.0)
a6.grid(True)


plt.show()