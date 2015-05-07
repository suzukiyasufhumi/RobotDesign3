#!/bin/bash -xv

exec 2> /tmp/log

###スティッキービットの解除###
sudo chmod o-t /run/shm/

###マニピュレータの書き込みOKに###
sudo chmod 777 /dev/ttyUSB0

###アプリの起動###
chmod a+x /home/pi/RobotDesign3/robot_io.py
/home/pi/RobotDesign3/robot_io.py
