#!/bin/sh

sudo ln -s /home/hornet/catkin_ws/src/asdp4_hornet/services/roscore/roscore.service /etc/systemd/system/
sudo ln -s /home/hornet/catkin_ws/src/asdp4_hornet/services/mavros/mavros.service /etc/systemd/system/

sudo systemctl enable --now roscore
sudo systemctl enable --now mavros

