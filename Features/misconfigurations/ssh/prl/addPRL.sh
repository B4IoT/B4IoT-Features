#!/bin/bash
sed -i '32 a PermitRootLogin yes' /etc/ssh/sshd_config
