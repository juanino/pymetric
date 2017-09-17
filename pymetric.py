#!/usr/bin/python

import time
import ping
import time
import socket

# get the graphite server from config file
import pymetric_config as cfg

def collect_metric(name, value, timestamp):
    sock = socket.socket()
    sock.connect( (cfg.graphite_server, 2003) )
    sock.send("%s %d %d\n" % (name, value, timestamp))
    sock.close()

def now():
    return int(time.time())

#collect_metric("pymetric.ping.switch", 49, now())

hosts = cfg.hosts

while True:
    for host in hosts:
        try:
            hname = host.replace('.','_')
            metric_name = "pymetric.ping." + hname
            print "working on " + metric_name
            result =  ping.quiet_ping(host, count=5)
            [loss, maxrtt, artt] = result
            print loss, maxrtt, artt
            if loss == 100:
                print "loss is : " + str(loss)
                print "skipping report on artt"
                #raise Exception('bad data')
            else:
                collect_metric("pymetric.ping."+hname, artt, now())
        except socket.error, e:
            print "Ping Error:", e
    print "sleeping..."
    time.sleep(10)
