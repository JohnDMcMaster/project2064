#!/usr/bin/env python

def gen(funci):
    out = ''
    def line(s):
        out += s + '\n'
    
    out += '''
LCANET,5
PART, 2064PC68-70
PWR, 1, VCC
PWR, 0, GND
'''

    '''
    A function of N variables requires 2**N 

    ; SOP form
    ; A B C D  O
    ; 0 0 0 0  0
    ; 0 0 0 1  1*
    ; 0 0 1 0  0
    ; 0 0 1 1  1*
    ; 0 1 0 0  0
    ; 0 1 0 1  0
    ; 0 1 1 0  0
    ; 0 1 1 1  1*
    ; 1 0 0 0  0
    ; 1 0 0 1  0
    ; 1 0 1 0  0
    ; 1 0 1 1  0
    ; 1 1 0 0  0
    ; 1 1 0 1  0
    ; 1 1 1 0  0
    ; 1 1 1 1  1*
    '''
    
    line('SYM, S1, EQN, EQN=(%s)' % func)
    out += '''
PIN, I0, I, ANET
PIN, I1, I, BNET
PIN, I2, I, CNET
    PIN, I3, I, DNET
    PIN, O, O, XNET
END

SYM,S2,IBUF
    PIN,I,I,AIN
    PIN,O,O,ANET
END
SYM,S3,IBUF
    PIN,I,I,BIN
    PIN,O,O,BNET
END
SYM,S4,IBUF
    PIN,I,I,CIN
    PIN,O,O,CNET
END
SYM,S5,IBUF
    PIN,I,I,DIN
    PIN,O,O,DNET
END
SYM,S6,OBUF
    PIN,I,I,XNET
    PIN,O,O,XOUT
END

EXT, AIN, I, , LOC=2
EXT, BIN, I, , LOC=3
EXT, CIN, I, , LOC=4
EXT, DIN, I, , LOC=5
EXT, XOUT, O, , LOC=6

EOF
'''
