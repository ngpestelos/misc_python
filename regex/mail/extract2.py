# Data Crunching, p. 53

import sys, re

pattern = "([\\w.-]+@[\\w-]+(\\.[\\w-]+)*)(.*)"

# use example.txt
for arg in sys.argv[1:]:
    input = open(arg, 'r')
    for line in input:
        while line:
            m = re.search(pattern, line)
            if m:
                address = m.group(1)
                remainder = m.group(3)
                print address
                line = remainder
            else:
                line = None
    input.close()
