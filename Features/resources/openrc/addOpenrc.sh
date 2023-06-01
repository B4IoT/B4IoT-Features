#!/bin/bash
apk add openrc
rc-update
/sbin/openrc
mkdir -p /run/openrc/
touch /run/openrc/softlevel
