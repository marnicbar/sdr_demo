# Demonstrator for Digital Signal Transmission
This repository contains all project files necessary to build and run the final transmitter/receiver demonstration and all previous demonstrations.

The documentation is available in a separate [GitHub repository](https://github.com/marnicbar/sdr_demo_report/releases/tag/submission).

## Volume normalization and reduction of dynamic range
Convert the mp3 source to a mono channel 48 kHz wav file.

`ffmpeg -i "Nocturne in E flat major, Op. 9 no. 2.mp3" -af loudnorm=I=-5:TP=-0.3:LRA=5 -ar 48000 -ac 1 -c:a pcm_s16le nocturne_e_flat_major_op_9_no_2.wav`

