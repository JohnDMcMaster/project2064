#!/bin/bash

set -ex

source ${P2064_GENHEADER}

rm -f *.LCA *.BIT *.BITS

python ../generate.py
$P2064_LCA2BIT
$P2064_BIT2BITS DESIGN.BIT DESIGN.BITS
python ../theorem.py DESIGN.BITS design.csv  design.segd

