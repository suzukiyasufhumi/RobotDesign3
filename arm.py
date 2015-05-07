#!/usr/bin/python
# vim:fileencoding=utf-8

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

import sys,time
import struct

uart = open('/dev/ttyUSB0',"wb")

def sendAngles(j1,j2,j3,j5,j6):
	global uart

	J1_ULMT = 150
	J1_LLMT = -150
	angles = [j1,j2,j3,j5,j6]
	for a in angles:
		if a > J1_ULMT:   a = J1_ULMT
		elif a < J1_ULMT: a = J1_LLMT

	s = ",".join([str(x) for x in angles]) + '\r'
	uart.write(s)

if __name__ == '__main__':
	sendAngles(40,10,10,10,10)
