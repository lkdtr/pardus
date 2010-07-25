#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools

WorkDir='wxsvg-1.0b7_3'

def setup():
    libtools.libtoolize("--copy --force")
    autotools.configure()
    
def build():
    autotools.make()
    
def install():
    autotools.install()

    pisitools.dodoc("COPYING", "AUTHORS", "ChangeLog", "TODO")
