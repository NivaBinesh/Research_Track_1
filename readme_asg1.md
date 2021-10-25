                                                               RESEARCH TRACK - 1
                                                                  ASSIGNMENT 1
NAME:NIVA BINESH
REG:NO:5061518
TOPIC:controlling a holonomic robot in a 2D space with a simple 2D simulator
YEAR:2020/2021
PROFESSOR:Carmine Tommaso Recchiuto, Phd

ASSIGNMENT DESCRIPTION:
          This assignment mainly focus on controlling a holonomic robot in a 2D space. It should move continuously making an infinite loop within the boundary set by a given set of coordinates.
          
CODE EXECUTION AND DEPENDENCIES:
          Initially the assignment (GIT LINK) should be git cloned inside the /src folder of your ros workspace. This assignment script is written in python. Before running the code, the following two nodes should be made executable.
          
                  $ chmod +x robo_server.py
                  $ chmod +x robo_client.py

          After the execution, our workspace should be build again with the command: 
          
                  $ catkin_make

PROCESS 1:
          After building our workspace with the catkin_make command, we can run the assignment by two execution processes- First method is using 'roslaunch' command. Here,the nodes are called altogether (we should create a seperate launchfile in which we include the node names and path for the final execution) in a single call.
          
          
                  $ roslaunch rt1_asg1 robo_launch.xml
                  
          In this command, "rt1_asg1" defines the complete package and "robo_launch.xml" define the launch file in which we have decleared the name and path of the individual nodes of our assignment. With this single command, we can launch the complete assignment which calls the master ,the 2d simulator,server and client nodes. Thus, the complete process will run on single step.

PROCESS 2:
          Here we launch the package with individual commands using 'rosrun' for calling individual nodes. So, after running the master, we call the 'stageros' using the following the command:
          
            $ rosrun stage_ros stageros $(rospack find rt1_asg1)/world/exercise.world
            
          While executing the above command, the 2D simulator will start running with the package data provided, as per the depenencies. This is downloaded from the git link- https://github.com/CarmineD8/assignment1.git.
          
          After calling the simulator node, server node is triggered with the command. The server node plays a significant role of generating a new destination point for the robot to move, inside the simulator map.

           $rosrun rt1_asg1 robo_server.py
          
          Once the server node is executed, client node should be executed with the following command and the client works based on the feedback from the server.
           
           $rosrun rt1_asg1 robo_client.py
           
           
         Using either of the above mentioned processes, we can execute the assignment. The execution time for 'roslaunch' is less compared to the 'rosrun' (individual command node execution). There are some factors to be considered- rosrun can only launch one node at a time from a single package, while roslaunch can launch multiple nodes simultaneously.

SYSYTEM NODES:
         In this assignment we are working with two nodes, namely, server and client.
         
Servernode:
          Server node provides new_target, for the Service "Destination". It rsponds to the request of the client with a new random position that consist of two random coordinates named x_destination and y_destination.  
          
client node:
          It updates the speed of the robot and the distance between the current position of the robot and target point. Once the target reached, the node will call the Service new_target which will provide the coordinates of a new destination point.


          
DESCRIBING THE COMPLETE PACKAGE:

 
-robo_server.py
          This file contains the server node script.
          
-robo_client.py
          This file contains the client node script.
-robo_launch.xml:
          It is a launch file, that includes all nodes.
-Destination.srv:
          It specifies a new position for the robot.
           float32 x_destination
           float32 y_destination
           Server generates random numbers in x_destination and y_destination, between the range -6.0 and 6.0 

-CMakelist.txt:
          The CMakelist.txt file contains a set of directives and instructions describing the project's source files and target files.
           If the code is written in python, it should be declared in the script, in cmakelist python section shown below:

           install(PROGRAMS
  	   scripts/robo_server.py
           scripts/robo_client.py
   	   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
           )

 
-package.xml:
           The control file of our assignment that determines the set of metadata components, to retrieve or deploy in a project.   
           
           
         And a rqt graph is attached below to check out the layout of the output of this assignment i.e, the complete relational graph of our system. With this graph we can analyse the ros graph of our application. The communication between the nodes and topics  are also plotted in it.
           
 
               
          
           
 
                  
 
          
                                                                      
