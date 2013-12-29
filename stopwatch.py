#!/usr/bin/env python

import time
import sys
import subprocess

if sys.argv[1]:
    minutes = int(sys.argv[1]) * 60

    for sec in xrange(minutes):
        time.sleep(1)
        if sec < 60:
            sys.stdout.write('\r00:%.2d' % sec)
            sys.stdout.flush()
        else:
            sys.stdout.write('\r%.2d:%.2d' % (sec/60, sec - 60 * (sec / 60)))
            sys.stdout.flush()
    sys.stdout.write('\n')
    subprocess.call(['gimp'])
else:
    print 'usage:  %s <number of minutes to countdown>' % (sys.argv[0])
