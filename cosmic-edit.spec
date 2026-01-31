Name:           cosmic-edit
Version:        0.1.0
Release:        1%{?dist}
Summary:        COSMIC text editor
License:        GPLv3
URL:            https://github.com/pop-os/cosmic-edit
Source0:        %{name}-%{version}.tar.gz

# DebianのBuild-Dependsに対応するRPMの依存
BuildRequires:  just
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  git
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  gcc-c++

%description
COSMIC Edit is a multi-window text editor for the COSMIC Desktop Environment, 
built using the iced GUI library and the cosmic-text shaping engine.

%prep
%setup -q

%build
# Debianのdh_auto_build相当
just build-vendored

%install
# Debianのdh_auto_install相当
just rootdir=%{buildroot} install

%files
%{_bindir}/cosmic-edit
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/metainfo/*.xml

%changelog
* Sat Jan 31 2026 Your Name <you@example.com> - 0.1.0-1
- Initial RPM build using just and AlmaLinux 9
