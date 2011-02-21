#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("qmake-qt4")

def build():
    autotools.make()

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())

    # Update Turkish translation
    shelltools.system("lrelease-qt4 src/translations/keepassx-tr_TR.ts")
    pisitools.insinto("/usr/share/keepassx/i18n/", "src/translations/*tr*.qm")

    pisitools.dodoc("changelog", "COPYING")
