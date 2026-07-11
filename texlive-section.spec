%global tl_name section
%global tl_revision 20180

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Modifying section commands in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/section
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/section.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/section.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package implements a pretty extensive scheme to make more manageable
the business of configuring LaTeX output.

