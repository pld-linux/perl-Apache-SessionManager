#
# Conditional build:
# _with_tests - perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Apache
%define	pnam	SessionManager
Summary:	Apache::SessionManager - simple mod_perl extension to manage sessions
Summary(pl):	Apache::SessionManager - proste rozszerzenie mod_perla do obs³ugi sesji
Name:		perl-Apache-SessionManager
Version:	0.01
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildRequires:	apache-mod_perl
BuildRequires:	perl-Apache-Session
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apache::SessionManager is a mod_perl module that helps session
management of a web application. This simple module is a wrapper around
Apache::Session persistence framework for session data.  It creates a
session object and makes it available to all other handlers by putting
in pnotes. In a mod_perl handler you can retrieve the session object
directly from pnotes with predefined key 'SESSION_MANAGER_HANDLE':

# %description -l pl
# TODO

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
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
