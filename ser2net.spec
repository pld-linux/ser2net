#
# Conditional build:
%bcond_without	ipmi	# OpenIPMI support

Summary:	Serial to network proxy
Summary(pl.UTF-8):	Proxy między portem szeregowym a siecią
Name:		ser2net
Version:	3.5.1
Release:	1
License:	GPL v2+
Group:		Networking/Daemons
Source0:	http://downloads.sourceforge.net/ser2net/%{name}-%{version}.tar.gz
# Source0-md5:	569267b37b8f507d8874f28f5334b5d2
Patch0:		%{name}-libwrap.patch
URL:		http://ser2net.sourceforge.net/
%{?with_ipmi:BuildRequires:	OpenIPMI-devel}
BuildRequires:	autoconf >= 2.50
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
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules \
	%{!?with_ipmi:--without-openipmi} \
	--with-tcp-wrappers
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
%attr(755,root,root) %{_sbindir}/ser2net
%{_mandir}/man8/ser2net.8*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ser2net.conf
