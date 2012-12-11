%define upstream_name    Goo-Canvas
%define upstream_version 0.06

# Newx calls Perl_croak_nocontext with a char * without "%s", may be
# valid or not but it isn't fixable here, keep this until perl is fixed 
%define Werror_cflags %nil


Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Goo::Canvas Perl interface to the GooCanvas 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/Y/YE/YEWENBIN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	libgoocanvas-devel
BuildRequires:	perl-ExtUtils-Depends
BuildRequires:	perl-ExtUtils-PkgConfig
BuildRequires:	perl-Glib
BuildRequires:	perl-Gtk2
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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


%changelog
* Wed Aug 05 2009 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2010.0
+ Revision: 410071
- rebuild using %%perl_convert_version

* Sat May 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2010.0
+ Revision: 373735
- update to new version 0.06

* Sat Jan 17 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.05-2mdv2009.1
+ Revision: 330437
- Rebuild for fixed package changelog.

* Fri Jan 16 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.05-1mdv2009.1
+ Revision: 330161
- Add missing BuildRequires for perl-Gtk2.
- Add missing BuildRequires for perl-Glib.
- Newx perl function breaks build with -Werror=format-security, if a fix
  is needed must be done in perl, while this doesn't happen fix build
  here by disabling Werror_cflags.
- Remove uneeded BuildArch tag.
- Import perl-Goo-Canvas package, made/sent by Ednilson Miura.


* Wed Jan 14 2009 Ednilson Miura <miura@mandriva.com> 0.05-1mdv2008.1
- First build
