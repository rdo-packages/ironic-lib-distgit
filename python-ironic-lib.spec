%{!?upstream_version: %global upstream_version %{version}}

%global srcname ironic-lib
%global sum A common library to be used by various projects in the Ironic ecosystem

Name:           python-%{srcname}
Version:        2.14.3
Release:        1%{?dist}
Summary:        %{sum}

License:        ASL 2.0
URL:            http://pypi.python.org/pypi/%{srcname}
Source0:        https://tarballs.openstack.org/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python2-pbr
BuildRequires:  python2-setuptools
BuildRequires:  openstack-macros
Requires: python2-oslo-concurrency >= 3.26.0
Requires: python2-oslo-config >= 2:5.2.0
Requires: python2-oslo-i18n >= 3.15.3
Requires: python2-oslo-log >= 3.36.0
Requires: python2-oslo-serialization >= 2.18.0
Requires: python2-oslo-service >= 1.24.0
Requires: python2-oslo-utils >= 3.33.0
Requires: python2-pbr
Requires: python2-requests
Requires: python2-six

# These are requirements for unit testing
BuildRequires: python2-eventlet
BuildRequires: python2-oslo-concurrency
BuildRequires: python2-oslo-config
BuildRequires: python2-oslo-i18n
BuildRequires: python2-oslo-log
BuildRequires: python2-oslo-service
BuildRequires: python2-oslo-utils
BuildRequires: python2-oslotest
BuildRequires: python2-requests
BuildRequires: python2-six
BuildRequires: python2-testtools

%description
A common library to be used by various projects in the Ironic ecosystem

%prep
%autosetup -n %{srcname}-%{upstream_version} -p1
%py_req_cleanup

%build
%{__python2} setup.py build

%check
%{__python2} setup.py test

%install
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}

%files
%license LICENSE
%doc README.rst
%{python2_sitelib}/*

%changelog
* Fri Mar 13 2020 RDO <dev@lists.rdoproject.org> 2.14.3-1
- Update to 2.14.3

* Wed Jun 12 2019 RDO <dev@lists.rdoproject.org> 2.14.2-1
- Update to 2.14.2

* Fri Feb 01 2019 RDO <dev@lists.rdoproject.org> 2.14.1-1
- Update to 2.14.1

* Fri Aug 10 2018 RDO <dev@lists.rdoproject.org> 2.14.0-1
- Update to 2.14.0

