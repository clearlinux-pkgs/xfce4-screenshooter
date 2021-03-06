#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xfce4-screenshooter
Version  : 1.9.9
Release  : 23
URL      : https://archive.xfce.org/src/apps/xfce4-screenshooter/1.9/xfce4-screenshooter-1.9.9.tar.bz2
Source0  : https://archive.xfce.org/src/apps/xfce4-screenshooter/1.9/xfce4-screenshooter-1.9.9.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: xfce4-screenshooter-bin = %{version}-%{release}
Requires: xfce4-screenshooter-data = %{version}-%{release}
Requires: xfce4-screenshooter-lib = %{version}-%{release}
Requires: xfce4-screenshooter-license = %{version}-%{release}
Requires: xfce4-screenshooter-locales = %{version}-%{release}
Requires: xfce4-screenshooter-man = %{version}-%{release}
BuildRequires : help2man
BuildRequires : intltool
BuildRequires : pkgconfig(exo-2)
BuildRequires : pkgconfig(gdk-3.0)
BuildRequires : pkgconfig(gdk-x11-3.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(libxfce4panel-2.0)
BuildRequires : pkgconfig(libxfce4ui-2)
BuildRequires : pkgconfig(libxfce4util-1.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(pango)
BuildRequires : pkgconfig(xext)

%description
[![License](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://gitlab.xfce.org/apps/xfce4-screenshooter/-/blob/master/COPYING)

%package bin
Summary: bin components for the xfce4-screenshooter package.
Group: Binaries
Requires: xfce4-screenshooter-data = %{version}-%{release}
Requires: xfce4-screenshooter-license = %{version}-%{release}

%description bin
bin components for the xfce4-screenshooter package.


%package data
Summary: data components for the xfce4-screenshooter package.
Group: Data

%description data
data components for the xfce4-screenshooter package.


%package lib
Summary: lib components for the xfce4-screenshooter package.
Group: Libraries
Requires: xfce4-screenshooter-data = %{version}-%{release}
Requires: xfce4-screenshooter-license = %{version}-%{release}

%description lib
lib components for the xfce4-screenshooter package.


%package license
Summary: license components for the xfce4-screenshooter package.
Group: Default

%description license
license components for the xfce4-screenshooter package.


%package locales
Summary: locales components for the xfce4-screenshooter package.
Group: Default

%description locales
locales components for the xfce4-screenshooter package.


%package man
Summary: man components for the xfce4-screenshooter package.
Group: Default

%description man
man components for the xfce4-screenshooter package.


%prep
%setup -q -n xfce4-screenshooter-1.9.9
cd %{_builddir}/xfce4-screenshooter-1.9.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1621439592
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1621439592
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xfce4-screenshooter
cp %{_builddir}/xfce4-screenshooter-1.9.9/COPYING %{buildroot}/usr/share/package-licenses/xfce4-screenshooter/73ccddd0c27b4492f8182c35f0f7c434b998757c
%make_install
%find_lang xfce4-screenshooter

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xfce4-screenshooter

%files data
%defattr(-,root,root,-)
/usr/share/applications/xfce4-screenshooter.desktop
/usr/share/icons/hicolor/128x128/apps/org.xfce.screenshooter.png
/usr/share/icons/hicolor/16x16/apps/org.xfce.screenshooter.png
/usr/share/icons/hicolor/24x24/apps/org.xfce.screenshooter.png
/usr/share/icons/hicolor/32x32/apps/org.xfce.screenshooter.png
/usr/share/icons/hicolor/48x48/apps/org.xfce.screenshooter.png
/usr/share/icons/hicolor/scalable/apps/org.xfce.screenshooter.svg
/usr/share/metainfo/xfce4-screenshooter.appdata.xml
/usr/share/xfce4/panel/plugins/screenshooter.desktop

%files lib
%defattr(-,root,root,-)
/usr/lib64/xfce4/panel/plugins/libscreenshooterplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xfce4-screenshooter/73ccddd0c27b4492f8182c35f0f7c434b998757c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xfce4-screenshooter.1

%files locales -f xfce4-screenshooter.lang
%defattr(-,root,root,-)

