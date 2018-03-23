'''
Figure 13. XC2064 Internal Configuration Data Arrangement
11111111                DUMMY BITS (4 BITS MINIMUM) XACT 2.10 GENERATE 8 BITS
0010                    PREAMBLE CODE
<24-BIT LENGTH COUNT>   CONFIGURATION PROGRAM LENGTH
1111                    DUMMY BITS (4 BITS MINIMUM)
0 <DATA FRAME # 0001> 111
0 <DATA FRAME # 0002> 111
0 <DATA FRAME # 0003> 111
...
1111                    POSTAMBLE CODE (4 BITS MIMIMUM)


DATA PROGRAM DATA
REPEATED FOR EACH LOGIC CELL ARRAY IN DAISY CHAIN
                        XC2018        XC2064
CONFIGURATION FRAMES    196            160
BITS PER FRAME    87            71

START-UP REQUIRES THREE CONFIGURATION CLOCKS BEYOND LENGTH COUNT

Sample:
00000000  ff 04 40 0f fb 2e bf 3f  fe 7f fe fc bc ff b7 79  |..@....?.......y|
00000010  b5 fa ff c7 fd fd ff bf  f9 f5 e3 ee cd 9b 8f c5  |................|
00000020  ef 8d ef df 9d ff df f2  fb 6f ef ff fd ba ff db  |.........o......|
...
00007f60  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
*
00007fe0  00 00 00 00 00 00 00 00  00 00 c0 fa f5 f9 f5 f9  |................|
00007ff0  f5 f9 f5 f9 f5 f9 f5 f9  f5 f9 f5 f9 bc fa f5 f9  |................|

0x04 => 0000 0100
Not a good match
Reversing bit order doesn't match => 0010 0000
Switching nibble seems weird
but could possibly be a memory artifact?

so
00000000  ff 04 40 0f fb 2e bf 3f  fe 7f fe fc bc ff b7 79  |..@....?.......y|
ff: dummy
4: preamble
040: length
f: dummy

Bitstream size
xc2064: 12,038 bits
xc2018: 17,878 bits

Configuration data frames
xc2064: 160
xc2018: 197
    conflicts with earlier number

ROM .bin files are 32 KB
Bitstream is only supposed to be < 2KB though

-rwxr-xr-x  1 mcmaster mcmaster 2.2K Sep  9  2012 SBAPR.BIT
Hmm lets focus on those for now


python parse.py test.bit 
'length': 12049
xc2064: 12,038 bits
Sounds promising
Why 11 bit difference?
Note header is 40 bits
Lets just try to read frames
'''

import bitstring
import binascii

def revbits8(n):
    return int('{:08b}'.format(n)[::-1], 2)

def revbits4(n):
    return int('{:04b}'.format(n)[::-1], 2)

def revnib(n):
    return ((n & 0xF) << 4) | ((n >> 4) & 0xF)

def munge(n):
    return (revbits4(n & 0xF) << 4) | revbits4((n >> 4) & 0xF)

class Parser(object):
    def __init__(self, bits, dev='xc2064'):
        self.dev = dev
        self.nframes =      {'xc2018': 196, 'xc2064': 160}[dev]
        self.frame_bits =   {'xc2018': 87,  'xc2064': 71}[dev]
        #self.bits = bitstring.ConstBitStream(self.f.read())
        self.bits = bits
        self.cfglen = None

    def expect(self, want, nbits, msg='expect'):
        got = self.bits.read(nbits).uint
        if want != got:
            raise Exception('%s: want 0x%x, got 0x%x' % (msg, want, got))
        return got

    def expect_run(self, want, minrun, msg):
        '''Keep grabbing bits of type want until not want comes'''
        ret = ''
        while True:
            p = self.bits.peek(1).uint
            if p != want:
                break
            ret += chr(self.bits.read(1).uint)
        if len(ret) < minrun:
            raise Exception("%s: want at least %d bits, got %d" % (msg, want, len(ret)))
        return ret

    def header(self):
        # 4 min, but 8 is typical value (at least XACT 2.10 does)
        pad1 = self.expect_run(1, 4, 'dummy bits 1')
        preamble = self.expect(0b0010, 4, 'preamble code')
        self.cfglen = self.bits.read(24).uint
        pad2 = self.expect_run(1, 4, 'dummy bits 2')
        return {'pad1': pad1, 'preamble': preamble, 'length': self.cfglen, 'pad2': pad2}

    def frame(self):
        preamble = self.expect(0b0, 1, 'frame preamble')
        payload = self.bits.read(71)
        postamble = self.expect(0b111, 3, 'frame postamble')
        return {'preamble': preamble, 'payload': payload, 'postamble': postamble}

    def frames(self):
        ret = []
        for _framei in xrange(self.nframes):
            ret.append(self.frame())
        return ret

    def footer(self):
        postamble = self.expect_run(1, 4, 'postamble')
        return {'postamble': postamble}

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
    p = Parser(bits)

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
