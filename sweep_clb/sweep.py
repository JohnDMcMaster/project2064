import subprocess
import os
import sys

def gen_clb_names():
    # "The format for CLB locations is two letters. The first letter indicates the row, the second letter indicates the column
    for row in [chr(ord('A') + i) for i in xrange(8)]:
        for col in [chr(ord('A') + i) for i in xrange(8)]:
            yield row + col


def init_clbs():
    global clbs
    clbs = {}
    for clb_name in gen_clb_names():
        # value doesn't matter so much as long as its fixed
        clbs[clb_name] = 0x0
init_clbs()

def canonical_sop_term(mask):
    def f(id, set):
        if set:
            return id
        else:
            return '(~%s)' % id
    if mask > 0xF:
        raise ValueError('4 variable max of 0xF')
    return f('A', mask & 1) + '*' + f('B', mask & 2) + '*' + f('C', mask & 4) + '*' + f('D', mask & 8)
    
def func(clb):
    # (~A*(~C*(~B*~D)))+((~A*(~C*(~B*D)))+((~A*(~C*(B*~D)))+((~A*(~C*(B*D)))+((~A*(C*(B*D)))+(A*(C*(B*D)))))))
    # Do non-canonical SOP
    print 'Generating for CLB 0x%04X' % clb
    if clb == 0:
        # Special case: make a contradiction
        return '((~A)*A)'
    ret = ''
    for i in xrange(16):
        mask = 1 << i
        if clb & mask:
            print 'Masked %d (bit position 0x%04X)' % (i, mask)
            if len(ret):
                ret += '+'
            ret += canonical_sop_term(i)
    return '(' + ret + ')'

def equate(which):
    return func(clbs[which])

from sweep_lca import *

def make(export_to):
    print 'Cleaning old output...'
    subprocess.check_call("make clean", shell=True)
    print 'Generating LCA...'
    lca = clb2lca(equate)
    print 'Writing LCA...'
    open('SBAPR.LCA', 'w').write(lca)
    print 'Synthesizing...'
    subprocess.check_call("make bits morebits", shell=True)
    print 'Saving result...'
    subprocess.check_call("./release.sh %s" % export_to, shell=True)

def loop_clb(clb_name, clb_config):
    export_to = 'CLB_%s_0x%04X' % (clb_name, clb_config)
    if os.path.exists(export_to):
        if g_overwrite:
            print 'WARNING: removing old dir %s' % export_to
            subprocess.check_call("rm -rf %s" % export_to, shell=True)
        else:
            print 'WARNING: skipping existing dir %s' % export_to
            return
    #print 'Tried synth on %s' % export_to
    #sys.exit(1)
    print
    print
    print
    print '****************************' 
    init_clbs()
    clbs[clb_name] = clb_config
    print 'Genearting %s w/ config 0x%04X (%s)' % (clb_name, clb_config, func(clb_config))
    make(export_to)
    #sys.exit(1)

g_overwrite = False
    
print
print
print
for clb_name in gen_clb_names():
    print
    print
    print
    print '****************************' 
    print 'Das CLB %s' % clb_name
    print '****************************' 
    print
    print
    loop_clb(clb_name, 0x0000)
    loop_clb(clb_name, 0xFFFF)
    # 4 variables => 16 bit memory required
    for clb_config in xrange(16):
        loop_clb(clb_name, 1 << clb_config)
