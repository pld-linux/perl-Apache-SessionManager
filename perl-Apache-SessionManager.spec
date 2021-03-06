#
# Conditional build:
%bcond_with	tests	# perform "make test"

%define		pdir	Apache
%define		pnam	SessionManager
Summary:	Apache::SessionManager - simple mod_perl extension to manage sessions
Summary(pl.UTF-8):	Apache::SessionManager - proste rozszerzenie mod_perla do obsługi sesji
Name:		perl-Apache-SessionManager
Version:	1.03
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	85b412074edde465fcf291a1fef0e5e2
URL:		http://search.cpan.org/dist/Apache-SessionManager/
BuildRequires:	apache-mod_perl
BuildRequires:	perl-Apache-Session
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apache::SessionManager is a mod_perl module that helps session
management of a web application. This simple module is a wrapper
around Apache::Session persistence framework for session data. It
creates a session object and makes it available to all other handlers
by putting in pnotes. In a mod_perl handler you can retrieve the
session object directly from pnotes with predefined key
'SESSION_MANAGER_HANDLE'.

%description -l pl.UTF-8
Apache::SessionManager to moduł do mod_perla pomagający w zarządzaniu
sesjami w aplikacjach WWW. Ten prosty moduł jest obudowaniem szkieletu
zachowywania danych sesji Apache::Session. Tworzy on obiekt sesji i
czyni go dostępnym dla wszystkich innych funkcji obsługujących poprzez
umieszcenie w pnotes. W obsłudze mod_perla można odczytywać obiekt
sesji bezpośrednio z pnotes przy pomocy predefiniowanego klucza
'SESSION_MANAGER_HANDLE'.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
