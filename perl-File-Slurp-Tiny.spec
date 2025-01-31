#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-File-Slurp-Tiny
Version  : 0.004
Release  : 30
URL      : https://cpan.metacpan.org/authors/id/L/LE/LEONT/File-Slurp-Tiny-0.004.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/L/LE/LEONT/File-Slurp-Tiny-0.004.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfile-slurp-tiny-perl/libfile-slurp-tiny-perl_0.004-1.debian.tar.xz
Summary  : 'A simple, sane and efficient file slurper [DISCOURAGED]'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-File-Slurp-Tiny-license = %{version}-%{release}
Requires: perl-File-Slurp-Tiny-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution File-Slurp-Tiny,
version 0.004:
A simple, sane and efficient file slurper [DISCOURAGED]

%package dev
Summary: dev components for the perl-File-Slurp-Tiny package.
Group: Development
Provides: perl-File-Slurp-Tiny-devel = %{version}-%{release}
Requires: perl-File-Slurp-Tiny = %{version}-%{release}

%description dev
dev components for the perl-File-Slurp-Tiny package.


%package license
Summary: license components for the perl-File-Slurp-Tiny package.
Group: Default

%description license
license components for the perl-File-Slurp-Tiny package.


%package perl
Summary: perl components for the perl-File-Slurp-Tiny package.
Group: Default
Requires: perl-File-Slurp-Tiny = %{version}-%{release}

%description perl
perl components for the perl-File-Slurp-Tiny package.


%prep
%setup -q -n File-Slurp-Tiny-0.004
cd %{_builddir}
tar xf %{_sourcedir}/libfile-slurp-tiny-perl_0.004-1.debian.tar.xz
cd %{_builddir}/File-Slurp-Tiny-0.004
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/File-Slurp-Tiny-0.004/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-Slurp-Tiny
cp %{_builddir}/File-Slurp-Tiny-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-File-Slurp-Tiny/5b460a74fc176dd569fe582e58fe0be43ea65d6a || :
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-File-Slurp-Tiny/1b8356a83a7c509464a3f527c377e097f3017313 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::Slurp::Tiny.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-Slurp-Tiny/1b8356a83a7c509464a3f527c377e097f3017313
/usr/share/package-licenses/perl-File-Slurp-Tiny/5b460a74fc176dd569fe582e58fe0be43ea65d6a

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
