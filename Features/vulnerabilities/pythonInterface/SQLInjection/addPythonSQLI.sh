#!/bin/bash
mv /tmp/backend/Features/vulnerabilities/pythonInterface/SQLInjection/sqlInjection.py SQLInjection.py 
mv /tmp/backend/Features/vulnerabilities/pythonInterface/SQLInjection/login.db login.db
mkdir -p /opt/dvd/services/vulns/python/
mv ./SQLInjection.py /opt/dvd/services/vulns/python/
mv ./login.db /opt/dvd/services/vulns/python/
chmod -R +x /opt/dvd/services/vulns/python/
chmod -R +s /opt/dvd/services/vulns/python/
