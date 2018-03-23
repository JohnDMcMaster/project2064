# These commands don't return failure codes
# thus the best thing to do is to rerun from scratch so that files don't exist if fails
.PHONY: run
run:
	$(MAKE) clean
	$(MAKE) all

.PHONY: all
all:
	$(MAKE) SB.MAP
	$(MAKE) SB.LCA
	$(MAKE) SBAPR.LCA
	$(MAKE) bits
	
.PHONY: full
full:
	$(MAKE) clean
	$(MAKE) all
	$(MAKE) morebits

lca:
	$(MAKE) clean
	$(MAKE) SB.MAP
	$(MAKE) SB.LCA
	$(MAKE) SBAPR.LCA
	
.PHONY: SB.MAP
SB.MAP:
	# generates sb.crf, sb.map, sb.pgf
	xnfmap sb.xnf SB.MAP |tee SB.MAP.log
	fgrep 'DESIGN SUMMARY' SB.MAP.log

.PHONY: SB.LCA
SB.LCA:
	# generates sb.lca, sb.scp
	map2lca SB.MAP SB.LCA |tee SB.LCA.log

.PHONY: SBAPR.LCA
SBAPR.LCA:
	apr SB.LCA SBAPR.LCA |tee SBAPR.LCA.log

.PHONY: bits
bits:
    # Generate .bit (bitstream) file
	makebits -v SBAPR.LCA |tee SBAPR.BIT.log
    
.PHONY: morebits
morebits:
	# Generate .rbt (raw bits) file
	makebits -v -b SBAPR.LCA |tee SBAPR.RBT.log
    # Generate mask file
	makebits -v -m SBAPR.LCA |tee SBAPR.MSK.log

.PHONY: clean
clean:
	rm -f *.CRF *.LCA *.MAP *.PBK *.PGF *.SCP *.BIT *.MBO *.RPT *.RBT *.MSK *.log

