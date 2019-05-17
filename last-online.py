#!/usr/bin/python
import sys
users= open(sys.argv[1] if len(sys.argv) > 1 else 'usercache.json')
from json import load
from datetime import datetime as dt, timedelta as d
print('PLAYER'.ljust(16) + '  DAYS HR:MN')
for user in (
 (
  e[1].ljust(16), str(e[0].days).rjust(5),
  e[0].seconds/3600, e[0].seconds/60%60
 )
 for e in sorted(
  (
   dt.today() -
   (dt.strptime(u['expiresOn'][:16],'%Y-%m-%d %H:%M')
   - d(days=31)), u['name']
  )
  for u in load(users)
 )
): print("%s %s %02i:%02i" % user)
