import subprocess
import os

from xc2k.clb2lca import clb2lca

def canonical_sop_term(mask):
    def func(id, set):
        if set:
            return id
        else:
            return '(~%s)' % id
    return func('A', mask & 1) + '*' + func('B', mask & 2) + '*' + func('C', mask & 4) + '*' + func('D', mask & 8)
    
    
def make(clb):
    print 'Cleaning old output...'
    clbs = '0x%04X' % clb
    print 'Generating LCA...'
    lca = clb2lca(clb)
    print 'Writing LCA...'
    open('SBAPR.LCA', 'w').write(lca)
    print 'Synthesizing...'
    subprocess.check_call("make bits morebits", shell=True)
    print 'Saving result...'
    if os.path.exists(clbs):
        print 'WARNING: removing old dir'
        subprocess.check_call("rm -rf %s" % clbs, shell=True)
    subprocess.check_call("./release.sh %s" % clbs, shell=True)

print
print
print
print 'Generating references...'
# 4 variables => 16 bit memory required
make(0x0000)
make(0xFFFF)
for maski in xrange(16):
    print
    print
    print
    mask = 1 << maski
    print 'Genearting 0x%04X (%s)' % (mask, func(mask))
    make(clb)
