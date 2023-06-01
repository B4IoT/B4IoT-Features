#!/bin/bash
mkdir -p /opt/dvd/code/c/

mkdir -p /tmp/c
cd /tmp/c/

if [[ $(uname -a | grep "arm") ]] ; then
    mv /tmp/backend/Features/vulnerabilities/c/armv7/BufferOverflow/bof1 BufferOverflow 
elif [[ $(uname -a | grep "x86") ]] ; then
    mv /tmp/backend/Features/vulnerabilities/c/x86/BufferOverflow/bof1 BufferOverflow 
else
    echo "shouldn't get here"
fi
mv /tmp/c/* /opt/dvd/code/c/
chmod -R +x /opt/dvd/code/c/
chmod -R +s /opt/dvd/code/c/

