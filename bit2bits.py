#!/usr/bin/env python

'''
Inspired by the .bits format from project x-ray
Unlike 7 series though, there are a lot of 1's in unused logic
'''

from xc2k.bit2bits import bit2bits

def run(fin, fout, format):
    bit2bits(fin, fout, format)

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
