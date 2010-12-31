#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="%s-%s-1156.i386.linux" % (get.srcNAME(), get.srcVERSION())

def build():
    # Flashplugin hack for Opera, see pardus #13989
    autotools.compile("-shared -fPIC -L/opt/netscape/plugins/ -lflashplayer \
                       -o libflashplayer.so -Wl,-rpath \
                       /opt/netscape/plugins/ opera-flash-workaround.c")

def install():
    shelltools.system("./install --prefix /usr --repackage %s/usr" % get.installDIR())

    pisitools.insinto("/usr/lib/opera/plugins/", "libflashplayer.so")
