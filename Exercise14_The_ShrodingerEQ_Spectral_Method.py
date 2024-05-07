#Exersice 9.9 : The Schrodiner Equations using Spectral Method
"""

"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation 
import scipy
from numpy.fft import rfft,irfft

#Initial conditions X(x,0) function 
M= 9.109e-31 #(kg)kilogram 
L= 1e-8 #(m) meters 
x0= L*0.5
theta=1e-10 #(m) meters
k=5e10 #(m^-1) 1/meters 

def initial_conditions(x,t=0): 
    fx = np.exp(-(x-x0)**2/(2*(theta**2)) )* np.exp(1j*k*x)

    return fx 

#Sample plot to ensure I get what I expect to get

x=np.linspace(0,L,1000)
y=initial_conditions(x) #this is a complex number ( real and imaginary part)

plt.figure(figsize=(8,6))
plt.plot(x,y)
plt.title("Initial Wave Function")
plt.xlabel("x (m)")
plt.ylabel('y (m)')
plt.show()


#To get the b of k's we need to fourer tranform the initial function (discrete sin transform)
#To do this we'll take the one the book provides 
def dst(y):
    N = len(y)
    y2 = np.empty (2*N,float)
    y2[0] = y2[N] = 0.0
    y2[1:N] = y[1:]
    y2[:N:-1] = -y[1:]
    a = -np.imag(rfft(y2))[:N]
    b = np.real(rfft(y2)[:N])
    a[0] = 0.0 #imaginary part
    b[0] = 0.0 #real part


    return a,b

#Once you get the b'k you separete it into real and imaginary parts 
#Modify the coefs iterively
img, real=dst(y)

def time_evolution(real,img,t=1e-16): 
     N = 1000 
     h= 1e-16
     pi= np.pi
     evo_coefs= np.zeros(N)

     for i in range(N) :

        evo_coefs = np.sin(pi*k*x[i])*(real* np.cos((pi**2) *h* (k**2) *t / (2* M* (L**2)))  -  img* np.sin((pi**2) *h* (k**2) *t/ (2* M* (L**2))) )
        evo_coefs += evo_coefs
     
     evo_coefs =evo_coefs/N

     return evo_coefs

evo_coefs =time_evolution(real,img)

#now we need to to an inverse fft to  get out wave 
def idst(a):
    N = len(a)
    c = np.empty(N+1,complex)
    c[0] = c[N] = 0.0
    c[1:N] = -1j*a[1:]
    y = irfft(c)[:N]
    y[0] = 0.0

    return y

evo_y= idst(evo_coefs) #the evolved y values 

plt.figure(figsize=(8,6))
plt.plot(x,evo_y)
plt.title("Evolved Wave Function at t=1e-16")
plt.xlabel("x (m)")
plt.ylabel('y (m)')
plt.show()

#Now to animate 
t= np.arange(0,1e-13,1e-16)#should be 1000 points

evo_y=np.zeros(len(t))


fig, ax = plt.subplots(figsize=(8, 8))
wave = ax.plot(x ,y , lw=1) 

       
def init():
    wave.set_data(x, evo_y)
    return wave

def animate(i): 
    evo_coefs= time_evolution(real,img,t=t[i])
    evo_y= idst(evo_coefs)
    wave.set_ydata(evo_y)


anim = animation.FuncAnimation(fig, animate, frames=len(t), init_func=init, interval=30)
plt.show()