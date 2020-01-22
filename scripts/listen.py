#!/usr/bin/env python
import rospy
from mavros_msgs.msg import WaypointReached

def waypointSuccessCallback(msg):
    print(msg.wp_seq)
    

if __name__ == '__main__':
   rospy.init_node('iris_waypoint_node', anonymous=True)
   rospy.Subscriber("/mavros/mission/reached", WaypointReached, waypointSuccessCallback)

   rospy.spin()