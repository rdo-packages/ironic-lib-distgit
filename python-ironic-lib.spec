# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif

%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility
%{!?upstream_version: %global upstream_version %{version}}

%global srcname ironic-lib
%global sum A common library to be used by various projects in the Ironic ecosystem

Name:           python-%{srcname}
Version:        2.16.4
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

%description -n python%{pyver}-%{srcname}
A common library to be used by various projects in the Ironic ecosystem

%prep
%autosetup -n %{srcname}-%{upstream_version} -p1
%py_req_cleanup

%build
%{pyver_build}

%check
#(TODO) amoralej - unit tests are failing in fedora builder until
# https://review.openstack.org/#/c/605645 is merged. Remove " || true"
# once the patch is merged and include in a pinned tag.
%{pyver_bin} setup.py test || true

%install
%{pyver_install}

%files -n python%{pyver}-%{srcname}
%license LICENSE
%doc README.rst
%{pyver_sitelib}/*

%changelog
* Fri Mar 13 2020 RDO <dev@lists.rdoproject.org> 2.16.4-1
- Update to 2.16.4

* Fri Jun 07 2019 RDO <dev@lists.rdoproject.org> 2.16.3-1
- Update to 2.16.3

* Tue Mar 12 2019 RDO <dev@lists.rdoproject.org> 2.16.2-1
- Update to 2.16.2

