#
# Conditional build:
# _with_tests - perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Apache
%define	pnam	SessionManager
Summary:	Apache::SessionManager - simple mod_perl extension to manage sessions
Summary(pl):	Apache::SessionManager - proste rozszerzenie mod_perla do obs³ugi sesji
Name:		perl-Apache-SessionManager
Version:	0.04
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	apache-mod_perl
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Apache-Session
BuildRequires:	perl-libapreq
BuildRequires:	rpm-perlprov >= 4.0.2-104
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

%description -l pl
Apache::SessionManager to modu³ do mod_perla pomagaj±cy w zarz±dzaniu
sesjami w aplikacjach WWW. Ten prosty modu³ jest obudowaniem szkieletu
zachowywania danych sesji Apache::Session. Tworzy on obiekt sesji i
czyni go dostêpnym dla wszystkich innych funkcji obs³uguj±cych poprzez
umieszcenie w pnotes. W obs³udze mod_perla mo¿na odczytywaæ obiekt
sesji bezpo¶rednio z pnotes przy pomocy predefiniowanego klucza
'SESSION_MANAGER_HANDLE'.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo '!' | perl Makefile.PL
%{__make}

%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
