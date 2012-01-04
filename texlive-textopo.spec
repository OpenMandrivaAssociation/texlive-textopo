# revision 23796
# category Package
# catalog-ctan /macros/latex/contrib/textopo
# catalog-date 2011-06-02 21:02:40 +0200
# catalog-license gpl
# catalog-version 1.5
Name:		texlive-textopo
Version:	1.5
Release:	2
Summary:	Annotated membrane protein topology plots
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/textopo
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textopo.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textopo.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textopo.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A LaTeX package for setting shaded and annotated membrane
protein topology plots and helical wheels.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/textopo/biotex.sty
%{_texmfdistdir}/tex/latex/textopo/textopo.def
%{_texmfdistdir}/tex/latex/textopo/textopo.sty
%doc %{_texmfdistdir}/doc/latex/textopo/AQP1.SP
%doc %{_texmfdistdir}/doc/latex/textopo/AQP1.hmm
%doc %{_texmfdistdir}/doc/latex/textopo/AQP1.phd
%doc %{_texmfdistdir}/doc/latex/textopo/AQP1.swp
%doc %{_texmfdistdir}/doc/latex/textopo/AQP1.tpo
%doc %{_texmfdistdir}/doc/latex/textopo/AQP2spec.ALN
%doc %{_texmfdistdir}/doc/latex/textopo/AQPpro.MSF
%doc %{_texmfdistdir}/doc/latex/textopo/AQPpro1.shd
%doc %{_texmfdistdir}/doc/latex/textopo/textopo.pdf
%doc %{_texmfdistdir}/doc/latex/textopo/textopo.txt
#- source
%doc %{_texmfdistdir}/source/latex/textopo/textopo.dtx
%doc %{_texmfdistdir}/source/latex/textopo/textopo.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
