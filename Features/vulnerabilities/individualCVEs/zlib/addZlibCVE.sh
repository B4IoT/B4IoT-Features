#!/bin/bash
cd /tmp
apk add alpine-sdk
wget https://github.com/HardySimpson/zlog/archive/refs/tags/1.2.15.tar.gz
tar -zxvf 1.2.15.tar.gz
cd zlog-1.2.15
make PREFIX=/usr/local/
make PREFIX=/usr/local/ install
# CVE-2021-43521