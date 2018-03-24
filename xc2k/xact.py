'''
XACT=/opt/XACT

echo >RUN.BAT
echo "D:" >>RUN.BAT
echo "CD D:\DATA" >>RUN.BAT
echo "D:\MAKEBITS -V -O C:\DESIGN.BIT C:\DESIGN.LCA" >>RUN.BAT

SDL_VIDEODRIVER=dummy dosbox RUN.BAT -c "MOUNT D: $XACT" -exit
'''

import os
import subprocess

XACT_DIR = os.getenv('XACT_DIR', '/opt/XACT')

def lca2bit(lca_dir):
    '''
    Take LCA text file named DESIGN.LCA in lca_dir and compile to BIT file in same directory
    ''' 
    batch = '''\
D:
CD D:\DATA
D:\MAKEBITS -V -O C:\DESIGN.BIT C:\DESIGN.LCA
'''
    batch_fn = os.path.join(lca_dir, 'RUN.BAT')
    try:
        open(batch_fn, 'w').write(batch)
        subprocess.check_call('SDL_VIDEODRIVER=dummy dosbox %s -c "MOUNT D: %s" -exit >/dev/null' % (batch_fn, XACT_DIR), shell=True)
    finally:
        if os.path.exists(batch_fn):
            os.unlink(batch_fn)
