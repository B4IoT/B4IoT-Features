#!/bin/bash
su manager
mkdir -p /home/manager/.ssh/
cd /home/manager/.ssh/

mv /tmp/backend/Features/misconfigurations/ssh/key/id_rsa id_rsa
mv /tmp/backend/Features/misconfigurations/ssh/key/id_rsa.pub  id_rsa.pub

chown manager:managerGroup id_rsa
chown manager:managerGroup id_rsa.pub

echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC0HEGdIR2iiBXkz4LfuwazxXBP79/9QLlSiaePxv619umLTRLekgnxbOG9uIcRoUXnliSlj/Y3l9XcMDsBBb13EpiklgdMOVhWvQmNGo/zK8WnWYlE2zVKAARYCNiWRPM7zET6dVlBjMImaeb+MaYgHXLBYpD2zNoSktz9AY51u5q1K6QI2H6mPNkCZ/6Ab3SyDezc3VMY/JCeWv9SoGBovEFveDRuQb9lscV7+gNGcFA+5HiJdeRRtye8rtqrq2LSW+hmc1kkfRkB+8CYpJjsLxNbzYGxTwfSEEDoG9vnVbltZnTky03JezQcGCBvDYzD5ZWamtZJYrXqw3iPCE/ezyHYpYwJ1QqsFly7RKVFXSsfUSgunAd4uKSH6bG5ArczEqQHiMYbOwJEoFmEeYrK05tzMyg99mzqn1uSNqig6lQZelw3oSs6GGzmJuMzlVlGus+qY7Q+Qcx1aIxnAjMtmmQ256BDoW4F5r3tZhZD7KxvVz4SzjZ6SVi+qYPFz58= manager@55dc2768c52a" >> /home/manager/.ssh/authorized_keys
chown 700 authorized_keys