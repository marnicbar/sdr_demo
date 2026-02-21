#!/usr/bin/env bash
DIR_OF_THIS_SCRIPT=$(dirname "$(realpath $0)")

export GRC_BLOCKS_PATH=$DIR_OF_THIS_SCRIPT/custom_blocks
export PYTHONPATH=$GRC_BLOCKS_PATH

if [ -z "$1" ]; then
	echo "Usage: $0 <flowgraph.grc>" >&2
	exit 1
fi

grcc "$1"
