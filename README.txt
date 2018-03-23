Ubuntu setup:
sudo apt-get install -y python-bitstring dosbox

This project loosely follows the methodology from prjxray (https://github.com/SymbiFlow/prjxray)

Languages
Verilog first appeared in 1984 while the XC2064 was announced in 1985
Therefore it likely wasn't seriously considered for XACTStep
Instead, "high level" synthesis is done in .XNF while the "FPGA assembly" (think XDL) is .LCA
I'm primarily working in .LCA
While there isn't a lot of documentation on LCA, I generated some example XNF designs
and took a look at the resulting LCA
Even still, LCA is relatively high leven in that you supply SOP form for LUTs rather than memory values

