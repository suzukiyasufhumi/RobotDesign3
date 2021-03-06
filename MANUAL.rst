===============================================
設計製作論3 コントローラ操作マニュアル
===============================================

このドキュメント
======================================

コントローラの操作方法を記述したものです。

コントローラの構成
======================================

Raspberry Pi 2にAD変換チップ、電磁弁のスイッチを取り付けたものです。
また、Raspberry Pi内部にはWebサーバ（apache2）が動作しており、
一通りの操作は手持ちのPCのブラウザ経由で行うことができます。

推奨環境
======================================

Google Chromeで動作確認済み。画面が小さい場合は縮小して使用のこと。

コントローラのウェブアプリ立ち上げ
======================================

コントローラには演習室のLAN環境に合わせてIPアドレスが振られています。
IPアドレスは、コントローラにつけたタグに書いてあります。

PCを演習室のLAN環境に接続
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PCを演習室のLANに接続します。DHCPを使って接続します。
接続後、ブラウザで外部のサイト（Yahoo等）が閲覧できることを確認します。

次にpingを打ってみましょう。

.. code-block:: bash

	$ ping <コントローラのIPアドレス>
	PING 198.51.100.1 (198.51.100.1): 56 data bytes
	64 bytes from 198.51.100.1: icmp_seq=0 ttl=64 time=0.086 ms
	64 bytes from 198.51.100.1: icmp_seq=1 ttl=64 time=0.088 ms
	64 bytes from 198.51.100.1: icmp_seq=2 ttl=64 time=0.074 ms
	^C

接続が確認できたら、ブラウザを開き、URLの欄に
「http://<コントローラのIPアドレス>」
を入力します。

ロボット用のコントロールパネルが開けば成功です。

オフラインでのウェブアプリの使用
======================================

コントローラに接続しなくても、ブラウザからリポジトリ内のcgi/index.html
を立ち上げることでシミュレータを使うことができます。

