#!/bin/bash
apk add busybox-extras
mv /tmp/backend/Features/resources/telnet/telnetd telnetd
mv ./telnetd /etc/init.d/
chmod +x /etc/init.d/telnetd
# Warning openrc needed!
rc-update add telnetd default