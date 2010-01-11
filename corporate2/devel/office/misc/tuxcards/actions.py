#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = 'tuxcards'

def setup():
    pisitools.dosed("tuxcards.pro", "/usr/local/doc/tuxcards", "/usr/share/tuxcards")
    pisitools.dosed("tuxcards.pro", "/usr/local", "/usr")
    pisitools.dosed("src/CTuxCardsConfiguration.cpp", "/usr/local/doc/tuxcards", "/usr/share/tuxcards")
    pisitools.dosed("src/gui/dialogs/configurationDialog/IConfigurationDialog.ui", "/usr/local/bin", "/usr/bin")
    shelltools.system("/usr/qt/4/bin/qmake tuxcards.pro")

def build():
    autotools.make()

def install():
    pisitools.dodoc("COPYING", "AUTHORS")
    pisitools.insinto("/usr/share/pixmaps", "src/icons/attic/lo32-app-tuxcards.xpm", "tuxcards.xpm")

    pisitools.dobin("tuxcards")
