#!/bin/bash
echo 'Defaults secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"' >> /etc/sudoers
echo 'Defaults env_keep += "LD_PRELOAD"' >> /etc/sudoers