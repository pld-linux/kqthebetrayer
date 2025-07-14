Summary:	Classic RPG game based on KQlives engine
Summary(pl.UTF-8):	Klasyczna gra RPG oparta na silniku KQlives
Name:		kqthebetrayer
Version:	0.2.7
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/kqthebetrayer/%{name}%{version}src.tar.gz
# Source0-md5:	62eca9c1c67db749347e770c62e1f7fd
#Source1:	%{name}.desktop
URL:		http://virtualkingdoms.net/kqthebetrayer/
Source1:	%{name}.desktop
Patch0:		%{name}-naming_scheme.patch
Patch1:		%{name}-install_once.patch
BuildRequires:	allegro-devel >= 4.2.1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dumb-devel
BuildRequires:	lua50
BuildRequires:	lua50-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
“The Betrayer” is an RPG adventure written to run under the KQlives
engine. KQthebetrayer is a standalone game and is completely separate
from mainline KQlives. It is based in the same world as the Virtual
Kingdoms fantasy world building project.

%description -l pl.UTF-8
“The Betrayer” jest przygodowym RPG, korzystającym z silnika KQlives.
KQthebetrayer jest samodzielną grą, i jest kompletnie oddzielona od
głównej linii KQlives. Osadzona jest w tym samym świecie co Virtual
Kingdoms fantasy world building project.

%prep
%setup -q -n %{name}%{version}src
%patch -P0
%patch -P1 -p1
%{__sed} 's/luac/luac50/g' -i scripts/Makefile.{am,in}
# workaround for not fully cleaned scripts dir from compiled lua files:
rm scripts/*.lob

%build
CFLAGS="-I/usr/include/lua50 %{rpmcflags}"
LDFLAGS="-lm %{rpmldflags}"
%{__aclocal}
%{__autoconf}
%{__automake}
%{configure} \
	 --program-suffix=thebetrayer
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install debian/kq.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.xpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/scripts
%attr(755,root,root) %{_libdir}/%{name}/scripts/*.lob
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/data
%{_datadir}/%{name}/data/*
%dir %{_datadir}/%{name}/maps
%{_datadir}/%{name}/maps/*
%dir %{_datadir}/%{name}/music
%{_datadir}/%{name}/music/*
%{_mandir}/man6/%{name}.6*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.xpm
