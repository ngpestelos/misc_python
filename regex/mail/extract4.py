import sys, re

# group 1 (email)
# group 2 (domain)
# group 3 (remainder)
pattern = re.compile("([\\w.-]+@[\\w-]+(\\.[\\w-]+)*)")

for arg in sys.argv[1:]:
    input = open(arg, 'r')
    for line in input:
        for address in re.finditer(pattern, line):
            print address.group(1)
