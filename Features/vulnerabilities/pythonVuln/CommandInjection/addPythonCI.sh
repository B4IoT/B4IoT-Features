#!/bin/bash
mv /tmp/backend/Features/vulnerabilities/pythonVuln/CommandInjection/vulnerablepython.py CommandInjection.py 
mkdir -p /opt/dvd/code/python/
mv ./CommandInjection.py  /opt/dvd/code/python/
chmod -R +x /opt/dvd/code/python/
chmod -R +s /opt/dvd/code/python/
