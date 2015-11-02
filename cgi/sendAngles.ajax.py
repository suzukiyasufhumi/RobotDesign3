#!/usr/bin/env python
#vim:fileencoding=utf-8

'''
The MIT License (MIT)

Copyright (c) 2015 Ryuichi Ueda

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
import os,cgi
import sys,time
import struct

def sendAngles(angles):
	uart = open('/dev/ttyUSB0',"wb")

	J1_ULMT = 150
	J1_LLMT = -150
	angles = [ a if a < J1_ULMT else J1_ULMT for a in angles ]
	angles = [ a if a > J1_LLMT else J1_LLMT for a in angles ]

	s = [str(a) for a in angles ]
	s = ['0' + a if len(a) == 1 else a for a in s ]
	s = ",".join(s) + '\r'
	uart.write(s)

if __name__ == '__main__':
	form = cgi.FieldStorage()

	http_header = "Content-type: text/html\n\n"
	print http_header

	if form.has_key("angles"):
		values = form["angles"].value.split(',')
		values = [ int(x) for x in values ]
		sendAngles(values)
		print "ok"
