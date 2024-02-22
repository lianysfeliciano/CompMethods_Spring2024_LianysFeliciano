#Exercise 2.4: Spaceship
# Task:  Write a program to ask the user for the value of x and the speed v as a fraction of the speed of light c, then print out the time in years that the spaceship takes to reach its destination 
#(a) In the rest frame of an observer on Earth 
#(b) As perceived by a passenger on board the ship.
# Use your program to calculate the answers for a planet 10 light years away with v = 0.99c.

import numpy as np
import argparse 

parser = argparse.ArgumentParser(description='Something I have yet to understand') #allows you to name and take argumetns

parser.add_argument('-distance',type=float, action='store',required="True") #creating distance input argument
parser.add_argument('-velocity',type=float, action='store',required="True") #creating velocity input argument

args = parser.parse_args() # putting the args into a list so its ealiy 
print("Distance",args.distance, "Velocity", args.velocity) #print out input values to notify user

def Rest_Frame(dis,vel): 
        """
        Computes rest frame time. Point of voew from user on Earth from imput distnace and velocity
        """
        t_rest=dis/vel
        print("Earth Time: ", t_rest)
        return t_rest #returnes Rest Frame Time

def Passenger_POV(vel,t_rest):
        """
        Computes space frame time from velocity and rest frame time
        """
        gamma = 1/np.sqrt(1-(vel**2)) #gamma is our divisor

        t_space= t_rest/gamma #computing time from space refrance frame

        print("Space Time:", t_space)
        
# Rest_Frame(x,v)
Passenger_POV(args.velocity,Rest_Frame(args.distance,args.velocity)) #calling function to compute both rest and space frame times 
