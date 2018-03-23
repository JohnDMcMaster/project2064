N := 1
SPECIMENS := $(addprefix specimen_,$(shell seq -f '%03.0f' $(N)))
SPECIMENS_OK := $(addsuffix /OK,$(SPECIMENS))

all: $(SPECIMENS_OK)
	
database: $(SPECIMENS_OK)
	${XRAY_SEGMATCH} -o seg_clblx.segbits $(addsuffix /segdata_clbl[lm]_[lr].txt,$(SPECIMENS))

pushdb:
	echo

$(SPECIMENS_OK):
	bash generate.sh $(subst /OK,,$@)
	touch $@

$(SPECIMENS_OK):
	bash generate.sh $(subst /OK,,$@)
	touch $@

clean:
	rm -rf specimen_[0-9][0-9][0-9]/ seg_clblx.segbits __pycache__ run.ok
	rm -rf vivado*.log vivado_*.str vivado*.jou design *.bits *.dcp *.bit

.PHONY: database pushdb run clean

