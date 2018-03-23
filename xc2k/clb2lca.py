#!/usr/bin/env python

def gen_clbs():
    # "The format for CLB locations is two letters. The first letter indicates the row, the second letter indicates the column
    for row in [chr(ord('A') + i) for i in xrange(8)]:
        for col in [chr(ord('A') + i) for i in xrange(8)]:
            yield row + col

def canonical_sop_term(mask):
    def f(id, set):
        if set:
            return id
        else:
            return '(~%s)' % id
    if mask > 0xF:
        raise ValueError('4 variable max of 0xF')
    return f('A', mask & 1) + '*' + f('B', mask & 2) + '*' + f('C', mask & 4) + '*' + f('D', mask & 8)
    
def equate(clb):
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

def clb2lca(clbs):
    out = ''
    out += '''
; LCA Design=SB Part=2064PC68 -- Blocks=120 Nets=92.
; Program=APR Version=5.2.0-base Date=Sun Sep  9 18:30:33 2012.
; Speed File Version 2000.1 Revision 2064.6
Design 2064PC68
Speed -70
Programorder On
Addnet P2NET P2.I BD.A
Netdelay P2NET BD.A 1.5
NProgram BE.8.1.0 BE.8.1.7 row.B.local.1:BD.A col.E.local.1:PAD8.I
Addnet P3NET AD.Y P3.O
Netdelay P3NET P3.O 1.4
NProgram AE.8.2.5 AE.8.2.6 col.E.local.3:AD.Y row.A.local.4:PAD7.O
Addnet P3TEMPNET BD.X AD.C
Netdelay P3TEMPNET AD.C 0.0
NProgram AD.C:BD.X
Addnet P4NET P4.I BC.A
Netdelay P4NET BC.A 3.5
NProgram BD.8.1.0 BD.8.1.7 row.B.local.1:BC.A col.D.local.1:PAD6.I
Addnet P5NET AC.Y P5.O
Netdelay P5NET P5.O 3.4
NProgram AD.8.2.5 AD.8.2.6 col.D.local.3:AC.Y row.A.local.4:PAD5.O
Addnet P5TEMPNET BC.X AC.C
Netdelay P5TEMPNET AC.C 0.0
NProgram AC.C:BC.X
Addnet P6NET P6.I BB.A
Netdelay P6NET BB.A 1.5
NProgram BC.8.1.0 BC.8.1.7 row.B.local.1:BB.A col.C.local.1:PAD4.I
Addnet P7NET AB.Y P7.O
Netdelay P7NET P7.O 1.4
NProgram AC.8.2.5 AC.8.2.6 col.C.local.3:AB.Y row.A.local.4:PAD3.O
Addnet P7TEMPNET BB.X AB.C
Netdelay P7TEMPNET AB.C 0.0
NProgram AB.C:BB.X
Addnet P8NET P8.I BA.A
Netdelay P8NET BA.A 1.5
NProgram BB.8.1.0 BB.8.1.7 row.B.local.1:BA.A col.B.local.1:PAD2.I
Addnet P9NET AA.Y P9.O
Netdelay P9NET P9.O 1.4
NProgram AB.8.2.5 AB.8.2.6 col.B.local.3:AA.Y row.A.local.4:PAD1.O
Addnet P9TEMPNET BA.X AA.C
Netdelay P9TEMPNET AA.C 0.0
NProgram AA.C:BA.X
Addnet P11NET P11.I CA.A
Netdelay P11NET CA.A 2.7
NProgram CA.8.1.1 CA.8.1.2 BA.8.1.1 BA.8.1.4 row.C.local.1:CA.A col.A.local.2:PAD58.I
Addnet P12NET CB.Y P12.O
Netdelay P12NET P12.O 5.0
NProgram CC.8.2.0 CC.8.2.5 BB.8.2.3 BB.8.2.7 BC.8.2.5 BC.8.2.6 col.C.local.3:CB.Y row.B.local.4:PAD57.O
Addnet P12TEMPNET CA.Y CB.B
Netdelay P12TEMPNET CB.B 0.0
NProgram CB.B:CA.Y
Addnet P13NET P13.I CC.A
Netdelay P13NET CC.A 2.1
NProgram row.C.long.1:CC.A row.C.long.1:PAD56.I
Addnet P14NET CD.Y P14.O
Netdelay P14NET P14.O 7.6
NProgram CC.8.2.3 CC.8.2.6 CB.8.2.3 CB.8.2.7 CD.8.2.3 CD.8.2.6 CE.8.2.5 CE.8.2.6 col.E.local.3:CD.Y row.C.local.4:PAD55.O
Addnet P14TEMPNET CC.Y CD.B
Netdelay P14TEMPNET CD.B 0.0
NProgram CD.B:CC.Y
Addnet P15NET P15.I EB.C
Netdelay P15NET EB.C 3.4
NProgram EB.8.2.0 EB.8.2.4 DB.8.2.5 DB.8.2.7 col.B.local.4:EB.C row.D.local.4:PAD54.I
Addnet P16NET DB.Y P16.O
Netdelay P16NET P16.O 2.6
NProgram DB.8.1.2 DB.8.1.7 DC.8.1.5 DC.8.1.7 col.C.local.1:DB.Y row.D.local.1:PAD53.O
Addnet P16TEMPNET EB.X DB.C
Netdelay P16TEMPNET DB.C 0.0
NProgram DB.C:EB.X
Addnet P17NET P17.I DA.B
Netdelay P17NET DA.B 0.0
NProgram DA.B:PAD52.I
Addnet P19NET EA.Y P19.O
Netdelay P19NET P19.O 1.4
NProgram FB.8.2.0 FB.8.2.6 col.B.local.3:EA.Y row.F.local.5:PAD51.O
Addnet P19TEMPNET DA.X EA.A
Netdelay P19TEMPNET EA.A 0.0
NProgram DA.X:EA.A
Addnet P20NET P20.I EC.C
Netdelay P20NET EC.C 4.7
NProgram FA.8.1.3 FA.8.1.5 FB.8.1.2 FB.8.1.6 FC.8.1.1 FC.8.1.7 col.C.local.2:EC.C col.A.local.1:PAD50.I
Addnet P21NET DC.X P21.O
Netdelay P21NET P21.O 10.3
NProgram ED.8.1.1 ED.8.1.4 FD.8.1.1 FD.8.1.4 GB.8.1.2 GB.8.1.6 GD.8.1.1 GD.8.1.7 GC.8.1.2 GC.8.1.7 col.D.local.2:DC.X row.G.local.3:PAD49.O
Addnet P21TEMPNET EC.X DC.C
Netdelay P21TEMPNET DC.C 0.0
NProgram DC.C:EC.X
Addnet P22NET P22.I FA.D
Netdelay P22NET FA.D 0.6
NProgram row.G.local.5:FA.D row.G.local.5:PAD48.I
Addnet P23NET FB.X P23.O
Netdelay P23NET P23.O 7.2
NProgram GC.8.1.1 GC.8.1.4 HB.8.1.2 HB.8.1.6 HC.8.1.1 HC.8.1.7 col.C.local.2:FB.X row.H.local.3:PAD47.O
Addnet P23TEMPNET FA.Y FB.B
Netdelay P23TEMPNET FB.B 0.0
NProgram FB.B:FA.Y
Addnet P24NET P24.I HA.B
Netdelay P24NET HA.B 0.0
NProgram PAD46.I:HA.B
Addnet P27NET GA.Y P27.O
Netdelay P27NET P27.O 3.1
NProgram HB.8.1.0 HB.8.1.4 IB.8.1.1 IB.8.1.7 col.B.local.1:GA.Y row.I.local.3:PAD45.O
Addnet P27TEMPNET HA.X GA.C
Netdelay P27TEMPNET GA.C 0.0
NProgram GA.C:HA.X
Addnet P28NET P28.I HB.C
Netdelay P28NET HB.C 0.5
NProgram col.B.local.3:HB.C col.B.local.3:PAD44.I
Addnet P29NET GB.Y P29.O
Netdelay P29NET P29.O 3.3
NProgram HC.8.1.0 HC.8.1.6 HB.8.1.3 HB.8.1.5 col.C.local.1:GB.Y col.B.local.1:PAD43.O
Addnet P29TEMPNET HB.X GB.C
Netdelay P29TEMPNET GB.C 0.0
NProgram GB.C:HB.X
Addnet P30NET P30.I GC.C
Netdelay P30NET GC.C 1.3
NProgram HC.8.2.0 HC.8.2.5 col.C.local.3:GC.C col.C.local.3:PAD42.I
Addnet P31NET FC.Y P31.O
Netdelay P31NET P31.O 8.5
NProgram GD.8.1.0 GD.8.1.5 HD.8.1.0 HD.8.1.6 HC.8.1.3 HC.8.1.5 col.D.local.1:FC.Y col.C.local.1:PAD41.O
Addnet P31TEMPNET GC.X FC.C
Netdelay P31TEMPNET FC.C 0.0
NProgram FC.C:GC.X
Addnet P32NET P32.I HD.C
Netdelay P32NET HD.C 0.6
NProgram col.D.local.1:HD.C col.D.local.1:PAD40.I
Addnet P33NET HC.Y P33.O
Netdelay P33NET P33.O 0.5
NProgram col.D.local.3:HC.Y col.D.local.3:PAD39.O
Addnet P33TEMPNET HD.Y HC.D
Netdelay P33TEMPNET HC.D 4.5
NProgram IE.8.1.0 IE.8.1.6 ID.8.1.3 ID.8.1.6 col.E.local.1:HD.Y row.I.local.4:HC.D
Addnet P34NET P34.I GD.D
Netdelay P34NET GD.D 1.5
NProgram HE.8.2.5 HE.8.2.6 row.H.local.5:GD.D col.E.local.3:PAD38.I
Addnet P36NET FD.X P36.O
Netdelay P36NET P36.O 2.6
NProgram col.E.long.1:FD.X col.E.long.1:PAD37.O
Addnet P36TEMPNET GD.X FD.C
Netdelay P36TEMPNET FD.C 0.0
NProgram FD.C:GD.X
Addnet P37NET P37.I HE.D
Netdelay P37NET HE.D 0.6
NProgram row.I.local.1:HE.D row.I.local.1:PAD36.I
Addnet P38NET GE.Y P38.O
Netdelay P38NET P38.O 1.3
NProgram HF.8.2.0 HF.8.2.5 col.F.local.3:GE.Y col.F.local.3:PAD35.O
Addnet P38TEMPNET HE.X GE.C
Netdelay P38TEMPNET GE.C 0.0
NProgram GE.C:HE.X
Addnet P39NET P39.I HF.D
Netdelay P39NET HF.D 0.5
NProgram row.I.local.1:HF.D row.I.local.1:PAD34.I
Addnet P40NET GF.Y P40.O
Netdelay P40NET P40.O 1.3
NProgram HG.8.2.0 HG.8.2.5 col.G.local.3:GF.Y col.G.local.3:PAD33.O
Addnet P40TEMPNET HF.X GF.C
Netdelay P40TEMPNET GF.C 0.0
NProgram GF.C:HF.X
Addnet P41NET P41.I HG.D
Netdelay P41NET HG.D 0.6
NProgram row.I.local.1:HG.D row.I.local.1:PAD32.I
Addnet P42NET GG.Y P42.O
Netdelay P42NET P42.O 1.3
NProgram HH.8.2.0 HH.8.2.5 col.H.local.3:GG.Y col.H.local.3:PAD31.O
Addnet P42TEMPNET HG.X GG.C
Netdelay P42TEMPNET GG.C 0.0
NProgram GG.C:HG.X
Addnet P43NET P43.I HH.D
Netdelay P43NET HH.D 0.6
NProgram row.I.local.1:HH.D row.I.local.1:PAD30.I
Addnet P46NET GH.X P46.O
Netdelay P46NET P46.O 1.6
NProgram HI.8.1.1 HI.8.1.5 col.I.local.2:GH.X col.I.local.1:PAD29.O
Addnet P46TEMPNET HH.X GH.C
Netdelay P46TEMPNET GH.C 0.0
NProgram GH.C:HH.X
Addnet P47NET P47.I FH.D
Netdelay P47NET FH.D 1.5
NProgram GI.8.1.5 GI.8.1.7 row.G.local.1:FH.D col.I.local.1:PAD28.I
Addnet P48NET EH.Y P48.O
Netdelay P48NET P48.O 4.3
NProgram FI.8.2.0 FI.8.2.5 GI.8.2.0 GI.8.2.5 col.I.local.3:EH.Y col.I.local.3:PAD27.O
Addnet P48TEMPNET FH.X EH.C
Netdelay P48TEMPNET EH.C 0.0
NProgram EH.C:FH.X
Addnet P49NET P49.I FE.D
Netdelay P49NET FE.D 5.4
NProgram GF.8.1.2 GF.8.1.7 GG.8.1.2 GG.8.1.7 GH.8.1.3 GH.8.1.7 row.G.local.1:FE.D row.G.local.3:PAD26.I
Addnet P50NET FG.Y P50.O
Netdelay P50NET P50.O 1.4
NProgram col.H.local.5:FG.Y row.F.local.3:PAD25.O col.H.local.6:row.F.local.3
Addnet P50TEMP1NET FE.Y FF.B
Netdelay P50TEMP1NET FF.B 0.0
NProgram FF.B:FE.Y
Addnet P50TEMP2NET FF.Y FG.B
Netdelay P50TEMP2NET FG.B 0.0
NProgram FG.B:FF.Y
Addnet P51NET P51.I DE.D
Netdelay P51NET DE.D 4.3
NProgram row.E.long.1:DE.D col.I.local.1:PAD24.I col.I.local.1:row.E.long.1
Addnet P53NET DF.Y P53.O
Netdelay P53NET P53.O 2.6
NProgram EG.8.1.0 EG.8.1.2 EH.8.1.2 EH.8.1.7 col.G.local.1:DF.Y row.E.local.1:PAD23.O
Addnet P53TEMP1NET DE.Y EF.C
Netdelay P53TEMP1NET EF.C 1.1
NProgram col.F.local.5:EF.C col.F.local.5:DE.Y col.F.local.5:row.E.local.0
Addnet P53TEMP2NET EF.X DF.C
Netdelay P53TEMP2NET DF.C 0.0
NProgram DF.C:EF.X
Addnet P54NET P54.I EG.A
Netdelay P54NET EG.A 3.4
NProgram EH.8.2.2 EH.8.2.6 EI.8.2.1 EI.8.2.7 row.E.local.5:EG.A col.I.local.4:PAD22.I
Addnet P55NET CG.Y P55.O
Netdelay P55NET P55.O 3.8
NProgram col.H.local.5:CG.Y row.D.local.4:PAD21.O col.H.local.5:row.D.local.4
Addnet P55TEMP1NET EG.X DG.C
Netdelay P55TEMP1NET DG.C 0.0
NProgram DG.C:EG.X
Addnet P55TEMP2NET DG.X CG.C
Netdelay P55TEMP2NET CG.C 0.0
NProgram CG.C:DG.X
Addnet P56NET P56.I DH.A
Netdelay P56NET DH.A 3.6
NProgram DI.8.1.1 DI.8.1.7 row.D.local.1:DH.A col.I.local.2:PAD20.I
Addnet P57NET BH.X P57.O
Netdelay P57NET P57.O 0.0
NProgram PAD19.O:BH.X
Addnet P57TEMP1NET DH.X CH.C
Netdelay P57TEMP1NET CH.C 0.0
NProgram CH.C:DH.X
Addnet P57TEMP2NET CH.X BH.C
Netdelay P57TEMP2NET BH.C 0.0
NProgram BH.C:CH.X
Addnet P58NET P58.I ED.D
Netdelay P58NET ED.D 6.8
NProgram row.F.long.1:ED.D col.I.long.2:PAD18.I col.I.long.2:row.F.long.1
Addnet P59NET EE.X P59.O
Netdelay P59NET P59.O 8.7
NProgram BH.8.2.2 BH.8.2.6 BG.8.2.3 BG.8.2.6 col.F.long.1:EE.X row.B.local.4:PAD17.O col.F.long.1:row.B.local.5
Addnet P59TEMP1NET ED.X DD.C
Netdelay P59TEMP1NET DD.C 0.0
NProgram DD.C:ED.X
Addnet P59TEMP2NET DD.Y EE.C
Netdelay P59TEMP2NET EE.C 1.1
NProgram col.E.local.5:EE.C col.E.local.5:DD.Y col.E.local.5:row.E.local.0
Addnet P61NET P61.I AH.A
Netdelay P61NET AH.A 0.6
NProgram row.A.local.4:AH.A row.A.local.4:PAD16.I
Addnet P62NET AG.Y P62.O
Netdelay P62NET P62.O 0.5
NProgram col.H.local.3:AG.Y col.H.local.3:PAD15.O
Addnet P62TEMP1NET AH.X BG.A
Netdelay P62TEMP1NET BG.A 2.5
NProgram BI.8.1.1 BI.8.1.7 BH.8.1.2 BH.8.1.7 row.B.local.1:BG.A col.I.local.2:AH.X
Addnet P62TEMP2NET BG.X AG.C
Netdelay P62TEMP2NET AG.C 0.0
NProgram AG.C:BG.X
Addnet P63NET P63.I CF.A
Netdelay P63NET CF.A 6.1
NProgram BH.8.1.0 BH.8.1.4 CH.8.1.1 CH.8.1.7 CG.8.1.2 CG.8.1.7 row.C.local.1:CF.A col.H.local.1:PAD14.I
Addnet P64NET AF.Y P64.O
Netdelay P64NET P64.O 0.5
NProgram col.G.local.3:AF.Y col.G.local.3:PAD13.O
Addnet P64TEMP1NET CF.X BF.C
Netdelay P64TEMP1NET BF.C 0.0
NProgram BF.C:CF.X
Addnet P64TEMP2NET BF.X AF.C
Netdelay P64TEMP2NET AF.C 0.0
NProgram AF.C:BF.X
Addnet P65NET P65.I CE.A
Netdelay P65NET CE.A 6.0
NProgram BG.8.1.0 BG.8.1.5 CG.8.1.0 CG.8.1.6 CF.8.1.3 CF.8.1.7 row.C.local.1:CE.A col.G.local.1:PAD12.I
Addnet P66NET AE.Y P66.O
Netdelay P66NET P66.O 0.5
NProgram col.F.local.3:AE.Y col.F.local.3:PAD11.O
Addnet P66TEMP1NET CE.X BE.C
Netdelay P66TEMP1NET BE.C 0.0
NProgram BE.C:CE.X
Addnet P66TEMP2NET BE.X AE.C
Netdelay P66TEMP2NET AE.C 0.0
NProgram AE.C:BE.X
Nameblk P2 P2IN
Editblk P2
Base IO
Config I:PAD BUF:
Endblk
Nameblk AD P3NET
Editblk AD
Base F
Config F:C Y:F X: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['AD']) + '''
Endblk
Nameblk P3 P3OUT
Editblk P3
Base IO
Config I: BUF:ON
Endblk
Nameblk BD P3TEMPNET
Editblk BD
Base F
Config F:A X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['BD']) + '''
Endblk
Nameblk P4 P4IN
Editblk P4
Base IO
Config I:PAD BUF:
Endblk
Nameblk AC P5NET
Editblk AC
Base F
Config F:C Y:F X: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['AC']) + '''
Endblk
Nameblk P5 P5OUT
Editblk P5
Base IO
Config I: BUF:ON
Endblk
Nameblk BC P5TEMPNET
Editblk BC
Base F
Config F:A X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['BC']) + '''
Endblk
Nameblk P6 P6IN
Editblk P6
Base IO
Config I:PAD BUF:
Endblk
Nameblk AB P7NET
Editblk AB
Base F
Config F:C Y:F X: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['AB']) + '''
Endblk
Nameblk P7 P7OUT
Editblk P7
Base IO
Config I: BUF:ON
Endblk
Nameblk BB P7TEMPNET
Editblk BB
Base F
Config F:A X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['BB']) + '''
Endblk
Nameblk P8 P8IN
Editblk P8
Base IO
Config I:PAD BUF:
Endblk
Nameblk AA P9NET
Editblk AA
Base F
Config F:C Y:F X: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['AA']) + '''
Endblk
Nameblk P9 P9OUT
Editblk P9
Base IO
Config I: BUF:ON
Endblk
Nameblk BA P9TEMPNET
Editblk BA
Base F
Config F:A X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['BA']) + '''
Endblk
Nameblk P11 P11IN
Editblk P11
Base IO
Config I:PAD BUF:
Endblk
Nameblk CB P12NET
Editblk CB
Base F
Config F:B Y:F X: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['CB']) + '''
Endblk
Nameblk P12 P12OUT
Editblk P12
Base IO
Config I: BUF:ON
Endblk
Nameblk CA P12TEMPNET
Editblk CA
Base F
Config F:A Y:F X: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['CA']) + '''
Endblk
Nameblk P13 P13IN
Editblk P13
Base IO
Config I:PAD BUF:
Endblk
Nameblk CD P14NET
Editblk CD
Base F
Config F:B Y:F X: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['CD']) + '''
Endblk
Nameblk P14 P14OUT
Editblk P14
Base IO
Config I: BUF:ON
Endblk
Nameblk CC P14TEMPNET
Editblk CC
Base F
Config F:A Y:F X: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['CC']) + '''
Endblk
Nameblk P15 P15IN
Editblk P15
Base IO
Config I:PAD BUF:
Endblk
Nameblk DB P16NET
Editblk DB
Base F
Config F:C Y:F X: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['DB']) + '''
Endblk
Nameblk P16 P16OUT
Editblk P16
Base IO
Config I: BUF:ON
Endblk
Nameblk EB P16TEMPNET
Editblk EB
Base F
Config F:C X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['EB']) + '''
Endblk
Nameblk P17 P17IN
Editblk P17
Base IO
Config I:PAD BUF:
Endblk
Nameblk EA P19NET
Editblk EA
Base F
Config F:A Y:F X: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['EA']) + '''
Endblk
Nameblk P19 P19OUT
Editblk P19
Base IO
Config I: BUF:ON
Endblk
Nameblk DA P19TEMPNET
Editblk DA
Base F
Config F:B X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['DA']) + '''
Endblk
Nameblk P20 P20IN
Editblk P20
Base IO
Config I:PAD BUF:
Endblk
Nameblk DC P21NET
Editblk DC
Base F
Config F:C X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['DC']) + '''
Endblk
Nameblk P21 P21OUT
Editblk P21
Base IO
Config I: BUF:ON
Endblk
Nameblk EC P21TEMPNET
Editblk EC
Base F
Config F:C X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['EC']) + '''
Endblk
Nameblk P22 P22IN
Editblk P22
Base IO
Config I:PAD BUF:
Endblk
Nameblk FB P23NET
Editblk FB
Base F
Config F:B X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['FB']) + '''
Endblk
Nameblk P23 P23OUT
Editblk P23
Base IO
Config I: BUF:ON
Endblk
Nameblk FA P23TEMPNET
Editblk FA
Base F
Config F:D Y:F X: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['FA']) + '''
Endblk
Nameblk P24 P24IN
Editblk P24
Base IO
Config I:PAD BUF:
Endblk
Nameblk GA P27NET
Editblk GA
Base F
Config F:C Y:F X: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['GA']) + '''
Endblk
Nameblk P27 P27OUT
Editblk P27
Base IO
Config I: BUF:ON
Endblk
Nameblk HA P27TEMPNET
Editblk HA
Base F
Config F:B X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['HA']) + '''
Endblk
Nameblk P28 P28IN
Editblk P28
Base IO
Config I:PAD BUF:
Endblk
Nameblk GB P29NET
Editblk GB
Base F
Config F:C Y:F X: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['GB']) + '''
Endblk
Nameblk P29 P29OUT
Editblk P29
Base IO
Config I: BUF:ON
Endblk
Nameblk HB P29TEMPNET
Editblk HB
Base F
Config F:C X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['HB']) + '''
Endblk
Nameblk P30 P30IN
Editblk P30
Base IO
Config I:PAD BUF:
Endblk
Nameblk FC P31NET
Editblk FC
Base F
Config F:C Y:F X: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['FC']) + '''
Endblk
Nameblk P31 P31OUT
Editblk P31
Base IO
Config I: BUF:ON
Endblk
Nameblk GC P31TEMPNET
Editblk GC
Base F
Config F:C X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['GC']) + '''
Endblk
Nameblk P32 P32IN
Editblk P32
Base IO
Config I:PAD BUF:
Endblk
Nameblk HC P33NET
Editblk HC
Base F
Config F:D Y:F X: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['HC']) + '''
Endblk
Nameblk P33 P33OUT
Editblk P33
Base IO
Config I: BUF:ON
Endblk
Nameblk HD P33TEMPNET
Editblk HD
Base F
Config F:C Y:F X: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['HD']) + '''
Endblk
Nameblk P34 P34IN
Editblk P34
Base IO
Config I:PAD BUF:
Endblk
Nameblk FD P36NET
Editblk FD
Base F
Config F:C X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['FD']) + '''
Endblk
Nameblk P36 P36OUT
Editblk P36
Base IO
Config I: BUF:ON
Endblk
Nameblk GD P36TEMPNET
Editblk GD
Base F
Config F:D X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['GD']) + '''
Endblk
Nameblk P37 P37IN
Editblk P37
Base IO
Config I:PAD BUF:
Endblk
Nameblk GE P38NET
Editblk GE
Base F
Config F:C Y:F X: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['GE']) + '''
Endblk
Nameblk P38 P38OUT
Editblk P38
Base IO
Config I: BUF:ON
Endblk
Nameblk HE P38TEMPNET
Editblk HE
Base F
Config F:D X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['HE']) + '''
Endblk
Nameblk P39 P39IN
Editblk P39
Base IO
Config I:PAD BUF:
Endblk
Nameblk GF P40NET
Editblk GF
Base F
Config F:C Y:F X: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['GF']) + '''
Endblk
Nameblk P40 P40OUT
Editblk P40
Base IO
Config I: BUF:ON
Endblk
Nameblk HF P40TEMPNET
Editblk HF
Base F
Config F:D X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['HF']) + '''
Endblk
Nameblk P41 P41IN
Editblk P41
Base IO
Config I:PAD BUF:
Endblk
Nameblk GG P42NET
Editblk GG
Base F
Config F:C Y:F X: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['GG']) + '''
Endblk
Nameblk P42 P42OUT
Editblk P42
Base IO
Config I: BUF:ON
Endblk
Nameblk HG P42TEMPNET
Editblk HG
Base F
Config F:D X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['HG']) + '''
Endblk
Nameblk P43 P43IN
Editblk P43
Base IO
Config I:PAD BUF:
Endblk
Nameblk GH P46NET
Editblk GH
Base F
Config F:C X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['GH']) + '''
Endblk
Nameblk P46 P46OUT
Editblk P46
Base IO
Config I: BUF:ON
Endblk
Nameblk HH P46TEMPNET
Editblk HH
Base F
Config F:D X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['HH']) + '''
Endblk
Nameblk P47 P47IN
Editblk P47
Base IO
Config I:PAD BUF:
Endblk
Nameblk EH P48NET
Editblk EH
Base F
Config F:C Y:F X: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['EH']) + '''
Endblk
Nameblk P48 P48OUT
Editblk P48
Base IO
Config I: BUF:ON
Endblk
Nameblk FH P48TEMPNET
Editblk FH
Base F
Config F:D X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['FH']) + '''
Endblk
Nameblk P49 P49IN
Editblk P49
Base IO
Config I:PAD BUF:
Endblk
Nameblk FG P50NET
Editblk FG
Base F
Config F:B Y:F X: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['FG']) + '''
Endblk
Nameblk P50 P50OUT
Editblk P50
Base IO
Config I: BUF:ON
Endblk
Nameblk FE P50TEMP1NET
Editblk FE
Base F
Config F:D Y:F X: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['FE']) + '''
Endblk
Nameblk FF P50TEMP2NET
Editblk FF
Base F
Config F:B Y:F X: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['FF']) + '''
Endblk
Nameblk P51 P51IN
Editblk P51
Base IO
Config I:PAD BUF:
Endblk
Nameblk DF P53NET
Editblk DF
Base F
Config F:C Y:F X: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['DF']) + '''
Endblk
Nameblk P53 P53OUT
Editblk P53
Base IO
Config I: BUF:ON
Endblk
Nameblk DE P53TEMP1NET
Editblk DE
Base F
Config F:D Y:F X: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['DE']) + '''
Endblk
Nameblk EF P53TEMP2NET
Editblk EF
Base F
Config F:C X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['EF']) + '''
Endblk
Nameblk P54 P54IN
Editblk P54
Base IO
Config I:PAD BUF:
Endblk
Nameblk CG P55NET
Editblk CG
Base F
Config F:C Y:F X: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['CG']) + '''
Endblk
Nameblk P55 P55OUT
Editblk P55
Base IO
Config I: BUF:ON
Endblk
Nameblk EG P55TEMP1NET
Editblk EG
Base F
Config F:A X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['EG']) + '''
Endblk
Nameblk DG P55TEMP2NET
Editblk DG
Base F
Config F:C X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['DG']) + '''
Endblk
Nameblk P56 P56IN
Editblk P56
Base IO
Config I:PAD BUF:
Endblk
Nameblk BH P57NET
Editblk BH
Base F
Config F:C X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['BH']) + '''
Endblk
Nameblk P57 P57OUT
Editblk P57
Base IO
Config I: BUF:ON
Endblk
Nameblk DH P57TEMP1NET
Editblk DH
Base F
Config F:A X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['DH']) + '''
Endblk
Nameblk CH P57TEMP2NET
Editblk CH
Base F
Config F:C X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['CH']) + '''
Endblk
Nameblk P58 P58IN
Editblk P58
Base IO
Config I:PAD BUF:
Endblk
Nameblk EE P59NET
Editblk EE
Base F
Config F:C X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['EE']) + '''
Endblk
Nameblk P59 P59OUT
Editblk P59
Base IO
Config I: BUF:ON
Endblk
Nameblk ED P59TEMP1NET
Editblk ED
Base F
Config F:D X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['ED']) + '''
Endblk
Nameblk DD P59TEMP2NET
Editblk DD
Base F
Config F:C Y:F X: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['DD']) + '''
Endblk
Nameblk P61 P61IN
Editblk P61
Base IO
Config I:PAD BUF:
Endblk
Nameblk AG P62NET
Editblk AG
Base F
Config F:C Y:F X: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['AG']) + '''
Endblk
Nameblk P62 P62OUT
Editblk P62
Base IO
Config I: BUF:ON
Endblk
Nameblk AH P62TEMP1NET
Editblk AH
Base F
Config F:A X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['AH']) + '''
Endblk
Nameblk BG P62TEMP2NET
Editblk BG
Base F
Config F:A X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['BG']) + '''
Endblk
Nameblk P63 P63IN
Editblk P63
Base IO
Config I:PAD BUF:
Endblk
Nameblk AF P64NET
Editblk AF
Base F
Config F:C Y:F X: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['AF']) + '''
Endblk
Nameblk P64 P64OUT
Editblk P64
Base IO
Config I: BUF:ON
Endblk
Nameblk CF P64TEMP1NET
Editblk CF
Base F
Config F:A X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['CF']) + '''
Endblk
Nameblk BF P64TEMP2NET
Editblk BF
Base F
Config F:C X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['BF']) + '''
Endblk
Nameblk P65 P65IN
Editblk P65
Base IO
Config I:PAD BUF:
Endblk
Nameblk AE P66NET
Editblk AE
Base F
Config F:C Y:F X: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['AE']) + '''
Endblk
Nameblk P66 P66OUT
Editblk P66
Base IO
Config I: BUF:ON
Endblk
Nameblk CE P66TEMP1NET
Editblk CE
Base F
Config F:A X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['CE']) + '''
Endblk
Nameblk BE P66TEMP2NET
Editblk BE
Base F
Config F:C X:F Y: Q: RES: SET: CLK:
Equate F = ''' + equate(clbs['BE']) + '''
Endblk
'''
    return out
