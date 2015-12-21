install:
	cp ./robot_design_3.sh /etc/init.d/
	chmod +x /etc/init.d/robot_design_3.sh
	update-rc.d robot_design_3.sh defaults
	rsync -av /home/pi/RobotDesign3/cgi/ /var/www/
	#echo 21 > /sys/class/gpio/export
	#echo out > /sys/class/gpio/gpio21/direction

uninstall:
	update-rc.d robot_design_3.sh remove
	rm /etc/init.d/robot_design_3.sh
	rm -f /var/www/*
