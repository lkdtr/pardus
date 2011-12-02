# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "server"

serviceDesc = _({"en": "GNUMP3d Server",
                 "tr": "GNUMP3d Sunucusu"})

@synchronized
def start():
    startService(command="/usr/bin/gnump3d",
                 makepid=True,
                 pidfile="/var/run/gnump3d.pid",
                 detach=True,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/gnump3d.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/gnump3d.pid")
