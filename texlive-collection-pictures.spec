# revision 25777
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-pictures
Epoch:		1
Version:	20120413
Release:	1
Summary:	Graphics packages and programs
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-pictures.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-adjustbox
Requires:	texlive-asyfig
Requires:	texlive-autoarea
Requires:	texlive-bardiag
Requires:	texlive-bloques
Requires:	texlive-bodegraph
Requires:	texlive-bondgraph
Requires:	texlive-braids
Requires:	texlive-cachepic
Requires:	texlive-chemfig
Requires:	texlive-combinedgraphics
Requires:	texlive-circuitikz
Requires:	texlive-curve
Requires:	texlive-curve2e
Requires:	texlive-curves
Requires:	texlive-dcpic
Requires:	texlive-diagmac2
Requires:	texlive-doc-pictex
Requires:	texlive-dottex
Requires:	texlive-dot2texi
Requires:	texlive-dratex
Requires:	texlive-drs
Requires:	texlive-duotenzor
Requires:	texlive-eepic
Requires:	texlive-epspdf
Requires:	texlive-epspdfconversion
Requires:	texlive-esk
Requires:	texlive-fig4latex
Requires:	texlive-gincltex
Requires:	texlive-gnuplottex
Requires:	texlive-gradientframe
Requires:	texlive-grafcet
Requires:	texlive-here
Requires:	texlive-hvfloat
Requires:	texlive-knitting
Requires:	texlive-knittingpattern
Requires:	texlive-lapdf
Requires:	texlive-lpic
Requires:	texlive-mathspic
Requires:	texlive-miniplot
Requires:	texlive-modiagram
Requires:	texlive-numericplots
Requires:	texlive-pb-diagram
Requires:	texlive-petri-nets
Requires:	texlive-pgf
Requires:	texlive-pgf-soroban
Requires:	texlive-pgf-umlsd
Requires:	texlive-pgfgantt
Requires:	texlive-pgfmolbio
Requires:	texlive-pgfopts
Requires:	texlive-pgfplots
Requires:	texlive-piano
Requires:	texlive-picinpar
Requires:	texlive-pict2e
Requires:	texlive-pictex
Requires:	texlive-pictex2
Requires:	texlive-pinlabel
Requires:	texlive-pmgraph
Requires:	texlive-prerex
Requires:	texlive-productbox
Requires:	texlive-randbild
Requires:	texlive-randomwalk
Requires:	texlive-reotex
Requires:	texlive-roundbox
Requires:	texlive-rviewport
Requires:	texlive-schemabloc
Requires:	texlive-swimgraf
Requires:	texlive-texdraw
Requires:	texlive-tikz-cd
Requires:	texlive-tikz-3dplot
Requires:	texlive-tikz-dependency
Requires:	texlive-tikz-inet
Requires:	texlive-tikz-qtree
Requires:	texlive-tikz-timing
Requires:	texlive-tikzpagenodes
Requires:	texlive-tikzpfeile
Requires:	texlive-tqft
Requires:	texlive-tkz-base
Requires:	texlive-tkz-berge
Requires:	texlive-tkz-doc
Requires:	texlive-tkz-euclide
Requires:	texlive-tkz-fct
Requires:	texlive-tkz-graph
Requires:	texlive-tkz-kiviat
Requires:	texlive-tkz-linknodes
Requires:	texlive-tkz-orm
Requires:	texlive-tkz-tab
Requires:	texlive-tsemlines
Requires:	texlive-tufte-latex
Requires:	texlive-xypic
Requires:	texlive-collection-basic

%description
TeXLive collection-pictures package.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install


%changelog
* Sat Apr 14 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120413-1
+ Revision: 790885
- Update to latest release.

* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780506
- Update to latest release.
- Import texlive-collection-pictures
- Import texlive-collection-pictures

