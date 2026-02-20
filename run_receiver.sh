#!/usr/bin/env bash
DIR_OF_THIS_SCRIPT=$(dirname "$(realpath $0)")

$DIR_OF_THIS_SCRIPT/compile_flowgraphs.sh

export GRC_BLOCKS_PATH=$DIR_OF_THIS_SCRIPT/custom_blocks
export PYTHONPATH=$GRC_BLOCKS_PATH

python3 $DIR_OF_THIS_SCRIPT/receiver.py

