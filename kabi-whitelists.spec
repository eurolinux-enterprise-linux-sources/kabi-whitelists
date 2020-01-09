%define ksc_source_version 0.9.4

Name:		kabi-whitelists
Version:	20130129
Release:	1%{?dist}
Summary:	The Red Hat Enterprise Linux kernel ABI symbol whitelists

Group:		System Environment/Kernel
License:	GPLv2
URL:		http://www.redhat.com/
Source0:	kabi-whitelists-%{version}.tar.bz2
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

%description
The kABI package contains information pertaining to the Red Hat Enterprise
Linux kernel ABI, including lists of kernel symbols that are needed by
external Linux kernel modules, and a yum plugin to aid enforcement.

%package -n ksc
Summary: Kernel source code checker (source version %{ksc_source_version})
Group: Development/Tools
AutoReqProv: no
Requires: kabi-whitelists
Requires: cpp
Requires: file
Source1: ksc-%{ksc_source_version}.tar.gz
%description -n ksc
A kernel module source code checker to find usage of non whitelist symbols

%prep
# unpack kabi-whitelists
tar xjvf %{SOURCE0}

# unpack ksc
tar xzvf %{SOURCE1}

%build
# build only, no need for kabi-whitelists
pushd ksc-%{ksc_source_version}
%{__python} setup.py build
popd

%install
# install kabi-whitelists
pushd kabi-whitelists-%{version}
KABI_INSTALL_DIR=$RPM_BUILD_ROOT/lib/modules/
mkdir -p $KABI_INSTALL_DIR
cp -R * $KABI_INSTALL_DIR
popd

# install ksc
pushd ksc-%{ksc_source_version}
%{__python} setup.py install -O1 --root %{buildroot}
install -D ksc.1 %{buildroot}%{_mandir}/man1/ksc.1
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/lib/modules/kabi-*

%files -n ksc
%defattr(-,root,root,-)
%doc ksc-%{ksc_source_version}/README
%{_bindir}/ksc
%{_datadir}/ksc
%{_mandir}/man1/ksc.*
%config(noreplace) %{_sysconfdir}/ksc.conf
%{python_sitelib}/ksc-%{ksc_source_version}*.egg-info

%changelog
* Tue Jan 29 2013 Jiri Olsa <jolsa@redhat.com> - 20130129-1
- Update the kABI for RHEL6.4
- Resolves #826795

* Tue Jan 22 2013 Jiri Olsa <jolsa@redhat.com> - 20130122-1
- Update the kABI for RHEL6.4
- Resolves #864893
- Resolves #826795

* Mon Jan 21 2013 Jiri Olsa <jolsa@redhat.com> - 20130103-2
- Update ksc package
- Resolves #869353

* Wed Jan 03 2013 Jiri Olsa <jolsa@redhat.com> - 20130103-1
- Update the kABI for RHEL6.4
- Resolves #864893

* Thu Nov 07 2012 Jiri Olsa <jolsa@redhat.com> - 20121107-1
- Update the kABI for RHEL6.4
- Resolves #826795
- Adding ksc subpackage
- Resolves #869353

* Thu Nov 01 2012 Jiri Olsa <jolsa@redhat.com> - 20121101-1
- Adding ksc subpackage
- Update the kABI for RHEL6.4
- Resolves #869353

* Mon May 07 2012 Jiri Olsa <jolsa@redhat.com> - 20120516-1
- Update the kABI for RHEL6.3
- Resolves: #816533 #812463

* Mon May 07 2012 Jiri Olsa <jolsa@redhat.com> - 20120507-1
- Fix rhel62 whitelist that got mixed by fix for 810456
- Resolves: #810456

* Mon Apr 06 2012 Jiri Olsa <jolsa@redhat.com> - 20120427-1
- Update the kABI for RHEL6.3
- Resolves: #810456 #803885

* Mon Apr 06 2012 Jiri Olsa <jolsa@redhat.com> - 20120406-1
- Update the kABI for RHEL6.3
- Resolves: #737276

* Mon Mar 26 2012 Jiri Olsa <jolsa@redhat.com> - 20120326-1
- Update the kABI for RHEL6.3
- Resolves: #737276

* Mon Mar 15 2012 Jiri Olsa <jolsa@redhat.com> - 20120315-1
- Update the kABI for RHEL6.3
- Resolves: #753771

* Mon Mar 14 2012 Jiri Olsa <jolsa@redhat.com> - 20120314-1
- Update the kABI for RHEL6.3
- Resolves: #753771

* Mon Mar 03 2012 Jiri Olsa <jolsa@redhat.com> - 20120305-1
- Update the kABI for RHEL6.3
- Resolves: #753771

* Mon Feb 20 2012 Jiri Olsa <jolsa@redhat.com> - 20120220-1
- Update the kABI for RHEL6.3
- Resolves: #737276

* Mon Dec 19 2011 Jiri Olsa <jolsa@redhat.com> - 20111219-1
- Update the kABI for RHEL6.3

* Mon Oct 27 2011 Jiri Olsa <jolsa@redhat.com> - 20111027-1
- Update the kABI for RHEL6.2
- Resolves: #703125, #730410

* Mon Oct 24 2011 Jiri Olsa <jolsa@redhat.com> - 20111024-1
- Update the kABI for RHEL6.2
- Resolves: #702675

* Wed Sep 01 2011 Jiri Olsa <jolsa@redhat.com> - 20110901-1
- Update the kABI for RHEL6.2
- Resolves: #700406, #700432

* Wed Aug 17 2011 Jiri Olsa <jolsa@redhat.com> - 20110817-1
- Update the kABI for RHEL6.2
- Resolves: #690479 #680469

* Tue Apr 12 2011 Jon Masters <jcm@redhat.com> - 20110412-1
- Update the kABI for RHEL6.1
- Resolves: #682967

* Fri Oct 15 2010 Jon Masters <jcm@redhat.com> - 20101015-1
- Update the kABI whitelists for block symbol correction
- Resolves: #636975

* Fri Aug 20 2010 Jon Masters <jcm@redhat.com> - 20100820-1
- Update the kABI whitelists for snapshot 13 release
- Resolves: #612735

* Tue Aug 17 2010 Jon Masters <jcm@redhat.com> - 20100817-1
- Update the kABI whitelists for snapshot 12 release
- Resolves: #612735

* Wed May 12 2010 Jon Masters <jcm@redhat.com> - 20100512-2
- Initial public build of kABI whitelists package
- Resolves: #591675
