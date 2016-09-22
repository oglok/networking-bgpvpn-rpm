%global pypi_name networking-bgpvpn
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           python-%{pypi_name}
Version:        4.0.1
Release:        1%{?dist}
Summary:        API and Framework to interconnect bgpvpn to neutron networks

License:        ASL 2.0
URL:            http://www.openstack.org/
Source0:        https://files.pythonhosted.org/packages/source/n/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python-webob >= 1.2.3
BuildRequires:  python-webtest >= 2.0
BuildRequires:  python-coverage >= 3.6
BuildRequires:  python-hacking >= 0.10.0
BuildRequires:  python-networking-odl
BuildRequires:  python-oslo-sphinx >= 2.5.0
BuildRequires:  python-oslotest >= 1.10.0
BuildRequires:  python-pbr >= 1.8
BuildRequires:  python-reno >= 0.1.1
BuildRequires:  python-setuptools
BuildRequires:  python-sphinx >= 1.1.2
BuildRequires:  python-subunit >= 0.0.18
BuildRequires:  python-testrepository >= 0.0.18
BuildRequires:  python-testscenarios >= 0.4
BuildRequires:  python-testtools >= 1.4.0
BuildRequires:  python2-devel
BuildRequires:  python2-sphinxcontrib-blockdiag
BuildRequires:  python2-sphinxcontrib-seqdiag

%description
 BGPMPLS VPN Extension for OpenStack Networking This project provides an API
and Framework to interconnect BGP/MPLS VPNs to Openstack Neutron networks,
routers and ports.The Border Gateway Protocol and MultiProtocol Label Switching
are widely used Wide Area Networking technologies. The primary purpose of this
project is to allow attachment of Neutron networks and/or routers to carrier
provided ...

%package -n     python2-%{pypi_name}
Summary:        API and Framework to interconnect bgpvpn to neutron networks
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python-pbr >= 1.6
Requires:       python-Babel >= 1.3
Requires:       python-oslo-config >= 2.3.0
Requires:       python-oslo-db >= 2.4.1
Requires:       python-oslo-log >= 1.8.0
Requires:       python-oslo-utils >= 2.0.0
Requires:       python-sphinxcontrib-blockdiag
Requires:       python-sphinxcontrib-seqdiag
Requires:       python-setuptools

%description -n python2-%{pypi_name}
 BGPMPLS VPN Extension for OpenStack Networking This project provides an API
and Framework to interconnect BGP/MPLS VPNs to Openstack Neutron networks,
routers and ports.The Border Gateway Protocol and MultiProtocol Label Switching
are widely used Wide Area Networking technologies. The primary purpose of this
project is to allow attachment of Neutron networks and/or routers to carrier
provided ...

%package -n python-%{pypi_name}-doc
Summary:        networking-bgpvpn documentation
%description -n python-%{pypi_name}-doc
Documentation for networking-bgpvpn

%package -n python-%{pypi_name}-tests
Summary:        networking-bgpvpn tests
Requires:   python-%{pypi_name} = %{upstream_version}-%{release}

%description -n python-%{pypi_name}-tests
Networking-bgpvpn set of tests

%prep
%autosetup -n %{pypi_name}-%{upstream_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
# generate html docs 
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py2_install

%check
%{__python2} setup.py test

%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst networking_bgpvpn_tempest/README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/networking_bgpvpn_tempest
%{python2_sitelib}/networking_bgpvpn-*.egg-info
%exclude %{python2_sitelib}/%{module}/tests

%files -n python-%{pypi_name}-doc
%doc html 
%license LICENSE

%files -n python-%{pypi_name}-tests
%license LICENSE
%{python2_sitelib}/%{module}/tests

%changelog
* Thu Sep 15 2016 Ricardo Noriega <rnoriega@redhat.com> - 4.0.1-1
- Initial package.
