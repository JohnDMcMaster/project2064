#!/usr/bin/env python

from xc2k import parser
from xc2k import container

def run(f, format):
    p = parser.Parser(container.getbits(f, format))

    header = p.header()

    print 'header'
    print '  pad1: %d bytes (min: 4)' % len(header['pad1'])
    print '  preamble: %d' % header['preamble']
    print '  length: %d' % header['length']
    print '  pad2: %d bytes (min: 4)' % len(header['pad2'])

    for frame in p.frames_raw():
        #print frame
        print 'frame: %s' % frame['payload']
    footer = p.footer()
    print 'footer: %d bytes (min: 4)' % len(footer['postamble'])

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description=
        'Dump bitstream info'
    )

    parser.add_argument('--verbose', type=int, help='')
    parser.add_argument('--format', default='bit', help='One of: bin, bit, rom')
    parser.add_argument('fin', help='Input file')
    args = parser.parse_args()
    run(open(args.fin, 'r'), format=args.format)

if __name__ == '__main__':
    main()
