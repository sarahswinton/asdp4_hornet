#!/bin/bash

# This script starts up the mavros_posix_sitl.launch file under ros (with a ros node obviously) on a ubuntu vm
# as well as starting an instance of QGC.

cd ~/PX4/Firmware
QGroundControl
source setup_px4_ros.sh

### BODY OF ~/PX4/Firmware/setup_px4_ros.sh
###
### Requires: gazebo px4 mavros qgroundcontrol

#	#!/bin/bash
#	
#	# SETUP ENV
#	
#	source ~/catkin_ws/devel/setup.zsh    # (optional)
#	source Tools/setup_gazebo.bash $(pwd) $(pwd)/build/px4_sitl_default
#	export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:$(pwd)
#	export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:$(pwd)/Tools/sitl_gazebo
#	export ROS_MASTER_URI="http://ubiquityrobot:11311" # ros master node hosted on seperate pc
#	
#	roslaunch px4 mavros_posix_sitl.launch
