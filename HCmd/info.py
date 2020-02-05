import blessed
import curses
import time
import numpy as np
import rospy

from sensor_msgs.msg import Joy, BatteryState, Imu
from geometry_msgs.msg import PoseStamped

global axes, buttons
axes = np.zeros(12)
buttons = np.zeros(12)

def _joy_cb(msg):
	global axes, buttons
	axes = ((-1*np.array(msg.axes))+1)/2
	buttons = msg.buttons

def _format_axes(ind,width=20):
    global axes
    width = width-2
    ax = "."*width
    ax_ind = int(axes[ind]*width)
    if ax_ind == width:
        ax_ind = width-1
    ax = "[" + ax[:ax_ind] + "|" + ax[ax_ind+1:] + "] {:.2f}%".format(axes[ind]*100) 
    return ax

def controller_info():
        global axes, buttons
	rospy.init_node("controller_info",anonymous=True)
	rospy.Subscriber("joy", Joy, _joy_cb)	

	term = blessed.Terminal()
	with term.fullscreen(), term.cbreak():
            inp = None
            
            while inp != "q":
	        print(term.clear())
                with term.location(0,term.width-1):
                    print("press 'q' to exit")
                print("YAW   "+_format_axes(0,term.width/2))
                print("PITCH "+_format_axes(1,term.width/2))
                print("ROLL  "+_format_axes(3,term.width/2))
               	inp = term.inkey(0.1)

global battery, local_pose, imu_data

def _battery_cb(msg):
    global battery
    battery = msg

def _local_pose_cb(msg):
    global local_pose
1    local_pose = msg

def _imu_data_cb(msg):
    global imu_data
    imu_data = msg

def drone_info():
    
    global battery, local_pose, imu_data
    battery = ""
    local_pose = ""
    imu_data = ""
    
    rospy.init_node("drone_info", anonymous=True)
    rospy.Subscriber("/mavros/battery", BatteryState, _battery_cb)
    rospy.Subscriber("/mavros/local_position/pose", PoseStamped, _local_pose_cb)
    rospy.Subscriber("/mavros/imu/data", Imu, _imu_data_cb)

    term = blessed.Terminal()
    with term.fullscreen(), term.cbreak():
        inp = None
        
        while inp != "q":
            print(term.clear()) 
            print("BATTERY " + str(battery))
            print("LOCAL POSE " + str(local_pose))
            print("IMU DATA " + str(imu_data))
            inp = term.inkey(0.1)

if __name__ == "__main__":
    drone_info()

