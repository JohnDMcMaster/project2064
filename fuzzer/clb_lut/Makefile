N := 1
SPECIMENS := $(addprefix specimen_,$(shell seq -f '%03.0f' $(N)))
SPECIMENS_OK := $(addsuffix /OK,$(SPECIMENS))

all: database

database: $(SPECIMENS_OK)
	${P2064_SEGMATCH} -o lut.segbits specimen_*/design.segd
	#${P2064_SEGMATCH} -o seg_clblx.segbits $(addsuffix /segdata_clbl[lm]_[lr].txt,$(SPECIMENS))
	echo

pushdb:
	${P2064_MERGEDB} clbll_l seg_clblx.segbits

$(SPECIMENS_OK):
	bash generate.sh $(subst /OK,,$@)
	touch $@

$(SPECIMENS_OK):
	bash generate.sh $(subst /OK,,$@)
	touch $@

clean:
	rm -rf specimen_[0-9][0-9][0-9]/ __pycache__ run.ok

.PHONY: database pushdb run clean

