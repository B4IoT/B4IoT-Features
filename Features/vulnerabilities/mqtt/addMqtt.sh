#!/bin/bash
apk add mosquitto
mkdir -p /opt/dvd/services/mqtt
mv /tmp/backend/Features/vulnerabilities/mqtt/dist/* /opt/dvd/services/mqtt/
pip install -r /opt/dvd/services/mqtt/requirements.txt
chmod +x /opt/dvd/services/mqtt/check_daemon.sh
echo "*/1 * * * * /opt/dvd/services/mqtt/check_daemon.sh" >> /etc/crontabs/root

rc-update add mosquitto default
 