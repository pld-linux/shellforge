%include /usr/lib/rpm/macros.python
Summary:	C to shellcode conversion programm
Summary(pl):	Program do konwersji program�w w C do shellcode
Name:		shellforge
Version:	0.1.14
Release:	1
License:	GPL v2+
Group:		Development/Languages
Source0:	http://www.cartel-info.fr/pbiondi/python/%{name}-%{version}.tar.gz
# Source0-md5:	4fa4e99303e7fc9b47f4534d2bea0b05
URL:		http://www.cartel-info.fr/pbiondi/shellforge.html
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
shellforge enables you to write shellcode programs in C. It transforms
C program code into shellcode that will run on a Linux/x86 system. It
provides macros to substitute libc calls with direct system calls and
a Python script to automate compilation, extraction, encoding, and
tests.

%description -l pl
shellforge pozwana na pisanie shellcode w j�zyku C. Dokonuje
translacji kodu w C na shellcode kt�ry uruchomi si� w �rodowisku
Linux/x86. Udost�pnia makra do podmiany wywo�a� funkcji libc z
bezpo�rednimi wywo�aniami oraz skrypt w Pythonie do automatyzacji
kompilacji, rozpakowywania, kodowania i test�w.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir}/%{name}}
install shellforge.py $RPM_BUILD_ROOT/%{_bindir}
install include/* $RPM_BUILD_ROOT/%{_includedir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc hello.c
%{_includedir}/%{name}
