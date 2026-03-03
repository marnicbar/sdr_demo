FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV TZ=Europe/Berlin

# Install system packages + Python + pip
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    gnuradio \
    sudo \
    python3 \
    python3-pip \
    openssh-client \
    sshpass \
    tzdata \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Ansible via pip
RUN pip3 install --no-cache-dir --break-system-packages ansible ansible-lint matplotlib

# Configure sudo for ubuntu user
RUN usermod -aG sudo ubuntu \
    && echo "ubuntu ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Change to the unprivileged user
USER ubuntu
