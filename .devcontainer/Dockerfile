FROM ubuntu:24.04

# Install packages
RUN apt-get update && apt-get install -y \
    git \
    gnuradio \
    sudo \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN usermod -aG sudo ubuntu \
    && echo "ubuntu ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Change to the unprivileged user
USER ubuntu
