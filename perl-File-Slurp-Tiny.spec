#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-Slurp-Tiny
Version  : 0.004
Release  : 10
URL      : https://cpan.metacpan.org/authors/id/L/LE/LEONT/File-Slurp-Tiny-0.004.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/L/LE/LEONT/File-Slurp-Tiny-0.004.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libf/libfile-slurp-tiny-perl/libfile-slurp-tiny-perl_0.004-1.debian.tar.xz
Summary  : A simple, sane and efficient file slurper
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-File-Slurp-Tiny-license = %{version}-%{release}
BuildRequires : buildreq-cpan

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


%prep
%setup -q -n File-Slurp-Tiny-0.004
cd ..
%setup -q -T -D -n File-Slurp-Tiny-0.004 -b 1
mkdir -p deblicense/
cp -r %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/File-Slurp-Tiny-0.004/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-Slurp-Tiny
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-File-Slurp-Tiny/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-File-Slurp-Tiny/deblicense_copyright
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
/usr/lib/perl5/vendor_perl/5.28.2/File/Slurp/Tiny.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::Slurp::Tiny.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-Slurp-Tiny/LICENSE
/usr/share/package-licenses/perl-File-Slurp-Tiny/deblicense_copyright
