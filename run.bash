#!/bin/bash -exv

###スティッキービットの解除###
sudo chmod o-t /run/shm/

###マニピュレータの書き込みOKに###
sudo chmod 777 /dev/ttyUSB0

###ウェブサーバとアプリのセットアップ###
sudo apt-get install apache2
sudo cp ./apache2.conf /etc/apache2/sites-available/default
sudo service apache2 restart
sudo rsync -av --delete /home/pi/RobotDesign3/cgi/ /var/www/

chmod a+x /home/pi/RobotDesign3/robot_io.py
sudo /home/pi/RobotDesign3/robot_io.py
