#question no 1
#Many of Python's time functions handle time as a tuple of 9 numbers

#Index	Field	           Values
#0	4-digit year	   2008
#1	Month    	   1 to 12
#2	Day	           1 to 31
#3	Hour	           0 to 23
#4	Minute	           0 to 59
#5	Second	           0 to 61 (60 or 61 are leap-seconds)
#6	Day of Week	   0 to 6 (0 is Monday)
#7	Day of year	   1 to 366 (Julian day)
#8	Daylight savings   -1, 0, 1, -1 means library determines DST






#question no 2
import time
print(time.gmtime())

#queston 3 4 and 5
import datetime
now =  datetime.datetime.now()
print(now.strftime("%B"))
print(now.strftime("%A"))
print(now.strftime("%d"))


#question no 6
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)


#question no 7 and 8
import math
print(math.factorial(5))
print(math.gcd(30,45))

#question no 9
import os
print(os.getcwd())

