#!/usr/bin/env bash
DIR_OF_THIS_SCRIPT=$(dirname "$(realpath $0)")

export GRC_BLOCKS_PATH=$DIR_OF_THIS_SCRIPT/custom_blocks
export PYTHONPATH=$GRC_BLOCKS_PATH

if [ -z "$1" ]; then
	echo "Usage: $0 <flowgraph.grc>" >&2
	exit 1
fi

grcc "$1"

# Get the name of the generated Python file by replacing the .grc extension with .py
py_file="${1%.*}.py"
py_file_fullscreen="${1%.*}_fullscreen.py"

# Copy the generated Python file and modify it to show the GUI in fullscreen
cp "$py_file" "$py_file_fullscreen"
sed -i 's/tb\.show()/tb.showFullScreen()/' "$py_file_fullscreen"
