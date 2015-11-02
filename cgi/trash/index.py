#!/usr/bin/env python
#vim:fileencoding=utf-8

main_html = "/var/www/main.html"
http_header = "Content-type: text/html\n\n"

print http_header

with open(main_html,'r') as f:
	for line in f:
		print line
