#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xfce4-screenshooter
Version  : 1.9.1
Release  : 7
URL      : http://archive.xfce.org/src/apps/xfce4-screenshooter/1.9/xfce4-screenshooter-1.9.1.tar.bz2
Source0  : http://archive.xfce.org/src/apps/xfce4-screenshooter/1.9/xfce4-screenshooter-1.9.1.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: xfce4-screenshooter-bin
Requires: xfce4-screenshooter-lib
Requires: xfce4-screenshooter-data
Requires: xfce4-screenshooter-locales
Requires: xfce4-screenshooter-doc
BuildRequires : intltool
BuildRequires : pkgconfig(exo-1)
BuildRequires : pkgconfig(exo-2)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(libxfce4panel-1.0)
BuildRequires : pkgconfig(libxfce4panel-2.0)
BuildRequires : pkgconfig(libxfce4ui-1)
BuildRequires : pkgconfig(libxfce4ui-2)
BuildRequires : pkgconfig(libxfce4util-1.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xext)

%description
This application allows you to capture the entire screen, the active
window or a selected region. You can set the delay that elapses
before the screenshot is taken and the action that will be done with
the screenshot: save it to a PNG file, copy it to the clipboard, open
it using another application, or host it on ZimageZ or imgur.com,
some free online image hosting service.

%package bin
Summary: bin components for the xfce4-screenshooter package.
Group: Binaries
Requires: xfce4-screenshooter-data

%description bin
bin components for the xfce4-screenshooter package.


%package data
Summary: data components for the xfce4-screenshooter package.
Group: Data

%description data
data components for the xfce4-screenshooter package.


%package doc
Summary: doc components for the xfce4-screenshooter package.
Group: Documentation

%description doc
doc components for the xfce4-screenshooter package.


%package lib
Summary: lib components for the xfce4-screenshooter package.
Group: Libraries
Requires: xfce4-screenshooter-data

%description lib
lib components for the xfce4-screenshooter package.


%package locales
Summary: locales components for the xfce4-screenshooter package.
Group: Default

%description locales
locales components for the xfce4-screenshooter package.


%prep
%setup -q -n xfce4-screenshooter-1.9.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1498699657
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1498699657
rm -rf %{buildroot}
%make_install
%find_lang xfce4-screenshooter

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xfce4-screenshooter

%files data
%defattr(-,root,root,-)
/usr/share/appdata/xfce4-screenshooter.appdata.xml
/usr/share/applications/xfce4-screenshooter.desktop
/usr/share/icons/hicolor/48x48/apps/applets-screenshooter.png
/usr/share/icons/hicolor/scalable/apps/applets-screenshooter.svg
/usr/share/xfce4/panel/plugins/screenshooter.desktop

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/xfce4/panel/plugins/libscreenshooterplugin.so

%files locales -f xfce4-screenshooter.lang
%defattr(-,root,root,-)

