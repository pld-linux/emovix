Summary:	Tiny CD distro
Summary(pl):	Ma³a dystrybucja na CD
Name:		emovix
Version:	0.9.0
Release:	1
Epoch:          1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/movix/%{name}-%{version}.tar.gz
# Source0-md5:	a96492f338824b24c5a9e714c57eddcf
URL:		http://movix.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A micro Linux distro meant to be embedded in a CD together with all
video/audio files you want, so that the CD will be able to boot and
automagically play all of its own files. eMoviX CDs can now be written
with K3b (Linux), MoviXMaker (Linux) & MoviXISOCreator (Windows).

%description -l pl
Mikrodystrybucja, która umieszczona na CD razem z dowolnymi plikami
audio/wideo bêdzie w stanie wystartowaæ komputer i automagicznie
odtworzyæ wszystkie te pliki. P³ytki z eMoviksem mog± byæ nagrane przy
pomocy K3b (Linux), MoviXMaker (Linux) i MoviXISOCreator (Windows).

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README* TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
