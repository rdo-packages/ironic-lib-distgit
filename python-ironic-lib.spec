%{!?upstream_version: %global upstream_version %{version}}

%global srcname ironic-lib
%global sum A common library to be used by various projects in the Ironic ecosystem

Name:           python-%{srcname}
Version:        XXX
Release:        XXX
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

BuildRequires:  openstack-macros
BuildRequires:  python3-devel
BuildRequires:  python3-pbr
BuildRequires:  python3-setuptools

Requires: python3-bcrypt >= 3.1.3
Requires: python3-oslo-concurrency >= 3.26.0
Requires: python3-oslo-config >= 2:5.2.0
Requires: python3-oslo-i18n >= 3.15.3
Requires: python3-oslo-log >= 3.36.0
Requires: python3-oslo-serialization >= 2.18.0
Requires: python3-oslo-service >= 1.24.0
Requires: python3-oslo-utils >= 3.33.0
Requires: python3-pbr >= 2.0.0
Requires: python3-requests >= 2.14.2
Requires: python3-webob >= 1.7.1
Requires: python3-zeroconf >= 0.24.0

# These are requirements for unit testing
BuildRequires: python3-bcrypt
BuildRequires: python3-eventlet
BuildRequires: python3-oslo-concurrency
BuildRequires: python3-oslo-config
BuildRequires: python3-oslo-i18n
BuildRequires: python3-oslo-log
BuildRequires: python3-oslo-service
BuildRequires: python3-oslo-utils
BuildRequires: python3-oslotest
BuildRequires: python3-requests
BuildRequires: python3-testtools
BuildRequires: python3-webob
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
