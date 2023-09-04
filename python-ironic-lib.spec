%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x815AFEC729392386480E076DCC0DFE2D21C023C9
%{!?upstream_version: %global upstream_version %{version}}
# we are excluding some BRs from automatic generator
%global excluded_brs doc8 bandit pre-commit hacking flake8-import-order

%global srcname ironic-lib
%global sum A common library to be used by various projects in the Ironic ecosystem

Name:           python-%{srcname}
Version:        5.5.0
Release:        1%{?dist}
Summary:        %{sum}

License:        Apache-2.0
URL:            http://pypi.python.org/pypi/%{srcname}
Source0:        https://tarballs.openstack.org/%{srcname}/%{srcname}-%{version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{srcname}/%{srcname}-%{version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
BuildRequires:  openstack-macros
%endif

%description
A common library to be used by various projects in the Ironic ecosystem

%package -n     python3-%{srcname}
Summary:        %{sum}

BuildRequires:  openstack-macros
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%if 0%{?fedora} || 0%{?rhel} > 7
Recommends: python3-keystoneauth1 >= 4.2.0
Recommends: python3-os-service-types >= 1.2.0
Recommends: python3-oslo-service >= 1.24.0
%endif

%description -n python3-%{srcname}
A common library to be used by various projects in the Ironic ecosystem

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{srcname}-%{upstream_version} -p1

sed -i /.*-c{env:TOX_CONSTRAINTS_FILE.*/d tox.ini
sed -i /^minversion.*/d tox.ini
sed -i /^requires.*virtualenv.*/d tox.ini

# Exclude some bad-known BRs
for pkg in %{excluded_brs};do
  for reqfile in doc/requirements.txt test-requirements.txt; do
    if [ -f $reqfile ]; then
      sed -i /^${pkg}.*/d $reqfile
    fi
  done
done

%generate_buildrequires
%pyproject_buildrequires -t -e %{default_toxenv}

%build
%pyproject_wheel

%check
%tox -e %{default_toxenv}

%install
%pyproject_install

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
* Mon Sep 04 2023 RDO <dev@lists.rdoproject.org> 5.5.0-1
- Update to 5.5.0

