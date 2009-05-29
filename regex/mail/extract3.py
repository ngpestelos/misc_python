# Data Crunching, p. 54

import sys, re

# compiled (see extract2.py)
patObj = re.compile("([\\w.-]+@[\\w-]+(\\.[\\w-]+)*)(.*)")

for arg in sys.argv[1:]:
    input = open(arg, 'r')
    for line in input:
        while line:
            m = patObj.search(line)
            if m:
                address = m.group(1) # it's your job to count groups
                remainder = m.group(3)
                print address
                line = remainder
            else:
                line = None
    input.close()
