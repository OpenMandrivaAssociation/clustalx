Summary:	GUI interface for ClustalW
Name:		clustalx
Version:	2.0.11
Release:	%mkrel 1
License:	Redistributable when non-commercial
URL:		http://www.clustal.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
BuildRequires:	qt4-devel
Source:		http://www.clustal.org/download/%{version}/clustalx-%{version}.tar.gz
Group:		Sciences/Biology

%description
Clustal X is a windows interface for the ClustalW multiple sequence
alignment program. It provides an integrated environment for performing
multiple sequence and profile alignments and analysing the results. The
sequence alignment is displayed in a window on the screen. A versatile
coloring scheme has been incorporated allowing you to highlight conserved
features in the alignment. The pull-down menus at the top of the window
allow you to select all the options required for traditional multiple
sequence and profile alignment.

Users are free to redistribute ClustalW or ClustalX in it's unmodified
form as long as it is not for commercial gain.

Anyone wishing to redistribute Clustal commercially should contact Toby
Gibson at gibson@embl.de

%prep
%setup -q clustalx-%{version}
rm -f moc_*

%build
%qmake_qt4
%make

%install
rm -fr %buildroot
mkdir -p %buildroot%_bindir
install -m755 clustalx %buildroot%_bindir/clustalx

mkdir -p %buildroot%_datadir/applications
cat << EOF > %buildroot%_datadir/applications/mandriva-%name.desktop
[Desktop Entry]
Name=Clustal X
Comment=GUI interface for ClustalW
Exec=%{name}
Icon=biology
Terminal=false
Type=Application
Categories=Biology;Science;Qt;
EOF

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
%doc README LICENSE clustalx.hlp
%_bindir/*
%_datadir/applications/mandriva-%name.desktop
