Summary:	Serial to network proxy
Summary(pl):	Proxy mi�dzy portem szeregowym a sieci�
Name:		ser2net
Version:	1.5
Release:	1
License:	GPL
Group:		Daemons
Source0:	http://prdownloads.sf.net/ser2net/%{name}-%{version}.tar.gz
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
Program udost�pniaj�cy porty szeregowe przez po��czenie TCP/IP.

%prep
%setup -q
%patch -p1

%build
libtoolize --copy --force
aclocal
autoconf
automake -a -c -f
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install ser2net.conf $RPM_BUILD_ROOT%{_sysconfdir}

gzip -9nf README NEWS ChangeLog AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/ser2net.conf
