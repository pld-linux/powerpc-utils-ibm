Summary:	Utilities for PowerPC platforms from IBM
Summary(pl.UTF-8):	Narzędzia dla platform PowerPC wyprodukowanych przez IBM
# NOTE: original name is powerpc-utils, but this name in PLD was already
# occupied by (renamed) pmac-utils package (which is for PowerPCs from Apple)
Name:		powerpc-utils-ibm
Version:	1.3.5
Release:	1
License:	GPL v2+
Group:		Applications/System
#Source0Download: https://github.com/nfont/powerpc-utils/releases
Source0:	https://github.com/nfont/powerpc-utils/archive/v%{version}/powerpc-utils-%{version}.tar.gz
# Source0-md5:	204aaf9811ec0d37a68a9afd9c0578cb
Patch0:		powerpc-utils-includes.patch
Patch1:		powerpc-utils-install.patch
URL:		http://powerpc-utils.sourceforge.net/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.10
BuildRequires:	librtas-devel
BuildRequires:	rpmbuild(macros) >= 1.644
Obsoletes:	powerpc-utils-papr
ExclusiveArch:	ppc ppc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utilities for maintaining and servicing PowerPC systems on IBM
hardware.

%description -l pl.UTF-8
Narzędzia do administrowania i serwisowania systemów PowerPC na
sprzęcie firmy IBM.

%prep
%setup -q -n powerpc-utils-%{version}
%patch0 -p1
%patch1 -p1

%build
install -d config
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules \
	--with-systemd=%{systemdunitdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/packages

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_bindir}/amsstat
%attr(755,root,root) %{_sbindir}/activate_firmware
%attr(755,root,root) %{_sbindir}/bootlist
%attr(755,root,root) %{_sbindir}/drmgr
%attr(755,root,root) %{_sbindir}/errinjct
%attr(755,root,root) %{_sbindir}/hvcsadmin
%attr(755,root,root) %{_sbindir}/lparstat
%attr(755,root,root) %{_sbindir}/ls-vdev
%attr(755,root,root) %{_sbindir}/ls-veth
%attr(755,root,root) %{_sbindir}/ls-vscsi
%attr(755,root,root) %{_sbindir}/lsdevinfo
%attr(755,root,root) %{_sbindir}/lsprop
%attr(755,root,root) %{_sbindir}/lsslot
%attr(755,root,root) %{_sbindir}/nvram
%attr(755,root,root) %{_sbindir}/nvsetenv
%attr(755,root,root) %{_sbindir}/ofpathname
%attr(755,root,root) %{_sbindir}/ppc64_cpu
%attr(755,root,root) %{_sbindir}/pseries_platform
%attr(755,root,root) %{_sbindir}/rtas_dbg
%attr(755,root,root) %{_sbindir}/rtas_dump
%attr(755,root,root) %{_sbindir}/rtas_event_decode
%attr(755,root,root) %{_sbindir}/rtas_ibm_get_vpd
%attr(755,root,root) %{_sbindir}/serv_config
%attr(755,root,root) %{_sbindir}/set_poweron_time
%attr(755,root,root) %{_sbindir}/snap
%attr(755,root,root) %{_sbindir}/sys_ident
%attr(755,root,root) %{_sbindir}/uesensor
%attr(755,root,root) %{_sbindir}/update_flash
%attr(755,root,root) %{_sbindir}/update_flash_nv
%{systemdunitdir}/smt_off.service
%{_mandir}/man1/amsstat.1*
%{_mandir}/man5/lparcfg.5*
%{_mandir}/man8/activate_firmware.8*
%{_mandir}/man8/bootlist.8*
%{_mandir}/man8/errinjct.8*
%{_mandir}/man8/hvcsadmin.8*
%{_mandir}/man8/lparstat.8*
%{_mandir}/man8/lsslot.8*
%{_mandir}/man8/nvram.8*
%{_mandir}/man8/ofpathname.8*
%{_mandir}/man8/ppc64_cpu.8*
%{_mandir}/man8/rtas_dbg.8*
%{_mandir}/man8/rtas_dump.8*
%{_mandir}/man8/rtas_ibm_get_vpd.8*
%{_mandir}/man8/serv_config.8*
%{_mandir}/man8/set_poweron_time.8*
%{_mandir}/man8/snap.8*
%{_mandir}/man8/sys_ident.8*
%{_mandir}/man8/uesensor.8*
%{_mandir}/man8/update_flash.8*
