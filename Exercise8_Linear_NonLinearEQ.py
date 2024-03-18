# Exercise 6.14
#Tasks: 
#a) For an electron (mass 9.1094×10−31 kg) in a well with V = 20eV and w = 1nm, write a Python program to plot the three quantities on the same graph, as a function of E from E = 0 to E = 20eV. From your plot make approximate estimates of the energies of the first six energy levels of the particle.
#b) Write a second program to calculate the values of the first six energy levels in electron volts to an accuracy of 0.001 eV using binary search.


import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u
import astropy.constants as c

print("This program uses Bisection to find the first 6 energy levels of an infinite square well")

#Constants and Initial Arrays
E = np.linspace(1,20,1000)
w= 1e-9
V = 20
m= 9.1094e-31
hbar=c.hbar.value
E_voltage=E*1.60218e-19 

#inner portion of eq y1
inner= np.sqrt( (w**2 * m * E_voltage)/ (2* hbar**2) )

#functions 
y1= np.tan(inner)
y1[:-1][np.diff(y1)<0]=np.NaN #removes the infinite points

y2= np.sqrt((V-E )/E)
y3= -np.sqrt(E/ (V-E))

def Y1(E):
    E_voltage=E*1.60218e-19 
    inner= np.sqrt( (w**2 * m * E_voltage)/ (2* hbar**2) )
    y1= np.tan(inner)
    return y1

#using a function for y1 so it's easier to take bisection
def transform_y1_y2(E):
    """
    Function for y1, y2 transormation curve

    E = value for volatege
    """
    E_voltage=E*1.60218e-19 

    inner= np.sqrt( (w**2 * m * E_voltage)/ (2* hbar**2) ) 
    y1= np.tan(inner)
    
    y2= np.sqrt((V-E )/E)

    y=  y1 - y2
    y[:-1][np.diff(y)<0]=np.NaN #removes infinity vals

    return y

def transform_y1_y3(E):
    """
    Function for y1, y3 transformation curve to use in the bisection curve

    E= value for volatege

    """
    E_voltage= E * 1.60218e-19

    inner= np.sqrt( (w**2 * m * E_voltage)/ (2* hbar**2) ) 
    y1= np.tan(inner)
    
    y3= -np.sqrt(E/ (V -E))
   
    y= y1- y3
    y[:-1][np.diff(y)<0]=np.NaN #removes infinity vals

    return y



#function to locate roots
def bisection(func, a, b, tol= 0.001): 
    """
    Determins the roots of a function given an initial interval using bisection

    func= desired function that produces value
    a= selected starting point
    b =selected ending point
    tol= tolerance or level of acuracy 

    """
    while np.abs(a-b) > tol : 
        
        mid = (a+b)*0.5

        if func(mid) == 0: 
            return mid
        
        elif np.sign(func(a))== np.sign(func(mid)):  #our sign check
            a = mid
        
        else: 
            b = mid 

        return mid



roots1=np.zeros(3)
roots2=np.zeros(3)

#giving the function some starting values to get estimate
a2= np.array([1.14,4.61,10.99])
b2=np.array([1.53,5.85,11.64])

a1=np.array([2.77,7.62,14.82])
b1=np.array([3.00,8.01,15.05])
for i in range(len(a2)): 
    roots1[i]= bisection(Y1,a1[i],b1[i])

for i in range(len(a1)):
    roots2[i]= bisection(Y1,a2[i],b2[i])

print("First 6 energy levels of square well",np.sort(roots1),np.sort(roots2))


print(type(roots1))


fig,ax =plt.subplots(1,3,figsize=(14,5))
ax[0].plot(E,y1,label='y1')
ax[0].plot(E,y2,label='y2')
ax[0].plot(E,y3,label='y3')
ax[0].axhline(color='red',linestyle='--' )
ax[0].set_ylim(-5,5)
ax[0].set_xlabel('E (eV)')
ax[0].set_title('Y1')
ax[0].legend()

ax[1].plot(E,transform_y1_y2(E))
ax[1].scatter(roots1,[0,0,0],marker='x',label='bisection point',alpha=0.7)
ax[1].axhline(color='red',linestyle='--')
ax[1].set_xlabel('E (eV)')
ax[1].set_title("Y1 - Y2")
ax[1].set_ylim(-1,1)

ax[2].plot(E,transform_y1_y3(E))
ax[2].scatter(roots2,[0,0,0],marker='x',label='bisection point',alpha=0.7)
ax[2].axhline(color='red',linestyle='--')
ax[2].set_xlabel('E (eV)')
ax[2].set_title("Y1 - Y3")
ax[2].set_ylim(-1,1)

plt.show()

