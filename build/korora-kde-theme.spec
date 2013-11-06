%global backgrounds_kde_version 19.90.0

Name:		korora-kde-theme
Version:	19.90.5
Release:	1%{?dist}.1
Summary:	Korora KDE Theme

License:	GPLv2+ and CC-BY-SA

# We are upstream for this package
URL:		https://fedorahosted.org/fedora-kde-artwork/
Source0:	%{name}-%{version}.tar.gz
Patch0: korora-kde-theme.patch
BuildArch:	noarch
BuildRequires:	kde-filesystem
Requires:	kde-filesystem
Requires:	system-logos
Requires:	korora-backgrounds-kde >= %{backgrounds_kde_version}

Provides:	heisenbug-kdm-theme
Provides:	heisenbug-ksplash-theme
Provides:	heisenbug-plasma-desktoptheme
Provides:	heisenbug-kde-theme

Obsoletes:	heisenbug-kdm-theme
Obsoletes:	heisenbug-ksplash-theme
Obsoletes:	heisenbug-plasma-desktoptheme
Obsoletes:	heisenbug-kde-theme

# replace it later for F20
%if 0%{?fedora} > 20
Provides:	system-kde-theme = %{version}-%{release}
Provides:	system-kdm-theme = %{version}-%{release}
Provides:	system-ksplash-theme = %{version}-%{release}
Provides:	system-plasma-desktoptheme = %{version}-%{release}
%endif

%if 0%{?fedora} == 20
Provides:	system-kde-theme = %{version}-%{release}
Provides:	system-kdm-theme = %{version}-%{release}
Provides:	system-ksplash-theme = %{version}-%{release}
Provides:	system-plasma-desktoptheme = %{version}-%{release}
%endif

%description
This is Korora's KDE Theme Artwork containing KDM theme,
KSplash theme and Plasma Workspaces theme.


%prep
%setup -q
%patch0 -p1


%build
# blank

%install
rm -rf %{buildroot}

### Plasma desktoptheme's
mkdir -p %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/Heisenbug/ %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/Heisenbug-netbook/ %{buildroot}%{_kde4_appsdir}/desktoptheme/
# the branding image branding.svgz is still missing in fedora-logos
# we should add it in next fedora release
# pushd {buildroot}{_kde4_appsdir}/desktoptheme/widgets/
# ln -s ../../../../../../pixmaps/branding.svgz branding.svgz
# popd

### KDM
mkdir -p %{buildroot}%{_kde4_appsdir}/kdm/themes/
cp -rp kdm/Heisenbug/ %{buildroot}%{_kde4_appsdir}/kdm/themes/
pushd %{buildroot}%{_kde4_appsdir}/kdm/themes/Heisenbug/
# system logo
ln -s ../../../../../pixmaps/system-logo-white.png system-logo-white.png
popd

## KSplash
mkdir -p %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
cp -rp ksplash/Heisenbug/ %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
ln -s ../../../../../../backgrounds/heisenbug/default/standard/heisenbug.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Heisenbug/2048x1536/
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Heisenbug/1920x1200/
ln -s ../../../../../../backgrounds/heisenbug/default/wide/heisenbug.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Heisenbug/1920x1200/Heisenbug.png
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Heisenbug/1280x1024/
ln -s ../../../../../../backgrounds/heisenbug/default/normalish/heisenbug.png \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Heisenbug/1280x1024/Heisenbug.png
 
# system logo 
ln -s ../../../../../../pixmaps/system-logo-white.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/Heisenbug/2048x1536/logo.png

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README COPYING.CC-BY-SA COPYING.GPLv2
%{_kde4_appsdir}/desktoptheme/Heisenbug/
%{_kde4_appsdir}/desktoptheme/Heisenbug-netbook/
%{_kde4_appsdir}/kdm/themes/Heisenbug/
%{_kde4_appsdir}/ksplash/Themes/Heisenbug/

%changelog
* Wed Oct 16 2013 Rex Dieter <rdieter@fedoraproject.org> 19.90.5-1
- drop sddm theme (moved to sddm packaging)

* Tue Sep 10 2013 Martin Briza <mbriza@redhat.com> 19.90.4-1
- Fedora-brand the KDE theme, set it to username entry instead of user list (#1007065)

* Tue Sep 10 2013 Martin Briza <mbriza@redhat.com> 19.90.3-1
- fix the symlink to SDDM theme's background
- fix the screenshots
- fixed the wallpaper name in the KDM theme
- stopped linking the font in the SDDM theme'

* Tue Sep 10 2013 Jaroslav Reznik <jreznik@redhat.com> 19.90.2-1
- fix png suffix and version for desktop theme

* Mon Sep 09 2013 Jaroslav Reznik <jreznik@redhat.com> 19.90.1-1
- fix backgrounds suffix to match heisenbug-backgrounds
- fix screenshots

* Mon Sep 09 2013 Martin Briza <mbriza@redhat.com> 19.90.0-1
- initial package

