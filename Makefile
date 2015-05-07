install:
	#nkfのインストール
	apt-get install nkf

	#ウェブサーバとアプリのセットアップ
	apt-get install apache2
	cp ./apache2.conf /etc/apache2/sites-available/default
	service apache2 restart
	rsync -av --delete /home/pi/RobotDesign3/cgi/ /var/www/

	chmod a+x /home/pi/RobotDesign3/robot_io.py

	#init.dに起動スクリプトを仕込む
	cp robotdesign3.sh /etc/init.d/
	chmod +x /etc/init.d/robotdesign3.sh
	update-rc.d robotdesign3.sh defaults

uninstall:
	#init.dのスクリプトを消す
	update-rc.d robotdesign3.sh remove
	rm /etc/init.d/robotdesign3.sh
	#他のものはインストールしっぱなしで
