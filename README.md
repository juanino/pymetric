# pymetric
Originally whipped together to capture ping times and send to
graphite for graphing in grafana, but can be used as an example to collect other things

# usage
* copy the sample config file
* get some modules from pip 
* edit the config with your graphite server
* run the program
* add a line to your rc.local before the exit 0
```
/bin/bash /home/pi/pymetric/start_pymetric.sh
```


```
# cp  pymetric_config_sample.py pymetric_config.py
# ./getmodules.sh
# vi pymetric_config.py 
# ./pymetric.py
```
