%define name    konvertible        
%define version 0.1.4    
%define release %mkrel 1           
 
Name:           %name
Version:        %version
Release:        %release
Source0:        http://kde-apps.org/CONTENT/content-files/116892-%name-%version.tar.bz2
Summary:        A simple KDE audio converter                                      
License:        GPLv2                                                                  
Group:          Sound                                                             
Url:            http://kde-apps.org/content/show.php/Konvertible?content=116892                                 
BuildRoot:      %{_tmppath}/%{name}-%{version}                  
BuildRequires:  kdelibs4-devel kdepimlibs4-devel
Requires:       kdebase4-runtime ffmpeg
 
%description
The Konvertible is a program to convert audio files to other audio formats using ffmpeg. The Konvertible simplifies file conversion for ffmpeg users. You can add more than one audio file and then click the convert button to transcode them one after the other.

 
%prep
%setup -q
 
%build
%cmake_kde4
%make
 
%install
rm -rf %{buildroot}
%{makeinstall_std} -C build
 



%files
%defattr(-,root,root)
%doc INSTALL COPYING README TODO
%{_bindir}/konvertible
%{_datadir}/applications/kde4/konvertible.desktop
%{_datadir}/icons/*
%{_defaultdocdir}/HTML/en/konvertible/*.*
%{_defaultdocdir}/HTML/en/konvertible/common


 
%clean
rm -rf %{buildroot}
 
%post
%update_icon_cache hicolor
 
%postun
%clean_icon_cache hicolor

