Summary:	GNU PIES - Program Invocation and Execution Supervisor
Summary(pl.UTF-8):	GNU PIES - nadzorca wywoływania i wykonywania programów
Name:		pies
Version:	1.6
Release:	1
License:	GPL v3+
Group:		Daemons
Source0:	https://ftp.gnu.org/gnu/pies/%{name}-%{version}.tar.bz2
# Source0-md5:	46402d25b98b79f3d0abbf42293eaae8
Patch0:		%{name}-info.patch
URL:		https://www.gnu.org.ua/software/pies/
BuildRequires:	gettext-tools >= 0.19
BuildRequires:	pam-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Pies (pronounced "p-yes") stands for the Program Invocation and
Execution Supervisor. This utility starts and controls execution of
external programs, called "components". Each component is a
stand-alone program, designed to be executed in the foreground. Upon
startup pies reads the list of components from its configuration file,
starts them, and remains in the background, controlling their
execution. When a component terminates, pies tries to restart it. Its
configuration allows to specify actions other than simple restart,
depending on the exit code of the component.

%description -l pl.UTF-8
GNU Pies (wymawiane "pies") to skrót od Program Invocation and
Execution Supervisor (nadzorca wywoływania i wykonywania programów).
Narzędzie to uruchamia i kontroluje wykonywanie programów zewnętrznych
zwanych "komponentami". Każdy komponent to samodzielny program,
zaprojektowany do wykonywania pierwszoplanowego. Po uruchomieniu pies
czyta listę komponentów z pliku konfiguracyjnego, uruchamia je i
pozostaje w tle, kontrolując ich wykonywanie. Po przerwaniu działania
komponentu pies próbuje go zrestartować. Konfiguracja pozwala
określać akcje inne niż zwykły restart - w zależności od kodu wyjścia
komponentu.

%package inetd
Summary:	Pies inetd replacement
Summary(pl.UTF-8):	Zamiennik inetd dla psa
Group:		Daemons
Requires:	%{name} = %{version}-%{release}
# TODO: rc-inetd support
#Provides:	inetdaemon
Obsoletes:	inetdaemon
Obsoletes:	inetd

%description inetd
Pies inetd replacement.

%description inetd -l pl.UTF-8
Zamiennik inetd dla psa.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--disable-silent-rules \
	--enable-inetd \
	--enable-sysvinit
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/piesctl
%attr(755,root,root) %{_sbindir}/pies
%{_datadir}/pies
%{_infodir}/pies.info*

%files inetd
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/inetd
