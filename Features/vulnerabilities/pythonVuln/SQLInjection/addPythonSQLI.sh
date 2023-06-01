#!/bin/bash
mv /tmp/backend/Features/vulnerabilities/pythonVuln/SQLInjection/sqlInjection.py SQLInjection.py 
mv /tmp/backend/Features/vulnerabilities/pythonVuln/SQLInjection/login.db login.db
mkdir -p /opt/dvd/code/python/
mv ./SQLInjection.py /opt/dvd/code/python/
mv ./login.db /opt/dvd/code/python/
chmod -R +x /opt/dvd/code/python/
chmod -R +s /opt/dvd/code/python/