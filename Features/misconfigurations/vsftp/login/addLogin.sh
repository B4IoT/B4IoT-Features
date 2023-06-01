#!/bin/bash
sed -i '12 a anonymous_enable=YES' /etc/vsftpd/vsftpd.conf
sed -i '13 a no_anon_password=YES' /etc/vsftpd/vsftpd.conf
sed -i '15 a local_enable=YES' /etc/vsftpd/vsftpd.conf

