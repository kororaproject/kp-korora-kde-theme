%global backgrounds-kde-version 17.91.0

Name:		korora-kde-theme
Version:	17.91.1
Release:	1%{?dist}
Summary:	Korora KDE Theme

Group:		User Interface/Desktops
License:	GPLv2+ and CC-BY-SA

URL:		https://kororaproject.org
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch
BuildRequires:	kde-filesystem
Requires:	kde-filesystem
Requires:	system-logos
Requires:	spherical-cow-backgrounds-kde >= %{backgrounds-kde-version}

Provides:	spherical-cow-kdm-theme
Provides:	spherical-cow-ksplash-theme
Provides:	spherical-cow-plasma-desktoptheme
Provides:	spherical-cow-kde-theme

Obsoletes:	spherical-cow-kdm-theme
Obsoletes:	spherical-cow-ksplash-theme
Obsoletes:	spherical-cow-plasma-desktoptheme
Obsoletes:	spherical-cow-kde-theme

# replace it later for F19
%if 0%{?fedora} > 18
Provides:	system-kde-theme = %{version}-%{release}
Provides:	system-kdm-theme = %{version}-%{release}
Provides:	system-ksplash-theme = %{version}-%{release}
Provides:	system-plasma-desktoptheme = %{version}-%{release}
%endif

%if 0%{?fedora} == 18
Provides:	system-kde-theme = %{version}-%{release}
Provides:	system-kdm-theme = %{version}-%{release}
Provides:	system-ksplash-theme = %{version}-%{release}
Provides:	system-plasma-desktoptheme = %{version}-%{release}
%endif

%description
This is Korora KDE Theme Artwork containing KDM theme,
KSplash theme and Plasma Workspaces theme.


%prep
%setup -q


%build
# blank

%install
rm -rf %{buildroot}

### Plasma desktoptheme's
mkdir -p %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/Spherical_Cow/ %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/Spherical_Cow-netbook/ %{buildroot}%{_kde4_appsdir}/desktoptheme/
# the branding image branding.svgz is still missing in fedora-logos
# we should add it in next fedora release
# pushd %{buildroot}%{_kde4_appsdir}/desktoptheme/widgets/
# ln -s ../../../../../../pixmaps/branding.svgz branding.svgz
# popd

### KDM
mkdir -p %{buildroot}%{_kde4_appsdir}/kdm/themes/
cp -rp kdm/SphericalCow/ %{buildroot}%{_kde4_appsdir}/kdm/themes/
pushd %{buildroot}%{_kde4_appsdir}/kdm/themes/SphericalCow/
# system logo
ln -s ../../../../../pixmaps/system-logo-white.png system-logo-white.png
popd

## KSplash
mkdir -p %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
cp -rp ksplash/SphericalCow/ %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
ln -s ../../../../../../backgrounds/spherical-cow/default/standard/spherical-cow.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SphericalCow/2048x1536/
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SphericalCow/1920x1200/
ln -s ../../../../../../backgrounds/spherical-cow/default/wide/spherical-cow.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SphericalCow/1920x1200/Spherical_Cow.png
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SphericalCow/1280x1024/
ln -s ../../../../../../backgrounds/spherical-cow/default/normalish/spherical-cow.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SphericalCow/1280x1024/Spherical_Cow.png
 
# system logo 
ln -s ../../../../../../pixmaps/system-logo-white.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SphericalCow/2048x1536/logo.png

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README COPYING.CC-BY-SA COPYING.GPLv2
%{_kde4_appsdir}/desktoptheme/Spherical_Cow/
%{_kde4_appsdir}/desktoptheme/Spherical_Cow-netbook/
%{_kde4_appsdir}/kdm/themes/SphericalCow/
%{_kde4_appsdir}/ksplash/Themes/SphericalCow/

%changelog
* Mon Aug 20 2012 Martin Briza <mbriza@redhat.com> 17.91.1-1
- Fixed symlink locations
- Added a proper screenshot

* Wed Aug 15 2012 Martin Briza <mbriza@redhat.com> 17.91.0-1
- initial package
