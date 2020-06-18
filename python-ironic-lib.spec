# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif

%global pyver_bin python%{pyver}
%global pyver_sitelib %{expand:%{python%{pyver}_sitelib}}
%global pyver_install %{expand:%{py%{pyver}_install}}
%global pyver_build %{expand:%{py%{pyver}_build}}
# End of macros for py2/py3 compatibility
%{!?upstream_version: %global upstream_version %{version}}

%global srcname ironic-lib
%global sum A common library to be used by various projects in the Ironic ecosystem

Name:           python-%{srcname}
Version:        2.21.2
Release:        1%{?dist}
Summary:        %{sum}

License:        ASL 2.0
URL:            http://pypi.python.org/pypi/%{srcname}
Source0:        https://tarballs.openstack.org/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
A common library to be used by various projects in the Ironic ecosystem

%package -n     python%{pyver}-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python%{pyver}-%{srcname}}

BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-pbr
BuildRequires:  python%{pyver}-setuptools
BuildRequires:  openstack-macros
Requires: python%{pyver}-oslo-concurrency >= 3.26.0
Requires: python%{pyver}-oslo-config >= 2:5.2.0
Requires: python%{pyver}-oslo-i18n >= 3.15.3
Requires: python%{pyver}-oslo-log >= 3.36.0
Requires: python%{pyver}-oslo-serialization >= 2.18.0
Requires: python%{pyver}-oslo-service >= 1.24.0
Requires: python%{pyver}-oslo-utils >= 3.33.0
Requires: python%{pyver}-pbr
Requires: python%{pyver}-requests
Requires: python%{pyver}-six
Requires: python%{pyver}-zeroconf >= 0.19.1

# These are requirements for unit testing
BuildRequires: python%{pyver}-eventlet
BuildRequires: python%{pyver}-oslo-concurrency
BuildRequires: python%{pyver}-oslo-config
BuildRequires: python%{pyver}-oslo-i18n
BuildRequires: python%{pyver}-oslo-log
BuildRequires: python%{pyver}-oslo-service
BuildRequires: python%{pyver}-oslo-utils
BuildRequires: python%{pyver}-oslotest
BuildRequires: python%{pyver}-requests
BuildRequires: python%{pyver}-six
BuildRequires: python%{pyver}-testtools
BuildRequires: python%{pyver}-zeroconf

%description -n python%{pyver}-%{srcname}
A common library to be used by various projects in the Ironic ecosystem

%prep
%autosetup -n %{srcname}-%{upstream_version} -p1
%py_req_cleanup

%build
%{pyver_build}

%check
%{pyver_bin} setup.py test

%install
%{pyver_install}

%files -n python%{pyver}-%{srcname}
%license LICENSE
%doc README.rst
%{pyver_sitelib}/*

%changelog
* Thu Jun 18 2020 RDO <dev@lists.rdoproject.org> 2.21.2-1
- Update to 2.21.2

* Fri May 22 2020 RDO <dev@lists.rdoproject.org> 2.21.1-1
- Update to 2.21.1

* Mon Sep 23 2019 RDO <dev@lists.rdoproject.org> 2.21.0-1
- Update to 2.21.0

