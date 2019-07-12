# 3
import time
mytime = time.localtime()
if mytime.tm_hour < 6 or mytime.tm_hour > 20:
    print ('It is night-time')
else:
    print ('It is day-time')