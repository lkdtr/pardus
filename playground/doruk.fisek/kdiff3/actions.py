#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def build():
    autotools.rawConfigure("qt4")

def install():
    shelltools.cd("src-QT4")
    autotools.install("INSTALL_ROOT=%s" % get.installDIR())

    pisitools.insinto("/usr/share/applications", "kdiff3.desktop")
    pisitools.insinto("/usr/share/pixmaps", "hi32-app-kdiff3.png", "kdiff3.png")
