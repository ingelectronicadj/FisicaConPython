from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

fig = plt.figure()
ax = fig.gca(projection='3d')

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(-np.pi, np.pi, 100)
u, v = np.meshgrid(u, v)

r = np.abs((np.sin(u+np.pi/2))**2)
x = r*(np.cos(u) * np.sin(v))
y = r*(np.sin(u) * np.sin(v))

z = r*(np.cos(v))
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='green')

plt.show()
