'''
Given CLB_NM
N row => frame bit offset
M col => frame number
'''
lut_r2off = {
    'A': 0x3e,
    'B': 0x36,
    'C': 0x2e,
    # +
    'D': 0x25,
    'E': 0x1d,
    'F': 0x15,
    # +
    'G': 0x0c,
    'H': 0x04,
    }
# Potential vs observed
# LUT_NOFF = 0x08
LUT_NOFF = 0x02

lut_c2frame = {
    'A': 0x8b,
    'B': 0x79,
    'C': 0x67,
    # +
    'D': 0x53,
    'E': 0x41,
    'F': 0x2f,
    # +
    'G': 0x1b,
    'H': 0x09,
    }
LUT_NFRAMES = 0x12

def load_bits(fin):
    ret = set()
    for l in fin:
        # bit_04_0f
        _prefix, wordi, offi = l.split('_')
        ret.add((int(wordi, 16), int(offi, 16)))
    return ret

def load_design(fin):
    ret = {}
    fin.readline()
    for l in fin:
        k, v = l.split(',')
        v = int(v, 16)
        ret[k] = v
    return ret

def run(bitf, designf, fout):
    bitdb = load_bits(bitf)
    designdb = load_design(designf)

    for rowi, row in enumerate('ABCDEFGH'):
        for coli, col in enumerate('ABCDEFGH'):
            '''
            seg 00020500_000
            bit 00_22
            ...
            bit 35_52
            bit 35_53
            tag CLB.SLICE_X0.C5FF.ZINI 1
            tag CLB.SLICE_X0.C5FF.ZRST 0
            tag CLB.SLICE_X0.CLKINV 0
            '''
            fout.write('seg %02X%02X\n' % (rowi, coli))
            base_frame = lut_c2frame[col]
            base_off = lut_r2off[row]
            for framei in xrange(LUT_NFRAMES):
                frame = base_frame + framei
                for offi in xrange(LUT_NOFF):
                    off = base_off + offi  
                    if (frame, off) in bitdb:
                        fout.write('bit %02X_%02X\n' % (framei, offi))

            val = designdb[row + col]
            for maski in xrange(16):
                expect = 1 ^ int(bool((val & (1 << maski))))
                fout.write('tag CLB.LUT[%02X] %d\n' % (maski, expect))

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description=
        'Find bit locations'
    )

    parser.add_argument('--verbose', type=int, help='')
    parser.add_argument('bits', help='.bits input file')
    parser.add_argument('design', help='design.txt input file')
    parser.add_argument('segdata', help='segadata output file')
    args = parser.parse_args()
    run(open(args.bits, 'r'), open(args.design, 'r'), open(args.segdata, 'w'))

if __name__ == '__main__':
    main()
