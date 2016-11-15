%{!?upstream_version: %global upstream_version %{commit}}
%global commit 40e8515c0f824236d5f3d0fe491ed03f02cb9d9f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global alphatag .%{shortcommit}git

%define upstream_name puppetlabs-mongodb


Name:           puppet-mongodb
Version:        0.16.0
Release:        2%{?alphatag}%{?dist}
Summary:        Installs MongoDB on RHEL/Ubuntu/Debian.
License:        Apache-2.0

URL:            https://github.com/puppetlabs/puppetlabs-mongodb

Source0:        https://github.com/puppetlabs/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

#Requires:       puppet-apt
Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
Installs MongoDB on RHEL/Ubuntu/Debian.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/mongodb/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/mongodb/



%files
%{_datadir}/openstack-puppet/modules/mongodb/


%changelog
* Tue Nov 15 2016 Alfredo Moralejo <amoralej@redhat.com> 0.16.0-2.40e8515.git
- Newton update 0.16.0 (40e8515c0f824236d5f3d0fe491ed03f02cb9d9f)

* Thu Nov 03 2016 Jon Schlueter <jschluet@redhat.com> 0.16.0-1
- Update to 0.16.0 (5091b520053b33aca7e209f2ce5f6eab10cb130d)

* Thu Sep 22 2016 Haikel Guemar <hguemar@fedoraproject.org> - 0.14.0-1.1cfb235.git
- Newton update 0.14.0 (1cfb235894795f216ce3ae3fc02eb52d112e9197)


