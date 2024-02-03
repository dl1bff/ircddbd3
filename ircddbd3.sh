#!/bin/sh

#
# ircddbd3
#   starts ircDDB java program
#
# Copyright (C) 2017   Michael Dirska, DL1BFF (dl1bff@mdx.de)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

PRGMDIR=/usr/share/ircddbd3

FILE1=$PRGMDIR/app2.jar
FILE2=$PRGMDIR/ircDDB2.jar

PGSQL=/usr/share/java/postgresql-jdbc3.jar

export PACKAGE_VERSION="PkGvErSiOn"

cd /etc/ircddbd3

exec /usr/bin/java -cp $FILE1:$FILE2:$PGSQL net.ircDDB.IRCDDBApp
