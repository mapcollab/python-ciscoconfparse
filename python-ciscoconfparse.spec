Name:           python-ciscoconfparse
Version:        1.2.47
Release:        2%{?dist}
Url:            https://pypi.python.org/pypi/ciscoconfparse/
Summary:        Parse, Audit, Query, Build, and Modify Cisco IOS-style configurations
License:        GPLv3
Group:          Development/Languages/Python
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-root
Requires:       python-ipaddr
Requires:       python-dns
Requires:       python-colorama
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-ipaddr
BuildRequires:  python-dns
BuildRequires:  python-colorama
BuildArch:      noarch

%description
Parse, Audit, Query, Build, and Modify Cisco IOS-style configurations.

See http://pypi.python.org/pypi/ciscoconfparse/

%prep
%setup -q -n %{name}-%{version}

%build
%{__python} setup.py build

%install
export PYTHONPATH=$RPM_BUILD_ROOT/usr/lib/python2.7/site-packages
rm -rf $RPM_BUILD_ROOT
mkdir -p $PYTHONPATH

%{__python} setup.py install \
    --prefix=$RPM_BUILD_ROOT/usr \
    --record=filelist-%{name}-%{version}-%{release}-temp

cat filelist-%{name}-%{version}-%{release}-temp | \
    sed -e "s;^$RPM_BUILD_ROOT;;" | \
    grep -v "doc/" | \
    grep -v "bin/" \
    > filelist-%{name}-%{version}-%{release}

%files
%files -f filelist-%{name}-%{version}-%{release}
%defattr(-,root,root)
#doc LICENSE.md README.md
/usr/lib/python2.7/site-packages/*

%changelog
* Fri Jun 09 2017 Michal Gawlik <michal.gawlik@thalesgroup.com> 1.2.47-2
- tito: use ReleaseTagger (michal.gawlik@thalesgroup.com)
- setup.py: dependencies are handled at rpm level
  (tomasz.rostanski@thalesgroup.com)
- python-ciscoconfparse.spec: add missing build required packages
  (tomasz.rostanski@thalesgroup.com)

* Fri Mar 17 2017 Michal Gawlik <michal.gawlik@thalesgroup.com> 1.2.47-1
- new package built with tito

