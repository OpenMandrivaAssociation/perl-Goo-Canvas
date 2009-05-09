# Newx calls Perl_croak_nocontext with a char * without "%s", may be
# valid or not but it isn't fixable here, keep this until perl is fixed 
%define Werror_cflags %nil

%define real_name Goo-Canvas


Summary:	Goo::Canvas Perl interface to the GooCanvas 
Name:		perl-%{real_name}
Version:	0.06
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/Y/YE/YEWENBIN/%{real_name}-%{version}.tar.gz
BuildRequires:	libgoocanvas-devel
BuildRequires:	perl-devel
BuildRequires:	perl-ExtUtils-Depends
BuildRequires:	perl-ExtUtils-PkgConfig
BuildRequires:	perl-Glib
BuildRequires:	perl-Gtk2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
GTK+ does't has an buildin canvas widget. GooCanvas is wonderful. It is easy to use and has powerful and extensible way to create items in canvas. Just try it.  For more documents, please read GooCanvas Manual and the demo programs provided in the source distribution in both perl-Goo::Canvas and GooCanvas.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} OPTIMIZE="$RPM_OPT_FLAGS"

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}/usr/bin/perltetris.pl
rm -f %{buildroot}/usr/bin/perlmine.pl

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{perl_vendorarch}/Goo/Cairo
%dir %{perl_vendorarch}/Goo/Canvas
%{perl_vendorarch}/Goo/*.pod
%{perl_vendorarch}/Goo/*.pm
%{perl_vendorarch}/Goo/Cairo/*.pod
%{perl_vendorarch}/Goo/Canvas/*.pod
%{perl_vendorarch}/Goo/Canvas/Install/*
%{perl_vendorarch}/auto/Goo/Canvas/Canvas.so
%{_mandir}/*/*

