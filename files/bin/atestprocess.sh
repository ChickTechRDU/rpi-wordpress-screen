#!/bin/bash
if [ "$#" -ne 1 ]; then
    echo "${0} start|stop"
    exit 1
fi

if [ "${1}" == "start" ]; then
     while /bin/true; do
        sleep infinity 
     done &
elif [ "${1}" == "stop" ]; then
     pkill -f atestprocess
else
    echo "${0} start|stop"
    exit 1
fi

