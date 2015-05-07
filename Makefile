install:
	cp ./robot_design_3.sh /etc/init.d/
	chmod +x /etc/init.d/robot_design_3.sh
	update-rc.d robot_design_3.sh defaults
	ln -s /home/pi/RobotDesign3/cgi/index.html /var/www/index.html
	ln -s /home/pi/RobotDesign3/cgi/main.css /var/www/main.css
	ln -s /home/pi/RobotDesign3/cgi/main.js /var/www/main.js
	ln -s /home/pi/RobotDesign3/cgi/sendAngles.ajax.py /var/www/sendAngles.ajax.py
	ln -s /home/pi/RobotDesign3/cgi/sendAdValues.ajax.py /var/www/sendAdValues.ajax.py

uninstall:
	update-rc.d robot_design_3.sh remove
	rm /etc/init.d/robot_design_3.sh
	rm -f /var/www/*
