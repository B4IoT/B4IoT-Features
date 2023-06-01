#!/bin/bash
apk add tar

mkdir -p /home/client/backups/
touch /home/client/backups/backup.sh

echo "#!/bin/bash" >> /home/client/backups/backup.sh
echo "cd /home/client" >> /home/client/backups/backup.sh
echo "tar --exclude='backups' -cf /home/client/backups/backup.tgz *" >> /home/client/backups/backup.sh
chmod +x /home/client/backups/backup.sh

echo '/10 * * * * /home/client/backups/backup.sh' >> /etc/crontabs/root