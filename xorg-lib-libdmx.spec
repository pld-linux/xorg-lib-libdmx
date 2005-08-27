Summary:	dmx library
Summary(pl):	Biblioteka dmx
Name:		xorg-lib-libdmx
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libdmx-%{version}.tar.bz2
# Source0-md5:	0a7bf1090d92fa4c3e27639115cbe2bc
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-proto-dmxproto-devel
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dmx library.

%description -l pl
Biblioteka dmx.

%package devel
Summary:	Header files libdmx development
Summary(pl):	Pliki nag³ówkowe do biblioteki libdmx
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-dmxproto-devel

%description devel
dmx library.

This package contains the header files needed to develop programs that
use these libdmx.

%description devel -l pl
Biblioteka dmx.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libdmx.

%package static
Summary:	Static libdmx library
Summary(pl):	Biblioteka statyczna libdmx
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
dmx library.

This package contains the static libdmx library.

%description static -l pl
Biblioteka dmx.

Pakiet zawiera statyczn± bibliotekê libdmx.

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
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libdmx.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdmx.so
%{_libdir}/libdmx.la
%{_pkgconfigdir}/dmx.pc
%{_mandir}/man3/*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libdmx.a
