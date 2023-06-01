#!/bin/bash
sed -i '58 a PermitEmptyPasswords yes' /etc/ssh/sshd_config
