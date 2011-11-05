# revision 20180
# category Package
# catalog-ctan /macros/latex/contrib/section
# catalog-date 2010-10-24 14:28:08 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-section
Version:	20101024
Release:	1
Summary:	Modifying section commands in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/section
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/section.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/section.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package implements a pretty extensive scheme to make more
manageable the business of configuring LaTeX output.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/section/section.sty
%doc %{_texmfdistdir}/doc/latex/section/section-doc.pdf
%doc %{_texmfdistdir}/doc/latex/section/section-doc.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
