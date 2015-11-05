Name:		korora-kde-theme
Version:	23.0
Release:	4%{?dist}.1
Summary:	Korora KDE Theme

License:	GPLv2+ and CC-BY-SA

# We are upstream for this package
URL:		https://fedorahosted.org/fedora-kde-artwork/
Source0:	%{name}-%{version}.tar.gz
Patch0:		korora-kde-theme.patch
BuildArch:	noarch

BuildRequires:	kde-filesystem
BuildRequires: korora-backgrounds-extras-base
Requires:	kde-filesystem
Requires:	system-logos
Requires:	korora-backgrounds-extras-kde

Provides:      f23-plasma-desktoptheme
Obsoletes:     f23-plasma-desktoptheme
Provides:      f23-plasma-theme
Obsoletes:     f23-plasma-theme
Provides:      f22-kde-theme
Obsoletes:     f22-kde-theme

Provides:       korora-plasma-desktoptheme = %{version}-%{release}
Provides:       korora-plasma-theme = %{version}-%{release}
Provides:       korora-kdm-theme = %{version}-%{release}

# replace it later for F24
%if 0%{?fedora} > 23
Provides:      system-kde-theme = %{version}-%{release}
Provides:      system-ksplash-theme = %{version}-%{release}
Provides:      system-plasma-desktoptheme = %{version}-%{release}
Provides:      system-plasma-theme = %{version}-%{release}
%endif

%if 0%{?fedora} == 23
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

rm -fv lookandfeel/contents/components/artwork/background.png
# link wallpaper from f23-backgrounds-kde
#ln -sf ../../../../../../wallpapers/F23/contents/images/1920x1080.png \
# copy wallpaper from f23-backgrounds-kde
cp --dereference -v \
   %{_datadir}/backgrounds/korora/extras/cairn-at-quoddy.png \
   lookandfeel/contents/components/artwork/background.png


%build


%install
### Look and feel
mkdir -p %{buildroot}%{_datadir}/plasma/look-and-feel/org.kororaproject.korora/
cp -rp lookandfeel/* %{buildroot}%{_datadir}/plasma/look-and-feel/org.kororaproject.korora/


### Plasma desktoptheme's
mkdir -p %{buildroot}%{_datadir}/plasma/desktoptheme/
cp -rp desktoptheme/Korora/ %{buildroot}%{_datadir}/plasma/desktoptheme/

### KDM
mkdir -p %{buildroot}%{_kde4_appsdir}/kdm/themes/
cp -rp kdm/Korora/ %{buildroot}%{_kde4_appsdir}/kdm/themes/
pushd %{buildroot}%{_kde4_appsdir}/kdm/themes/Korora/
# system logo
ln -s ../../../../../pixmaps/system-logo-white.png system-logo-white.png
popd


%files
%doc README
%license COPYING.CC-BY-SA
%license COPYING.GPLv2

%{_datadir}/plasma/desktoptheme/Korora/
%{_datadir}/plasma/look-and-feel/org.kororaproject.korora/

%files -n korora-kdm-theme
%doc README
%license COPYING.CC-BY-SA
%license COPYING.GPLv2
%{_kde4_appsdir}/kdm/themes/Korora


%changelog
* Thu Nov 5 2015 Chris Smart <csmart@kororaproject.org> 23.0-4
- Provide and obsolete f23-kde-theme

* Wed Jul 29 2015 Chris Smart <csmart@kororaproject.org> 22.0-2
- Provide and obsolete f22-kde-theme

* Mon Jul 20 2015 Ian Firns <firnsy@kororaproject.org> 22.0-1
- Updated to latest upstream

* Sat Dec 27 2014 Chris Smart <csmart@kororaproject.org> 21.0-1
- Update to upstream

* Sat Nov 9 2013 Chris Smart <csmart@kororaproject.org> 19.90.5-1
- Initial package
