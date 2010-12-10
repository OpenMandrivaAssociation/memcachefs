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
