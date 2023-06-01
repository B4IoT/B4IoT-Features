#!/bin/bash
sed -i '18 a write_enable=YES' /etc/vsftpd/vsftpd.conf
sed -i '19 a dirlist_enable=YES' /etc/vsftpd/vsftpd.conf
sed -i '20 a download_enable=YES' /etc/vsftpd/vsftpd.conf
sed -i '27 a anon_upload_enable=YES' /etc/vsftpd/vsftpd.conf
sed -i '31 a anon_mkdir_write_enable=YES' /etc/vsftpd/vsftpd.conf
