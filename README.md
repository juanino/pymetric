# pymetric
Originally whipped together to capture ping times and send to
graphite for graphing in grafana, but can be used as an example to collect other things

# usage
* copy the sample config file
* get some modules from pip (yes i know this is more than i need, but i need it for other projects)
* edit the config with your graphite server
* run the program

```
# cp  pymetric_config_sample.py pymetric_config.py
# ./getmodules.sh
# vi pymetric_config.py 
# ./pymetric.py
```
