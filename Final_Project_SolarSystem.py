#This program instends ot simulate the bodies in the solar system


#Imports 
import numpy as np
import matplotlib.pyplot as plt #allows me to plot things along the way to test
from matplotlib.animation import FuncAnimation  #allows me to create animation


#Setting Constants 
G= 6.67430e-11 #Gravitational Constant 
#Sun Mass
S_m=1.989E30 #Solar Mass (kg)

#Planets Masses 
Mu_m= 3.285E23 #Murcury Mass(kg)
V_m= 4.867E24 #Venus Mass (kg)
E_m= 5.972E24 #Earths Mass (kg)
M_m=6.38E23 #Mars Mass (kg)  

#Unsure How Far I will get...
J_m=1.8982E27 #Jupiter Mass (kg)
Sat_m= 5.6834E26 #Saturn Mass (kg)
U_m= 8.6810E25 #Uranis Mass (kg)
N_m= 1.024E26 #Neptune Mass (kg)


#Initial paramaters - Position and Velocity (distance from the sun in m,  mean orbital velocity in m/s)
E_position = np.array([1.4710e11, 0.0, 0.0])  
E_vel = np.array([0.0, 3.0287e4, 0.0])  

M_position = np.array([2.0674e11, 0.0, 0.0])  
M_vel = np.array([0.0, 2.6520e4, 0.0]) 

Me_position = np.array([0.460e11, 0.0, 0.0]) 
Me_vel = np.array([0.0, 4.787e4, 0.0])

V_position = np.array([1.0748e11, 0.0, 0.0])
V_vely = np.array([0.0, 3.502e4, 0.0]) 

S_position = np.array([0, 0, 0])  #The sun will be our center 
S_vel = np.array([0, 0, 0])  


#To go this problem we need the to solve Newtons 2nd law F= G* M* m /r^2 but we need to remember that each of the planets are gravitationally attracted to one another

def accel(position,masses):
    """
    Calculate the acceleration on each body due to gravitaty
    
    Input:
        position: The position vectors of the planet
        masses: The masses of all the planets and sun

    Outputs:
        acc: The acceleration vectors of the N bodies.
    """
    N = len(position) 

    acc = np.zeros(len(position))

    N = len(position)
    acc = np.zeros_like(position)
    for i in range(N):
        for j in range(N):
            if i != j: #we dont want the planet to experience gravity from itself

                r = position[j] - position[i] # our r vector 

                acc[i] += G * masses[j] / np.linalg.norm(r)**3 * r 
    return acc 

def verlet(func ,position, vel,masses, h):
    """
   Verlet integration method for solving 2nd order differential eqs 

   Input:
        func: A function that computes acceleration as a function of position
        position: Initial positions [x,y,z]
        vel: Initial Velocitis [vx,vy,vz]
        masses: masses of all the bodies we want to analyze
        h: time step size
           
   Output:
        position_new: the position after 1 step
            
        vel_new : the velocity after 1 step     
    """

    acc_half = func(position, masses) *0.5 # getting our a/2 term

    position_new = position + vel * h + 0.5 * acc_half * h**2 #get our position 

    acc_new = func(position_new, masses) #update our acceleration 

    vel_new = vel + 0.5 * (acc_half + acc_new) * h #update our velocity

    return position_new, vel_new
   
#We have an acceleration funciton and a varlet function now we need to loop over them to get our values 

#Making a positions and velocity  arrays to loop over 
init_position=np.array([E_position,M_position,Me_position,V_position,S_position])
init_velocity= np.array([E_vel,M_vel,Me_vel,V_vely,S_vel])
masses = np.array([E_m, M_m, Mu_m, V_m, S_m]) #we'll start with the inner planets

#Setting our step sizes
h= 2 * 24 * 3600   # 2 days in seconds 
num_steps = 2* 365   # 2 years 

def orbit(num_steps, h, initial_position, initial_velocity, masses): 
    """
    Calculates the orbital position using the varlet method
    """
    N = len(initial_position)

    positions = np.zeros((num_steps, N, 3))

    positions[0] = initial_position

    velocities = initial_velocity

    for i in range(1, num_steps):
        positions[i], velocities = verlet(accel ,positions[i-1], velocities ,masses,h)

    return positions

positions = orbit (num_steps, h, init_position, init_velocity, masses)


#Finally we need to animate these!!!
fig, ax = plt.subplots()
Earth, = ax.plot([], [], color='blue' , marker='o', markersize=10, label='Earth')
Mars, = ax.plot([], [], color='red',marker='o', markersize=8, label='Mars')
Mercury, = ax.plot([], [], color='black',marker='o', markersize=6, label='Mercury')
Venus, = ax.plot([], [], color='cyan', marker='o', markersize=7, label='Venus')
Sun, = ax.plot([], [], color='yellow',marker='o', markersize=15, label='Sun')
ax.set_xlim(-6e11, 6e11)
ax.set_ylim(-6e11, 6e11)
ax.set_aspect('equal', adjustable='box')
ax.legend()

def init():
    Earth.set_data([], [])
    Mars.set_data([], [])
    Mercury.set_data([], [])
    Venus.set_data([], [])
    Sun.set_data([], [])
    return Earth, Mars, Mercury, Venus, Sun

def animate(i):
    Earth.set_data(positions[i, 0, 0], positions[i, 0, 1])
    Mars.set_data(positions[i, 1, 0], positions[i, 1, 1])
    Mercury.set_data(positions[i, 2, 0], positions[i, 2, 1])
    Venus.set_data(positions[i, 3, 0], positions[i, 3, 1])
    Sun.set_data(positions[i, 4, 0], positions[i, 4, 1])
    return Earth, Mars, Mercury, Venus, Sun

ani = FuncAnimation(fig, animate, init_func=init, frames=num_steps, interval=10, blit=True)
plt.xlabel('X position (m)')
plt.ylabel('Y position (m)')
plt.title('Inner Planet Animation')
plt.grid()
plt.show()
 
