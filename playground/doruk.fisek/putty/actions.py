#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "putty-0.60-2011-02-01"
# NoStrip = "/"

def setup():
    shelltools.cd("unix")
    autotools.configure()

def build():
    shelltools.cd("unix")
    autotools.make()

def install():
    shelltools.cd("unix")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("../")
    pisitools.dodoc("LICENCE", "doc/puttydoc.txt")
    pisitools.dohtml("doc/*.html")