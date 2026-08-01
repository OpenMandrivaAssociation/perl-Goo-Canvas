%define upstream_name Goo-Canvas
%define upstream_version 0.06

# Newx calls Perl_croak_nocontext with a char * without "%s", may be
# valid or not but it isn't fixable here, keep this until perl is fixed 
%define Werror_cflags %nil


Name:		perl-%{upstream_name}
Version:	0.06
Release:	50
Summary:	Goo::Canvas Perl interface to the GooCanvas 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Goo-Canvas
Source0:	https://cpan.metacpan.org/authors/id/Y/YE/YEWENBIN/Goo-Canvas-0.06.tar.gz
BuildRequires:	make
Source1:	perl-Goo-Canvas.rpmlintrc

BuildRequires:	pkgconfig(goocanvas) 
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
%setup -q -n Goo-Canvas-0.06

# Public goocanvas headers omit still-exported pixbuf helpers used by XS.
# Inject prototypes before the include guard ends so types are in scope.
sed -i '/#endif \/\* _GOOCANVAS_PERL_H \*\//i\
/* wave12: prototypes missing from public goocanvas headers */\
cairo_surface_t *goo_canvas_cairo_surface_from_pixbuf (GdkPixbuf *pixbuf);\
cairo_pattern_t *goo_canvas_cairo_pattern_from_pixbuf (GdkPixbuf *pixbuf);\
' goocanvas-perl.h
# Also declare in the generated xs C file via a small header force-include
cat > goo-pixbuf-protos.h <<'EOH'
#ifndef GOO_PIXBUF_PROTOS_H
#define GOO_PIXBUF_PROTOS_H
#include <cairo.h>
#include <gdk-pixbuf/gdk-pixbuf.h>
cairo_surface_t *goo_canvas_cairo_surface_from_pixbuf (GdkPixbuf *pixbuf);
cairo_pattern_t *goo_canvas_cairo_pattern_from_pixbuf (GdkPixbuf *pixbuf);
#endif
EOH

%build
# clang defaults to erroring on implicit function decls; keep non-fatal as backup
export CFLAGS="%{optflags} -Wno-error=implicit-function-declaration -include $(pwd)/goo-pixbuf-protos.h"
export CXXFLAGS="$CFLAGS"
perl Makefile.PL INSTALLDIRS=vendor
%{__make} OPTIMIZE="$CFLAGS"

%check
make test || :

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


