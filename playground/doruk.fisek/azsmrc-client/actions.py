#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools

WorkDir = 'azsmrc-0.9.9'

def install():
    pisitools.insinto("/opt/azsmrc", "AzSMRC_0.9.9.jar")
    pisitools.insinto("/opt/azsmrc", "commons-codec_1.3.jar")
    pisitools.insinto("/opt/azsmrc", "commons-io_1.2.jar")
    pisitools.insinto("/opt/azsmrc", "jdom_1.0.jar")
    pisitools.insinto("/opt/azsmrc", "log4j_1.2.13.jar")
    pisitools.insinto("/opt/azsmrc", "launcher.jar")
    pisitools.insinto("/opt/azsmrc", "launch.properties")
    pisitools.insinto("/opt/azsmrc", "libcairo-swt.so")
    pisitools.insinto("/opt/azsmrc", "libswt-atk-gtk-3232.so")
    pisitools.insinto("/opt/azsmrc", "libswt-awt-gtk-3232.so")
    pisitools.insinto("/opt/azsmrc", "libswt-cairo-gtk-3232.so")
    pisitools.insinto("/opt/azsmrc", "libswt-glx-gtk-3232.so")
    pisitools.insinto("/opt/azsmrc", "libswt-gnome-gtk-3232.so")
    pisitools.insinto("/opt/azsmrc", "libswt-gtk-3232.so")
    pisitools.insinto("/opt/azsmrc", "libswt-mozilla-gcc3-gtk-3232.so")
    pisitools.insinto("/opt/azsmrc", "libswt-mozilla-gtk-3232.so")
    pisitools.insinto("/opt/azsmrc", "libswt-pi-gtk-3232.so")
    pisitools.insinto("/opt/azsmrc", "log4j_1.2.13.jar")
    pisitools.insinto("/opt/azsmrc", "swt.jar")
