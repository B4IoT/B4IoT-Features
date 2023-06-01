#!/bin/bash
# Creating the ssh keys for client user
mkdir -p /home/client/.ssh
chown client /home/client/.ssh
chmod 700 /home/client/.ssh
touch /home/client/.ssh/authorized_keys
chown client /home/client/.ssh/authorized_keys
# write keys to client authorized keys
echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC8Sf/vfRY+SGp6fS5ENgGPh3gAAL6EtGxoeku2g90JSP3hQh/GaszQotwYF3Kw7A4VtivSkUx63YKgvJXD73sxV+wHF9XTnY2OYo+ow7TqyNP9kG/Ld/nnZ7Pj5yuXXKzCUlhvBimUYEev3iePZ67Aqq6gMEypiDooiRi3F72OVk9ZxJsZU8Caa7lBYwg7YPsfsa+KjaOnENy/Sz6fkKat3RfAZ75bqOjsSIrRNoIdUoF2JleZOJ4QfAbZQcuijYHC3BaYlrrmd4WwI0t14N126//E5QRnnSyUdfFS4gAlqgQKN6oSCAEcYzs1eO72xs9CdW/Rj6s8cdB1UwtPckWV" >> /home/client/.ssh/authorized_keys
chmod 600 /home/client/.ssh/authorized_keys