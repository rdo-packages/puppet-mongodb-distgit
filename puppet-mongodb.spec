%global milestone .0rc0
%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-mongodb
%global commit a59b99ed9df3796b64c42bc4e499fdef53b3c39a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-mongodb
Version:        3.1.1
Release:        0.3%{?milestone}%{?alphatag}%{?dist}
Summary:        Installs MongoDB on RHEL/Ubuntu/Debian.
License:        ASL 2.0

URL:            https://github.com/voxpupuli/puppet-mongodb

Source0:        https://github.com/voxpupuli/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

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
* Thu Mar 25 2021 RDO <dev@lists.rdoproject.org> 3.1.1-0.3.0rc0.a59b99egit
- Update to post 3.1.1-rc0 (a59b99ed9df3796b64c42bc4e499fdef53b3c39a)

