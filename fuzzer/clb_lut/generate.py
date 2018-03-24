import random

from xc2k.clb2lca import clb2lca, gen_clbs
#from xc2k.xact import lca2bit

def run():
    # All CLBs set to random values
    # 4LUT => 16 possible values => 16 bit config
    clbs = {}
    metaf = open("design.csv", 'w')
    metaf.write('clb,val\n')
    for clb in gen_clbs():
        # 0000 is treated special, omit for now
        # omit FFFF as well just to be safe
        val = random.randint(0x1, 0xFFFE)
        metaf.write('%s,0x%04X\n' % (clb, val))
        clbs[clb] = val

    open('DESIGN.LCA', 'w').write(clb2lca(clbs))
    #lca2bit()

run()
