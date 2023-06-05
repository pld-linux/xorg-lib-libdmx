Summary:	DMX extension library
Summary(pl.UTF-8):	Biblioteka rozszerzenia DMX
Name:		xorg-lib-libdmx
Version:	1.1.5
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/lib/libdmx-%{version}.tar.xz
# Source0-md5:	ca5b5017987d2eee289485b54506ff5c
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel >= 1.6
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-proto-dmxproto-devel >= 2.2.99.1
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
Requires:	xorg-lib-libX11 >= 1.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DMX (Distributed Multihead X) extension library.

%description -l pl.UTF-8
Biblioteka rozszerzenia DMX (Distributed Multihead X).

%package devel
Summary:	Header files for libdmx library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libdmx
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libX11-devel >= 1.6
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-dmxproto-devel >= 2.2.99.1

%description devel
DMX (Distributed Multihead X) extension library.

This package contains the header files needed to develop programs that
use libdmx.

%description devel -l pl.UTF-8
Biblioteka rozszerzenia DMX (Distributed Multihead X).

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libdmx.

%package static
Summary:	Static libdmx library
Summary(pl.UTF-8):	Biblioteka statyczna libdmx
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
DMX (Distributed Multihead X) extension library.

This package contains the static libdmx library.

%description static -l pl.UTF-8
Biblioteka rozszerzenia DMX (Distributed Multihead X).

Pakiet zawiera statyczną bibliotekę libdmx.

%prep
%setup -q -n libdmx-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libdmx.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_libdir}/libdmx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdmx.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdmx.so
%{_includedir}/X11/extensions/dmxext.h
%{_pkgconfigdir}/dmx.pc
%{_mandir}/man3/DMX*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libdmx.a
