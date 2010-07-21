#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="%s-%s-6386.i386.linux" % (get.srcNAME(), get.srcVERSION())

def install():
    pisitools.dosed("install", "dest=\$PREFIX", "dest=%s/usr" % get.installDIR())
    pisitools.dosed("install", "\$HOME/.local", "/usr")
    pisitools.dosed("install", "update-[a-z]*-database", "XXpatchedXX")

    shelltools.system("./install --unattended --user")

    pisitools.dosym("/opt/netscape/plugins/libflashplayer.so", "/usr/lib/opera/plugins/libflashplayer.so")
