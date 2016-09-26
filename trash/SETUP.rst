======================================
コントローラ環境セットアップ
======================================

このドキュメント
======================================

コントローラのRaspberry Piセットアップマニュアルです。
TA用です。

ネットワークの設定
======================================

左側、前側のマニピュレータから順に、
<演習室のセグメント>.1, 
<演習室のセグメント>.2, 
・・・
とつけていくことにします。

セットアップ
======================================

以下のようにGitHubからリポジトリをダウンロードして、
makeします。リポジトリのクローンはホームで実行しましょう。

.. code-block:: bash

	pi@raspberrypi ~ $ git clone https://github.com/ryuichiueda/RobotDesign3.git
	pi@raspberrypi ~ $ cd RobotDesign3/
	pi@raspberrypi ~/RobotDesign3 $ sudo make
	...（ログはちゃんと見ましょう）
	insserv: warning: script 'K01robot_design_3.sh' missing LSB tags and overrides
	（↑このワーニングは無視でOK）
	pi@raspberrypi ~/RobotDesign3 $ sudo reboot
	（再度接続）
	#確認方法1（プロセスが立ち上がっているか調査）
	pi@raspberrypi ~ $ ps aux | grep robot | grep init
	root      2012  0.0  0.2   2752  2208 ?        S    19:47   0:00 /bin/bash -xv /etc/init.d/robotdesign3.sh start
	#確認方法2（センサの値のファイルについてiノード番号が変わっているか調査）
	pi@raspberrypi ~ $ ls -i /run/shm/adconv_values 
	56585 /run/shm/adconv_values
	pi@raspberrypi ~ $ ls -i /run/shm/adconv_values 
	56591 /run/shm/adconv_values

ロボット側の電源が立ち上がっていないと、/tmp/log中に以下のようなワーニングが出ます。
この場合はロボットの電源を入れてRaspberry Piを再起動し、再度/tmp/logを確認しましょう。

chmod: cannot access `/dev/ttyUSB0': No such file or directory
