#!/bin/bash
#golden image prep work:
#become root on pi.
#git clone repo.
#run this script
sed -i 's/PasswordAuthentication.*/PasswordAuthentication yes/' /etc/ssh/sshd_config
systemctl enable ssh
systemctl restart ssh
apt-get update
apt-get -y upgrade
apt-get -y install wordpress curl apache2 mariadb-server i2c-tools vim lsof python-bs4 php php-mysql libapache2-mod-php sendmail python-dev python-pip libfreetype6-dev libjpeg-dev build-essential
mkdir -p /opt/bin /opt/rsync_source /opt/rsync_destination
cp -Rf /root/2019-chicktech/files/bin/* /opt/bin/
cp -Rf /root/2019-chicktech/files/html/* /var/www/html/
su - pi -c "pip3 install -r /opt/bin/requirements.txt"
# Thonny reads python packages from below target. Install here as well so packages are available
# to both Thonny and CLI.
su - pi -c "pip3 install -t /home/pi/.local/lib/python3.7/site-packages -r /opt/bin/requirements.txt"
