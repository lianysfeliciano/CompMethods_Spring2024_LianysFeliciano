#Exercise 7.1: Fourier transforms of simple functions
# Write Python programs to calculate the coefficients in the discrete Fourier transforms of the following periodic functions sampled at N = 1000 evenly spaced points, and make plots of their amplitudes
#a) A single cycle of a square-wave with amplitude 1
#b) The sawtooth wave yn = n
#c) The modulated sine wave yn = sin(πn/N) sin(20πn/N)


import numpy as np 
import matplotlib.pyplot as plt
from numpy import fft  #to verify our fourtransfor is sutable and can be iverted properly

print(" In this program, a fourer transform is done on the following functions: A Square Wave, A Sawtooth Function and A Sin Function  ")

N = 1000 

square= np.linspace(0,1.0,N)
saw= np.linspace(0,1,N)
sin= np.linspace(0,2*np.pi,N)



def square_wave(x):
    """
    Computes the value of a square wave given a value or array. Outputs a value or array of y value/ values. 
    ========================================================================================================
    
    Inputs
    x: input value or array 

    --------------------------

    Outputs
    y: value or array 

    """
    y=np.zeros(len(x))

    for i in range (len(x)):
        if x[i]> 0.5:
            y[i]= -1
    
        elif x[i] == 0.5: 
            y[i]== 0

        else:
            y[i]= 1

    return y

def sawtooth(x):
    """
    Computes the value of a sawtooth wave given a value or array
    ==============================================================
    Inputs
    x: input value or array 

    --------------------------

    Outputs
    y: value or array 
    
    """
    y = np.zeros(len(x))

    for j,i in enumerate(x):
        
        if i<= 0.25: 
             y[j]= i 
        
        elif 0.25< i <=0.5:
            y[j] = i - 0.25
        
        elif 0.5< i <=0.75:

            y[j] = i - 0.50

        else:
            y[j] = i - 0.75

    return y
        
def mod_sin(x):
    """
    Computes the value of a modulated sine wave function given a value or array
    ===========================================================================
    
    Inputs
    x: input value or array 

    --------------------------

    Outputs
    y: value or array 

    """
    N= len(x)

    y= np.sin( (np.pi* x)/ N)* np.sin( (20* np.pi *x)/ N )

    return y


def ft(k):
    """
    Computes Fourier transform from a given input and output of a function you desire to Fourier transform
    ======================================================================================================

    Input
    k: your y values of the function you would like to transform
    x: your input values for a function you would like to transform 

    -------------------------------------------------------------------------------
    Output

    c : values after transformation

    """
    N = len(k)  # N is the number of points

    c = np.zeros(N // 2 + 1, dtype=complex)  # because these are real function we take 1/2 the points

    for i in range(N // 2 + 1):  # iterate over frequencies (k values)
        for n in range(N):  # iterate over time points (x values)
            c[i] += k[n] * np.exp(-2j * np.pi * i * n / N)

    return c



def ift(c, N):
    """
    Computes the inverse Fourier transform from given Fourier coefficients and number of points.
    ======================================================================================================

    Input
    c: Fourier coefficients
    N: Number of points

    -------------------------------------------------------------------------------
    Output

    x: Inverted values
    """
    x = np.zeros(N, dtype=complex)

    for n in range(N):
        for i, ck in enumerate(c):
            x[n] += ck * np.exp(2j * np.pi * i * n / N)

    return x/N


fig, ax=plt.subplots(1,3,figsize=(18,6))

ax[0].plot(square, square_wave(square))
ax[0].set_title("Square Plot")

ax[1].plot(saw,sawtooth(saw))
ax[1].set_title("Sawtooth")

ax[2].plot(sin,mod_sin(sin))
ax[2].set_title("Module Sin Wave")
fig.suptitle("Functions Prior to Fourier Transform", size=15)
plt.show()



ft_square= ft(square_wave(square))
ft_saw= ft(sawtooth(saw))
ft_sin = ft(mod_sin(sin))

print("The constans refreined after taking the fourier transform of the Square Function are: ", np.real(ft_square*np.conjugate(ft_square)))
print("The constans refreined after taking the fourier transform of the Saw Tooth are: ", np.real(ft_saw*np.conjugate(ft_saw)))
print("The constants retrieved after taking the fourier transform of the Sin function are:",np.real(ft_sin*np.conjugate(ft_sin)))


fig, ax=plt.subplots(1,3,figsize=(18,6))

coef= np.arange(0,501,1)

ax[0].plot(coef,ft_square*np.conjugate(ft_square))
ax[0].set_title("Square Plot")
ax[0].set_xlim(0,20)

ax[1].plot(coef,ft_saw*np.conjugate(ft_saw))
ax[1].set_title("Sawtooth")
ax[1].set_xlim(0,20)

ax[2].plot(coef,ft_sin*np.conjugate(ft_sin))
ax[2].set_title("Module Sin Wave")
ax[2].set_xlim(0,20)
fig.suptitle("Amplitudes", size=15)

plt.show()

