#!/usr/bin/env python

#To generate a new destination point for the robot
import rospy
import random
from rt1_asg1.srv import Destination , DestinationResponse



def random_targ(req):
    
    rospy.loginfo('robo_goal call')  
#Random point between the given coordinates is generated on x and y      
    x_destination = random.uniform(-6.0, 6.0)
    y_destination = random.uniform(-6.0, 6.0)
#Print a message for the feedback from the server
    print("Feedback from server:")
    print(x_destination, y_destination)
    return DestinationResponse(x_destination,y_destination)

#Initiating the node
rospy.init_node('robo_goal')
#Service of the node
rospy.Service('robo_goal', Destination, random_targ)
#Keep the code running until the service shuts down
rospy.spin()

