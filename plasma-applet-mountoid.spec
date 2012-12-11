%define name	plasma-applet-mountoid
%define srcname	mountoid
%define version	0.41
%define release	%mkrel 1
%define Summary	 Plasmoid for mount/unmount devices from fstab


Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
Source0:	http://www.kde-look.org/CONTENT/content-files/115943-%{srcname}-%{version}.tar.gz
License:	GPLv2
Group:		Graphical desktop/KDE
URL:		http://kde-look.org/content/show.php/Mountoid?content=115943
BuildRequires:	kdebase4-workspace-devel
Provides:	plasma-applet

%description
This plasmoid provides a way to mount/unmount devices from fstab (e.g. network
shares), show free space and open mount point location in a file manager. It is
fully configurable.


%files
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_mountoid.so
%_kde_iconsdir/hicolor/64x64/apps/mountoid.png
%_kde_iconsdir/hicolor/64x64/apps/os_macos.png
%_kde_iconsdir/hicolor/64x64/apps/os_winxp.png
%_kde_iconsdir/hicolor/64x64/apps/os_linux.png
%_kde_iconsdir/hicolor/16x16/apps/mountoid_connect_state.png
%_kde_iconsdir/hicolor/32x32/apps/mountoid_i_mounting.png
%_kde_iconsdir/hicolor/32x32/apps/mountoid_i_unmounting.png
%_kde_services/plasma-applet-mountoid.desktop
#---------------------------------------------------------------------

%prep
%setup -q -n %{srcname}

# switching from kdesudo to kdesu
sed -i 's|kdesudo|%{_libdir}/kde4/libexec/kdesu|g' device.cpp


%build
%cmake_kde4
%make

%install
%__rm -rf %buildroot
%makeinstall_std -C build


%clean
%__rm -rf %buildroot


%changelog
* Fri Dec 17 2010 John Balcaen <mikala@mandriva.org> 0.41-1mdv2011.0
+ Revision: 622736
- Update to 0.41
- Drop patch0 (merged upstream)
- Drop SOURCE1 (merged upstream)
- Fix file list

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Tue Jun 01 2010 John Balcaen <mikala@mandriva.org> 0.33-3mdv2010.1
+ Revision: 546872
- Add patch0 (submitted upstream) to fix linux icon name
- provides an icon from kappfinder

* Tue Apr 13 2010 John Balcaen <mikala@mandriva.org> 0.33-2mdv2010.1
+ Revision: 533755
- Use kdesu instead of kdesudo

* Sun Apr 11 2010 John Balcaen <mikala@mandriva.org> 0.33-1mdv2010.1
+ Revision: 533593
- import plasma-applet-mountoid

