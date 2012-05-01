%{!?tcl_version: %define tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitelib: %define tcl_sitelib %{_datadir}/tcl%{tcl_version}}

Name:           bwidget
Version:        1.8.0
Release:        5.1%{?dist}
Summary:        Extended widget set for Tk

Group:          Development/Libraries
License:        TCL
URL:            http://tcllib.sourceforge.net/
Source0:        http://downloads.sourceforge.net/tcllib/BWidget-1.8.0.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
Requires:       tcl(abi) = 8.5 tk
BuildRequires:  tcl

%description
An extended widget set for Tcl/Tk.

%prep
%setup -q -n BWidget-%{version}
%{__sed} -i 's/\r//' LICENSE.txt

%install
rm -rf $RPM_BUILD_ROOT
# Don't bother with the included configure script and Makefile.  They
# are missing a lot of pieces and won't work at all.  Installation is
# pretty simple, so we can just do it here manually.
mkdir -p $RPM_BUILD_ROOT/%{tcl_sitelib}/%{name}%{version}/
mkdir $RPM_BUILD_ROOT/%{tcl_sitelib}/%{name}%{version}/lang
mkdir $RPM_BUILD_ROOT/%{tcl_sitelib}/%{name}%{version}/images

install -m 0644 -pD *.tcl $RPM_BUILD_ROOT/%{tcl_sitelib}/%{name}%{version}/
install -m 0644 -pD lang/*.rc $RPM_BUILD_ROOT/%{tcl_sitelib}/%{name}%{version}/lang/
install -m 0644 -pD images/*.gif images/*.xbm $RPM_BUILD_ROOT/%{tcl_sitelib}/%{name}%{version}/images/


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{tcl_sitelib}/%{name}%{version}
%doc README.txt LICENSE.txt
%doc BWman/*.html

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.8.0-5.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan  3 2008 Marcela Maslanova <mmaslano@redhat.com> 1.8.0-3
- rebuild with new tcl8.5, changed abi in spec

* Wed Aug 22 2007 Wart <wart at kobold.org> 1.8.0-2
- License tag clarification
- Move files to a tcl-specific directory for faster loading

* Thu Oct 19 2006 Wart <wart at kobold.org> 1.8.0-1
- Update to 1.8.0
- Remove patch that was accepted upstream

* Mon Aug 28 2006 Wart <wart at kobold.org> 1.7.0-4
- Rebuild for Fedora Extras

* Fri Aug 11 2006 Wart <wart at kobold.org> 1.7.0-3
- Add patch for adding a color selector to the font dialog

* Sat Dec 10 2005 Wart <wart at kobold.org> 1.7.0-2
- added dist tag to release tag.

* Sat Dec 10 2005 Wart <wart at kobold.org> 1.7.0-1
- Initial spec file.
