%define git	1
%define gitdate	20120710
%define major	1
%define libname	%mklibname kvkontakte %{major}
%define devname	%mklibname -d kvkontakte

Summary:         Library for asynchronous interaction with vkontakte social network  
Name:            libkvkontakte
Group:           System/Libraries
Version:         2.7.0
Release:         0.git%{gitdate} 2
License:         GPLv2+ 
Url:             https://projects.kde.org/projects/extragear/libs/libkvkontakte
Source0:         %{name}-%{gitdate}.tar.bz2
BuildRequires:   kdelibs4-devel
BuildRequires:   pkgconfig(QJson)

%description
KDE C++ library for asynchronous interaction with vkontakte.ru social
network via its open API.

%package -n %{libname}
Summary:         %{name} Library

%description -n %{libname}
KDE C++ library for asynchronous interaction with vkontakte.ru social
network via its open API.

%package -n %{devname}
Summary:         %{name} Developpement Files
Group:           Development/C
Requires:        %{libname} = %{version}-%{release}
Provides:        %{name}-devel = %{version}-%{release}
Provides:        kvkontakte-devel = %{version}-%{release}

%description -n %{devname}
This package contains libraries and headers files needed to develop
progams that need libkvkontakte.

%prep
%setup -q%{?git:n %{name}}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%files -n %{libname}
%{_kde_libdir}/libkvkontakte.so.%{major}*

%files -n %{devname}
%{_kde_includedir}/libkvkontakte/
%{_kde_libdir}/cmake/LibKVkontakte/
%{_kde_libdir}/libkvkontakte.so

