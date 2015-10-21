%define major	1
%define libname	%mklibname kvkontakte %{major}
%define devname	%mklibname -d kvkontakte

Summary:         Library for asynchronous interaction with vkontakte social network  
Name:            libkvkontakte
Group:           System/Libraries
Version:         4.12.0
# epoch required as it used to be part of digikam
# which has epoch 2 and released 4.13.0
Epoch:		 3
Release:         1
License:         GPLv2+ 
Url:             https://projects.kde.org/projects/extragear/libs/libkvkontakte
Source0:         %{name}-%{version}.tar.xz
BuildRequires:   kdelibs4-devel
BuildRequires:   pkgconfig(QJson)

%description
KDE C++ library for asynchronous interaction with vkontakte.ru social
network via its open API.

%package -n %{libname}
Summary:         %{name} Library
Requires:	%{name}-common = %{EVRD}

%description -n %{libname}
KDE C++ library for asynchronous interaction with vkontakte.ru social
network via its open API.

%package -n %{name}-common
Summary:         %{name} Common files
BuildArch:	noarch

%description -n %{name}-common
KDE C++ library for asynchronous interaction with vkontakte.ru social
network via its open API.

%package -n %{devname}
Summary:         %{name} Developpement Files
Group:           Development/C
Requires:        %{libname} = %{EVRD}
Provides:        %{name}-devel = %{EVRD}
Provides:        kvkontakte-devel = %{EVRD}

%description -n %{devname}
This package contains libraries and headers files needed to develop
progams that need libkvkontakte.

%prep
%setup -q%{?git:n %{name}}

%build
# falls foul of 2.8.12
sed -i 's/2.8.12/2.8.11/' CMakeLists.txt
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name}

%files -n %{name}-common -f %{name}.lang

%files -n %{libname}
%{_kde_libdir}/libkvkontakte.so.%{major}*
%{_kde_libdir}/libkvkontakte.so.%{version}

%files -n %{devname}
%{_kde_includedir}/libkvkontakte/
%{_kde_libdir}/cmake/LibKVkontakte/
%{_kde_libdir}/libkvkontakte.so

