# These commands don't return failure codes
# thus the best thing to do is to rerun from scratch so that files don't exist if fails
run:
	$(MAKE) clean
	$(MAKE) all

all:
	xnfmap first.xnf FIRST.MAP
	map2lca first.map first.lca
	apr FIRST.LCA FIRSTPAR.LCA
	makebits FIRSTPAR.LCA

clean:
	rm -f *.CRF *.LCA *.MAP *.PBK *.PGF *.SCP *.BIT *.MBO *.RPT
	