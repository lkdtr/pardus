#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def install():
    pythonmodules.install()
    shelltools.chmod("%s/%s/man1/*" % (get.installDIR(), get.manDIR()),  0644)
    shelltools.chmod("%s/usr/share/doc/%s-%s/*" % (get.installDIR(), get.srcNAME(), get.srcVERSION()), 0644)
