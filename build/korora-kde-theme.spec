Name:		korora-kde-theme
Version:	22
Release:	1%{?dist}.1
Summary:	Korora KDE Theme

License:	GPLv2+ and CC-BY-SA

# We are upstream for this package
URL:		https://fedorahosted.org/fedora-kde-artwork/
Source0:	%{name}-%{version}.tar.gz
Patch0:		korora-kde-theme.patch
BuildArch:	noarch

BuildRequires:	kde-filesystem
Requires:	kde-filesystem
Requires:	system-logos
Requires:	korora-backgrounds-kde >= 21.91

Provides:       korora-plasma-desktoptheme = %{version}-%{release}
Provides:       korora-plasma-theme = %{version}-%{release}
Provides:       korora-kdm-theme = %{version}-%{release}

# replace it later for F22
%if 0%{?fedora} > 22
Provides:       system-kde-theme = %{version}-%{release}
Provides:       system-ksplash-theme = %{version}-%{release}
Provides:       system-plasma-desktoptheme = %{version}-%{release}
Provides:       system-plasma-theme = %{version}-%{release}
%endif

%if 0%{?fedora} == 22
Provides:       system-kde-theme = %{version}-%{release}
Provides:       system-ksplash-theme = %{version}-%{release}
Provides:       system-plasma-desktoptheme = %{version}-%{release}
Provides:       system-plasma-theme = %{version}-%{release}
%endif

%description
This is Korora's KDE Theme Artwork containing KDM theme.

%package -n korora-kdm-theme
Summary:	      Korora KDM Theme
Requires:       kde-filesystem
Requires:       system-logos
Requires:       korora-backgrounds-kde >= 21.91
Provides:       system-kdm-theme = %{version}-%{release}

%description -n korora-kdm-theme
This is the Korora Artwork containing KDM theme.

%prep
%setup -q
#%patch0 -p1

%build

%install
### Look and feel
mkdir -p %{buildroot}%{_datadir}/plasma/look-and-feel/org.kororaproject.korora.22/
cp -rp lookandfeel/* %{buildroot}%{_datadir}/plasma/look-and-feel/org.fedoraproject.fedora.twenty.two/


### Plasma desktoptheme's
mkdir -p %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/Korora/ %{buildroot}%{_kde4_appsdir}/desktoptheme/

### KDM
mkdir -p %{buildroot}%{_kde4_appsdir}/kdm/themes/
cp -rp kdm/Korora/ %{buildroot}%{_kde4_appsdir}/kdm/themes/
pushd %{buildroot}%{_kde4_appsdir}/kdm/themes/Korora/
# system logo
ln -s ../../../../../pixmaps/system-logo-white.png system-logo-white.png
popd


%files
%doc README COPYING.CC-BY-SA COPYING.GPLv2
%{_datadir}/kconf_update/korora-kde-theme.upd
%{_sysconfdir}/xdg/plasma-workspace/env/korora-kde-theme.sh
%{_sysconfdir}/xdg/plasma-workspace/shutdown/korora-kde-theme.sh
%{_datadir}/plasma/desktoptheme/Korora/
%{_datadir}/plasma/look-and-feel/org.fedoraproject.korora.22/

%files -n korora-kdm-theme
%{_kde4_appsdir}/kdm/themes/Korora


%changelog
* Mon Jul 20 2015 Ian Firns <firnsy@kororaproject.org> 22.0-1
- Updated to latest upstream

* Sat Dec 27 2014 Chris Smart <csmart@kororaproject.org> 21.0-1
- Update to upstream

* Sat Nov 9 2013 Chris Smart <csmart@kororaproject.org> 19.90.5-1
- Initial package
