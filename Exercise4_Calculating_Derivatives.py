#Exsersice  4.3: Calculating derivatives
# Task: 
#a)  Write a program that defines a function f(x) returning the value x(x−1), then calculates the derivative of the function at the point x = 1 using the formula above with δ = 10−2. Calculate the true value of the same derivative analytically and compare with the answer your program gives. The two will not agree perfectly. Why not?
#b)  Repeat the calculation for δ = 10−4, 10−6, 10−8, 10−10, 10−12, and 10−14. You should see that the accuracy of the calculation initially gets better as δ gets smaller, but then gets worse again. Plot your result as a function of δ . Why is this?

import numpy as np
import matplotlib.pyplot as plt
import time 

start= time.time() #used to time it takes to do run the program
x=1 #given value for x, we will take the derivative for one point
delta=np.array([1e-2,1e-4,1e-6,1e-8,1e-10,1e-12,1e-14]) #setting the array of delta values 

import argparse 
parser = argparse.ArgumentParser(description="This program calcuates a function's derivative with one point of x ") #
parser.add_argument('-xval',type=float, default=1 , action='store'
                    ,help=" x value used to calculate our derivative value| note* if this value is undefines it will default to 1")
args = parser.parse_args()

def func(x):
    """
    Calcultes the y value/values of function given an x value/values
    x: may be a singular value or array 
    """
    fx=x*(x-1)
    return fx

def derivative(function,x,delta):
    """
    Calculates the derivative of a given function 
    function: an outside math function you want to take the derivative of 
    x: your x value/ values
    delta: the change between your x points 
    """
    fx=function(x)
    
    df=np.zeros(len(delta))
   
    for i,k in enumerate(delta):
        fdelx= function(x+k)
        df[i]=(fdelx - fx) / k
    return df

df=derivative(func,x,delta)

#Plotting the figure and zoming in on desired area
plt.figure(figsize=(10,8),facecolor='w')
plt.scatter (np.log(delta), df,color='red',marker="*",alpha=0.3)
plt.xlabel("log10($\delta$)")
plt.ylabel("Derivative Value (df)")
plt.xlim(-25,-4)
plt.ylim(0.975,1.025)
plt.show()

#Calculating/ and displaying the time it takes to run the script
end=time.time()
print (f"All Done! This script took {end-start} sec to run")