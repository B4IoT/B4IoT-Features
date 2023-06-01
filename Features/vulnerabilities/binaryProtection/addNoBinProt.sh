#!/bin/bash
mkdir -p /opt/dvd/code/c/


mkdir -p /tmp/c
cd /tmp/c/

wget /tmp/backend/Features/vulnerabilities/binaryProtection/noBinProt BufferOverflowWithoutProtection 

mv /tmp/c/* /opt/dvd/code/c/
chmod -R +x /opt/dvd/code/c/
chmod -R +s /opt/dvd/code/c/

