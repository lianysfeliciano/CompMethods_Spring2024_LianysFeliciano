#Exercise 3.2: Curve Plotting 

#Tasks:
# a)  Make a plot of the so-called deltoid curve, which is defined parametrically by the equations, x = 2 cos θ + cos 2θ, y = 2 sin θ − sin 2θ, where 0 ≤ θ < 2π. Take a set of values of θ between zero and 2π and calculate x and y for each from the equations above, then plot y as a function of x.
# b)  Taking this approach a step further, one can make a polar plot r = f(θ) for some function f by calculating r for a range of values of θ and then converting r and θ to Cartesian coordinates using the standard equations x = r cos θ, y = r sin θ. Use this method to make a plot of the Galilean spiral, r=θ2 for 0 ≤ θ ≤ 10π.
# c)  Using the same method, make a polar plot of “Fey’s function”
# Extra: Do the three functions as subplots next to one another | let there be arguments that you pass that will plot all 3 or one of the three 

import numpy as np
import matplotlib.pyplot as plt
import argparse 

parser = argparse.ArgumentParser(description='Something I have yet to understand')
parser.add_argument('-Plot',type=float, default=4 , action='store'
                    ,help="Plot Type values  1.Deltoit Curve , 2.Galelian, 3.Feys , 4.Multiplot | Default vallue is multiplot")
args = parser.parse_args()

theta= np.linspace(0,(2*np.pi),1000) # Our first theta range from 0 to 2pi
theta2= np.linspace(0,(10*np.pi),1000) # Our second theta range from 0 to 10pi
theta3=np.linspace(0,(24*np.pi),1000) # Out third theta range from 0 to 24pi

def Deltoid_Curve(theta):
    """
    Computes the Deltoic Curve x,y components for a given theta range
    """
    x= 2*np.cos(theta) + np.cos(2*theta) #converts theta to x cordinate 
    y= 2*np.sin(theta) - np.sin(2*theta) # converts theta to y cordinate
    
    return(x,y)

def Galelian_Spiral(theta): 
    """
    Computed the Galelian Spirean x,y pair for a given theta range 
    """
    r=theta*2 
    x=r*np.cos(theta) #converts theta to x cordinate 
    y=r*np.sin(theta) # converts theta to y cordinate
    
    return x,y

def Feys(theta):
    """
    Computes Fays x,y pair for a given theta range 
    """
    r=np.exp(np.cos(theta))-2*np.cos(4*theta)+np.sin(theta/12)**5 

    x=r*np.cos(theta) # converts theta to y cordinate
    y=r*np.sin(theta) # converts theta to y cordinate
    
    return x,y

# If loops to identify which plot to make   
if args.Plot == 1:  
    x,y =Deltoid_Curve(theta) # calls function to get x,y pair 

#Plotting Deltoid Curve 
    plt.plot(x,y,color='c')  
    plt.title("Deltoid Curve")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

if args.Plot == 2:
    x,y=Galelian_Spiral(theta2) # calls function to get x,y pair 

#Plotting the Galelian Spiral
    plt.plot(x,y,color='steelblue')
    plt.title("Galilean Spira")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

if args.Plot == 3:
    x,y=Feys(theta3)

#Plotting Fays graph 
    plt.plot(x,y,color='purple') # calls function to get x,y pair
    plt.title("Feys")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

if args.Plot == 4: #Plots all of them at once 
    fig,axs= plt.subplots(1,3,figsize=(16,8))
    axs[0].plot(Deltoid_Curve(theta)[0],Deltoid_Curve(theta)[1],color='c')
    axs[1].plot(Galelian_Spiral(theta2)[0], Galelian_Spiral(theta2)[1],color='steelblue')
    axs[2].plot(Feys(theta3)[0],Feys(theta3)[1],color='purple')

    axs[0].set_title("Deltoid Curve")
    axs[1].set_title("Galelian Spiral")
    axs[2].set_title("Fays")

    plt.show()
 



