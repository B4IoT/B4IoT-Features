#!/bin/bash
apk add openjdk11
mv /tmp/backend/Features/vulnerabilities/javaInterface/SQLInjection/sqlInjection.jar SQLInjection.jar 
mv /tmp/backend/Features/vulnerabilities/javaInterface/SQLInjection/login.db login.db 
mkdir -p /opt/dvd/services/vulns/java/
mv ./SQLInjection.jar  /opt/dvd/services/vulns/java/SQLInjection.jar  
mv ./login.db /opt/dvd/services/vulns/java/login.db  
