#Exercise 10.8: Calculate a value for the integral
#Tasks
#a) Show that the probability distribution p(x) from which the sample points should be drawn is given by
#b)Using your formula, sample N = 1,000,000 random points and hence evaluate the integral. You should get a value around 0.84.

import numpy as np


print("This progrma creates a transformation fucntion and uses imoprtant sampling to calculate the intergral of the function:  x^-0.5 / (e^x +1)")

rng= np.random.default_rng() # gets up our random number generator 

#Transformation 
def transformation_func(z):
    """
    This function transforms a set of unfirom distributed numbers to a set of numbers with a distribution of px.
    Where px= 1/(2 sqrt(x))

    Input:
    z= Normally distributes set of values

    Output:
    x= set of values with a distribution px
    """
    x=z**2
    return x

def func(x):
    """
    Function f(x)/w(x) which allowxs us to adjust for the ugly part of our original equation
    """
    f= 2 /( np.exp(x)+1 )
    return f


#Now lets compute the intergral

N=1000000

z= rng.uniform(low=0,high=1,size=N) # our uniform array of values between 0 and 1 

x=transformation_func(z) #this is our w(x) our tranformed array

f= func(x) #this is out f(x)

I= (1/N) * (np.sum(f))

print('Intergral Evaluated to Be:', I)




