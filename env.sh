# https://stackoverflow.com/questions/59895/getting-the-source-directory-of-a-bash-script-from-within
export P2064_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export XACT_DIR='/opt/XACT'
export PYTHONPATH=$P2064_DIR:$PYTHONPATH
export P2064_GENHEADER=$P2064_DIR/utils/genheader.sh

P2064_PARSE=$P2064_DIR/parse.py
alias parse=$P2064_PARSE

P2064_LCA2BIT=$P2064_DIR/lca2bit.py
alias lca2bit=$P2064_LCA2BIT

P2064_BIT2BITS=$P2064_DIR/bit2bits.py
alias bit2bits=$P2064_BIT2BITS

