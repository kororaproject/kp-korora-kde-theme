%global backgrounds_kde_version 21.0

Name:		korora-kde-theme
Version:	%{backgrounds_kde_version}
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
Requires:	korora-backgrounds-kde >= %{backgrounds_kde_version}

Provides:       korora-kdm-theme = %{version}-%{release}
Provides:       korora-ksplash-theme = %{version}-%{release}
Provides:       korora-plasma-desktoptheme = %{version}-%{release}

# replace it later for F22
# replace it later for F22
%if 0%{?fedora} > 21
Provides:       system-kde-theme = %{version}-%{release}
Provides:       system-kdm-theme = %{version}-%{release}
Provides:       system-ksplash-theme = %{version}-%{release}
Provides:       system-plasma-desktoptheme = %{version}-%{release}
%endif

%if 0%{?fedora} == 21
Provides:       system-kde-theme = %{version}-%{release}
Provides:       system-kdm-theme = %{version}-%{release}
Provides:       system-ksplash-theme = %{version}-%{release}
Provides:       system-plasma-desktoptheme = %{version}-%{release}
%endif

%description
This is Korora's KDE Theme Artwork containing KDM theme,
KSplash theme and Plasma Workspaces theme.


%prep
%setup -q
#%patch0 -p1


%build
# blank

%install
rm -rf %{buildroot}

### Plasma desktoptheme's
mkdir -p %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/Korora/ %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/Korora-netbook/ %{buildroot}%{_kde4_appsdir}/desktoptheme/
# the branding image branding.svgz is still missing in fedora-logos
# we should add it in next fedora release
# pushd {buildroot}{_kde4_appsdir}/desktoptheme/widgets/
# ln -s ../../../../../../pixmaps/branding.svgz branding.svgz
# popd

### KDM
mkdir -p %{buildroot}%{_kde4_appsdir}/kdm/themes/
cp -rp kdm/Korora/ %{buildroot}%{_kde4_appsdir}/kdm/themes/
pushd %{buildroot}%{_kde4_appsdir}/kdm/themes/Korora/
# system logo
ln -s ../../../../../pixmaps/system-logo-white.png system-logo-white.png
popd

## KSplash
mkdir -p %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
cp -rp ksplash/Korora/ %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
ln -s ../../../../../../backgrounds/korora/default/standard/korora.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Korora/2048x1536/
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Korora/1920x1200/
ln -s ../../../../../../backgrounds/korora/default/wide/korora.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Korora/1920x1200/korora.png
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Korora/1280x1024/
ln -s ../../../../../../backgrounds/Korora/default/normalish/korora.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Korora/1280x1024/korora.png
 
# system logo 
ln -s ../../../../../../pixmaps/system-logo-white.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Korora/2048x1536/logo.png

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README COPYING.CC-BY-SA COPYING.GPLv2
%{_kde4_appsdir}/desktoptheme/Korora/
%{_kde4_appsdir}/desktoptheme/Korora-netbook/
%{_kde4_appsdir}/kdm/themes/Korora/
%{_kde4_appsdir}/ksplash/Themes/Korora/

%changelog
* Sat Dec 27 2014 Chris Smart <csmart@kororaproject.org> 21.0-1
- Update to upstream

* Sat Nov 9 2013 Chris Smart <csmart@kororaproject.org> 19.90.5-1
- Initial package
