# Data Crunching, p. 50
# Usage: cat sent.mbox | python sent.py

import sys, re

for line in sys.stdin:
  m = re.search("^To: +(.+)$", line)
  if m:
      print m.group(1)
