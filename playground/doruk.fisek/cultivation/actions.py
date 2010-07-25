#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = 'Cultivation_6_UnixSource'

def setup():
    shelltools.system("cat game2/Makefile.GnuLinux game2/Makefile.common minorGems/build/Makefile.minorGems game2/gameSource/Makefile.all minorGems/build/Makefile.minorGems_targets > game2/gameSource/Makefile")    # custom game2/configure script replacement
    shelltools.cd("minorGems/sound/portaudio")
    shelltools.chmod("configure", 0755)
    autotools.configure()

def build():
    shelltools.cd("minorGems/sound/portaudio")
    autotools.make()
    shelltools.cd("../../../game2/gameSource")
    autotools.make()

def install():
    pisitools.insinto("/usr/share/cultivation", "game2/gameSource/Cultivation", "cultivation")
    pisitools.insinto("/usr/share/cultivation", "game2/gameSource/language.txt")
    pisitools.insinto("/usr/share/cultivation", "game2/gameSource/features.txt")
    pisitools.insinto("/usr/share/cultivation", "game2/gameSource/font.tga")
    pisitools.insinto("/usr/share/cultivation/languages", "game2/gameSource/languages/*.txt")

    pisitools.dodoc("game2/documentation/how_to_play.txt", "game2/changeLog.txt", "game2/documentation/gameDesign/design.tex")
