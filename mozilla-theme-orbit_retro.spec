Summary:	The best looking theme for Mozilla - retro style
Summary(pl):	Najlepszy motyw dla Mozilli jaki kiedykolwiek powsta³ - styl retro
Name:		mozilla-theme-orbit_retro
%define		_realname	orbit_r
%define	fver	1_4-20030830
Version:	0.0.7.2
Release:	2
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.uk1.mozdev.org/rsync/themes/themes/%{_realname}-%{fver}.jar
# Source0-md5:	889d93a3afc640563acdc2b4236373c7
Source1:	%{_realname}-installed-chrome.txt
URL:		http://themes.mozdev.org/themes/retro.html
BuildRequires:	perl-base
BuildRequires:	unzip
BuildRequires:	zip
Requires(post,postun):	textutils
Requires:	mozilla = 5:1.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_libdir}/mozilla/chrome

%description
The best looking theme for Mozilla - retro style.

%description -l pl
Najlepszy motyw dla Mozilli jaki kiedykolwiek powsta³ - styl retro.

%prep
%setup -c

%build
%{__perl} -pi -e 's/(skinVersion=)"1\.[0-9]"/$1"1.5"/' contents.rdf
find -name "*.css" | xargs %{__perl} -pi -e 's/:-moz-/::-moz-/'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

zip -r $RPM_BUILD_ROOT%{_chromedir}/%{_realname}.jar *

install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
