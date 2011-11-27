#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = "spaetz-offlineimap-b1bff15"

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
    pisitools.insinto("%s/%s/example-config" % (get.docDIR(), get.srcNAME()), "*.conf*")
    pisitools.dodoc("COPYING", "README.rst")
