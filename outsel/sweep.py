#!/usr/bin/env python
'''
Sweeps across LUT input muxes
'''
import subprocess
import os
import sys

def gen_clb_names():
    # "The format for CLB locations is two letters. The first letter indicates the row, the second letter indicates the column
    for row in [chr(ord('A') + i) for i in xrange(8)]:
        for col in [chr(ord('A') + i) for i in xrange(8)]:
            yield row + col


g_overwrite = False

def gen_loop(clb_name):
    def gen(f_vars, g_vars):
        # Config F:B:C:Q G:B:C:D X:F Y:G Q: RES:D SET:A CLK:
        config = 'F:%s G:%s X:F Y:G Q: RES:D SET:A CLK:' % (':'.join(f_vars), ':'.join(g_vars))
        f = '%s*(%s*%s)' %  (f_vars[0], f_vars[1], f_vars[2])
        g = '%s*(%s*%s)' % (g_vars[0], g_vars[1], g_vars[2])
        return ( '%s__F_%s__G_%s' % (clb_name, f_vars, g_vars), '''\
Design 2064PC68

Editblk ''' + clb_name + '''
    Base FG
    Config ''' + config + '''
    Equate F = ''' + f + '''
    Equate G = ''' + g + '''
Endblk''')

    yield gen('ABC', 'ABC')
    yield gen('ABD', 'ABC')
    yield gen('ABD', 'ABD')
    yield gen('ACD', 'ABD')
    yield gen('ACD', 'ACD')
    yield gen('BCD', 'ACD')
    yield gen('BCD', 'BCD')
    yield gen('BCQ', 'BCD')
    yield gen('BCQ', 'BCQ')
    
    
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
    
    for (out_name, lca) in gen_loop(clb_name):
        export_to = out_name
        if os.path.exists(export_to):
            if g_overwrite:
                print 'WARNING: removing old dir %s' % export_to
                subprocess.check_call("rm -rf %s" % export_to, shell=True)
            else:
                print 'WARNING: skipping existing dir %s' % export_to
                continue
        
        print 'Cleaning old output...'
        subprocess.check_call("make clean", shell=True)
        print 'Writing LCA...'
        open('SBAPR.LCA', 'w').write(lca)
        print 'Synthesizing...'
        subprocess.check_call("make bits morebits", shell=True)
        print 'Saving result...'
        subprocess.check_call("./release.sh %s" % export_to, shell=True)
