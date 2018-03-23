#!/usr/bin/env python

'''
Inspired by the .bits format from project x-ray
Unlike 7 series though, there are a lot of 1's in unused logic
'''

from xc2k import parser
from xc2k import container

def run(fin, fout, format):
    p = parser.Parser(container.getbits(fin, format))

    for framei, frame in enumerate(p.frames()):
        for biti, bit in enumerate(frame['payload']):
            # self.nframes =      {'xc2018': 196, 'xc2064': 160}[dev]
            # self.frame_bits =   {'xc2018': 87,  'xc2064': 71}[dev]
            if bit:
                fout.write('%02x_%02x\n' % (framei, biti))

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description=
        'Create a .bits file, a text equivalent representation of the bitstream'
    )

    parser.add_argument('--verbose', type=int, help='')
    parser.add_argument('--format', default='bit', help='One of: bin, bit, rom')
    parser.add_argument('fin', nargs='?', default='/dev/stdin', help='Input file')
    parser.add_argument('fout', nargs='?', default='/dev/stdout', help='Output file')
    args = parser.parse_args()
    run(open(args.fin, 'r'), open(args.fout, 'w'), format=args.format)

if __name__ == '__main__':
    main()
