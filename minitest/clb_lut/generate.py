import subprocess
import os

from xc2k.clb2lca import clb2lca, gen_clbs
from xc2k.xact import lca2bit
from xc2k.bit2bits import bit2bits

def make(clb, val):
    print '%s val: 0x%04X' % (clb, val)
    dout = 'out_%s_%04X' % (clb, val)
    if not os.path.exists(dout):
        os.mkdir(dout)

    clbs = dict([(k, 0) for k in gen_clbs()])
    clbs[clb] = val
    lca_fn = '%s/DESIGN.LCA' % dout
    open(lca_fn, 'w').write(clb2lca(clbs))

    bit_fn = '%s/DESIGN.BIT' % dout
    bits_fn = '%s/DESIGN.BITS' % dout
    lca2bit(dout)
    bit2bits(bit_fn, bits_fn)

def run():
    if 0:
        # 4 variables => 16 bit memory required
        clb = 'HH'
        make(clb, 0x0000)
        make(clb, 0xFFFF)
        for maski in xrange(16):
            make(clb, 1 << maski)

    for row in 'ABCDEFGH':
        make(row + 'H', 0xFFFE)
    for col in 'ABCDEFGH':
        make('H' + col, 0xFFFE)

run()
