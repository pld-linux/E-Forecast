Summary: Shows an icon with the current weather forecast
Name: E-Forecast
Version: 0.1
Release: 1
Copyright: GPL
Group: X11/Utilities
Source: E-Forecast-0.1.tar.gz
Requires: enlightenment >= 0.16.4
Requires: epplets >= 0.6
URL: http://waepplets.sourceforge.net/
BuildRoot: /tmp/e-forecast-root

%description
This Epplet is intended for use with Enlightenment windowmanager and Epplets
software. It displays an icon with the weather forecast for the city of your
choice.

%prep
%setup

%build
CFLAGS="$RPM_OPT_FLAGS" make

%install
export EBIN="/usr/bin"
export EROOT="/usr/share/enlightenment"
rm -rf $RPM_BUILD_ROOT
make PREFIX=$RPM_BUILD_ROOT install
du -k $RPM_BUILD_ROOT

%post
echo Please regenerate your Enlightenment menus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc COPYING
/usr/bin/E-Forecast.epplet
/usr/share/enlightenment/epplet_icons/E-Forecast.icon
/usr/share/enlightenment/epplet_data/*
