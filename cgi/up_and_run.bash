#!/bin/bash -xv

exec 2> /tmp/up_and_run.bash

tmp=/tmp/$$

dd bs=${CONTENT_LENGTH}	count=1	|
nkf -wLux > $tmp-upload

sed '1,/^$/s/^/\/\//' $tmp-upload	|
sed '$s/^/\/\//'	> $tmp-main.cc


gcc $tmp-main.cc -lm -o $tmp-main
chmod +x $tmp-main
$tmp-main
