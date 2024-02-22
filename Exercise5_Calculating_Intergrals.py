#Exercise 4.4 : Calculating Intergrals 
# Tasks 
#a) Write a program to evaluate the integral above with N = 100 and compare the result with the exact value. The two will not agree very well, because N = 100 is not a sufficiently large number of slices.
#b) Increase the value of N to get a more accurate value for the integral. If we require that the program runs in about one second or less, how accurate a value can you get?
import numpy as np
from tqdm import tqdm
import argparse 

parser = argparse.ArgumentParser(description="This program calcuates a function's intergral  with N slices")
parser.add_argument('-N',type=float, default=10 , action='store'
                   ,help=" The N argument determins teh number of slices for the intergral ")
args = parser.parse_args()

def intergrate (min,max,N):
    h=2/N
    y=0
    x=np.arange(0,N+1,1)
    #print(x)
    for i in tqdm(range(len(x))):
        x[i]=-1+h*i 
        y= y+ (np.sqrt(1-x[i]**2)) * h
    
    return y

print("Intergral= ",intergrate(-1,1,args.N))

