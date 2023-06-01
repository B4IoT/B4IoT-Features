#!/bin/bash
mkdir -p /opt/dvd/code/c/

/tmp/backend/Features/vulnerabilities/c/
mkdir -p /tmp/c
cd /tmp/c/
if [[ $(uname -a | grep "arm") ]] ; then
    mv /tmp/backend/Features/vulnerabilities/c/armv7/MutipleCVulns/damnvuln Vulnerable 
elif [[ $(uname -a | grep "x86") ]] ; then
    mv /tmp/backend/Features/vulnerabilities/c/x86/MutipleCVulns/damnvuln Vulnerable 
    mv /tmp/backend/Features/vulnerabilities/c/x86/MutipleCVulns/damnvuln2 Vulnerable2    
else
    echo "shouldn't get here"
fi
mv /tmp/c/* /opt/dvd/code/c/
chmod -R +x /opt/dvd/code/c/
chmod -R +s /opt/dvd/code/c/

