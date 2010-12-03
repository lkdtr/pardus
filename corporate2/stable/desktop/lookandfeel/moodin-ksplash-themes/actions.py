#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

WorkDir='moodin'

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()

    # Avoid file-conflicts with kdebase
    pisitools.remove("/usr/kde/3.5/lib/kde3/ksplashmoodin.so")
    pisitools.remove("/usr/kde/3.5/share/services/ksplashmoodin.desktop")
    pisitools.removeDir("/usr/kde/3.5/share/services")

    pisitools.dodoc("COPYING", "AUTHORS")   
