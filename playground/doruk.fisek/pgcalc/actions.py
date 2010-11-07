#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import kde

WorkDir = "pgcalc2-2.2-10"
# NoStrip = "/"

shelltools.export("HOME", get.workDIR())

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()

#    pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "NEWS")
