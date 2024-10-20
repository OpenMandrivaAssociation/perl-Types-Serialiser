%define upstream_name Types-Serialiser

Name:		perl-%{upstream_name}
Version:	1.01
Release:	1
Epoch:    1
Summary:	Simple data types for common serialisation formats
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Async/MLEHMANN/%{upstream_name}-%{version}.tar.gz

BuildRequires:  perl-devel
BuildRequires:	perl(common::sense)
BuildRequires:  perl(ExtUtils::MakeMaker)

BuildArch:	noarch

# Filter bogus provide of JSON::PP::Boolean (for rpm ≥ 4.9)
%global __provides_exclude ^perl\\(JSON::PP::Boolean\\)

%description
This module provides some extra datatypes that are used by common
serialisation formats such as JSON or CBOR. The idea is to have a
repository of simple/small constants and containers that can be shared
by different implementations so they become interoperable between each
other.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor

%make_build


%install
%make_install

%files
%doc Changes COPYING META.json META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*
