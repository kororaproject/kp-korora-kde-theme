%global backgrounds_kde_version 18.91.0

Name:		korora-kde-theme
Version:	18.91.5
Release:	1%{?dist}
Summary:	Korora KDE Theme

License:	GPLv2+ and CC-BY-SA

# We are upstream for this package
URL:		https://fedorahosted.org/fedora-kde-artwork/
Source0:	https://fedorahosted.org/releases/f/e/fedora-kde-artwork/schroedinger-cat-kde-theme-%{version}.tar.bz2
Patch0: korora-kde-theme.patch
BuildArch:	noarch
BuildRequires:	kde-filesystem
Requires:	kde-filesystem
Requires:	system-logos
Requires:	korora-backgrounds-kde >= %{backgrounds_kde_version}

Provides:  schroedinger-cat-kdm-theme
Provides:  schroedinger-cat-ksplash-theme
Provides:  schroedinger-cat-plasma-desktoptheme
Provides:  schroedinger-cat-kde-theme

Obsoletes: schroedinger-cat-kdm-theme
Obsoletes: schroedinger-cat-ksplash-theme
Obsoletes: schroedinger-cat-plasma-desktoptheme
Obsoletes: schroedinger-cat-kde-theme


# replace it later for F20
%if 0%{?fedora} > 19
Provides:	system-kde-theme = %{version}-%{release}
Provides:	system-kdm-theme = %{version}-%{release}
Provides:	system-ksplash-theme = %{version}-%{release}
Provides:	system-plasma-desktoptheme = %{version}-%{release}
%endif

%if 0%{?fedora} == 19
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
cp -rp desktoptheme/Schroedinger_Cat/ %{buildroot}%{_kde4_appsdir}/desktoptheme/
cp -rp desktoptheme/Schroedinger_Cat-netbook/ %{buildroot}%{_kde4_appsdir}/desktoptheme/
# the branding image branding.svgz is still missing in fedora-logos
# we should add it in next fedora release
# pushd {buildroot}{_kde4_appsdir}/desktoptheme/widgets/
# ln -s ../../../../../../pixmaps/branding.svgz branding.svgz
# popd

### KDM
mkdir -p %{buildroot}%{_kde4_appsdir}/kdm/themes/
cp -rp kdm/SchroedingerCat/ %{buildroot}%{_kde4_appsdir}/kdm/themes/
pushd %{buildroot}%{_kde4_appsdir}/kdm/themes/SchroedingerCat/
# system logo
ln -s ../../../../../pixmaps/system-logo-white.png system-logo-white.png
popd

## KSplash
mkdir -p %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
cp -rp ksplash/SchroedingerCat/ %{buildroot}%{_kde4_appsdir}/ksplash/Themes/
ln -s ../../../../../../backgrounds/schroedinger-cat/default/standard/schroedinger-cat.jpg \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SchroedingerCat/2048x1536/
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SchroedingerCat/1920x1200/
ln -s ../../../../../../backgrounds/schroedinger-cat/default/wide/schroedinger-cat.jpg \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SchroedingerCat/1920x1200/Schroedinger_Cat.jpg
mkdir %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SchroedingerCat/1280x1024/
ln -s ../../../../../../backgrounds/schroedinger-cat/default/normalish/schroedinger-cat.jpg \
  %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SchroedingerCat/1280x1024/Schroedinger_Cat.jpg
 
# system logo 
ln -s ../../../../../../pixmaps/system-logo-white.png %{buildroot}%{_kde4_appsdir}/ksplash/Themes/SchroedingerCat/2048x1536/logo.png

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README COPYING.CC-BY-SA COPYING.GPLv2
%{_kde4_appsdir}/desktoptheme/Schroedinger_Cat/
%{_kde4_appsdir}/desktoptheme/Schroedinger_Cat-netbook/
%{_kde4_appsdir}/kdm/themes/SchroedingerCat/
%{_kde4_appsdir}/ksplash/Themes/SchroedingerCat/

%changelog
* Wed Apr 03 2013 Martin Briza <mbriza@redhat.com> 18.91.5-1
- fixed default wallpaper file suffix

* Thu Mar 28 2013 Martin Briza <mbriza@redhat.com> 18.91.4-1
- removed unneeded sections from the spec
- fixed version dependency on backgrounds_kde

* Thu Mar 28 2013 Martin Briza <mbriza@redhat.com> 18.91.3-1
- fixed an undefined macro warning from rpmlint

* Thu Mar 28 2013 Martin Briza <mbriza@redhat.com> 18.91.2-1
- fixed the ksplash preview

* Wed Mar 27 2013 Martin Briza <mbriza@redhat.com> 18.91.1-1
- fixed the preview screenshots

* Wed Mar 27 2013 Martin Briza <mbriza@redhat.com> 18.91.0-1
- initial package
