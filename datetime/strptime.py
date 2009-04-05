# See the library documentation on the time module

from datetime import datetime
import time

tstamp = datetime.today().ctime()
parsed = time.strptime(tstamp, '%a %b %d %H:%M:%S %Y')

# fromtimestamp(...) needs a float
print datetime.fromtimestamp(time.mktime(parsed))
