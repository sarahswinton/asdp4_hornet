#!/usr/bin/env python

import rospy

from sensor_msgs.msg import Joy
from asdp4_hornet.msg import GimbalControl
from std_msgs.msg import Header

import numpy as np

def cb(msg):
	print("Buttons:")
	print(msg.buttons)
	print("Axses:")
	print(msg.axes)

        # This is just an example
        but = msg.buttons
        ax = msg.axes

        # Left analogue stick  -> left/right = yaw
        #                      -> up/down = pitch
        # Right analogue stick -> left/right = roll       

        yaw = ax[0]
        pitch = ax[1]
        roll = ax[3]

        A = but[0]
        B = but[1]
        X = but[2]
        Y = but[3]
        r1 = but[5]
        r2 = abs((-1+ax[5])/2) # Joy node returns -1 to 1 for r2 and l2, this converts it to 0 to 1)
        l1 = but[4]
        l2 = abs((-1+ax[2])/2)
      
        gimbContHeader = Header(seq=seq,frame_id='jan was here', stamp=rospy.Time.now()) 
        gimbCont = GimbalControl(header=gimbContHeader, buttons=(A,B,X,Y,r1,r2,l1,l2),axes=(yaw,pitch,roll))
        pub.publish(gimbCont)

if __name__ == "__main__":
        global seq
        seq = 0
        rospy.init_node("gimbalcontrol")
        global pub
        pub = rospy.Publisher("/gimbalcontrol/control/data",GimbalControl,queue_size=10)
        rospy.Subscriber("joy", Joy, cb)
        rospy.spin()
	




