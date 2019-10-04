#!/bin/bash
#set -x
if [ "$#" -ne 1 ]; then
    echo "${0} USERNAME"
    exit 1
fi
sed "s/REPLACEME/${1}/g" /root/2019-chicktech/files/apache2/wordpress.conf > /etc/apache2/sites-available/wordpress.conf
a2dissite 000-default
a2dissite default-ssl
#remove the static page we created earlier
rm -f /var/www/html/index.html
a2ensite wordpress.conf
#enable wordpress at the root of a site
if [ ! -f /etc/wordpress/htaccess.orig ]; then
cp -f /etc/wordpress/htaccess /etc/wordpress/htaccess.orig
cat << EOF > /etc/wordpress/htaccess
<IfModule mod_rewrite.c>
RewriteEngine On
RewriteBase /
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule . /index.php [L]
</IfModule>
EOF
fi

#enable direct plugin install (not-ftp based).
COUNT=$(grep -c "FS_METHOD" /usr/share/wordpress/wp-config.php)
if [ "${COUNT}" -lt 1 ]; then
cp -f /usr/share/wordpress/wp-config.php /usr/share/wordpress/wp-config.php.orig
sed -i 's^?>^define('FS_METHOD','direct');\n?>^g' /usr/share/wordpress/wp-config.php
fi

#allow anon comments via the API
COUNT=$(grep -c "chicktech_hack" /usr/share/wordpress/wp-includes/rest-api/endpoints/class-wp-rest-comments-controller.php)
if [ "${COUNT}" -lt 1 ]; then
cp -f /usr/share/wordpress/wp-includes/rest-api/endpoints/class-wp-rest-comments-controller.php /usr/share/wordpress/wp-includes/rest-api/endpoints/class-wp-rest-comments-controller.php.orig
sed -i 's^if ( ! $allow_anonymous ) {^if ( ! $allow_anonymous ) {\n return true; \n chicktech_hack;^g' /usr/share/wordpress/wp-includes/rest-api/endpoints/class-wp-rest-comments-controller.php
sed -i -e '/chicktech_hack/,+1 s%^%//%' /usr/share/wordpress/wp-includes/rest-api/endpoints/class-wp-rest-comments-controller.php
fi

#turn off posting too fast spam prevention
COUNT=$(grep -c "//add_action( 'check_comment_flood'," /usr/share/wordpress/wp-includes/default-filters.php)
if [ "${COUNT}" -lt 1 ]; then
cp -f /usr/share/wordpress/wp-includes/default-filters.php /usr/share/wordpress/wp-includes/default-filters.php.orig
sed -i -e "/add_action( 'check_comment_flood',/,+1 s%^%//%" /usr/share/wordpress/wp-includes/default-filters.php
fi

#restart apache to pickup the changes
systemctl restart apache2
