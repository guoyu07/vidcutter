Name:           vidcutter
Version:        5.5.0
Release:        1
Summary:        the simplest + fastest video cutter & joiner
License:        GPL-3.0+
Group:          Productivity/Multimedia/Video/Editors and Convertors
Url:            https://vidcutter.ozmartians.com
Source0:        https://github.com/ozmartian/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  mpv-devel
BuildRequires:  update-desktop-files
Requires:       ffmpeg
Requires:       libmpv1
Requires:       mediainfo
Requires:       python3-qt5
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A modern, simple to use, constantly evolving and hella fast MEDIA CUTTER + JOINER
w/ frame-accurate SmartCut technology + Qt5, libmpv, FFmpeg and MediaInfo powering
the backend.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --root %{buildroot}

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc LICENSE README.md
%{_bindir}/%{name}
%{python3_sitearch}/%{name}-%{version}-py*.egg-info/
%{python3_sitearch}/%{name}/
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/22x22/apps/%{name}.png
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/com.ozmartians.%{name}.desktop
%{_datadir}/appdata/
%{_datadir}/appdata/com.ozmartians.%{name}.appdata.xml
%{_datadir}/metainfo/
%{_datadir}/metainfo/com.ozmartians.%{name}.appdata.xml
%{_datadir}/mime/packages/x-%{name}.xml
%{_datadir}/pixmaps/%{name}.svg

%changelog
