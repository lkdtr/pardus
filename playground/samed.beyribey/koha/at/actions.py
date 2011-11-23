#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
   autotools.configure("--with-jobdir=/var/spool/atd --with-atspool=/var/spool/atd")

def build():
    autotools.make()

def install():
    autotools.rawInstall("IROOT=%s docdir=/usr/share/doc" % get.installDIR())

