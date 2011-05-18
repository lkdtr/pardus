#!/usr/bin/python
# -*- coding: utf-8 -*-

from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Calendar Service",
                 "tr": "Takvim Servisi"})

@synchronized
def start():
    startService(command="/usr/bin/radicale",
                 makepid=True,
                 pidfile="/var/run/radicale.pid",
                 detach=True,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/radicale.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/radicale.pid")
