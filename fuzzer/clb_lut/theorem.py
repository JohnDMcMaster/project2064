'''
Given CLB_NM
N => frame number
M => frame bit offset
is the first row or column? actually not sure
'''
lut_n2frame = {
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
LUT_NFRAMES = 2
lut_n2off = {
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

base_mask = [
    (0x09, 0x04),
    (0x09, 0x05),
    (0x0a, 0x05),
    (0x0a, 0x04),
    (0x0b, 0x04),
    (0x0c, 0x04),
    (0x0d, 0x04),
    (0x0e, 0x04),
    (0x0f, 0x04),
    (0x10, 0x04),
    (0x13, 0x04),
    (0x14, 0x04),
    (0x15, 0x04),
    (0x16, 0x04),
    (0x17, 0x04),
    (0x18, 0x04),
    (0x19, 0x04),
    (0x1a, 0x04),
    (0x1a, 0x05),
    ]

def run(fin, fout):
    for row in 'ABCDEFGH':
        for col in 'ABCDEFGH':
            

def main():
    import argparse

    parser = argparse.ArgumentParser(
        description=
        'Convert a .bits file into a segmatch compatible theorem file'
    )

    parser.add_argument('--verbose', type=int, help='')
    parser.add_argument('fin', nargs='?', default='/dev/stdin', help='Input file')
    parser.add_argument('fout', nargs='?', default='/dev/stdout', help='Output file')
    args = parser.parse_args()
    run(open(args.fin, 'r'), open(args.fout, 'w'))

if __name__ == '__main__':
    main()
