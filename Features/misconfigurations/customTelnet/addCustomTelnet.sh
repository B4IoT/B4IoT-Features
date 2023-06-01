#!/bin/bash
mkdir -p /opt/dvd/services/telnet
mv /tmp/backend/Features/misconfigurations/customTelnet/dist/* /opt/dvd/services/telnet/
pip install -r /opt/dvd/services/telnet/requirements.txt
chmod +x /opt/dvd/services/telnet/check_daemon.sh
echo "*/1 * * * * /opt/dvd/services/telnet/check_daemon.sh" >> /etc/crontabs/root