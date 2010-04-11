%define name	plasma-applet-mountoid
%define srcname	mountoid
%define version	0.33
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
%_kde_services/plasma-applet-mountoid.desktop

#---------------------------------------------------------------------

%prep
%setup -q -n %{srcname}

%build
%cmake_kde4
%make

%install
%__rm -rf %buildroot
%makeinstall_std -C build

%clean
%__rm -rf %buildroot
