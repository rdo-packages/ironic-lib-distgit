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

BuildRequires:  python-devel
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
Requires: python-oslo-concurrency >= 3.8.0
Requires: python-oslo-config >= 2:4.0.0
Requires: python-oslo-i18n >= 2.1.0
Requires: python-oslo-log >= 3.22.0
Requires: python-oslo-serialization >= 1.10.0
Requires: python-oslo-service >= 1.10.0
Requires: python-oslo-utils >= 3.20.0
Requires: python-pbr
Requires: python-requests
Requires: python-six

# These are requirements for unit testing
BuildRequires: python-eventlet
BuildRequires: python-oslo-concurrency
BuildRequires: python-oslo-config
BuildRequires: python-oslo-i18n
BuildRequires: python-oslo-log
BuildRequires: python-oslo-service
BuildRequires: python-oslo-utils
BuildRequires: python-oslotest
BuildRequires: python-requests
BuildRequires: python-six
BuildRequires: python-testtools

%description
A common library to be used by various projects in the Ironic ecosystem

%prep
%autosetup -n %{srcname}-%{upstream_version} -p1

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
