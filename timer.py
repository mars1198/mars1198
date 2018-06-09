import time
from datetime import datetime, timedelta


def setcount():
	global hrs
	global mins
	global secs
	global totalsecs
	print('Set the countdown timer:')
	hrs = int(input('hours: '))
	mins = int(input('minutes: '))
	secs = int(input('seconds: '))
	totalsecs = 3600 * hrs + 60 * mins + secs


def countdown():
	run = str(input('Start? (y/n) >'))
	# Only run if the user types in "y"
	if run == "y":
		ltotalsecs = totalsecs
		while ltotalsecs != 0:
			sec = timedelta(seconds=int(ltotalsecs))
			d = datetime(1, 1, 1) + sec
			print("%d hours %d minutes %d seconds left" % (d.hour, d.minute, d.second))
			# delay for a second
			time.sleep(1)
			# decrement the local seconds total
			ltotalsecs -= 1
			if ltotalsecs == 0:
				print('Tadaa')
setcount()
countdown()
