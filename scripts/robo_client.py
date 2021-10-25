#!/usr/bin/env python

import rospy
import math
import random
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from rt1_asg1.srv import Destination




#Initial position of the robot in the 2D simulator
x_pose = 0.0
y_pose = 0.0

#Setting threshold speed for the robot-Speed limits
speed_th = 0.1
speed_gain = 0.5

#Reads the position of the robot from the odometery topic
def my_odom(msg):

   
    #Defining global varaibles
    global x_pose
    global y_pose
    #Reading the values
    x_pose = msg.pose.pose.position.x
    y_pose = msg.pose.pose.position.y


def main():

    
    
    #To Create a subscriber for the odometry function
    odo_sub = rospy.Subscriber("odom", Odometry,my_odom)
    #To Create a publisher, to update the speed of the robot
    pub = rospy.Publisher('cmd_vel',Twist, queue_size=10)
    rate = rospy.Rate(10) # 10hz

    #Creating the service client  
    restart = rospy.ServiceProxy('robo_goal', Destination)

    while not rospy.is_shutdown():	
        
     	# Requesting a location to reach
    	print("/////Client requesting destination/////.")
    
    	rospy.wait_for_service('robo_goal')
    	try: 
    	    rst = restart()
	    print("/////Destination Reached://///:")
    	    x_destination = rst.x_destination
    	    y_destination = rst.y_destination
    	    print(x_destination, y_destination)
    	except rospy.ServiceException as e:
	    print("/////Service  failed/////: %s" %e)   
	
    	# Distance between the robot and the destination point is requested	
    	distance_x = (x_destination-x_pose)
    	distance_y = (y_destination-y_pose)    
    	distance = math.sqrt(distance_x**2 + distance_y**2)
    
     
    	# while the distance is below the threshold
    	# evaluate the distance between the target and the robot and update the speed
    	while distance > speed_th:

            # The speed of the robot is evaluated
            speed_x = speed_gain * distance_x
            speed_y = speed_gain * distance_y

      	    #And the speed is published
	    twist = Twist()
	    twist.linear.x = speed_x
	    twist.linear.y = speed_y        

	    pub.publish(twist)

            #This is to update the robot position
    	    distance_x = (x_destination-x_pose)
    	    distance_y = (y_destination-y_pose)    
    	    distance = math.sqrt(distance_x**2 + distance_y**2)

        #once the robot reaches the target
    	print('Target location achieved')
    
        
if __name__ == '__main__':

    try:
	#initializing the node
	# anonymous is True to have more than a listener
    	rospy.init_node("robo_controll", anonymous="True",disable_signals=True)
     	main()	
	rate.sleep()
    except KeyboardInterrupt:
	print("***Operation terminated***")
