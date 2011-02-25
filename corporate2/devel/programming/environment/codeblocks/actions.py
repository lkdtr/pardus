#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="%s-%s-release" % (get.srcNAME(), get.srcVERSION())

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--with-contrib-plugins=all")

    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")
    # Disable rpath
    pisitools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "hardcode_libdir_flag_spec=\"\"")
    pisitools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")


def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")

    # Remove plugins needing external libraries
    pisitools.remove("/usr/lib/codeblocks/plugins/libThreadSearch.so")
    pisitools.remove("/usr/lib/codeblocks/plugins/liblib_finder.so")
    pisitools.remove("/usr/lib/codeblocks/plugins/libwxsmithcontribitems.so")
