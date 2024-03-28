# Exercise 10.3: Brownian Motion
#Tasks
#a) Create a sim pf particles in gas that randomly colides 
#b) create an animation of said motion

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

print("This code simulated a Brownian Motion and animates it.")



rng= np.random.default_rng() # our random number generator 


#what kind of random number do we want? We want numbers that represent a step up or down 

 #this will determine weather we step forward of backwards 

steps=rng.integers(low=1,high=5,size=100) #used to determine where the point moves

point= np.array([0.0,0.0]) #our starting point is the origin

print("Demo for one point movement after 100 steps")

print ("Starting Point: ", point)

for i in steps:
    if i ==1: 
       point[1] =point[1] + 1 #moving up
    
    elif i== 2: 
        point[1]=point[1] - 1 #moving down
    
    elif i== 3: 
        point[0]=point[0]+ 1 #moving to the right
    
    else: 
        point[0]= point[0] -1 #moving to the left

print("Ending Point:", point)
    

#function for the animation 
def moving_point(rng,N):
    """
    This function will intake a random number renerator, generate a set of numbers that will trace the "Brownian Movement of a point

    Inputs: 
    rng = random number negerator
    N = number of steps for the point to move

    Outbuts: 
    x = an array of the x cordinates of the point
    y = an array of the y cordinates of the point
    """

    xpoint= np.zeros(N) #our starting point is the origin
    ypoint=np.zeros(N)

    for i in range(len(xpoint)-1): 
        
        step=rng.integers(low=1,high=5,size=1)

        if step== 1: 
            xpoint[i+1]=xpoint[i] + 1 #moving to the right

        elif step == 2: 
            xpoint[i+1]=xpoint[i] - 1 #moving to the left
        
        elif step== 3: 
            ypoint[i+1]=ypoint[i] + 1 #moving up
        
        else: 
            ypoint[i+1]=ypoint[i] - 1 #moving down

    return(xpoint,ypoint)

x,y = moving_point(rng,N= 100)


#creating the animation 
fig= plt.figure(figsize=(10,10))  
ax= plt.axes(xlim=(-50,50),ylim=(-50,50))
point=plt.Circle((0,0),radius=3,facecolor='steelblue')
plt.title("Brownian Motion")
ax.add_patch(point)

def init():
    point.center = (0, 0) 
    ax.add_patch(point)
    return point

def animate(i):
    x_animation = x[i] 
    y_animation = y[i]
    point.center = (x_animation, y_animation)
    return point,


anim = animation.FuncAnimation(fig, animate,frames=len(x), init_func= init)
#anim.save("Brownian_Motion.mp4")
plt.show()
