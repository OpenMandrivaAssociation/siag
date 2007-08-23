Summary:	An office suite
Name:		siag
Version:	3.6.0
Release:	%mkrel 2
License:	GPL
URL:		http://siag.nu/
Group:		Office

Source:		%name-%version.tar.bz2
Source1:	siag_icons.tar.bz2 
Patch0:		siag-fix-compil.patch

BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires: libMowitz-devel >= 0.3.0 
BuildRequires: libneXtaw-devel libxpm-devel
BuildRequires: libncurses-devel tcl python libgdbm-devel

%description
Siag Office consists of :
- the word processor Pathetic Writer,
- the spreadsheet Siag,
- the animation program Egon Animator,
- the file manager Xfiler,
- the text editor Xedplus,
- the Postscript viewer Gvu.


%package common
Summary:	Common files for Siag Office
Group:		Office
Requires:	siag-plugins = %version
requires:	tcl, python, 

%description common
These are the scheme library files for siag,
and examples sheets. 

%package plugins
Summary:	Plugins for Siag Office
Group:		Office
Requires:	siag-common = %version
%description plugins
These are the standard plugins for use with Siag Office.

%package -n egon
Summary:	The animator program from Siag Office
Requires:	siag-common = %version
Group:		Office
%description -n egon
The animator part of the Siag Office suite, which also contains SIAG and PW.
Siag Office uses the Offix DND Drag-and-Drop protocol.

A WWW browser is needed to read online doc. A postscript viewer is used for
document preview.

Be warned that this probably is the least stable part of Siag Office. All
suggestions are welcomed. 

%package -n xsiag
Summary:	A spreadsheet with an X11 user-interface
Group:		Office
Requires:	siag-common = %version 
%description -n xsiag
The spreadsheet part of the Siag Office suite, which also contains
EGON and PW.
Siag Office uses the Offix DND Drag-and-Drop protocol.

Siag is a spreadsheet based on X and scheme. Being based on scheme
allows any user to expand the functionality of siag in just about
any way imaginable.

It can read and write 1-2-3 files for inter-operation with other
well-know spreadsheet programs.

You can enter expressions in several languages: C, guile, SIOD, Tcl.

A WWW browser is needed to read online doc. A postscript viewer
is used for document preview.

This one uses an X11 user interface based on the Athena toolkit.
You will find a text version in the `tsiag' package.


%package -n pw
Summary:	The Pathetic Writer word-processor
Group:		Office 
Requires:	siag-common = %version
%description -n pw
The word-processor part of the Siag Office suite, which also
contains SIAG and EGON.
Siag Office uses the Offix DND Drag-and-Drop protocol.

A WWW browser is needed to read online doc. A postscript viewer
is used for document preview.

It can read and write RTF and HTML files for inter-operation
with other well-known word-processors.
It should read also .doc files with help from catdoc.

%package -n tsiag
Summary:	Text version of the SIAG spreadsheet
Group:		Office
Requires:	siag-common = %version
%description -n tsiag
The spreadsheet part of the Siag Office suite.

Siag is a spreadsheet based on X and scheme. Being based on scheme
allows any user to expand the functionality of siag in just about
any way imaginable.

It can read and write 1-2-3 files for inter-operation with
other well-known spreadsheet programs.

You can enter expressions in several languages: C, guile, SIOD, Tcl.

This one uses a test-based user interface (ncurses). You will find
an X11 version in the `siag' package. 

#
# END-OF-PACKAGES
#

%prep

%setup -q
%patch0 -p0
 
%build 
 
%configure2_5x --with-stocks  

%make

%install
rm -fr %buildroot

%makeinstall_std

