#!/bin/bash -xv

exec 2> /tmp/up_and_run.bash

tmp=/tmp/$$

###mimeマルチパートでPOSTされてくるデータを読み込む###
dd bs=${CONTENT_LENGTH}	count=1	|
nkf -wLux > $tmp-upload

cat $tmp-upload > /tmp/aho

###ファイル名を取り出す###
FILE=$(head -n 3 $tmp-upload | grep -o 'filename="[^"]*"' | sed 's/[^"]*"//' | sed 's/".*//')
echo $FILE > /tmp/boke

sed -n '/^$/,$p' $tmp-upload	|
tail -n +2 			|
grep -v '^----'			> $tmp-contents

###ファイル形式ごとの処理###
case "$FILE" in
*.cc )
	mv $tmp-contents $tmp-main.cc

	g++ $tmp-main.cc -lm -o $tmp-main
	chmod +x $tmp-main
	#実行したいファイルの名前を/tmp/executableに入れる
	mv $tmp-main /tmp/executable
;;
*.c )
	mv $tmp-contents $tmp-main.c

	gcc $tmp-main.cc -lm -o $tmp-main
	chmod +x $tmp-main
	#実行したいファイルの名前を/tmp/executableに入れる
	mv $tmp-main /tmp/executable
;;
*)
	cat $tmp-contents > /tmp/executable
;;
esac

chmod a+x /tmp/executable

echo 'Content-type: text/html'
echo 
/tmp/executable
