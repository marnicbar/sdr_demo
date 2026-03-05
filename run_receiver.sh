#!/usr/bin/env bash
DIR_OF_THIS_SCRIPT=$(dirname "$(realpath $0)")

$DIR_OF_THIS_SCRIPT/compile_flowgraphs.sh $DIR_OF_THIS_SCRIPT/demos/demo_08_receiver.grc

export GRC_BLOCKS_PATH=$DIR_OF_THIS_SCRIPT/custom_blocks
export PYTHONPATH=$GRC_BLOCKS_PATH

if [[ " $* " == *" --fullscreen "* ]]; then
	python3 $DIR_OF_THIS_SCRIPT/demos/demo_08_receiver_fullscreen.py
else
    python3 $DIR_OF_THIS_SCRIPT/demos/demo_08_receiver.py
fi
