
Name:		f23-kde-theme
Summary:        Fedora Twenty Three KDE Theme
Version:	23.0
Release:	1%{?dist}

License:	GPLv2+ and CC-BY-SA

# We are upstream for this package
URL:		https://fedorahosted.org/fedora-kde-artwork/
Source0:	https://fedorahosted.org/releases/f/e/fedora-kde-artwork/%{name}-%{version}.tar.bz2
BuildArch:	noarch

BuildRequires:	kde-filesystem
BuildRequires:  f23-backgrounds-kde
Requires:	kde-filesystem
Requires:	system-logos
Requires:	f23-backgrounds-kde

Provides:	f23-plasma-desktoptheme = %{version}-%{release}
Provides:	f23-plasma-theme = %{version}-%{release}

# replace it later for F24
%if 0%{?fedora} > 23
Provides:	system-kde-theme = %{version}-%{release}
Provides:	system-ksplash-theme = %{version}-%{release}
Provides:	systesm-plasma-desktoptheme = %{version}-%{release}
Provides:	system-plasma-theme = %{version}-%{release}
%endif

%if 0%{?fedora} == 23
Provides:	system-kde-theme = %{version}-%{release}
Provides:	system-ksplash-theme = %{version}-%{release}
Provides:	system-plasma-desktoptheme = %{version}-%{release}
Provides:	system-plasma-theme = %{version}-%{release}
%endif

%description
This is Fedora Twenty Three KDE Theme Artwork containing Plasma Workspaces theme.

%package -n f23-kdm-theme
Summary:	Fedora Twenty Three KDM Theme
Requires:       kde-filesystem
Requires:       system-logos
Requires:       f23-backgrounds-kde
Provides:       system-kdm-theme = %{version}-%{release}
%description -n f23-kdm-theme
This is Fedora Twenty Three KDE Theme Artwork containing KDM theme.


%prep
%setup -q

# copy wallpaper from f23-backgrounds-kde
rm -fv lookandfeel/contents/components/artwork/background.png
cp -a \
  %{_datadir}/wallpapers/F23/contents/images/1920x1080.png \
  lookandfeel/contents/components/artwork/background.png


%build


%install
### Look and feel
mkdir -p %{buildroot}%{_datadir}/plasma/look-and-feel/org.fedoraproject.fedora.twenty.three/
cp -rp lookandfeel/* %{buildroot}%{_datadir}/plasma/look-and-feel/org.fedoraproject.fedora.twenty.three/

### Plasma desktoptheme's
mkdir -p %{buildroot}%{_datadir}/plasma/desktoptheme/
cp -rp desktoptheme/F23/ %{buildroot}%{_datadir}/plasma/desktoptheme/

### KDM
mkdir -p %{buildroot}%{_kde4_appsdir}/kdm/themes/
cp -rp kdm/F23/ %{buildroot}%{_kde4_appsdir}/kdm/themes/
pushd %{buildroot}%{_kde4_appsdir}/kdm/themes/F23/
# system logo
ln -s ../../../../../pixmaps/system-logo-white.png system-logo-white.png
popd


%files
%doc README COPYING.CC-BY-SA COPYING.GPLv2
%{_datadir}/plasma/desktoptheme/F23/
%{_datadir}/plasma/look-and-feel/org.fedoraproject.fedora.twenty.three/

%files -n f23-kdm-theme
%{_kde4_appsdir}/kdm/themes/F23/


%changelog
* Thu Aug 06 2015 Rex Dieter <rdieter@fedoraproject.org> 23.0-1
- init f23-kde-theme

* Fri Jun 12 2015 Rex Dieter <rdieter@fedoraproject.org> 22.4-4
- f22-kde-theme.sh: org.fedoraproject.twentytwo.desktop

* Wed Jun 10 2015 Rex Dieter <rdieter@fedoraproject.org> 22.3-3
- disable verbose output

* Wed Jun 10 2015 Rex Dieter <rdieter@fedoraproject.org> 22.3-2
- handle org.fedoraproject.twentytwo => org.fedoraproject.fedora.twenty.two rename (#1228779)

* Tue May 19 2015 Jan Grulich <jgrulich@redhat.com> - 22.3-1
- Add fedora theme previews

* Tue May 19 2015 Jan Grulich <jgrulich@redhat.com> - 22.2-1
- Do not use symlinks, because Plasma doesn't allow to use them

* Fri May 15 2015 Jan Grulich <jgrulich@redhat.com> - 22.1-1
- Replace non-fedora themed parts by symlinks to breeze

* Wed May 13 2015 Jan Grulich <jgrulich@redhat.com> - 22.0-1
- Add KSplash and lockscreen fedora twenty two theme

* Mon Mar 09 2015 Rex Dieter <rdieter@fedoraproject.org> - 21.91-1.1
- (re)add Provides: system-ksplash-theme. easier to lie now than to re-add it later
- Provides: -plasma-theme,  for more consistent naming

* Tue Mar 03 2015 Than Ngo <than@redhat.com> 21.91-1
- drop unneeded ksplash theme

* Mon Mar 02 2015 Than Ngo <than@redhat.com> 21.90-1
- Initial package
