Name:	    python-mako
Version:    1.0.6
Release:    2
Summary:    python2-mako
Group:      Graphics & UI Framework
Url:        https://www.archlinux.org/packages/extra/any/python2-mako/
License:    MIT 
Source:		%{name}-%{version}.tar.gz
Source1001: %{name}.manifest

#BuildRequires:  cmake
BuildRequires:	pkg-config
BuildRequires:  libtool
BuildRequires:  python

%description
Hyperfast and lightweight templating for the Python2 platform

%prep
%setup -q

%build
cp %{SOURCE1001} .

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}

cd usr
cp -apr bin %{buildroot}/usr/
cd lib
cp -apr . %{buildroot}%{_libdir}
cd ..
cp -apr share %{buildroot}/usr/

%files
%manifest %{name}.manifest 
%defattr(-,root,root,-)
%{_libdir}/*
/usr/bin/*
/usr/share/*
