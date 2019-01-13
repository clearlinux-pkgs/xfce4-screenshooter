#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xfce4-screenshooter
Version  : 1.9.3
Release  : 12
URL      : http://archive.xfce.org/src/apps/xfce4-screenshooter/1.9/xfce4-screenshooter-1.9.3.tar.bz2
Source0  : http://archive.xfce.org/src/apps/xfce4-screenshooter/1.9/xfce4-screenshooter-1.9.3.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: xfce4-screenshooter-bin = %{version}-%{release}
Requires: xfce4-screenshooter-data = %{version}-%{release}
Requires: xfce4-screenshooter-lib = %{version}-%{release}
Requires: xfce4-screenshooter-license = %{version}-%{release}
Requires: xfce4-screenshooter-locales = %{version}-%{release}
Requires: xfce4-screenshooter-man = %{version}-%{release}
BuildRequires : intltool
BuildRequires : libX11-dev
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
it using another application, or host it on imgur.com,
a free online image hosting service.

%package bin
Summary: bin components for the xfce4-screenshooter package.
Group: Binaries
Requires: xfce4-screenshooter-data = %{version}-%{release}
Requires: xfce4-screenshooter-license = %{version}-%{release}
Requires: xfce4-screenshooter-man = %{version}-%{release}

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
%setup -q -n xfce4-screenshooter-1.9.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542223953
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1542223953
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xfce4-screenshooter
cp COPYING %{buildroot}/usr/share/package-licenses/xfce4-screenshooter/COPYING
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

%files lib
%defattr(-,root,root,-)
/usr/lib64/xfce4/panel/plugins/libscreenshooterplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xfce4-screenshooter/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/xfce4-screenshooter.1

%files locales -f xfce4-screenshooter.lang
%defattr(-,root,root,-)

