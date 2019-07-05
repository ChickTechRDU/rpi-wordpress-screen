#!/bin/bash
#set -x
if [ "$#" -ne 2 ]; then
    echo "${0} IP USERNAME"
    exit 1
fi
COUNT=$(grep -c "^${1}   .*" /etc/hosts)
if [ "${COUNT}" -lt 1 ]; then
   echo "${1}    ${2}.example.com" >> /etc/hosts
else
   sed -i "/${1}    /d" /etc/hosts
   echo "${1}    ${2}.example.com" >> /etc/hosts
fi
