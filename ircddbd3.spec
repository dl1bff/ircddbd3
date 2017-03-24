#
#
# ircddbd3
#   ircDDB java program
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



Name: ircddbd3
Version: 1.0
Release: 3
License: GPLv2
Group: Networking/Daemons
Summary: ircDDB java program
URL: http://ircddb.net
Packager: Michael Dirska DL1BFF <dl1bff@mdx.de>
Requires: java, postgresql, dstar_gw >= 3
Source0: ircddbd3.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
Requires(pre): shadow-utils
%{?systemd_requires}
BuildRequires: systemd
BuildArch: noarch

%description
The script starts the ircDDB java program.


%prep
%setup -n ircddbd3



%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/%{name}
cat %{name}.sh | sed 's/PkGvErSiOn/rpm:%{name}-%{version}-%{release}/' > %{buildroot}/usr/share/%{name}/%{name}.sh
cp app2.jar %{buildroot}/usr/share/%{name}/
cp ircDDB2.jar %{buildroot}/usr/share/%{name}/
mkdir -p %{buildroot}/%_unitdir
cp %{name}.service %{buildroot}/%_unitdir/%{name}.service
mkdir -p %{buildroot}/%_presetdir
cp %{name}.preset %{buildroot}/%_presetdir/51-%{name}.preset
mkdir -p %{buildroot}/etc/%{name}
cp ircDDB.keystore %{buildroot}/etc/%{name}
cp ircDDB.policy %{buildroot}/etc/%{name}
cp ircDDB.properties %{buildroot}/etc/%{name}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%config /etc/%{name}/ircDDB.properties
/etc/%{name}/ircDDB.policy
/etc/%{name}/ircDDB.keystore
/usr/share/%{name}/app2.jar
/usr/share/%{name}/ircDDB2.jar
%attr(755,root,root) /usr/share/%{name}/%{name}.sh
%_unitdir/%{name}.service
%_presetdir/51-%{name}.preset
%doc README.md LICENSE


%pre
getent group ircddb >/dev/null || groupadd -r ircddb
getent passwd ircddb >/dev/null || useradd -r -g ircddb -d /etc/%{name} -s /sbin/nologin ircddb
exit 0


%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service



