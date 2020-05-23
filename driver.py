#Walker Wind
#May 22, 2020

#Self_Playing_Chess_Board


#driver.py --- The program for controlling the motors

#The following code is used to control the motors for the xy plotter in
#the self-playing chess board. There are two motors and four limit 
#switches being controlled by the pi board. Given coordinates from the 
#chess game, the actuator of the board moves pieces off to the side. 

#Libraries included

import chess, pigpio, math

#Pins the circuit

#Limit Switches
lim1 = 1
lim2 = 1
lim3 = 1
lim4 = 1

#Motor 1
en1 = 1
step1 = 1
dir1 = 1

#Motor 2
en2 = 1
step2 = 1
dir2 = 1

#Functions


#Calibrate

#Move to Position
