# Removing Elements (Example 3.13 - Dive Into Python)
li = ['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']
print "Initial list"
print li

li.remove('z')
print "Removed z"
print li

li.remove('new') # removes only the first occurrence of new
print "Removed first new"
print li

li.pop()
print "Popped last element"
print li

li.remove('c') # throws an exception
