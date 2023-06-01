#!/bin/bash
mkdir -p /opt/dvd/code/bash/
mv /tmp/backend/Features/vulnerabilities/bash/CommandInjection/vulnerablebash.sh  CommandInjection.sh
mv ./CommandInjection.sh /opt/dvd/code/bash/
chmod -R +x /opt/dvd/code/bash/
chmod -R +s /opt/dvd/code/bash/
