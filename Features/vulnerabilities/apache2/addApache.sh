#!/bin/bash
apk add apache2 apache2-mod-wsgi

mkdir -p /opt/dvd/services/http
mv /tmp/backend/Features/vulnerabilities/apache2/dist/* /opt/dvd/services/http/
mv /opt/dvd/services/http/http.conf /etc/apache2/conf.d/http.conf

chown apache:apache /opt/dvd/services/http/cgi-bin/*
chmod 755 /opt/dvd/services/http/cgi-bin/*

pip install -r /opt/dvd/services/http/requirements.txt


echo "LoadModule cgi_module modules/mod_cgi.so" >> /etc/apache2/httpd.conf
echo "LoadModule cgid_module modules/mod_cgid.so" >> /etc/apache2/httpd.conf

rc-update add apache2 default
#rc-service apache2 start