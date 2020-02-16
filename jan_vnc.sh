#!/bin/sh

# https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-vnc-on-ubuntu-18-04

if [ "$1" = "local" ]; then
	if [ -z "$(which vncviewer)" ]; then
		echo "vncviewer is not installed\nPlease run apt-get install tigervnc"
	fi
	# Setup on local machine
	ssh -L 5902:127.0.0.1:5902 -C -N -J jhewers@jhe.duckdns.org jhewers@192.168.1.51 &
	# Connect via tigerVNC
	vncviewer DotWhenNoCursor=1 localhost:5902
elif [ "$1" = "server" ]; then
	if [ -z "$(which x0vncserver)" ]; then
		echo "x0vncserver is not installed\nPlease run apt-get install tigervnc-scraping-server"
	fi
	# Start server on ubuntu vm
	x0vncserver -passwordfile ~/.vnc/passwd -display :0 -rfbport 5902
else
	echo "Incorrect or empty option given"
	echo "\tlocal - local machine VNC setup"
	echo "\tserver - server VNC setup"
fi
