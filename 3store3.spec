Summary:	3store RDF engine
Summary(pl.UTF-8):	Silnik RDF 3store
Name:		3store3
Version:	3.0.17
Release:	3
License:	GPL v2+
Group:		Libraries
Source0:	http://dl.sourceforge.net/threestore/%{name}-%{version}.tar.gz
# Source0-md5:	6e5dceaa076e603e618384e01da6a50a
Patch0:		%{name}-link.patch
Patch1:		%{name}-rasqal.patch
Patch2:		%{name}-db.patch
Patch3:		%{name}-rasqal-disable-constrs.patch
URL:		http://threestore.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	db-devel >= 4.1
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	libtool
BuildRequires:	mysql-devel
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	rasqal-devel >= 0.9.16
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
3store is an RDF(S) triplestore, written in C and backed by MySQL. It
provides a RDF query engine that supports SPARQL and RDQL, over HTTP
or through a C API or command line inferface.

It can handle 100M triple knowledge bases, white retaining fast
response times, and provides RDFS inference capabilities.

%description -l pl.UTF-8
3store to triplestore dla RDF(S) napisany w C z backendem MySQL.
Udostępnia silnik zapytań RDF obsługujący SPARQL i RDQL po HTTP,
poprzez API C lub z linii poleceń.

Może obsłużyć bazy wiedzy rzędu 100M zachowując krótkie czasy
odpowiedzi; udostępnia możliwości wnioskowania RDFS.

%package devel
Summary:	Header files for 3store library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki 3store
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	db-devel >= 4.1
Requires:	glib2-devel >= 2.2.0
Requires:	mysql-devel
Requires:	rasqal-devel >= 0.9.16

%description devel
Header files for 3store library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki 3store.

%package static
Summary:	Static 3store library
Summary(pl.UTF-8):	Statyczna biblioteka 3store
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static 3store library.

%description static -l pl.UTF-8
Statyczna biblioteka 3store.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README RELEASE-NOTES TODO
%attr(755,root,root) %{_bindir}/ts-*
%attr(755,root,root) %{_libdir}/lib3store.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/lib3store.so.0
%{_datadir}/3store3
%{_mandir}/man1/ts-*.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib3store.so
%{_libdir}/lib3store.la
%{_includedir}/3store3
%{_pkgconfigdir}/3store3.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib3store.a
