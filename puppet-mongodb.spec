%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppetlabs-mongodb
%global commit 13af1c585a46b1450383a1b6a7fff99d077d0a01
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-mongodb
Version:        0.15.0
Release:        1%{?alphatag}%{?dist}
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
* Tue Nov 01 2016 Jon Schlueter <jschluet@redhat.com> 0.15.0-1
- Update to 0.15.0 (13af1c585a46b1450383a1b6a7fff99d077d0a01)

* Thu Sep 22 2016 Haikel Guemar <hguemar@fedoraproject.org> - 0.14.0-1.1cfb235.git
- Newton update 0.14.0 (1cfb235894795f216ce3ae3fc02eb52d112e9197)


