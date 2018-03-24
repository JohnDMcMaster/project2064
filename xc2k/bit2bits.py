from xc2k import parser
from xc2k import container

def bit2bits(fin, fout, format='bit'):
    bit2bitsf(open(fin, 'r'), open(fout, 'w'))

def bit2bitsf(fin, fout, format='bit'):
    p = parser.Parser(container.getbits(fin, format))

    for framei, frame in enumerate(p.frames()):
        for biti, bit in enumerate(frame['payload']):
            # self.nframes =      {'xc2018': 196, 'xc2064': 160}[dev]
            # self.frame_bits =   {'xc2018': 87,  'xc2064': 71}[dev]
            if bit:
                fout.write('%02x_%02x\n' % (framei, biti))
