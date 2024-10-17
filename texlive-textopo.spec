Name:		texlive-textopo
Version:	23796
Release:	2
Summary:	Annotated membrane protein topology plots
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/textopo
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textopo.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textopo.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/textopo.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
