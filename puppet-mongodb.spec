%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-mongodb
%global commit c60e4ca4d9344b733d6d8048c8ef8face92a720e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-mongodb
Version:        1.1.1
Release:        0.1%{?alphatag}%{?dist}
Summary:        Installs MongoDB on RHEL/Ubuntu/Debian.
License:        ASL 2.0

URL:            https://github.com/puppetlabs/puppet-mongodb

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
* Thu Feb 15 2018 RDO <dev@lists.rdoproject.org> 1.1.1-0.1.c60e4cagit
- Update to 1.1.1-rc0 (c60e4ca4d9344b733d6d8048c8ef8face92a720e)

