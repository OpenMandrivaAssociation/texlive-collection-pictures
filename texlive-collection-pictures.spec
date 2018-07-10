# revision 33688
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-pictures
Epoch:		1
Version:	20180601
Release:	2
Summary:	Graphics, pictures, diagrams
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-pictures.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-aobs-tikz
Requires:	texlive-askmaps
Requires:	texlive-asyfig
Requires:	texlive-asypictureb
Requires:	texlive-autoarea
Requires:	texlive-bardiag
Requires:	texlive-bloques
Requires:	texlive-bodegraph
Requires:	texlive-bondgraph
Requires:	texlive-braids
Requires:	texlive-bxeepic
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
Requires:	texlive-fast-diagram
Requires:	texlive-fig4latex
Requires:	texlive-flowchart
Requires:	texlive-forest
Requires:	texlive-gincltex
Requires:	texlive-gnuplottex
Requires:	texlive-gradientframe
Requires:	texlive-grafcet
Requires:	texlive-graphviz
Requires:	texlive-harveyballs
Requires:	texlive-here
Requires:	texlive-hf-tikz
Requires:	texlive-hobby
Requires:	texlive-hvfloat
Requires:	texlive-knitting
Requires:	texlive-knittingpattern
Requires:	texlive-lapdf
Requires:	texlive-lpic
Requires:	texlive-makeshape
Requires:	texlive-mathspic
Requires:	texlive-miniplot
Requires:	texlive-mkpic
Requires:	texlive-modiagram
Requires:	texlive-neuralnetwork
Requires:	texlive-numericplots
Requires:	texlive-pb-diagram
Requires:	texlive-petri-nets
Requires:	texlive-pgf
Requires:	texlive-pgf-blur
Requires:	texlive-pgf-soroban
Requires:	texlive-pgf-umlcd
Requires:	texlive-pgf-umlsd
Requires:	texlive-pgfgantt
Requires:	texlive-pgfkeyx
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
Requires:	texlive-pxpgfmark
Requires:	texlive-randbild
Requires:	texlive-randomwalk
Requires:	texlive-reotex
Requires:	texlive-rviewport
Requires:	texlive-sa-tikz
Requires:	texlive-schemabloc
Requires:	texlive-setdeck
Requires:	texlive-smartdiagram
Requires:	texlive-spath3
Requires:	texlive-swimgraf
Requires:	texlive-texdraw
Requires:	texlive-tikz-3dplot
Requires:	texlive-tikz-bayesnet
Requires:	texlive-tikz-cd
Requires:	texlive-tikz-dependency
Requires:	texlive-tikz-inet
Requires:	texlive-tikz-opm
Requires:	texlive-tikz-qtree
Requires:	texlive-tikz-timing
Requires:	texlive-tikzinclude
Requires:	texlive-tikzmark
Requires:	texlive-tikzorbital
Requires:	texlive-tikzpagenodes
Requires:	texlive-tikzpfeile
Requires:	texlive-tikzposter
Requires:	texlive-tikzscale
Requires:	texlive-tikzsymbols
Requires:	texlive-timing-diagrams
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
Requires:	texlive-venndiagram
Requires:	texlive-xpicture
Requires:	texlive-xypic

%description
Including TikZ, pict, etc., but MetaPost and PStricks are
separate.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
