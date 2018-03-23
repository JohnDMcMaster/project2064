import subprocess
import os

def canonical_sop_term(mask):
    def func(id, set):
        if set:
            return id
        else:
            return '(~%s)' % id
    return func('A', mask & 1) + '*' + func('B', mask & 2) + '*' + func('C', mask & 4) + '*' + func('D', mask & 8)
    

def func(clb):
    # (~A*(~C*(~B*~D)))+((~A*(~C*(~B*D)))+((~A*(~C*(B*~D)))+((~A*(~C*(B*D)))+((~A*(C*(B*D)))+(A*(C*(B*D)))))))
    # Do non-canonical SOP
    ret = ''
    for i in xrange(16):
        i = 1 << i
        if clb & i:
            if len(ret):
                ret += '+'
            ret += canonical_sop_term(i)
    return '(' + ret + ')'
    
def clb2lca(clb):
    out = ''
    out += '''
; LCA Design=SB Part=2064PC68 -- Blocks=6 Nets=5.
; Program=APR Version=5.2.0-base Date=Fri Sep  7 23:59:15 2012.
; Speed File Version 2000.1 Revision 2064.6
Design 2064PC68
Speed -70
Programorder On
Addnet ANET P11.I BA.A
Netdelay ANET BA.A 0.7
NProgram row.B.local.4:BA.A row.B.local.4:PAD58.I
Addnet BNET P12.I BA.C
Netdelay BNET BA.C 0.5
NProgram col.A.local.3:BA.C col.A.local.3:PAD57.I
Addnet CNET P13.I BA.B
Netdelay CNET BA.B 0.0
NProgram BA.B:PAD56.I
Addnet DNET P14.I BA.D
Netdelay DNET BA.D 0.6
NProgram row.C.local.5:BA.D row.C.local.5:PAD55.I
Addnet XNET BA.X P5.O
Netdelay XNET P5.O 2.9
NProgram BB.8.1.2 BB.8.1.4 BC.8.1.0 BC.8.1.7 col.B.local.2:BA.X col.C.local.1:PAD5.O
Nameblk P11 AIN
Editblk P11
Base IO
Config I:PAD BUF:
Endblk
Nameblk P12 BIN
Editblk P12
Base IO
Config I:PAD BUF:
Endblk
Nameblk P13 CIN
Editblk P13
Base IO
Config I:PAD BUF:
Endblk
Nameblk P14 DIN
Editblk P14
Base IO
Config I:PAD BUF:
Endblk
Nameblk BA XNET
Editblk BA
Base F
Config F:C:B:D:A X:F Y: Q: RES: SET: CLK:
'''
    out += 'Equate F = %s\n' % func(clb)
    out += '''
Endblk
Nameblk P5 XOUT
Editblk P5
Base IO
Config I: BUF:ON
Endblk
'''
    return out
    
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
for maski in xrange(16):
    print
    print
    print
    mask = 1 << maski
    print 'Genearting 0x%04X (%s)' % (mask, func(mask))
    make(clb)
    
