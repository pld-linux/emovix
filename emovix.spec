Summary:	Tiny CD distro
Summary(pl):	Ma³a dystrybucja na CD
Name:		emovix
Version:	0.9.0pre1
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/movix/%{name}-%{version}.tar.gz
# Source0-md5:	b0cf8ba50d1b1dc5680fcea3c892b71e
URL:		http://movix.sourceforge.net
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A micro Linux distro meant to be embedded in a CD together with all
video/audio files you want, so that the CD will be able to boot and
automagically play all of its own files. eMoviX CDs can now be written
with K3b (Linux), MoviXMaker (Linux) & MoviXISOCreator (Windows).

%description -l pl
Mikrodystrybucja która umieszczona na CD razem z dowolnymi plikami
audio/wideo bêdzie w stanie wystartowac komputer i automagicznie
odtworzyæ wszystkie te pliki. P³ytki z eMoviX-em mog± byæ nagrane przy
pomocy K3b (Linux), MoviXMaker (Linux) i MoviXISOCreator (Windows).

%prep
%setup -q -n %{name}-%{version}

%build
%configure
%{__make}

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/%{name}
%attr(755,root,root) %{_bindir}/*
