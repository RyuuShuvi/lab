Summary: A script to count files in /etc
Name: count_files
Version:1.0
Release: 1%{?dist}
License: MIT


%description
This script counts files in /etc directory 

%prep

%build

%install
mkdir -p %{buildroot}/usr/bin
install -m 755 calc_files.sh %{buildroot}/usr/bin/calc_files.sh

%files
%defattr(-,root,root,-)
/usr/bin/calc_files.sh


%changelog
* Tue Dec 19 2023 Sivko Denis - 1.0-1
- Initial build
