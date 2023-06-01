#!/bin/bash
# CVE-2019-14287
# https://security.alpinelinux.org/vuln/CVE-2019-14287
apk del sudo
apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/v3.5/main/ sudo=1.8.19_p1-r0