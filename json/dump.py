import simplejson as json

d = {"a" : [1,2,3], "b" : [4,5,6], "c" : [7,8,9]}
f = file('out.js', 'w')
json.dump(d, f)
print "See out.js"
