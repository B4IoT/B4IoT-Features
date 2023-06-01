#!/bin/bash
apk add openjdk11
mv /tmp/backend/Features/vulnerabilities/javaInterface/PathTraversal/pathTraversal.jar PathTraversal.jar 
mkdir -p /opt/dvd/services/vulns/java/
mv ./PathTraversal.jar  /opt/dvd/services/vulns/java/PathTraversal.jar  
