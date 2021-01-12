# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pywhatkit
Names = ["Aaron","Robin","Tom"] #Contact name
Number = ["+9191xxx","+91912xxx","+1-21xxx"] #Contact Number on WhatsApp
n = len(Names)
H = 3
M = 22 % 60
for i in range(n):
	text = "All The Best " + Names[i]
	pywhatkit.sendwhatmsg(Number[i],text,H,M)
	if (M%60 == 59 and H == 23):
		H = 0
	elif (M%60 == 59):
		H += 1
	else:
		M += 1
