#!/bin/bash

# to install, add this line:
#      /bin/bash /home/pi/pymetric/start_pymetric.sh
# 
# to the /etc/rc.local, right before the exit 0

SENSOR_HOME=/home/pi/pymetric
PATH=$SENSOR_HOME:/usr/local/bin/:$PATH
cd $SENSOR_HOME

screen -dmS pymetric -c screenPymetricRc
