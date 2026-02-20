#!/usr/bin/env bash
DIR_OF_THIS_SCRIPT=$(dirname "$(realpath $0)")

export GRC_BLOCKS_PATH=$DIR_OF_THIS_SCRIPT/custom_blocks
export PYTHONPATH=$GRC_BLOCKS_PATH

grcc transmitter.grc
grcc receiver.grc
