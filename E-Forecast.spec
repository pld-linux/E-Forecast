Summary:	Shows an icon with the current weather forecast
Summary(pl.UTF-8):	Pokazuje ikonę z aktualną prognozą pogody
Name:		E-Forecast
Version:	0.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/waepplets/%{name}-%{version}.tar.gz
# Source0-md5:	5243f7ca02dd368975ffeb7acfd83b74
URL:		http://waepplets.sourceforge.net/
Requires:	enlightenment >= 0.16.4
Requires:	epplets >= 0.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Epplet is intended for use with Enlightenment windowmanager and
Epplets software. It displays an icon with the weather forecast for
the city of your choice.

%description -l pl.UTF-8
Ten Eplet jest przeznaczony do używania z zarządcą okien Enlightenment
i innymi Epletami. Wyświetla ikonę z prognozą pogody dla wybranego
miasta.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags}" %{__make}

%install
rm -rf $RPM_BUILD_ROOT

EBIN="%{_bindir}"
EROOT="%{_datadir}/enlightenment"
export EBIN EROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/E-Forecast.epplet
%{_datadir}/enlightenment/epplet_icons/E-Forecast.icon
%{_datadir}/enlightenment/epplet_data/*
