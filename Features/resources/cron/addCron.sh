#!/bin/bash
apk add dcron
FILE=/sbin/openrc
rc-update add dcron default
