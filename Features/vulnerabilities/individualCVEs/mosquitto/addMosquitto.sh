#!/bin/bash
# CVE-2021-34431
# CVE-2021-41039
# https://security.alpinelinux.org/vuln/CVE-2021-34431
# https://security.alpinelinux.org/vuln/CVE-2021-41039
apk del mosquitto
apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/v3.10/main/ mosquitto=1.6.3-r0
rc-update add mosquitto default