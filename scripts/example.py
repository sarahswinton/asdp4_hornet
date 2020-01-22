#!/usr/bin/env python
# vim:set ts=4 sw=4 et:

import csv
import time

import rospy
import mavros

from mavros_msgs.msg import Waypoint, WaypointList, CommandCode
from mavros_msgs.srv import WaypointPull, WaypointPush, WaypointClear, \
    WaypointSetCurrent, CommandBool, CommandHome, CommandInt

from sensor_msgs.msg import NavSatFix

import numpy as np

import coverage_planner

#Taken from MAVROS source code for reference
#FRAMES = {
#    Waypoint.FRAME_GLOBAL: 'GAA',
#    Waypoint.FRAME_GLOBAL_REL_ALT: 'GRA',
#    Waypoint.FRAME_LOCAL_ENU: 'LOC-ENU',
#    Waypoint.FRAME_LOCAL_NED: 'LOC-NED',
#    Waypoint.FRAME_MISSION: 'MIS'
#}
#
#NAV_CMDS = {
#    CommandCode.NAV_LAND: 'LAND',
#    CommandCode.NAV_LOITER_TIME: 'LOITER-TIME',
#    CommandCode.NAV_LOITER_TURNS: 'LOITER-TURNS',
#    CommandCode.NAV_LOITER_UNLIM: 'LOITER-UNLIM',
#    CommandCode.NAV_RETURN_TO_LAUNCH: 'RTL',
#    CommandCode.NAV_TAKEOFF: 'TAKEOFF',
#    CommandCode.NAV_WAYPOINT: 'WAYPOINT',
#    # Maybe later i will add this enum to message
#    112: 'COND-DELAY',
#    113: 'COND-CHANGE-ALT',
#    114: 'COND-DISTANCE',
#    115: 'COND-YAW',
#    177: 'DO-JUMP',
#    178: 'DO-CHANGE-SPEED',
#    181: 'DO-SET-RELAY',
#    182: 'DO-REPEAT-RELAY',
#    183: 'DO-SET-SERVO',
#    184: 'DO-REPEAT-SERVO',
#    201: 'DO-SET-ROI',
#}

def setArm(bol):
    rospy.wait_for_service('/mavros/cmd/arming')
    try:
        arming = rospy.ServiceProxy('mavros/cmd/arming', CommandBool)
        arming(bol)
    except rospy.ServiceException, e:
        print("Service arm call failed: %s"%e)

def getCurPos():
    print("Getting global GPS position")

    global_string = "/mavros/global_position/global"    
    try:
        curPos = rospy.wait_for_message(global_string, NavSatFix) #/mavros/global_pos/global is a subscriber so use this to get one message. It broadcasts at around 50Hz otherwise
        print("Get cur pos: (%s, %s)"%(curPos.latitude, curPos.longitude))
        return curPos
    except rospy.ServiceException as exc:
        print("Service did not process request: " + str(exc))

def clearMission():
    print("Clearing misison of PX4")
    rospy.wait_for_service("/mavros/mission/clear")
    clear = rospy.ServiceProxy("mavros/mission/clear", WaypointClear)
    print("Cleared %s"%clear())

def setHome(lat, lng, alt, cur_gps=False):
    if cur_gps:
        print("Setting home to current position")
    else:
        print("Setting home to (%s, %s)"%(round(lat, 4), round(lng,4)))

    set_home_string = "/mavros/cmd/set_home"
    rospy.wait_for_service(set_home_string)
    setHome = rospy.ServiceProxy(set_home_string, CommandHome)
    try:
        print("Set home: %s"%setHome(cur_gps, lat, lng, alt).success)
    except rospy.ServiceException as exc:
        print("Service did not process request: " + str(exc))

def returnToLaunch():
    print("Calling RTL service")

    RTL_string = "/mavros/cmd/command_int"
    rospy.wait_for_service(RTL_string)
    RTL = rospy.ServiceProxy(RTL_string, CommandInt)
    try:
        print("RTL: %s"%RTL(command=CommandCode.NAV_RETURN_TO_LAUNCH))
    except rospy.ServiceException as exc:
        print("Service did not process request: " + str(exc))

def setWayPoints(swirl=True):

    clearMission()
    pos = getCurPos()

    wps = []
    lat = pos.latitude
    lng = pos.longitude
    setHome(0, 0, 0, cur_gps=True)
    wps.append(Waypoint(command= CommandCode.NAV_TAKEOFF,frame=Waypoint.FRAME_GLOBAL_REL_ALT, x_lat=lat, y_long=lng, z_alt=5, autocontinue=True))

    x = lat
    y = lng
    if swirl:            
        for i in np.arange(0, 10*np.pi, 0.2):
            # Cause circles are boring
            x = lat + 0.00001*i*np.cos(i)
            y = lng +0.00001*i*np.sin(i)
            wps.append(Waypoint(command= CommandCode.NAV_WAYPOINT, frame=Waypoint.FRAME_GLOBAL_REL_ALT, x_lat=x, y_long=y,  z_alt=5, autocontinue=True))
    else:

        start_lat = lat
        start_lng = lng

        scale = 0.01
        ox = [lat, lat+scale+scale/2, lat+scale, lat, lat]
        oy = [lng, lng, lng+scale, lng+scale/2, lng]
        reso = 0.0005

        rx, ry = coverage_planner.planning(ox, oy, reso)

        print("Number of nodes: {}".format(len(rx)))

        for i in range(len(rx)):
            x = rx[i]
            y = ry[i]
            wps.append(Waypoint(command= CommandCode.NAV_WAYPOINT, frame=Waypoint.FRAME_GLOBAL_REL_ALT, x_lat=x, y_long=y,  z_alt=5, autocontinue=True))




    wps.append(Waypoint(command= CommandCode.NAV_RETURN_TO_LAUNCH, frame=Waypoint.FRAME_MISSION, x_lat=0, y_long=0,  z_alt=0, autocontinue=True))
 

    print("Beginning WPs push")
    path = '/mavros/mission/push' 
    rospy.wait_for_service(path)
    print("Response from service... pushing WPs")
    wps_push = rospy.ServiceProxy(path, WaypointPush)
    try:
          resp1 = wps_push(0,wps)
          print("WPs pushed: %s"%resp1.success)
    except rospy.ServiceException as exc:
          print("Service did not process request: " + str(exc))

if __name__ == "__main__":
	print("Beginning example.py...")
	rospy.init_node("mavros_test", anonymous=True)
        setArm(True)
        setWayPoints(swirl=False)

