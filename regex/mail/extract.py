# Data Crunching, p. 52-53

import sys, re

pattern = "([\\w.-]+@[\\w-]+(\\.[\\w-]+)*)"

for arg in sys.argv[1:]:
    input = open(arg, 'r')
    for line in input:
        m = re.search(pattern, line)
        if m:
            address = m.group(1)
            print address
    input.close()
