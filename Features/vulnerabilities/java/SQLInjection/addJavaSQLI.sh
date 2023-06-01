#!/bin/bash
apk add openjdk11
mv /tmp/backend/Features/vulnerabilities/java/SQLInjection/sqlInjection.jar SQLInjection.jar 
mv /tmp/backend/Features/vulnerabilities/java/SQLInjection/login.db login.db 
mkdir -p /opt/dvd/code/java/
mv ./SQLInjection.jar  /opt/dvd/code/java/SQLInjection.jar  
mv ./login.db  /opt/dvd/code/java/login.db  
chmod -R +x /opt/dvd/code/java/
chmod -R +s /opt/dvd/code/java/
