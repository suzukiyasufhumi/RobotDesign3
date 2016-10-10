install:
	#Raspbianのアップデート
	rpi-update

	#WiringPiのインストール
	sudo pip install wiringpi2 --upgrade

	#nkfのインストール
	apt-get install nkf

	#ウェブサーバとアプリのセットアップ
	apt-get install apache2
	cp ./apache2.conf /etc/apache2/sites-available/default
	service apache2 restart
	rsync -av --delete /home/pi/RobotDesign3/cgi/ /var/www/

	sudo crontab crontab.conf
	echo "DO REBOOT"
uninstall:
	sudo crontab -r
