#!/bin/bash
mv /tmp/backend/Features/vulnerabilities/pythonInterface/Deserialization/deserialization.py Deserialization.py 
mkdir -p /opt/dvd/services/vulns/python/
mv ./Deserialization.py  /opt/dvd/services/vulns/python/
chmod -R +x /opt/dvd/services/vulns/python/
chmod -R +s /opt/dvd/services/vulns/python/
