Summary:	Doulos SIL - TrueType Fonts
Summary(pl.UTF-8):	Doulos SIL - fonty TrueType
Name:		fonts-TTF-DoulosSIL
Version:	4.106
Release:	1
License:	SIL OFL
Group:		Fonts
# Source0Download:	http://scripts.sil.org/cms/scripts/render_download.php?site_id=nrsi&format=file&media_id=DoulosSIL4.106b.zip&filename=DoulosSIL4.106.zip
Source0:	DoulosSIL%{version}.zip
# Source0-md5:	db548b9854ce7cc673c94c92d59fd95c
URL:		http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&item_id=DoulosSILfont
BuildRequires:	unzip
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
The goal for this product was to provide a single Unicode-based font
family that would contain a comprehensive inventory of glyphs needed
for almost any Roman- or Cyrillic-based writing system, whether used
for phonetic or orthographic needs. In addition, there is provision
for other characters and symbols useful to linguists. This font makes
use of state-of-the-art font technologies to support complex
typographic issues, such as the need to position arbitrary
combinations of base glyphs and diacritics optimally.

Doulos is very similar to Times/Times New Roman, but only has a single
face - regular. It is intended for use alongside other Times-like
fonts where a range of styles (italic, bold) are not needed.

%description -l pl.UTF-8
Przeznaczeniem niniejszego produktu jest zaoferowanie jednej
unikodowej rodziny fontów, która zawiera obszerny inwentarz glifów
potrzebnych do niemal każdego systemu pisma opartego na alfabecie
łacińskim bądź cyrylicy, zarówno dla potrzeb fonetycznych, jak i
ortograficznych. Dodatkowo dostarczone są znaki i symbole użyteczne
dla językoznawców. Font ten używa najnowszych technik fontów
wspierających złożone zagadnienia typograficzne, takie jak optymalne
pozycjonowanie dowolnych kombinacji glifów bazowych i diakrytyków.

Doulos jest bardzo podobny do fontu Times/Times New Roman, ale zawiera
tylko jeden krój: zwykły. Jest przeznaczony do użycia razem z innymi
fontami podobnymi do Timesa, gdzie zestaw stylów (kursywa, pogrubiony)
nie jest potrzebny.

%prep
%setup -q -n DoulosSIL

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ttffontsdir}

install *.ttf $RPM_BUILD_ROOT%{ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc *.txt
%{ttffontsdir}/DoulosSIL*.ttf
