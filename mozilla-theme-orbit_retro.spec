Summary:	The best looking theme for Mozilla - retro style
Summary(pl):	Najlepszy temat dla Mozilli jaki kiedykolwiek powsta³ - styl retro
Name:		mozilla-theme-orbit_retro
%define		_realname	orbit_r
%define		_snap		1_0-20020619
Version:	0.0.4
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.alfordot.com/e/p/cdn/orbit3/%{_realname}-%{_snap}.jar
Source1:	%{_realname}-installed-chrome.txt
URL:		http://themes.mozdev.org/skins/retro.html
BuildArch:	noarch
Requires:	mozilla >= 1.0-7
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_libdir}/mozilla/chrome

%description
The best looking theme for Mozilla - retro style.

%description -l pl
Najlepszy temat dla Mozilli jaki kiedykolwiek powsta³ - styl retro.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install %{SOURCE0} %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

mv -f $RPM_BUILD_ROOT%{_chromedir}/%{_realname}-%{_snap}.jar \
	$RPM_BUILD_ROOT%{_chromedir}/%{_realname}.jar

%post 
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
