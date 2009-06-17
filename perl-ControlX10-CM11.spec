#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	ControlX10
%define	pnam	CM11
Summary:	ControlX10::CM11 - Perl extension for X10 'ActiveHome' Controller
Summary(pl.UTF-8):	Obsługa X10 przez urządzenie CM11A
Name:		perl-ControlX10-CM11
Version:	2.09
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b59c85e92eae2c14ffa63af7ac0a1d9a
URL:		http://search.cpan.org/dist/ControlX10-CM11/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Obsoletes:	perl-ControlX10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The CM11A is a bi-directional X10 controller that connects to a serial
port and transmits commands via AC power line to X10 devices. This
module translates human-readable commands (eg. 'A2', 'AJ') into the
Interface Communication Protocol accepted by the CM11A.

%description -l pl.UTF-8
CM11A jest dwukierunkowym kontrolerem X10 podłączanym do portu
szeregowego. Steruje on urządzeniami zgodnymi z X10 transmitując
polecenia po linii zasilania AC. Ten moduł tłumaczy polecenia z
postaci czytelnej dla człowieka (np 'A2', 'AJ') na polecenia
interfejsu ICP akceptowalne przez CM11A.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README README.txt
%{perl_vendorlib}/ControlX10/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
