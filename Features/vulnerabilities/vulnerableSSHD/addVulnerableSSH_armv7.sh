#!/bin/bash
apk add openssh libressl-dev
mkdir -p /usr/local/sbin/
mv /tmp/backend/Features/vulnerabilities/vulnerableSSHD/sshd_armv7 sshd
chmod +x sshd
rm /usr/sbin/sshd
mv sshd /usr/sbin/
# Fixing library bug with the binary
ln /usr/lib/libcrypto.so.49 /usr/lib/libcrypto.so.47
#make sure all libs are on the device
#ldd /usr/local/sbin/sshd
mkdir -p /usr/local/etc/
ln /etc/ssh/* /usr/local/etc/
sed -i '18 a HostKey /etc/ssh/ssh_host_rsa_key' /usr/local/etc/sshd_config

rc-update add /usr/sbin/sshd default
