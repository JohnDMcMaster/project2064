.PHONY: all
all:
	$(MAKE) clean
	$(MAKE) bits
	
.PHONY: full
full:
	$(MAKE) clean
	$(MAKE) bits
	$(MAKE) morebits
	

.PHONY: bits
bits:
# Generate .bit (bitstream) file
	makebits -v SBAPR.LCA |tee SBAPR.BIT.log
# wtf...it writes a bitstream on failure
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
	rm -f *.CRF SB.LCA *.MAP *.PBK *.PGF *.SCP *.BIT *.MBO *.RPT *.RBT *.MSK *.log

