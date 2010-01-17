#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def build():
    shelltools.system('/usr/qt/4/bin/lrelease Merkaartor.pro')
    shelltools.system('/usr/qt/4/bin/qmake Merkaartor.pro GEOIMAGE=1 PREFIX=/usr NODEBUG=1')

def install():
    autotools.rawInstall('INSTALL_ROOT="%s"' % get.installDIR())
    pisitools.insinto('/usr/share/applications', 'src/merkaartor.desktop')

    pisitools.dodoc("AUTHORS", "CHANGELOG", "HACKING", "LICENSE")
