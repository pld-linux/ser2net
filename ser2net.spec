Summary:	Serial to network proxy
Summary(pl):	Proxy miêdzy portem szeregowym a sieci±
Name:		ser2net
Version:	2.1
Release:	1
License:	GPL
Group:		Daemons
Source0:	http://dl.sourceforge.net/ser2net/%{name}-%{version}.tar.gz
# Source0-md5:	c0b380158288870cc585a8d5dc13eeac
Patch0:		%{name}-libwrap.patch
URL:		http://ser2net.sf.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libwrap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Make serial ports available to network via TCP/IP connection.

%description -l pl
Program udostêpniaj±cy porty szeregowe przez po³±czenie TCP/IP.

%prep
%setup -q
%patch -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install ser2net.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS ChangeLog AUTHORS
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/ser2net.conf
