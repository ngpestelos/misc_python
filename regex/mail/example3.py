import sys, re

patObj = re.compile("([\\w.-]+@[\\w-]+(\\.[\\w-]+)*)(.*)")

for arg in sys.argv[1:]:
    input = open(arg, 'r')
    for line in input:
        while line:
            m = patObj.search(line)
            if m:
                address = m.group(1)
                remainder = m.group(3)
                print address
                line = remainder
            else:
                line = None
    input.close()
