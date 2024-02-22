#Exersice2.1: Ball Dropped From a Tower
#Task: Write a program that asks the user to enter the height in meters of the tower and then calculates and prints the time the ball takes until it hits the ground, ignoring air resistance. Use your program to calculate the time for a ball dropped from a 100 m high tower.

import numpy as np
import sys

print(sys.argv, "\n\n", len(sys.argv)) # sys.argv Allows us to interpret arguments as a list of strings

if len(sys.argv) != 1:
    h = float(sys.argv[1])#This is our user input for the height of the ball
else: 
    print("Please Enter The Height")
    h=float(input()) # In case it wasnt stated when running the script

g= 9.81 #The acceleration due to gravity 

t= np.sqrt(2*h/g) #computes time it takes for ball to land

print(t)
