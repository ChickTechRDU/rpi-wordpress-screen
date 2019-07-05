#!/bin/bash
COUNT=$(pgrep -c atestprocess)
if [ "${COUNT}" -lt 1 ]; then
	echo "ALERT"
	exit 1
else
    echo "Application is running"
    exit 0
fi

