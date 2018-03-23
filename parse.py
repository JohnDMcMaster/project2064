import bitstring
import binascii

import xc2k.parser

def revbits8(n):
    return int('{:08b}'.format(n)[::-1], 2)

def revbits4(n):
    return int('{:04b}'.format(n)[::-1], 2)

def revnib(n):
    return ((n & 0xF) << 4) | ((n >> 4) & 0xF)

def munge(n):
    return (revbits4(n & 0xF) << 4) | revbits4((n >> 4) & 0xF)

def getbits_bin(f):
    return bitstring.ConstBitStream(bytes=f.read())

def getbits_bit(f):
    # bit w/ header
    buff = f.read()
    buff = buff[0x76:]
    return bitstring.ConstBitStream(bytes=buff)

def getbits_rom(f):
    # random rom file they gave me
    buff = bytearray()
    for b in f.read():
        # Reverse bits, swap nibbles
        buff += chr(munge(ord(b)))
    return bitstring.ConstBitStream(bytes=buff)

def run(f, format):
    bits = {
        'bin': getbits_bin,
        'bit': getbits_bit,
        'rom': getbits_rom,
        }[format](f)
    p = xc2k.parser.Parser(bits)

    header = p.header()

    print 'header'
    print '  pad1: %d bytes (min: 4)' % len(header['pad1'])
    print '  preamble: %d' % header['preamble']
    print '  length: %d' % header['length']
    print '  pad2: %d bytes (min: 4)' % len(header['pad2'])

    for frame in p.frames():
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
