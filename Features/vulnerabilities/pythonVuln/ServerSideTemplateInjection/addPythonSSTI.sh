#!/bin/bash
mv /tmp/backend/Features/vulnerabilities/pythonVuln/ServerSideTemplateInjection/test.py SSTI.py 
mkdir -p /opt/dvd/code/python/
mv ./SSTI.py /opt/dvd/code/python/
chmod -R +x /opt/dvd/code/python/
chmod -R +s /opt/dvd/code/python/