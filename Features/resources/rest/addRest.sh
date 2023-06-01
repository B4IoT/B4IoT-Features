#!/bin/bash
mkdir -p /opt/dvd/services/rest/
mv /tmp/backend/Features/resources/rest/dist/* /opt/dvd/services/rest/
pip install -r /opt/dvd/services/rest/requirements.txt 
chmod +x /opt/dvd/services/rest/check_daemon.sh
echo "*/1 * * * * /opt/dvd/services/rest/check_daemon.sh" >> /etc/crontabs/root