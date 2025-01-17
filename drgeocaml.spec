%define name    drgeocaml
%define version cvs20051014
%define sionver cvs10142005
%define release %mkrel 7

%define title       Dr.GeoCaml
%define longtitle   DrGeoCaml Interactive Geometry Tool

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Dynamic geometry software
URL:            https://home.gna.org/geocaml/
License:        GPL
Group:          Sciences/Mathematics
Source0:        http://download.gna.org/geocaml/drgeocaml/%{name}-%{sionver}.tar.bz2
BuildRequires:  ocaml-lablgtk2-devel 
BuildRequires:  ocaml-xml-light-devel
BuildRequires:  ocaml-creal-devel
BuildRequires:  gtk+2-devel
BuildRequires:  gmp-devel
BuildRequires:  librsvg-devel
BuildRequires:  imagemagick
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
DrGeoCaml is a dynamic geometry software.
This program is an interactive geometry software similar to Cabri
Geometre,GeoPlan, Kig... 
It contains automatic theorem proving features. 
Interactive theorem proving is planned.

%prep
%setup -q -n %{name}

%build
make nc

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
make install BINDIR=%{buildroot}%{_bindir}

# menu entry

install -d -m 755 %{buildroot}%{_datadir}/applications
cat >  %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{title}
Comment=%{longtitle}
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=false
Categories=X-MandrivaLinux-MoreApplications-Sciences-Mathematics;Science;Math;
EOF

# icons
mkdir -p %{buildroot}%{_iconsdir} \
     %{buildroot}%{_miconsdir}
install -m 0644 -D      icons/%{name}.png %{buildroot}%{_liconsdir}/%{name}.png
convert -geometry 32x32 icons/%{name}.png %{buildroot}%{_iconsdir}/%{name}.png
convert -geometry 16x16 icons/%{name}.png %{buildroot}%{_miconsdir}/%{name}.png

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc AUTHORS INSTALL README README.i18n TODO FAQ
%{_bindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

