
Name:		f21-kde-theme
Summary:        Fedora Twenty One KDE Theme
Version:	20.90
Release:	1%{?dist}

License:	GPLv2+ and CC-BY-SA

# We are upstream for this package
URL:		https://fedorahosted.org/fedora-kde-artwork/
Source0:	https://fedorahosted.org/releases/f/e/fedora-kde-artwork/%{name}-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	kde-filesystem
Requires:	kde-filesystem
Requires:	system-logos
Requires:	f21-backgrounds-kde >= 20.91

Provides:	f21-kdm-theme = %{version}-%{release}
Provides:	f21-ksplash-theme = %{version}-%{release}
Provides:	f21-plasma-desktoptheme = %{version}-%{release}

# replace it later for F22
%if 0%{?fedora} > 21
Provides:	system-kde-theme = %{version}-%{release}
Provides:	system-kdm-theme = %{version}-%{release}
Provides:	system-ksplash-theme = %{version}-%{release}
Provides:	system-plasma-desktoptheme = %{version}-%{release}
%endif

%if 0%{?fedora} == 21
Provides:	system-kde-theme = %{version}-%{release}
Provides:	system-kdm-theme = %{version}-%{release}
Provides:	system-ksplash-theme = %{version}-%{release}
Provides:	system-plasma-desktoptheme = %{version}-%{release}
%endif

%description
This is Fedora Twenty One KDE Theme Artwork containing KDM theme,
KSplash theme and Plasma Workspaces theme.


%prep
%setup -q


%build
# blank

%install
### Plasma desktoptheme's
mkdir -p %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/F21/ %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/F21-netbook/ %{buildroot}%{_kde4_appsdir}/desktoptheme/
# the branding image branding.svgz is still missing in fedora-logos
# we should add it in next fedora release
# pushd {buildroot}{_kde4_appsdir}/desktoptheme/widgets/
# ln -s ../../../../../../pixmaps/branding.svgz branding.svgz
# popd

### KDM
mkdir -p %{buildroot}%{_kde4_appsdir}/kdm/themes/
cp -rp kdm/F21/ %{buildroot}%{_kde4_appsdir}/kdm/themes/
pushd %{buildroot}%{_kde4_appsdir}/kdm/themes/F21/
# system logo
ln -s ../../../../../pixmaps/system-logo-white.png system-logo-white.png
popd

## KSplash
mkdir -p %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
cp -rp ksplash/F21/ %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
ln -s ../../../../../../backgrounds/f21/default/standard/f21.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/F21/2048x1536/F21.png
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/F21/1920x1200/
ln -s ../../../../../../backgrounds/f21/default/wide/f21.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/F21/1920x1200/f21.png
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/F21/1280x1024/
ln -s ../../../../../../backgrounds/F21/default/normalish/f21.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/F21/1280x1024/f21.png
# system logo 
ln -s ../../../../../../pixmaps/system-logo-white.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/F21/2048x1536/logo.png


%files
%doc README COPYING.CC-BY-SA COPYING.GPLv2
%{_kde4_appsdir}/desktoptheme/F21/
%{_kde4_appsdir}/desktoptheme/F21-netbook/
%{_kde4_appsdir}/kdm/themes/F21/
%{_kde4_appsdir}/ksplash/Themes/F21/

%changelog
* Tue Sep 02 2014 Rex Dieter <rdieter@fedoraproject.org> 20.90-1
- Initial package
