# Deleting Items (Example 3.5 - Dive Into Python)
d = {'server' : 'mpilgrim', 'uid' : 'sa', 'database' : 'master', \
  42 : 'douglas', 'retrycount' : 3}
del d[42]
print d

d.clear()
print d