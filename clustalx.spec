Summary:	GUI interface for ClustalW
Name:		clustalx
Version:	2.1
Release:	2
License:	GPLv3 and LGPLv3
URL:		http://www.clustal.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
BuildRequires:	qt4-devel
Source:		http://www.clustal.org/download/%{version}/clustalx-%{version}.tar.gz
Group:		Sciences/Biology

%description
CLUSTAL W and CLUSTAL X Multiple Sequence Alignment Programs
                (version 2.1, 17th Nov 2010)

Contact email address: clustalw@ucd.ie

For details and citation purposes see paper "Clustal W and Clustal X
version 2.0", Larkin M., et al. Bioinformatics 2007 23(21):2947-2948
http://bioinformatics.oxfordjournals.org/cgi/content/full/23/21/2947

Clustal X provides a window-based user interface to the ClustalW
multiple alignment program.

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
%doc README COPYING COPYING.LESSER clustalx.hlp
%_bindir/*
%_datadir/applications/mandriva-%name.desktop
