#!/usr/bin/env python
import sys

header = None

indenting = False

nets = list()

# Nameblk P2 P2IN
pin_blocks = dict()
# Nameblk AD P3NET
clb_blocks = dict()

buffer = []

for line in open(sys.argv[1]).readlines():
    line = line.strip()
    if len(line) == 0:
        continue
    if line == 'Addnet':
        complete_line()
        active_list = 
    