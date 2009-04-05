# http://mail.python.org/pipermail/tutor/2006-March/045729.html

import time, datetime
timestring = '2005-09-01 12:30:09'
time_format = '%Y-%m-%d %H:%M:%S'
mytime = time.strptime(timestring, time_format)
t = time.mktime(mytime)
print datetime.datetime.fromtimestamp(t)
