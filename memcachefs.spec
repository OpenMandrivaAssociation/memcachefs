Name:           memcachefs
Version:        0.5
Release:        %mkrel 4
Epoch:          0
Summary:        Filesystem which mounts the memcache server
License:        GPLv2+
Group:          System/Kernel and hardware
URL:            http://memcachefs.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Requires:       kmod(fuse)
Requires:       fuse
BuildRequires:  fuse-devel
BuildRequires:  memcache-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
memcachefs is FUSE-based filesystem which mounts the memcache
server. It allows you to view cache data of memcached as if they
were regular files.

%prep
%setup -q

%build
%{configure2_5x}
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%clean 
%{__rm} -rf %{buildroot} 

%files 
%defattr(0644,root,root,0755)
%doc AUTHORS ChangeLog INSTALL NEWS README
%attr(-,root,root) %{_bindir}/memcachefs
%{_mandir}/man1/memcachefs.1*


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0:0.5-4mdv2011.0
+ Revision: 620319
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0:0.5-3mdv2010.0
+ Revision: 430016
- rebuild

* Tue Jul 15 2008 Adam Williamson <awilliamson@mandriva.org> 0:0.5-2mdv2009.0
+ Revision: 236167
- require kmod(fuse) not dkms-fuse
- don't package COPYING
- new license policy
- better source location

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Aug 11 2007 David Walluck <walluck@mandriva.org> 0:0.5-1mdv2008.0
+ Revision: 61866
- fix Group
- Import memcachefs

