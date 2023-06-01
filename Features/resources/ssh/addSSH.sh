#!/bin/bash
apk add openssh
ln /etc/ssh/* /usr/local/
rc-update add sshd default