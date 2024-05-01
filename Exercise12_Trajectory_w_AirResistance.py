#Exercise 8.7: Trajectory with air resistance
"""
Many elementary mechanics problems deal with the physics of objects moving or flying through the air, but they almost always ignore friction and air resistance to make the equations solvable. If we’re using a computer, however, we don’t need solvable equations.
Consider, for instance, a spherical cannonball shot from a cannon standing on level ground. The air resistance on a moving sphere is a force in the opposite direction to the motion with magnitude

F = \frac{1}{2} \pi R^2\rho C v^2, 

where R is the sphere’s radius, ρ is the density of air, v is the velocity, and C is the so-called coefficient of drag (a property of the shape of the moving object, in this case a sphere).

Starting from Newton’s second law, F = ma, show that the equations of motion for the position (x, y) of the cannonball are
\ddot{x} = - {\pi R^2\rho C\over2m}\, \dot{x}\sqrt{\dot{x}^2+\dot{y}^2},
\ddot{y} = - g - {\pi R^2\rho C\over2m}\, \dot{y}\sqrt{\dot{x}^2+\dot{y}^2},

where m is the mass of the cannonball, g is the acceleration due to gravity, and \dot{x} and \ddot{x} are the first and second derivatives of x with respect to time.

Change these two second-order equations into four first-order equations using the methods you have learned, then write a program that solves the equations for a cannonball of mass 1 kg and radius 8 cm, shot at 30º to the horizontal with initial velocity 100 ms−1. The density of air is ρ = 1.22 kg m−3 and the coefficient of drag for a sphere is C = 0.47. Make a plot of the trajectory of the cannonball (i.e., a graph of y as a function of x).
When one ignores air resistance, the distance traveled by a projectile does not depend on the mass of the projectile. In real life, however, mass certainly does make a difference. Use your program to estimate the total distance traveled (over horizontal ground) by the cannonball above, and then experiment with the program to determine whether the cannonball travels further if it is heavier or lighter. You could, for instance, plot a series of trajectories for cannonballs of different masses, or you could make a graph of distance traveled as a function of mass. Describe briefly what you discover.

Use Plotly for this labs 
"""

import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import astropy.constants as c

print("This lab shows the tragetory of a thrown object accoundting for air resistance.")
#Constants
m= 1
R= 0.8 
V0=100
density= 1.22
p = 1.22 
C= 0.47
theta= np.radians(30)
g=c.g0.value



#We need to have our 4 iniital values 

xi= 0 #the sparting x-position is 0

yi= 0 #the starting y-position is 0

Vxi=V0*np.cos(theta) #this is our initial Vx (what we feed into 4th order Runge Kunta)

Vyi=V0*np.sin(theta) #this is our iniital Vy (What we feed into our 4th order Runge Kunta)

init_array=np.array([xi,yi,Vxi,Vyi]) # our initial array




def Delta_Velocity(array,t):
    """
    Computes the change of the x and y velocity

    Input: 
    array: initial array 

    Output 
    dVx, dVy : some point

    """
    Vx = array[2]
    Vy = array[3]
 
    V = np.sqrt( Vx**2 + Vy**2)
    dx = Vx
    dy = Vy
    dVx = - (np.pi * R**2 * p * C * Vx * V) / (2*m)
    dVy = - g - (np.pi * R**2 * p * C * Vy * V) / (2*m)
    return np.array([dx,dy,dVx,dVy,],float)
    

def fouth_order_Runge_Kunta(func,h, r0, num_points=int(10)): 
    """
    Computes the fourth order RUnge Kunta. 

    Inputs: 
    func : a function that describes the change in your variable
    h : desired step size
    r0 : starting point
    max_time : how much time passes 

    Output: 
    r : array
    time: array 
    """
    
    r = np.zeros ((len(n_points), len(r0)))
 
    r[0] = r0 #setting the starting value to our initial conditions 

    for i in range(1, len(num_points)):
            
        k1 = h * func(r[i - 1], num_points[i - 1])

        k2 = h * func(r[i - 1] + 0.5 * k1, num_points[i - 1] + 0.5 * h)

        k3 = h * func(r[i - 1] + 0.5 * k2, num_points[i - 1] + 0.5 * h)

        k4 = h * func(r[i - 1] + k3, num_points[i - 1] + h)
        
        r[i] = r[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6    
        
    return r

#Picking an h 
h=0.01 # Lets try this first \(O_o)/

# Time interval and step size
t0= 0 
tf=10

# Create arrays for t and r values
n_points = np.arange(t0, tf, h)

array =fouth_order_Runge_Kunta(Delta_Velocity,h, init_array, num_points=n_points)

x_points=array[0]
y_points=array[1]

#Plotting path of moition
plt.plot(x_points,y_points)
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Projectile Motion Trajectory" )
plt.show()

#Plot using plotly express
label_dict = dict(x = "Distance (m)", y = "Height (m)")
fig = px.line(x = x_points, y = y_points, title = "Projectile Motion Trajectory", labels = label_dict)
fig.update
fig.show()

#Using Varying Masses 

mass = np.linspace(0,10,5) #making an arrat of masses to distance as a function of mass
label_dict = dict(x="Distance (m)", y="Height (m)")
fig = px.line(title="Trajectory", labels=label_dict)

t2_points = np.arange(0, 10, h)

# Iterate over each mass value
for m in mass: 
    array2=fouth_order_Runge_Kunta(Delta_Velocity,h, init_array, num_points=n_points)

    x_points = array2[0]
    y_points = array2[1]

    # Add a trace for this mass value
    fig.add_scatter(x=x_points, y=y_points, mode='lines', name=f"Mass {m}")

# Show the plot
fig.show()
print("From this result we should find that the more massive an object is the less distance it travels however we don't see this, this is probably becasue of a bug that I cant seem to find")

