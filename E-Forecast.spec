Summary:	Shows an icon with the current weather forecast
Name:		E-Forecast
Version:	0.1
Release:	1
License:	GPL
Group:		X11/Utilities
Group(pl):	X11/Narzêdzia
Source0:	ftp://download.sourceforge.net/pub/sourceforge/waepplets/%{name}-%{version}.tar.gz
Requires:	enlightenment >= 0.16.4
Requires:	epplets >= 0.6
URL:		http://waepplets.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This Epplet is intended for use with Enlightenment windowmanager and
Epplets software. It displays an icon with the weather forecast for
the city of your choice.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" make

%install
rm -rf $RPM_BUILD_ROOT

EBIN="%{_bindir}"
EROOT="%{_datadir}/enlightenment"
export EBIN EROOT

%{__make} PREFIX=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/E-Forecast.epplet
%{_datadir}/enlightenment/epplet_icons/E-Forecast.icon
%{_datadir}/enlightenment/epplet_data/*
