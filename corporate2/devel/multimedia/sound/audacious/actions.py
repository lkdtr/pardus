#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-nls \
                         --enable-chardet \
                         --enable-dbus \
                         --enable-samplerate \
                         --enable-xspf \
                         --enable-sm \
                         --disable-sse2 \
                         --disable-xmltest")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "COPYING", "NEWS", "README", "doc/NEW_FORMATS" , "doc/HACKING", "doc/TODO")
