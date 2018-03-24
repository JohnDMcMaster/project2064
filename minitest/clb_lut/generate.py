import subprocess
import os

from xc2k.clb2lca import clb2lca, gen_clbs
from xc2k.xact import lca2bit
from xc2k.bit2bits import bit2bits

def make(val):
    print
    print
    print
    print 'val: 0x%04X' % val
    dout = 'out_%04X' % val
    if not os.path.exists(dout):
        os.mkdir(dout)

    clbs = dict([(k, 0) for k in gen_clbs()])
    clbs['HH'] = val
    lca_fn = '%s/DESIGN.LCA' % dout
    open(lca_fn, 'w').write(clb2lca(clbs))

    bit_fn = '%s/DESIGN.BIT' % dout
    bits_fn = '%s/DESIGN.BITS' % dout
    lca2bit(dout)
    bit2bits(bit_fn, bits_fn)

def run():
    # 4 variables => 16 bit memory required
    make(0x0000)
    make(0xFFFF)
    for maski in xrange(16):
        make(1 << maski)

run()
