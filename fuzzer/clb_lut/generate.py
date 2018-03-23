import random

from xc2k.clb2lca import clb2lca, gen_clbs
#from xc2k.xact import lca2bit

def run():
    # All CLBs set to random values
    # 4LUT => u16
    #clbs = dict([(k, random.randint(0xFFFF)) for k in gen_clbs()])
    clbs = {}
    metaf = open("design.txt", 'w')
    metaf.write('clb,val')
    for clb in gen_clbs():
        val = random.randint(0x0000, 0xFFFF)
        metaf.write('%s,0x%04X' % (clb, val))
        clbs[clb] = val

    open('DESIGN.LCA', 'w').write(clb2lca(clbs))
    #lca2bit()

run()
