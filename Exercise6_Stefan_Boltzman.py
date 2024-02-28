#Extercise 5.12: The Stefan-Boltzmann Eq
#Tasks: 
#a)  Show that the total energy per unit area radiated by a black body is
#b)  Write a program to evaluate the integral in this expression. Explain what method you used, and how accurate you think your answer is.
#c)  Even before Planck gave his theory of thermal radiation around the turn of the 20th century, it was known that the total energy W given off by a black body per unit area per second followed Stefan’s law: W = alphaT4, where σ is the Stefan–Boltzmann constant. Use your value for the integral above to compute a value for the Stefan–Boltzmann constant (in SI units) to three significant figures. Check your result against the known value, which you can find in books or on-line. You should get good agreement.

import numpy as np
import scipy.constants as cons #used ot get physcial constants that are up to date very large 
import astropy.constants as c #used for getting constant (this is used for this assignment)
import astropy.units as u  # to have a way of coding units 


x=np.linspace(0+0.0001,1-0.0001,10000)

def func(u): 
    """
    """
    x=(1/(1/u)-1)
    du=1/(x+1)**2
    uterm= (u**3/(np.exp(u)-1))*du

    return uterm

def Simpson_Rule(function,a,b,n_max):
    """
    Computes the Simpsons Rule for Interegration
    function: desired function you are taking the intergral of 
    a: lower bound of intergration
    b: uppper bound of intergration
    n_max: the number of slices to compute
    """
    
    f_a=function(a) #passing the first values into the function
    
    f_b=function(b) # passing the last value into the function
    
    delta_x=(b-a)/n_max # computing the change of each step (delta x)
    
    K_sum1=0.0 # This is needed to sum over our equation in the loop
    K_sum2=0.0 # For the second loop
    
    for k in range (1,n_max//2):
        
        K_sum1= K_sum1+ function(a+delta_x*(2*k-1))
        
    for k in range (1,(n_max//2)-1):
    
        K_sum2= K_sum2 + function(a +(2*k*delta_x)) # computing the sum
        
    
    F= (delta_x/3)*(f_a+f_b +4*K_sum1 +2*K_sum2) # computing the trapazoidal reimen sum
    
    return (F)

I =Simpson_Rule(func,0,1,10000)

const= (c.k_B**4 )/(4*np.pi**2 *c.c**2 *c.hbar**3)

alpha=const*I
print(I)
print("Alpha= ", alpha)