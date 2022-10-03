%define    _topdir /github/workspace/rpmbuild

Name:      springboot-selinux
Version:   1
Release:   1
Summary:   SELinux policy module for Springboot applications
License:   GPLv2
URL:       https://github.com/hubertqc/selinux_springboot
BuildRoot: %{buildroot}
BuildArch: noarch

Requires:       selinux-policy-devel
Requires:       selinux-policy-targeted
Requires:       policycoreutils
Requires:       make

%description
SELinux policy module to confine Springboot applications started using systemd.
The systemd service unit name must start with springboot, the start script must be
assigned the springboot_exec_t SELinux type.
The Springboot application will run in the springboot_t domain.

%clean
%{__rm} -rf %{buildroot}

%build
make -f /usr/share/selinux/devel/Makefile -C $RPM_SOURCE_DIR  springboot.pp

%install
mkdir -p -m 0755 %{buildroot}/usr/share/selinux/packages/targeted
mkdir -p -m 0755 %{buildroot}/usr/share/selinux/devel/include/apps
install -m 0444 $RPM_SOURCE_DIR/springboot.if %{buildroot}/usr/share/selinux/devel/include/apps/springboot.if
cd $RPM_SOURCE_DIR && bzip2 springboot.pp
install -m 0444 $RPM_SOURCE_DIR/springboot.pp.bz2 %{buildroot}/usr/share/selinux/packages/targeted/springboot.pp.bz2

%post
bzcat -dc /usr/share/selinux/packages/targeted/springboot.pp.bz2 >> /usr/share/selinux/packages/targeted/springboot.pp
semodule -i /usr/share/selinux/packages/targeted/springboot.pp
rm -rf /usr/share/selinux/packages/targeted/springboot.pp

%postun
semodule -r springboot

%files
/usr/share/selinux/devel/include/apps/springboot.if
/usr/share/selinux/packages/targeted/springboot.pp.bz2
