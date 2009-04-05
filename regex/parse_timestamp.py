import re

tstamp = 'Sun Apr  5 08:19:36 2009'
print re.match('^\w{3}\W(\w{3})\W\W(\d)\W(\d{2}):(\d{2}):(\d{2})\W(\d{4})$', tstamp).groups()
