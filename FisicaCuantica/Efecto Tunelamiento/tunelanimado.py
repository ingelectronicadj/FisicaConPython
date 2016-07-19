# -*- coding: utf-8  -*-

"""
    Quantum Tunneling simulation with perfectly matched layers
    with mouse controlled plotting

    Copyright (C) 2013 Greg von Winckel

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    Created: Tue Oct  8 19:51:05 MDT 2013
"""

import numpy as np
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import splu
from pylab import *

class incrementor(object):
    def __init__(self,x,t,y,xlim):
 
        fig = figure()
        fig.canvas.set_window_title('Left click to play, '+\
                       'Right to rewind')
        self.ax = fig.add_subplot(111)
        self.ax.set_xlabel('Incremente el tiempo con la rueda del '+\
                           'mouse o las flechas',fontsize=16)
        self.ax.set_xlim(xlim)
        self.x = x
        self.t = t
        self.y = y

        self.maxsteps = len(t)
        self.tstep = 0
         
        self.line, = self.ax.plot(x,np.abs(y[:,0])**2,lw=4)
        self.update_time()
        draw()

    def update_time(self):
        self.ax.set_title('t = %0.4f' % self.t[self.tstep])
        draw()

    def draw_barrier(self,xy,width,height,color,transp):
        rect = self.ax.add_patch(Rectangle(xy,width,height))
        rect.set_facecolor(color)
        rect.set_alpha(transp)

    def key_press(self,event):
        if event.key in ['down','right']:
            if self.tstep < self.maxsteps-1:
                self.tstep += 1
        elif event.key in ['left','up']:
            if self.tstep > 0:
                self.tstep -= 1
        else:
            return
        
        self.line.set_ydata(np.abs(y[:,self.tstep])**2)
        self.update_time()
        draw()


    def mouse_scroll(self,event):
        if event.button == 'up':
            if self.tstep < self.maxsteps-1:
                self.tstep += 1
        elif event.button == 'down':
            if self.tstep > 0:
                self.tstep -= 1
        else:
            return
        
        self.line.set_ydata(np.abs(y[:,self.tstep])**2)
        self.update_time()
        draw()

    def mouse_click(self,event):
        if event.button == 1:
            while self.tstep < self.maxsteps-1:
                self.line.set_ydata(np.abs(y[:,self.tstep])**2)
                self.tstep += 1
                self.update_time()
                draw()

        elif event.button == 3:
            while self.tstep > 0:
                self.line.set_ydata(np.abs(y[:,self.tstep])**2)
                self.tstep -= 1
                self.update_time()
                draw()

class layer(object):
    def __init__(self,thickness,potential,rotation):
        self.d = thickness
        self.V = potential
        self.theta = rotation




if __name__ == '__main__':

    # Barrier height
    V0 = 1000

    # Set up layers
    structure = []     
    structure.append(layer(1,0,np.pi/3))
    structure.append(layer(2,0,0))
    structure.append(layer(1,V0,0))
    structure.append(layer(1,0,0))
    structure.append(layer(1,0,np.pi/3))
   
    # Number of layers
    nl = len(structure)
    
    # requested element size
    dx =  0.01

    # Thickness of each layer
    d = [np.ceil(structure[ll].d) for ll in range(nl)]

    # Number of elements in each layer
    nel = [int(np.ceil(structure[ll].d/dx)) for ll in range(nl)]

    # Total number of elements
    n = sum(nel)

    # Actual elemental thickness in each layer
    dx = [d[ll]/float(nel[ll]) for ll in range(nl)]

    # Potential in each layer
    v = [structure[ll].V for ll in range(nl)]

    # Complex coordinate rotation
    phase = np.array([np.exp(1j*structure[ll].theta) \
                               for ll in range(nl)])

    def rep(s):
        return np.repeat(s,nel)

    pdx = rep(phase*dx)
    
    # Number of time steps
    m = 300

    # Final time
    T = .10

    t = np.linspace(0,T,m)

    # Time step size
    dt = float(T)/m

    # Elemental end points
    x = np.hstack((0,np.cumsum(rep(dx))))
    
    # Wavepacket width factor
    sig = 0.1

    # Initial center of the wavepacket
    x0 = 2

    # Spatial broadness parameter
    sigma = 0.1

    # Wavenumber 
    k = 35

    # Initial data
    y0 = np.exp(-(x-x0)**2/(2*sigma**2))*np.exp(1j*k*x)/\
         (sigma*np.sqrt(2*pi))

    E = np.array(((0,0),(1,1)))

    shift = np.kron(np.arange(n),np.ones((2,2)))

    rows = (shift + np.tile(E,n)).flatten()
    cols = (shift + np.tile(E.T,n)).flatten()

    # Elemental mass matrix
    Me = np.array(((2,1),(1,2)))/6.0

    # Elemental stiffness matrix
    Ke = np.array(((1,-1),(-1,1)))
   
    mvals = np.kron(pdx,Me).flatten()
    kvals = np.kron(1/pdx,Ke).flatten()
    vvals = np.kron(pdx*rep(v),Me).flatten()


    # Global mass matrix
    M = csc_matrix((mvals,(rows,cols)),shape=(n+1,n+1))

    # Global stiffness matrix
    K = csc_matrix((kvals,(rows,cols)),shape=(n+1,n+1))

    # Global potential matrix
    V = csc_matrix((vvals,(rows,cols)),shape=(n+1,n+1))


    A = splu(M+0.5j*dt*(K+V))
    B = M-0.5j*dt*(K+V)


    y = np.zeros((n+1,m),dtype=complex)
    y[:,0] = y0


    for ll in range(m-1):

        y[:,ll+1] = A.solve(B*y[:,ll])

    # Right end points of each layer
    xend = np.cumsum(d)
    xlim = (xend[0],xend[-2])
    inc = incrementor(x,t,y,xlim)
    
    height = 0.5*max(np.abs(y0)**2)
    inc.draw_barrier((xend[1],0),structure[2].d,height,'r',0.3)
    connect('scroll_event',inc.mouse_scroll)
    connect('key_press_event',inc.key_press)
    connect('motion_notify_event',inc.mouse_click)
    show()
     
















