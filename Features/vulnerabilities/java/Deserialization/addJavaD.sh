#!/bin/bash
apk add openjdk11
mv /tmp/backend/Features/vulnerabilities/java/Deserialization/deserialization.jar Deserialization.jar 
mkdir -p /opt/dvd/code/java/
mv ./Deserialization.jar  /opt/dvd/code/java/Deserialization.jar  
chmod -R +x /opt/dvd/code/java/
chmod -R +s /opt/dvd/code/java/
