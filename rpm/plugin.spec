Summary: Qt Platform Input Contexts for Maliit keyboard
Name: opt-qt5-sfos-maliit-platforminputcontext
Version: 1.0.0
Release: 1%{?dist}

License: LGPLv2
Url:     https://github.com/sailfishos-flatpak/maliit-framework
Source0: %{name}-%{version}.tar.bz2

# filter plugin provides
%global __provides_exclude_from ^%{_opt_qt5_plugindir}/platforminputcontexts/.*\\.so$
%{?opt_qt5_default_filter}

BuildRequires: make
BuildRequires: cmake

BuildRequires: opt-qt5-qtbase-devel
BuildRequires: opt-qt5-qtbase-private-devel
BuildRequires: opt-qt5-qtdeclarative-devel
#libQt5Quick.so.5(Qt_5_PRIVATE_API)(64bit)
%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
Requires: opt-qt5-qtbase-gui
Requires: opt-qt5-qtdeclarative

%description
This input plugin links Maliit keyboard provided by Sailfish OS to
applications using newer Qt.

%prep
%autosetup -n %{name}-%{version}/upstream


%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

mkdir -p build
cd build

export CMAKE_PREFIX_PATH=%{_opt_qt5_prefix}
cmake \
    -DCMAKE_INSTALL_PREFIX=%{_opt_qt5_prefix} \
    -Denable-docs=OFF \
    -Denable-tests=OFF \
    -Denable-glib=off \
    -Denable-xcb=OFF \
    -Denable-wayland=OFF \
    -Denable-wayland-gtk=OFF \
    -Denable-qt5-inputcontext=ON \
    -Denable-hwkeyboard=ON \
    ..

make V=1 VERBOSE=1 %{?_smp_mflags} maliitplatforminputcontextplugin

%install

cd build

install -D -t %{buildroot}%{_opt_qt5_plugindir}/platforminputcontexts libmaliitplatforminputcontextplugin.so

%files
%license LICENSE.*
%{_opt_qt5_plugindir}/platforminputcontexts/libmaliitplatforminputcontextplugin.so
