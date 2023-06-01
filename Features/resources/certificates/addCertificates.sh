#!/bin/bash
mv /tmp/backend/Features/resources/certificates/client.cnf client.cnf
mv /tmp/backend/Features/resources/certificates/root.cnf root.cnf
mv /tmp/backend/Features/resources/certificates/server.cnf server.cnf

mkdir -p /tmp/cert
mkdir -p /tmp/tmp

#Create selfisgned CA Certificate
openssl req -x509 -new -keyout /tmp/cert/root.key -out /tmp/cert/root.cer -config root.cnf -passout pass:test
#Creating client key pair & cert request
openssl req -nodes -new -keyout /tmp/cert/client.key -out /tmp/tmp/client.csr -config client.cnf -passout pass:test
#generate client certifacates
openssl x509 -req -in /tmp/tmp/client.csr -CA /tmp/cert/root.cer -CAkey /tmp/cert/root.key -passin pass:test -out /tmp/cert/client.cer -CAcreateserial -days 365 -extfile client.cnf -extensions x509_ext
#Ceeate pkc12 keystore for android
openssl pkcs12 -export -inkey /tmp/cert/client.key  -in /tmp/cert/client.cer -certfile /tmp/cert/root.cer -passout pass:test -out /tmp/cert/client.pfx

echo "DNS.2 = DVD">> server.cnf
echo "IP.1 = 127.0.0.1" >> server.cnf 

#Create server key pair & certificate request
openssl req -nodes -new -keyout /tmp/server.key -out /tmp/tmp/server.csr -config server.cnf
#Generate server certificate
openssl x509 -days 3650 -req -in /tmp/tmp/server.csr -CA /tmp/cert/root.cer -passin pass:test -CAkey /tmp/cert/root.key -CAcreateserial -out /tmp/cert/server.cer -extfile server.cnf -extensions x509_ext

mkdir -p /etc/credentials

cp /tmp/cert/root.cer /etc/credentials/clients.pem
cat /tmp/cert/client.cer >> /etc/credentials/clients.pem
mv /tmp/cert/root.cer /etc/credentials/
mv /tmp/cert/server.cer/ /etc/credentials/
mv /tmp/server.key /etc/credentials/

rm client.cnf
rm root.cnf
rm server.cnf
rm -r /tmp/tmp
