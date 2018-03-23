#!/usr/bin/env python
import sys

indenting = False
for line in open(sys.argv[1]).readlines():
    line = line.strip()
    if line.find('Endblk') == 0:
        indenting = False
    if line.find('Addnet') == 0:
        print
    if line.find('Nameblk') == 0:
        print
    prefix = ''
    if indenting:
        prefix = '    '
    print prefix + line
    if line.find('Editblk') == 0:
        indenting = True

    