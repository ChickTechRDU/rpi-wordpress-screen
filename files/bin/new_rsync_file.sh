#!/bin/bash
DATE=$(date +%Y%m%d-%H%M%S)
touch /opt/rsync_source/${DATE}
if [ $? -ne 0 ]; then
    echo "ERROR: could not create /opt/rsync_source/${DATE}"
    exit 1
else
    echo "SUCCESS: created /opt/rsync_source/${DATE}"
    exit 0
fi
