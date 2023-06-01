#!/bin/bash
touch /home/manager/checkNetwork.sh
echo 'ping -c 1 google.com' > /home/manager/checkNetwork.sh
chown :managerGroup /home/manager/checkNetwork.sh
chmod 771 /home/manager/checkNetwork.sh
echo '* * * * * /home/manager/checkNetwork.sh' >> /etc/crontabs/root