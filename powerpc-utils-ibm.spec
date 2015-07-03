Summary:	Utilities for PowerPC platforms from IBM
Summary(pl.UTF-8):	Narzędzia dla platform PowerPC wyprodukowanych przez IBM
# NOTE: original name is powerpc-utils, but this name in PLD was already
# occupied by (renamed) pmac-utils package (which is for PowerPCs from Apple)
Name:		powerpc-utils-ibm
Version:	1.2.26
Release:	1
License:	CPL v1.0
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/powerpc-utils/powerpc-utils-%{version}.tar.gz
# Source0-md5:	2b1b84cf300a4b4bc2873e949cafc06f
Patch0:		powerpc-utils-includes.patch
URL:		http://powerpc-utils.sourceforge.net/
BuildRequires:	librtas-devel
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

%build
%configure \
	--disable-silent-rules
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
%doc COPYRIGHT Changelog README
%attr(755,root,root) %{_bindir}/amsstat
%attr(755,root,root) %{_sbindir}/activate_firmware
%attr(755,root,root) %{_sbindir}/bootlist
%attr(755,root,root) %{_sbindir}/drmgr
%attr(755,root,root) %{_sbindir}/hvcsadmin
%attr(755,root,root) %{_sbindir}/lparstat
%attr(755,root,root) %{_sbindir}/ls-vdev
%attr(755,root,root) %{_sbindir}/ls-veth
%attr(755,root,root) %{_sbindir}/ls-vscsi
%attr(755,root,root) %{_sbindir}/lsdevinfo
%attr(755,root,root) %{_sbindir}/lsprop
%attr(755,root,root) %{_sbindir}/lsslot
%attr(755,root,root) %{_sbindir}/nvram
%attr(755,root,root) %{_sbindir}/ofpathname
%attr(755,root,root) %{_sbindir}/ppc64_cpu
%attr(755,root,root) %{_sbindir}/pseries_platform
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
%{_mandir}/man1/amsstat.1*
%{_mandir}/man5/lparcfg.5*
%{_mandir}/man8/activate_firmware.8*
%{_mandir}/man8/bootlist.8*
%{_mandir}/man8/hvcsadmin.8*
%{_mandir}/man8/lparstat.8*
%{_mandir}/man8/lsslot.8*
%{_mandir}/man8/nvram.8*
%{_mandir}/man8/ofpathname.8*
%{_mandir}/man8/ppc64_cpu.8*
%{_mandir}/man8/rtas_dump.8*
%{_mandir}/man8/rtas_ibm_get_vpd.8*
%{_mandir}/man8/serv_config.8*
%{_mandir}/man8/set_poweron_time.8*
%{_mandir}/man8/snap.8*
%{_mandir}/man8/sys_ident.8*
%{_mandir}/man8/uesensor.8*
%{_mandir}/man8/update_flash.8*
