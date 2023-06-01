#!/bin/bash
mv /tmp/backend/Features/vulnerabilities/pythonInterface/PathTraversal/PathTraversal.py PathTraversal.py 
mkdir -p /opt/dvd/services/vulns/python/
mv ./PathTraversal.py  /opt/dvd/services/vulns/python/
chmod -R +x /opt/dvd/services/vulns/python/
chmod -R +s /opt/dvd/services/vulns/python/
