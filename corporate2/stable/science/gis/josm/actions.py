#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = 'josm'

def build():
    shelltools.system("ant")

def install():
    pisitools.insinto("/usr/share/pixmaps", "images/logo.png", "josm.png")
    pisitools.insinto("/usr/share/josm", "dist/josm-custom.jar", "josm.jar")

    pisitools.dodoc("README", "LICENSE", "CONTRIBUTION")
