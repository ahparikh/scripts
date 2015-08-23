#!/usr/bin/python
import sys

f = open('/tmp/gqtest', 'w')
if len(sys.argv) > 1:
  out = ' '.join(sys.argv[1:])
  f.write(out)
  f.write('\n')
else:
  f.write("hello world\n")

f.close
