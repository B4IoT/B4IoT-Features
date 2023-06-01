#!/bin/bash
apk add openjdk11
mv /tmp/backend/Features/vulnerabilities/java/CommandInjection/CommandInjection.jar CommandInjection.jar 
mkdir -p /opt/dvd/code/java/
mv ./CommandInjection.jar  /opt/dvd/code/java/CommandInjection.jar 
chmod -R +x /opt/dvd/code/java/
chmod -R +s /opt/dvd/code/java/
