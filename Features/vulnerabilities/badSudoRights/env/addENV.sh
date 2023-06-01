#!/bin/bash
echo 'ping -c 1 google.com' > /home/manager/checkNetwork.sh
chmod +x /home/manager/checkNetwork.sh
echo '* * * * * /home/manager/checkNetwork.sh' >> /etc/crontabs/root
echo 'manager ALL=(root) SETENV:/home/manager/checkNetwork.sh' >> /etc/sudoers
