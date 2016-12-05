%{!?upstream_version: %global upstream_version %{version}}

%global srcname ironic-lib
%global sum A common library to be used by various projects in the Ironic ecosystem

Name:           python-%{srcname}
Version:        2.1.2
Release:        1%{?dist}
Summary:        %{sum}

License:        ASL 2.0
URL:            http://pypi.python.org/pypi/%{srcname}
Source0:        https://tarballs.openstack.org/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
Requires: python-oslo-concurrency
Requires: python-oslo-config
Requires: python-oslo-i18n
Requires: python-oslo-log
Requires: python-oslo-service
Requires: python-oslo-utils
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
%autosetup -n %{srcname}-%{upstream_version}

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
* Mon Dec 05 2016 Alfredo Moralejo <amoralej@redhat.com> 2.1.2-1
- Update to 2.1.2

* Tue Oct 11 2016 Haikel Guemar <hguemar@fedoraproject.org> 2.1.1-1
- Update to 2.1.1

* Wed Sep 14 2016 Haikel Guemar <hguemar@fedoraproject.org> 2.1.0-1
- Update to 2.1.0

