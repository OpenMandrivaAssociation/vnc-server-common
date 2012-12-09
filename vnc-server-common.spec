Name:    vnc-server-common
Version: 1.0
Release: %mkrel 2

License:   GPLv2+
URL:       http://www.mandriva.com
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

Source0: vncserver-initscript
Source1: sysconfig-vncservers

Summary: Common files for VNC servers
Group:   Networking/Remote access

Requires(post):  rpm-helper
Requires(preun): rpm-helper

# Packages that used to provide the common files:
# Can't conflict with vnc-server since it is provided as a virtual package...
#Conflicts: vnc-server <= 4.1.2-2mdv2008.1
Conflicts: tightvnc-server <= 1.3.10-4mdv2011.0
Conflicts: tigervnc-server <= 1.0.90-0.201012034210.3mdv2011.0

%description
This package contains files that are common between multiple VNC server
implementations:
  - the vncserver initscript
  - the vncservers configuration file

%prep

%build

%install
rm -rf %{buildroot}

install -D -m 644 %{_sourcedir}/sysconfig-vncservers \
                  %{buildroot}/%{_sysconfdir}/sysconfig/vncservers
install -D -m 755 %{_sourcedir}/vncserver-initscript \
                  %{buildroot}/%{_initrddir}/vncserver

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_initrddir}/vncserver
%config(noreplace) %{_sysconfdir}/sysconfig/vncservers

%post
%_post_service vncserver

%preun
%_preun_service vncserver


%changelog
* Mon Jan 03 2011 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0-2mdv2011.0
+ Revision: 628003
- Initscript: fix reporting of "status"
- Initscript: add '\n' to "Usage" string

* Thu Dec 23 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0-1mdv2011.0
+ Revision: 624168
- imported package vnc-server-common

