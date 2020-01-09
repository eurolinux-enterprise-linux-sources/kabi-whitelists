Name:		kabi-whitelists
Version:	20120516
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

%prep
%setup -q

%build
# nothing to build

%install
INSTALL_DIR=$RPM_BUILD_ROOT/lib/modules/

rm -rf $RPM_BUILD_ROOT
mkdir -p $INSTALL_DIR
cp -R * $INSTALL_DIR

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/lib/modules/kabi-*

%changelog
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
