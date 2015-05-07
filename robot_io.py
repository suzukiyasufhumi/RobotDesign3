#!/usr/bin/python
# vim:fileencoding=utf-8
# ref: http://qiita.com/f_nishio/items/93387feade923a0d20a0

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

import time, os
import wiringpi2 as wp

class RobotIO:
	PIN_BASE = 100
	EV_PIN = 21

	def __init__(self):
		wp.mcp3002Setup (RobotIO.PIN_BASE, 0)
		wp.wiringPiSetupGpio()

	def read_da(self,ch):
		return wp.analogRead(RobotIO.PIN_BASE+ch)

	def write_ev(self,value):
		wp.digitalWrite(RobotIO.EV_PIN,value)

if __name__ == '__main__':
	rio = RobotIO()
	while True:
		with open("/run/shm/adconv_values.tmp","w") as f:
			ans = str(rio.read_da(0)) + " " + str(rio.read_da(1)) + "\n"
			f.write(ans)
		
		os.rename("/run/shm/adconv_values.tmp","/run/shm/adconv_values")

		try:
			with open("/run/shm/ev_on_off","r") as f:
				v = int(f.readline())
				rio.write_io(v)
		except:
			pass
			

		time.sleep(0.1)
	
