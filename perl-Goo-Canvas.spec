%define upstream_name Goo-Canvas
%define upstream_version 0.06

# Newx calls Perl_croak_nocontext with a char * without "%s", may be
# valid or not but it isn't fixable here, keep this until perl is fixed 
%define Werror_cflags %nil


Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5
Summary:	Goo::Canvas Perl interface to the GooCanvas 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/Y/YE/YEWENBIN/%{upstream_name}-%{upstream_version}.tar.gz
Source1:	perl-Goo-Canvas.rpmlintrc

BuildRequires:	libgoocanvas-devel
BuildRequires:	perl-ExtUtils-Depends
BuildRequires:	perl-ExtUtils-PkgConfig
BuildRequires:	perl-Glib
BuildRequires:	perl-Gtk2
BuildRequires:	perl-devel

%description
GTK+ does't has an buildin canvas widget. GooCanvas is wonderful. It is
easy to use and has powerful and extensible way to create items in
canvas. Just try it.  For more documents, please read GooCanvas Manual
and the demo programs provided in the source distribution in both
perl-Goo::Canvas and GooCanvas.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} OPTIMIZE="$RPM_OPT_FLAGS"

%check
%{__make} test

%install
%makeinstall_std
rm -f %{buildroot}/usr/bin/perltetris.pl
rm -f %{buildroot}/usr/bin/perlmine.pl


%files
%dir %{perl_vendorarch}/Goo/Cairo
%dir %{perl_vendorarch}/Goo/Canvas
%dir %{perl_vendorarch}/Goo/Canvas/Install
%{perl_vendorarch}/Goo/*.pod
%{perl_vendorarch}/Goo/*.pm
%{perl_vendorarch}/Goo/Cairo/*.pod
%{perl_vendorarch}/Goo/Canvas/*.pod
%{perl_vendorarch}/Goo/Canvas/Install/*
%{perl_vendorarch}/auto/Goo/Canvas/Canvas.so
%{_mandir}/*/*


