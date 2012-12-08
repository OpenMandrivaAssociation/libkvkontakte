%define git 1
%define gitdate 20120710

%define major 1
%define libname %mklibname kvkontakte %{major}
%define libnamedev %mklibname -d kvkontakte

Name:		libkvkontakte
Summary:	Library for asynchronous interaction with vkontakte social network  
Group:		System/Libraries
Version:	1.0.0
Release:	0.git%{gitdate}.1
License:	GPLv2+
Url:		https://projects.kde.org/projects/extragear/libs/libkvkontakte
Source0:	%{name}-%{gitdate}.tar.bz2
BuildRequires:	qjson-devel
BuildRequires:	kdelibs4-devel

%description
KDE C++ library for asynchronous interaction with vkontakte.ru social
network via its open API.

#--------------------------------------------------------------------
%package -n %{libname}
Summary:	%{name} Library
Group:		System/Libraries

%description -n %{libname}
KDE C++ library for asynchronous interaction with vkontakte.ru social
network via its open API.

%files -n %{libname}
%{_kde_libdir}/libkvkontakte.so.%{major}*

#--------------------------------------------------------------------
%package -n %{libnamedev}
Summary:	%{name} Developpement Files
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	libkvkontakte-devel = %{version}-%{release}
Provides:	kvkontakte-devel = %{version}-%{release}

%description -n %{libnamedev}
This package contains libraries and headers files needed to develop
progams that need libkvkontakte.

%files -n %{libnamedev}
%{_kde_includedir}/libkvkontakte/
%{_kde_libdir}/cmake/LibKVkontakte/
%{_kde_libdir}/libkvkontakte.so

#--------------------------------------------------------------------
%prep
%setup -q%{?git:n %{name}}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue Nov 15 2011 Zé <ze@mandriva.org> 1.0.0-0.git20111115.1
+ Revision: 730683
- fix lib naming
- imported package libkvkontakte


* Thu Nov 15 2011 Zé <ze@mandriva.org> 1.0.0-1
- first package
