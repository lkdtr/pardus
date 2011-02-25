#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

shelltools.export("HOME", get.workDIR())

def build():
    autotools.make()

def install():
    docdir = "%s/%s/%s" % (get.installDIR(), get.docDIR(), get.srcNAME())
    autotools.rawInstall("PKG_ROOT=%s DOC_PREFIX=%s" % (get.installDIR(), docdir))

    pisitools.domove("/usr/share/doc/tuxpaint-dev", "%s/%s/dev" % (get.docDIR(), get.srcNAME()))

    pisitools.remove("/usr/lib/tuxpaint/plugins/puzzle.so")
