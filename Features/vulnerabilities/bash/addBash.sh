#!/bin/bash
mkdir -p /opt/dvd/code/bash/
bashURL="${VulnerabilitiesURL}bash/"
cd /tmp/bash/
wget "${bashURL}CommandInjection/vulnerablebash.sh" -O CommandInjection.sh
wget "${bashURL}PathTraversal/pathTraversal.sh" -O PathTraversal.sh 
mv /tmp/bash/* /opt/dvd/code/bash/
chmod -R +x /opt/dvd/code/bash/
chmod -R +s /opt/dvd/code/bash/
rm /opt/dvd/code/bash/addBash.sh