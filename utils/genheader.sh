# header for fuzzer generate.sh scripts

if [ -z "$P2064_DIR" ]; then
	echo "No P2064 environment found. Make sure to source the env file first!"
	exit 1
fi

set -ex

# Get aliases, which don't seem to propagate correctly
# also the python path
pushd $P2064_DIR
source env.sh
popd

#test $# = 1
#test ! -e $1
mkdir -p $1
cd $1

