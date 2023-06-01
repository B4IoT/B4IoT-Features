#!/bin/bash

mv /tmp/backend/Features/vulnerabilities/pythonInterface/CommandInjection/commandInjection.py CommandInjection.py 
mkdir -p /opt/dvd/services/vulns/python/
mv ./CommandInjection.py  /opt/dvd/services/vulns/python/
chmod -R +x /opt/dvd/services/vulns/python/
chmod -R +s /opt/dvd/services/vulns/python/
