#!/bin/bash
#golden image prep work:
#become root on pi.
#git clone repo.
#run this script
sed -i 's/PasswordAuthentication.*/PasswordAuthentication yes/' /etc/ssh/sshd_config
systemctl enable ssh
systemctl restart ssh
apt-get update
apt-get upgrade
apt-get install wordpress curl apache2 mariadb-server i2c-tools vim lsof python-bs4
mkdir -p /opt/bin /opt/rsync_source /opt/rsync_destination
cp -Rf /root/2019-chicktech/files/bin/* /opt/bin/