install -d -m 0755 %buildroot/%_docdir/%name-%version
mv %buildroot/%_prefix/doc/%name/* %buildroot/%_docdir/%name-%version/

 
install -d -m 0755 %buildroot/%_menudir
cat > %buildroot/%_menudir/xsiag <<EOF
?package(xsiag): \
command="siag" \
title="Siag" \
longtitle="Siag Office spreadsheet" \
needs="x11" \
section="Office/Spreadsheets" \
icon="siag_spreadsheet.png"
EOF

cat > %buildroot/%_menudir/pw <<EOF
?package(pw): \
command="pw" \
title="Pathetic Writer" \
longtitle="Siag Office Pathetic writer" \
needs="x11" \
section="Office/Wordprocessors" \
icon="siag_wordprocessor.png"
EOF

cat > %buildroot/%_menudir/siag-common<<EOF
?package(siag-common): \
command="xfiler" title="Xfiler" longtitle="Siag File manager" \
needs="x11" section="Applications/File Tools" icon="siag_file_tools.png"

?package(siag-common): \
command="xedplus" title="Xedplus" longtitle="Siag text editor" \
needs="x11" section="Applications/Editors" icon="siag_editors.png"

?package(siag-common): \
command="gvu" title="Gvu" longtitle="Siag Postscript viewer" \
needs="x11" section="Applications/Publishing" icon="siag_publishing.png"
EOF


cat > %buildroot/%_menudir/egon <<EOF
?package(egon): \
command="egon" \
title="Egon" \
longtitle="Siag Office Egon Animator" \
needs="x11" \
section="Office/Presentations" \
icon="siag_publishing3.png"
EOF


#mdk icons
mkdir -p $RPM_BUILD_ROOT%_iconsdir
tar xjf %SOURCE1 -C $RPM_BUILD_ROOT%_iconsdir

cd $RPM_BUILD_ROOT%_iconsdir
for i in  */ ./;do cp $i/siag_publishing.png $i/siag_publishing2.png;done
for i in  */ ./;do cp $i/siag_publishing.png $i/siag_publishing3.png;done
 
%post common
%update_menus
 
%postun common
%clean_menus
 
%post -n xsiag
%update_menus
 
%postun -n xsiag
%clean_menus
 
%post -n pw
%update_menus
 
%postun -n pw
%clean_menus
 
%post -n egon
%update_menus
 
%postun -n egon
%clean_menus

%clean
rm -fr %buildroot


%files common
%defattr (-,root,root)
%doc  AUTHORS COPYING FILES NLS README common/docs/ 
%_docdir/*/* 
%dir %_libdir/siag
%_bindir/gvu
%_bindir/mgptotxt
%_bindir/runcmd
%_bindir/siaghelp
%_bindir/siagrun
%_bindir/xedplus
%_bindir/xfiler
%_libdir/*/*/* 
%_datadir/%name
%_menudir/siag-common
%_iconsdir/siag_editors.png
%_miconsdir/siag_editors.png
%_liconsdir/siag_editors.png
%_iconsdir/siag_file_tools.png
%_miconsdir/siag_file_tools.png
%_liconsdir/siag_file_tools.png
%_iconsdir/siag_publishing.png
%_miconsdir/siag_publishing.png
%_liconsdir/siag_publishing.png
%_datadir/icons/mini/siag_editor.png
%_mandir/*/*

%files -n xsiag
%defattr (-,root,root)
%doc COPYING siag/docs/ siag/examples/
%_menudir/xsiag
%_bindir/siag
%_mandir/man1/siag.*
%_iconsdir/siag_spreadsheet.png
%_miconsdir/siag_spreadsheet.png
%_liconsdir/siag_spreadsheet.png

%files -n egon
%defattr (-,root,root)
%doc COPYING egon/docs/ egon/examples/ 
%_menudir/egon
%_bindir/egon
%_datadir/%name/egon/*
%_mandir/man1/egon.*
%_iconsdir/siag_publishing3.png
%_miconsdir/siag_publishing3.png
%_liconsdir/siag_publishing3.png

%files -n tsiag
%defattr (-,root,root)
%doc COPYING
%_bindir/tsiag
%_iconsdir/siag_publishing2.png
%_miconsdir/siag_publishing2.png
%_liconsdir/siag_publishing2.png

%files -n pw
%defattr (-,root,root)
%doc COPYING pw/docs/ pw/examples/ 
%_menudir/pw
%_bindir/pw
%_mandir/man1/pw.*
%_iconsdir/siag_wordprocessor.png
%_miconsdir/siag_wordprocessor.png
%_liconsdir/siag_wordprocessor.png

%files plugins
%defattr (-,root,root)
%doc COPYING 
%dir %_libdir/siag/plugins
%_libdir/siag/plugins/*
%_mandir/man1/dummy_plugin.*

