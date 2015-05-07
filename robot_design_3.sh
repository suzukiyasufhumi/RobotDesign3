#!/bin/sh -evx

exec 2> /tmp/log

#デバイスファイルのパーミッション変更
sudo chmod 777 /dev/ttyUSB0

#実行
chmod a+x /home/pi/RobotDesign3/adconv.py
/home/pi/RobotDesign3/adconv.py

echo OK > /tmp/OK
