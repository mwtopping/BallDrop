#BallDrop.py
#many diagnostic print statements are commented out


#imports
import numpy as np
import matplotlib.pyplot as plt
import random

#define constants here
dt = 0.02

#define the ball class
class ball():
    
    #initial conditions
    def __init__(self,xinit,yinit):
        self.pos = np.array([xinit,yinit])
        self.vel = np.array([0,0])
        self.ncollide = 0

    #update position
    def update_position(self):
        self.pos = self.pos+self.vel*dt


    #update the velocity of the ball
    def update_velocity(self):
        
        #do this if there is a collision detected
        if self.collision_detect():
            #print "Collision Detected with object number :", self.collide_index
            #r is the vector from the object to the ball
            #rmag is the magnitude and runit is the normalized r vactor
            r = self.pos - ObstacleList[self.collide_index].pos
            rmag = np.sqrt(r[0]**2+r[1]**2)
            runit = r / rmag
            
            #new velocity calculated based off of the incoming velocity reflected
            #  about the normal to the obstacle
            newvel = (-2*(np.dot(self.vel, runit))*runit + self.vel)
            #print "The objects are ", rmag, " away from each other"
            #print "The normal vector is :", runit
            #print "The resulting velocity is :", newvel
            self.vel = newvel
        elif self.pos[0] > 10:
            self.vel[0] = -self.vel[0]
        elif self.pos[0] < 0:
            self.vel[0] = - self.vel[0]
        else:
            
            accel = np.array([0,-9.8])
            self.vel = self.vel + (accel*dt)


    #draw the ball
    def draw(self):
        ballpoint.set_xdata(self.pos[0])
        ballpoint.set_ydata(self.pos[1])


	#detect collisions for each obstacle in the window
    def collision_detect(self):
        for ii in range(len(ObstacleList)):
            r = self.pos - ObstacleList[ii].pos
            rmag = np.sqrt(r[0]**2+r[1]**2)

            if rmag < 0.3:
                #set a variable for the object that is collided with
                self.collide_index = ii
                self.ncollide += 1
                return 1
        return 0

    




#define the obstacle class
class Obstacle:

    def __init__(self):
        #be created at a random position
        self.pos=[10*random.random(),10*random.random()]

    #add the obstacles position to a list
    def positionadd(self, obstaclepositions):
        obstaclepositions = np.vstack((obstaclepositions,self.pos))
        return obstaclepositions
    
        


#-----------------------------------------------------------------
#
#
#MAIN
#
#
#
#-----------------------------------------------------------------
if __name__ == "__main__":

    #initialize the plot
    #print "Initializing the Plot"
    plt.ion()
    ballpoint, = plt.plot(0.,0.,'ro', markersize=12)
    obstaclepoint, = plt.plot(0.,0., 'ro', markersize=12)
    plt.axis([0,10,0,10])

    #initialize optimization variables
    best_pos_index = 0
    ncolls = np.array([])
    max_ncollide=0

    #print "Initializing the objects"
    #initialize obstacles
    ObstacleList=[]
    for Nobstacles in range(10):
        x = Obstacle()
        ObstacleList.append(x)




    
    
    for startpos in xrange(100):



        #initialize objects
        Ball = ball(startpos/10.,10.5)
        
        #time loop
        #print "Starting the time loop, will be terminated once the ball falls off of the screen."
        #the loop will continue until the ball falls off of the screen
        while Ball.pos[1] > 0:
            #initialize an array that contains the positions of the stationary obstacles
            obstaclepositions = np.array([-1.,-1.])
            #update the velocity and position of the ball object
            Ball.update_velocity()
            Ball.update_position()
            #draw the ball
            Ball.draw()
            #add the obstacles positions to the list
            for obstacle in range(len(ObstacleList)):
                obstaclepositions = ObstacleList[obstacle].positionadd(obstaclepositions)

            #draw the obstacles
            obstaclepoint.set_xdata(obstaclepositions[:,0])
            obstaclepoint.set_ydata(obstaclepositions[:,1])
            #plt.draw()
        ncolls = np.append(ncolls,Ball.ncollide)
        if Ball.ncollide > max_ncollide:
            #print "This time it collided ",Ball.ncollide,"Times, last time it collided ",max_ncollide
            best_pos_index = startpos
            max_ncollide = Ball.ncollide
            
        last_ncollide = Ball.ncollide
        #print "Number of collisions: ", Ball.ncollide
    #print "The best starting position was :", best_pos_index
    #print "The number of collisions for each starting position was :", ncolls



    Ball = ball(best_pos_index/10.,10.5)
        
    #time loop
    #print "Starting the time loop, will be terminated once the ball falls off of the screen."
    #the loop will continue until the ball falls off of the screen
    while Ball.pos[1] > 0:
        #initialize an array that contains the positions of the stationary obstacles
        obstaclepositions = np.array([-1.,-1.])
        #update the velocity and position of the ball object
        Ball.update_velocity()
        Ball.update_position()
        #draw the ball
        Ball.draw()
        #add the obstacles positions to the list
        for obstacle in range(len(ObstacleList)):
            obstaclepositions = ObstacleList[obstacle].positionadd(obstaclepositions)

        #draw the obstacles
        obstaclepoint.set_xdata(obstaclepositions[:,0])
        obstaclepoint.set_ydata(obstaclepositions[:,1])
        plt.draw()
    print Ball.ncollide
        
