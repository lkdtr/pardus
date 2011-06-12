# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Knockd port-knocking daemon",
                 "tr": "Knockd port-knocking sunucusu"
                 })
serviceDefault = "off"

@synchronized
def start():
    startService(command="/usr/sbin/knockd",
                 args="-d",
                 makepid=True,
                 pidfile="/var/run/knockd.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/knockd",
                donotify=True)

def status():
    return isServiceRunning("/var/run/knockd.pid")
