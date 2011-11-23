#!/usr/bin/python
# -*- coding: utf-8 -*-

from comar.service import *

serviceType = "local"

serviceDesc = _({"en": "at scheduler service",
                 "tr": "at zamanlama servisi"})

@synchronized
def start():
    startService(command="/usr/sbin/atd",
                 detach=True,
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/atd",
                donotify=True)

def status():
    return isServiceRunning(command="/usr/sbin/atd")

