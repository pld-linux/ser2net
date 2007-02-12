Summary:	Serial to network proxy
Summary(pl.UTF-8):   Proxy między portem szeregowym a siecią
Name:		ser2net
Version:	2.3
Release:	1
License:	GPL
Group:		Daemons
Source0:	http://dl.sourceforge.net/ser2net/%{name}-%{version}.tar.gz
# Source0-md5:	5f83a3e8aec18331cb61069dccdfba47
Patch0:		%{name}-libwrap.patch
URL:		http://ser2net.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libwrap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Make serial ports available to network via TCP/IP connection.

%description -l pl.UTF-8
Program udostępniający porty szeregowe przez połączenie TCP/IP.

%prep
%setup -q
%patch0 -p1

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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ser2net.conf
