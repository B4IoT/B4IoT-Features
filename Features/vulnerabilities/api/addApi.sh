#!/bin/bash
mkdir -p /opt/dvd/services/api
mv /tmp/backend/Features/vulnerabilities/api/dist/* /opt/dvd/services/api/
pip install -r /opt/dvd/services/api/requirements.txt
chmod +x /opt/dvd/services/api/check_daemon.sh
echo "*/1 * * * * /opt/dvd/services/api/check_daemon.sh" >> /etc/crontabs/root
