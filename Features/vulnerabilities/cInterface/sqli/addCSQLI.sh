#!/bin/bash
mkdir -p /opt/dvd/services/vulns/c/


mkdir -p /tmp/cInterface
cd /tmp/cInterface/
if [[ $(uname -a | grep "arm") ]] ; then
    mv /tmp/backend/Features/vulnerabilities/cInterface/armv7/SQLInjection/sqlInjection_armv7 SQLInjection 
    mv /tmp/backend/Features/vulnerabilities/cInterface/armv7/SQLInjection/login.db login.db 
elif [[ $(uname -a | grep "x86") ]] ; then
    mv /tmp/backend/Features/vulnerabilities/cInterface/x86/SQLInjection/sqlInjection SQLInjection 
    mv /tmp/backend/Features/vulnerabilities/cInterface/x86/SQLInjection/login.db login.db 
else
    echo "shouldn't get here"
fi
mv /tmp/cInterface/* /opt/dvd/services/vulns/c/

chmod -R +x /opt/dvd/services/vulns/c/
chmod -R +s /opt/dvd/services/vulns/c/

