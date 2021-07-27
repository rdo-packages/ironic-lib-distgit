%{!?upstream_version: %global upstream_version %{version}}

%global srcname ironic-lib
%global sum A common library to be used by various projects in the Ironic ecosystem

Name:           python-%{srcname}
Version:        4.2.3
Release:        1%{?dist}
Summary:        %{sum}

License:        ASL 2.0
URL:            http://pypi.python.org/pypi/%{srcname}
Source0:        https://tarballs.openstack.org/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
A common library to be used by various projects in the Ironic ecosystem

%package -n     python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools
BuildRequires:  openstack-macros
Requires: python3-oslo-concurrency >= 3.26.0
Requires: python3-oslo-config >= 2:5.2.0
Requires: python3-oslo-i18n >= 3.15.3
Requires: python3-oslo-log >= 3.36.0
Requires: python3-oslo-serialization >= 2.18.0
Requires: python3-oslo-service >= 1.24.0
Requires: python3-oslo-utils >= 3.33.0
Requires: python3-pbr
Requires: python3-requests
Requires: python3-zeroconf >= 0.24.0

# These are requirements for unit testing
BuildRequires: python3-eventlet
BuildRequires: python3-oslo-concurrency
BuildRequires: python3-oslo-config
BuildRequires: python3-oslo-i18n
BuildRequires: python3-oslo-log
BuildRequires: python3-oslo-service
BuildRequires: python3-oslo-utils
BuildRequires: python3-oslotest
BuildRequires: python3-requests
BuildRequires: python3-six
BuildRequires: python3-testtools
BuildRequires: python3-zeroconf

%description -n python3-%{srcname}
A common library to be used by various projects in the Ironic ecosystem

%prep
%autosetup -n %{srcname}-%{upstream_version} -p1
%py_req_cleanup

%build
%{py3_build}

%check
python3 setup.py test

%install
%{py3_install}

# rootwrap related files
install -d -m 755 %{buildroot}%{_sysconfdir}/ironic
install -d -m 755 %{buildroot}%{_sysconfdir}/ironic/rootwrap.d
mv %{buildroot}/usr/etc/ironic/rootwrap.d/ironic-lib.filters %{buildroot}%{_sysconfdir}/ironic/rootwrap.d/

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/*
%config(noreplace) %attr(-, root, ironic) %{_sysconfdir}/ironic/rootwrap.d/ironic-lib.filters

%changelog
* Tue Jul 27 2021 RDO <dev@lists.rdoproject.org> 4.2.3-1
- Update to 4.2.3

* Mon Mar 15 2021 RDO <dev@lists.rdoproject.org> 4.2.2-1
- Update to 4.2.2

* Thu Jun 18 2020 RDO <dev@lists.rdoproject.org> 4.2.1-1
- Update to 4.2.1

* Mon Apr 27 2020 RDO <dev@lists.rdoproject.org> 4.2.0-1
- Update to 4.2.0

