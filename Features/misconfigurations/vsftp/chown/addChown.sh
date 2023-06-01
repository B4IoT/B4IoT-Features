#!/bin/bash
sed -i '46 a chown_uploads=YES' /etc/vsftpd/vsftpd.conf
sed -i '47 a chown_username=root' /etc/vsftpd/vsftpd.conf
