# Exercise 5.21: Electric Feild of a Charged Particle 
#Tasks: 
#a)You have two charges, of ±1 C, 10 cm apart. Calculate the resulting electric potential on a 1 m × 1 m square plane surrounding the charges and passing through them. Calculate the potential at 1 cm spaced points in a grid and make a visualization on the screen of the potential using a density plot.
#b)Now calculate the partial derivatives of the potential with respect to x and y and hence find the electric field in the xy plane. Make a visualization of the field also. This is a little trickier than visualizing the potential, because the electric field has both magnitude and direction. A visualization might use the arrow object from the visual package, drawing a grid of arrows with direction and length chosen to represent the field.

import numpy as np
import matplotlib.pyplot as plt
import astropy.constants as c 
from astropy import units as u 

#for my adjusting the color map
import matplotlib.colors as colors


print("This code computes the electric potential and electric feild.")

#Calculating Electric Potential
def E_potential(q1,q2,x,y):
    """
    Computes the electric potential from the distance between point and charge (r) and charge of particle (q)
    """

    r1=np.sqrt((x-0.55)**2+(y-0.5)**2)
    r2=np.sqrt((x-0.45)**2+(y-0.5)**2)
    electric_potenial =q1*u.coulomb/(4* np.pi * (r1*u.meter) * c.eps0)+ q2*u.coulomb/(4* np.pi * (r2*u.meter) * c.eps0)
    return electric_potenial

#Creating our visualizing grid 
#We need a 1m by 1m grid 

x_vals= np.arange(0.0,1.01,0.01)
y_vals=np.arange(0.0,1.01,0.01)

q1=-1
q2=1

feild = np.zeros([101,101]) #our 2D array

for i, x in enumerate(x_vals):
    for j, y in enumerate(y_vals):
       feild[i,j] = (E_potential(q1,q2,x,y)).value #takes just the value not including the unity


#first testing a contour map
       
plt.subplots(figsize=(10,8),facecolor='w')
contour = plt.contour(feild,levels=[-1.0e+12, -8.0e+11, -5.0e+11, -2.5e+11, 0.0e+00, 2.5e+11, 5.0e+11, 8.0e+11, 1.0e+12])#the levels should span negative numbers and polostives
plt.clabel(contour, inline=True,levels=contour.levels) 
plt.title("Contour Plot of Electric Potential ")
plt.text(1.0, 0.7 , 'Levels=[-1.0e+12 -8.0e+11 -5.0e+11 -2.5e+11  0.0e+00  2.5e+11  5.0e+11  8.0e+11 1.0e+12] ', color='black', 
        bbox=dict(facecolor='none', edgecolor='Black', boxstyle='round'))
plt.show()



#taking the derivatives 
derivativex=[]
derivativey=[]
x=[]
y=[]
for i in range(0,len(x_vals)-1): 
    for j in range (0,len(x_vals)-1):
        derivativex.append( (feild[i,j]-feild[i+1,j])/0.1 )
        derivativey.append( (feild[i,j]-feild[i,j+1])/0.1 ) 
        x.append(x_vals[i])
        y.append(y_vals[j])


x=np.array(x)*0.01
y=np.array(y)*0.01
derivativex=np.array(derivativex)*0.3
derivativey=np.array(derivativey)*0.3

#Visualization of Vectors
fig,ax=plt.subplots(figsize=(10,8))
ax.quiver(x, y, derivativex, derivativey, pivot='mid', units='x')
plt.title("Electric Feild")
plt.show()



