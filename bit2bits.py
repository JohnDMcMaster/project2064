'''
Create a .bits file, a text equivilent representation of the bitstream
Inspired by the .bits format from project x-ray

Unlike 7 series though, there are a lot of 1's in unused logic
'''

from xc2k import parser
from xc2k import container

def run(f, format):
    p = parser.Parser(container.getbits(f, format))

    for framei, frame in enumerate(p.frames()):
        for biti, bit in enumerate(frame['payload']):
            # self.nframes =      {'xc2018': 196, 'xc2064': 160}[dev]
            # self.frame_bits =   {'xc2018': 87,  'xc2064': 71}[dev]
            if bit:
                print '%02x_%02x' % (framei, biti)

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
