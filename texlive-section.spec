Name:		texlive-section
Version:	20180
Release:	2
Summary:	Modifying section commands in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/section
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/section.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/section.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package implements a pretty extensive scheme to make more
manageable the business of configuring LaTeX output.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/section/section.sty
%doc %{_texmfdistdir}/doc/latex/section/section-doc.pdf
%doc %{_texmfdistdir}/doc/latex/section/section-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
