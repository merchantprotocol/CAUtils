#!/bin/bash

# Get OS data.
OS=$(lsb_release -si)

# Create a directory for s3fs-fuse in the user's home directory.
cd $HOME
mkdir s3fs-fuse
cd s3fs-fuse

# Install dependencies and s3fs-fuse.
if [[ $OS == *"Ubuntu"* ]] || [[ $OS == *"Debian"* ]]; then
    sudo apt-get update
    sudo apt-get install -y automake autotools-dev fuse g++ git libcurl4-gnutls-dev libfuse-dev libssl-dev libxml2-dev make pkg-config
elif [[ $OS == *"CentOS"* ]] || [[ $OS == *"RedHat"* ]]; then
    sudo yum update -y
    sudo yum install -y automake fuse fuse-devel gcc-c++ git libcurl-devel libxml2-devel make openssl-devel
else
    echo "Unsupported operating system: $OS"
    exit 1
fi

# Clone the s3fs-fuse repository and build the project.
git clone https://github.com/s3fs-fuse/s3fs-fuse.git
cd s3fs-fuse
./autogen.sh
./configure
make

# Install s3fs-fuse.
sudo make install
