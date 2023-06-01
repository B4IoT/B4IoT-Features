#!/bin/bash
apk add openjdk11
mv /tmp/backend/Features/vulnerabilities/javaInterface/CommandInjection/commandInjection.jar CommandInjection.jar 
mkdir -p /opt/dvd/services/vulns/java/
mv ./CommandInjection.jar  /opt/dvd/services/vulns/java/CommandInjection.jar 
chmod -R +x /opt/dvd/services/vulns/java/
chmod -R +s /opt/dvd/services/vulns/java/