# These commands don't return failure codes
# thus the best thing to do is to rerun from scratch so that files don't exist if fails
.PHONY: run
run:
	$(MAKE) clean
	$(MAKE) all

.PHONY: all
all:
	echo 'Creating MAP file...'
	$(MAKE) SB.MAP
	echo 'Creating LCA...'
	$(MAKE) SB.LCA
	echo 'Running APR...'
	$(MAKE) SBAPR.LCA
	echo 'Creating bitstream...'
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

from_lca:
	$(MAKE) clean_lca
	$(MAKE) SB.MAP
	$(MAKE) SB.LCA
	$(MAKE) SBAPR.LCA

	
.PHONY: SB.MAP
SB.MAP:
# generates sb.crf, sb.map, sb.pgf
	xnfmap sb.xnf SB.MAP 2>&1 |tee SB.MAP.log
	test -f SB.MAP
	fgrep 'DESIGN SUMMARY' SB.MAP.log
	test $(shell fgrep ERROR SB.MAP.log |wc -l) -eq 0

.PHONY: SB.LCA
SB.LCA:
# generates sb.lca, sb.scp
	map2lca SB.MAP SB.LCA
	test -f SB.LCA

.PHONY: SBAPR.LCA
SBAPR.LCA:
	echo 'Preparing LCA'
	apr SB.LCA SBAPR.LCA 2>&1 |tee SBAPR.LCA.log
	test -f SBAPR.LCA
	test $(shell fgrep 'Error' SBAPR.LCA.log |wc -l) -eq 0

.PHONY: bits
bits:
# Generate .bit (bitstream) file
	makebits -v SBAPR.LCA |tee SBAPR.BIT.log
	test -f SBAPR.BIT

.PHONY: morebits
morebits:
# Generate .rbt (raw bits) file
	makebits -v -b SBAPR.LCA |tee SBAPR.RBT.log
	test -f SBAPR.RBT
# Generate mask file
	makebits -v -m SBAPR.LCA |tee SBAPR.MSK.log
	test -f SBAPR.MSK
	makebits -v -l SBAPR.LL |tee SBAPR.LL.log
	test -f SBAPR.LL

.PHONY: clean
clean:
	rm -f *.CRF *.LCA *.MAP *.PBK *.PGF *.SCP *.BIT *.MBO *.RPT *.RBT *.MSK *.log

.PHONY: clean_lca
clean_lca:
	rm -f *.CRF SB.LCA *.MAP *.PBK *.PGF *.SCP *.BIT *.MBO *.RPT *.RBT *.MSK *.log
