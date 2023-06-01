#!/bin/bash
# CVE-2020-8794
# https://security.alpinelinux.org/vuln/CVE-2020-8794
apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/v3.10/main/ opensmtpd=6.0.3p1-r3
rc-update add smtpd default