---
title: Presentations and posters
---

\documentclass[12pt,t]{beamer}
\usepackage{graphicx}
\setbeameroption{hide notes}
\setbeamertemplate{note page}[plain]
\usepackage{listings}

\input{../LaTeX/header.tex}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% end of header
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\title{}
\subtitle{Tools for Reproducible Research}
\author{[Karl Broman](http://kbroman.org)}
\institute{Biostatistics \& Medical Informatics, UW{\textendash}Madison}
\date{[\tt \scriptsize \color{foreground](http://kbroman.org) kbroman.org}
\\[-4pt]
[\tt \scriptsize \color{foreground](http://github.com/kbroman) github.com/kbroman}
\\[-4pt]
[\tt \scriptsize \color{foreground](https://twitter.com/kwbroman) @kwbroman}
\\[-4pt]
{\scriptsize Course web: [\tt kbroman.org/Tools4RR](http://kbroman.org/Tools4RR)}
}

\begin{document}

{
\setbeamertemplate{footline}{} % no page number here
\frame{
  \titlepage


  It's arguably less critical that presentation slides or a poster be
  reproducible. Nevertheless, there can be great personal advantage to
  the automated generation of figures and such in slides or a poster:
  if the primary data should change, or if some analysis mistake is
  discovered, it will be easier to revise the presentation.

  My primary goal is to get you to ditch Powerpoint/Keynote in favor
  of reproducible alternatives. I will primarily focus on the Beamer
  package for LaTeX, for both slides and posters. But I will also
  touch upon the use of slidify to make Markdown-based slides for a
  talk.

} }


## Powerpoint/Keynote



\begin{minipage}[t]{0.45\textwidth}

* [+] Standard
* [+] Easy to share slides
* [+] WYSIWYG (mostly)
* [+] Fancy animations
\end{minipage}

\begin{minipage}[t]{0.45\textwidth}

* [\textendash] Font problems
* [\textendash] Lots of copy-paste
* [\textendash] Hard to get equations
* [\textendash] Not reproducible
\end{minipage}


  Powerpoint and Keynote do have their advantages, the principal one
  being that everyone is using these tools, which makes it easy to
  share slides with friends.

  But we've all seen terrible font problems in important
  presentations, mostly due to incompatibilities between
  Windows and Mac versions of Powerpoint: fonts should be, but aren't,
  embedded in the presentation.

  And insertion of figures requires tedious copy-paste, usually followed
  by manual resizing and adjustment of figure placement.
  And if the figures are revised (because the data changed or some
  mistake was found in the analysis), we'll have to repeat all of
  that.




## \LaTeX/ Beamer package



\figh{Figs/Copenhagen-default-default-01.png}{0.75}


  Until recently, I'd been making \LaTeX/ slides using the {\tt
  article document class, just revising the page size and make the
  fonts big.

  The Beamer package for \LaTeX/ is easier, but I was turned off
  by the standard slides that people were producing with Beamer, such
  as the one shown: far too much junk on the screen, and on every
  single slide.

  You can get rid of all of that. All of the slides I'm making
  for this course are produced with Beamer.

  There's good facility for adding simple animations (progressively
  showing or hiding different elements on the slide).

  But you {\nhilit are} writing \LaTeX, so the coding can be a bit verbose.
}




## Get rid of the junk





```
\usetheme{default}

\beamertemplatenavigationsymbolsempty
```


  The first thing to do is to get rid of all of the junk.

  It's surprisingly easy: default theme and remove navigation symbols.




## Change colors



```
\definecolor{foreground}{RGB}{255,255,255}
\definecolor{background}{RGB}{24,24,24}
\definecolor{title}{RGB}{107,174,214}
\definecolor{subtitle}{RGB}{102,255,204}
\definecolor{hilit}{RGB}{102,255,204}
\definecolor{lolit}{RGB}{155,155,155}

\setbeamercolor{titlelike}{fg=title}
\setbeamercolor{subtitle}{fg=subtitle}
\setbeamercolor{institute}{fg=lolit}
\setbeamercolor{normal text}{fg=foreground,bg=background}
\setbeamercolor{item}{fg=foreground} % color of bullets
\setbeamercolor{subitem}{fg=lolit}
\setbeamercolor{itemize/enumerate subbody}{fg=lolit}
\setbeamertemplate{itemize subitem}{{\textendash}}
\setbeamerfont{itemize/enumerate subbody}{size=\footnotesize}
\setbeamerfont{itemize/enumerate subitem}{size=\footnotesize}

\newcommand{}{\color{hilit}}
\newcommand{\lolit}{\color{lolit}}
```


  I prefer light text on a dark background.

  The tricky part is that Beamer has special names for
  everything.

  It would be best if I created a new theme, but I don't want to take
  the time to figure that out.



## Also, slide numbers and fonts



```
% slide number
\setbeamertemplate{footline}{%
 \raisebox{5pt}{\makebox[\paperwidth]{\makebox[20pt]{\lolit
  \scriptsize\insertframenumber}}}\hspace*{5pt}}

% font
\usepackage{fontspec}
% http://www.gust.org.pl/projects/e-foundry/tex-gyre/
%      ...   heros/qhv2.004otf.zip
\setsansfont
  [ ExternalLocation = ../fonts/ ,
    UprightFont = *-regular ,
    BoldFont = *-bold ,
    ItalicFont = *-italic ,
    BoldItalicFont = *-bolditalic ]{texgyreheros}
% Palatino for notes
\setbeamerfont{note page}{family*=pplx,size=\footnotesize}
```


  I also want the slide number in the bottom-right, and I want a
  different font: something a bit more blocky, which I think is easier
  to read on the screen.





## Title slide



```
\title{Put title here}
\subtitle{And maybe a subtitle}
\author{Author name}
\institute{Biostatistics \& Medical Informatics,
   UW{\textendash}Madison}
\date`\scriptsize biostat.wisc.edu/{~`kbroman}

\begin{document}

{
\setbeamertemplate{footline}{} % no slide number here
\frame{
  \titlepage


  Summary of the talk, as a note.

} }
```


  The title slide is created with `{/`titlepage,
  having first defined `{/`title},
  `{/`author}, etc.

  The extra curly braces are to get the "no slide number" to apply
  just to the title slide. You can put notes on slides and then make a
  version that has the slide above the notes. See what I do with the
  slides for this course, or ask me for help.
}



% this is to get  within the lstlisting environment
% See http://tex.stackexchange.com/questions/73366/
\newsavebox{\codeboxone}
\begin{lrbox}{\codeboxone}
```
## Title of slide



*  Bullet 1
 *  Bullet 2
 *  Bullet 3

  Put a note here


```
\end{lrbox}

## Typical slide



\usebox{\codeboxone}




% this is to get  within the lstlisting environment
% See http://tex.stackexchange.com/questions/73366/
\newsavebox{\codeboxtwo}
\begin{lrbox}{\codeboxtwo}
```
## Title of slide



 \begin{itemize} * sep8pt
 *  Bullet 1
 *  Bullet 2
 *  Bullet 3
\end{itemize}


  Put a note here


```
\end{lrbox}

## Typical slide


\addtocounter{framenumber}{-1}

\usebox{\codeboxtwo}


  A typical slide is set between `{/`begin\{frame\\{title\}}
  and `{/`end\{frame\}}.

  You get bullet points with the `itemize` environment. I'll mess
  around a bit with `{/`vspace} and
  `{/`itemsep}. And I'll create shortcuts with
  `{/`newcommand} for these.
}



% this is to get  within the lstlisting environment
% See http://tex.stackexchange.com/questions/73366/
\newsavebox{\codeboxthree}
\begin{lrbox}{\codeboxthree}
```
## Title of slide



\figh{Figs/a_figure.png}{0.75}



  Put a note here


```
\end{lrbox}


## Slide with a figure



\usebox{\codeboxthree}



% this is to get  within the lstlisting environment
% See http://tex.stackexchange.com/questions/73366/
\newsavebox{\codeboxfour}
\begin{lrbox}{\codeboxfour}
```
## Title of slide



\centerline{\includegraphics[height=0.75\textheight]{%
            Figs/a_figure.png}}


  Put a note here


```
\end{lrbox}


## Slide with a figure


\addtocounter{framenumber}{-1}

\usebox{\codeboxfour}


  I'd typically generate figures externally and include them with
  `{/`includegraphics.
}




## Figures with KnitR



```
<<knitr_options, echo=FALSE>>=
opts_chunk$set(echo=FALSE, fig.height=7, fig.width=10)
change_colors <-
function(bg=rgb(24,24,24, maxColorValue=255), fg="white")
  par(bg=bg, fg=fg, col=fg, col.axis=fg, col.lab=fg,
      col.main=fg, col.sub=fg)
@

<<pdf_figure>>=
change_colors()
par(las=1)
n <- 100
x <- rnorm(n)
y <- 2*x + rnorm(n)
plot(x, y, pch=16, col="slateblue")
@
```


  You could use a knitr code chunk, in the same way we discussed
  for manuscripts, in the last lecture.




## Figures with KnitR



```
% << >>= all on one line!
<<png_figure, dev="png", fig.align="center",
  dev.args=list(pointsize=30),
  fig.height=15, fig.width=15, out.height="0.75\\textheight",
  out.width="0.75\\textheight">>=
change_colors(bg=rgb(32,32,32,maxColorValue=255))
par(las=1)
n <- 251
x <- y <- seq(-pi, pi, len=n)
z <- matrix(ncol=n, nrow=n)
for(i in seq(along=x))
  for(j in seq(along=y))
    z[i,j] <- sin(x[i]) + cos(y[j])
image(x,y,z)
@
```


  To create a PNG figure (which can give much smaller file sizes for
  things like an image or a dense scatterplot), use the chunk option
  `dev="png"`.

  For some reason, RGB colors don't match well between PNG files and
  the PDF, so I have to muck about to get the background of the PNG to
  match the background on the slides.

  It's also a bit of work to get the resolution and text size just
  right.

  I split the initial line defining the code chunk across multiple
  lines here, so it could all be seen, but in practice the whole
  `<< >>=` bit needs to be on one line.




## Slides with notes



```
\documentclass[12pt,t]{beamer}
\setbeameroption{hide notes}
\setbeamertemplate{note page}[plain]
```



```
\documentclass[12pt,t,handout]{beamer}
\setbeameroption{show notes}
\setbeamertemplate{note page}[plain]
\def\notescolors{1}
```



```
\ifx\notescolors\undefined % slides
  \definecolor{foreground}{RGB}{255,255,255}
  \definecolor{background}{RGB}{24,24,24}
\else % notes
  \definecolor{background}{RGB}{255,255,255}
  \definecolor{foreground}{RGB}{24,24,24}
\fi
```


  To create a version of your slides with notes, include
  `{/`note\{ \} on every slide.

  I then include the code in the top box in the slide version, the
  middle box in the note version, and the stuff at the bottom in both.
  The bit at the bottom selects colors to be light text on a dark
  background in the slides and dark text on a light
  background in the notes version.

  I wrote a ruby script to create a notes version from the slide
  version (replace the code in the top box with the code in the middle
  box).

  I then use `pdfnup` (part of PDFjam) to make 2-up pages (slides
  at the top, notes at the bottom). The only problem with `pdfnup`
  is that it strips off all of the hyperlinks.
}



% this is to get  within the lstlisting environment
% See http://tex.stackexchange.com/questions/73366/
\newsavebox{\codeboxfive}
\begin{lrbox}{\codeboxfive}
```
## Bullets entering one at a time



*  Bullet 1
\onslide<2->{*  Bullet 2}
\onslide<3->{*  Bullet 3}
\onslide<4->{*  Bullet 4}

  Do this sparingly.


```
\end{lrbox}

## Simple animations



\usebox{\codeboxfive}


  It's easy to add a bit of animation, such as with bullets appearing
  one by one. Use `{/`onslide or
  `{/`only}.

  Here, the bullets will appear one at a time.

  Beamer just expands the PDF, with this slide becoming multiple
  pages.
}



% this is to get  within the lstlisting environment
% See http://tex.stackexchange.com/questions/73366/
\newsavebox{\codeboxsix}
\begin{lrbox}{\codeboxsix}
```
## Bullets entering one at a time



*  \only<1>{\color{foreground} Bullet 1}
*  \only<2>{\color{foreground} Bullet 2}
*  \only<3>{\color{foreground} Bullet 3}
*  \only<4>{\color{foreground} Bullet 4}

  Do this sparingly.


```
\end{lrbox}



## Simple animations



\usebox{\codeboxsix}


  In this version, the bullets will go from dim to bright, one at a
  time.





## Slidify and R Markdown



\figh{Figs/slidify.png}{0.75}




## Slidify and R Markdown


\addtocounter{framenumber}{-1}

```
## Slide title

- Bullet 1
- Bullet 2
- Bullet 3
- Bullet 4

---

## A figure

"`{r a_figure, echo=FALSE, fig.align="center"}
par(las=1)
n <- 100
x <- rnorm(n)
y <- 2*x + rnorm(n)
plot(x, y, pch=16, col="slateblue")
"`
```


  Slidify makes it super easy to create html-based slides with R
  Markdown. Three dashes separate slides, and two pound symbols
  (section heading) indicate the slide title.

  The chief advantage is that you can make nice slides with very little
  markup. And there are a ton of options, like having embedded
  quizzes.

  The disadvantage is that it's a bit harder to get fine control of
  the layout. And I've found it a bit risky to use html-based slides
  for a presentation. PDF is more trustworthy.

  In principle, you can use pandoc to convert the slides to PDF, but
  I've not been happy with the result. You could also print them from
  the browser, but I only got a good result with Safari. (Firefox
  included some links on the first page, and Chrome produced total
  garbage.)

  Personally, I'm going to stick with Beamer for important
  presentations, but slidify seems good for informal presentations
  (e.g., to collaborators) or for a course.




## Using slidify



```
library(devtools)
install_github("slidify", "ramnathv")
install_github("slidifyLibraries", "ramnathv")

library(slidify)
setwd("~/Docs/Talks/")
author("slidify_example")

# edit ~/Docs/Talks/slidify_example/index.Rmd

slidify("index.Rmd")
browseURL("index.html")
```


  To use slidify, download the slidify and slidifyLibraries packages
  from GitHub, and use `author()` to create the file to edit, and
  then `slidify()` to compile the result.

  Note that `author("slidify_example")` changes the working
  directory.




## YAML header



```
---
title       : Slidify example
subtitle    : Tools for reproducible research
author      : Karl Broman
job         : Biostatistics & Medical Informatics, UW-Madison
framework   : io2012        # {io2012, html5slides, shower, ...}
highlighter : highlight.js  # {highlight.js, prettify, highlight}
hitheme     : tomorrow      #
widgets     : [mathjax]     # {mathjax, quiz, bootstrap}
mode        : standalone    # {selfcontained, standalone, draft}
---
```


  There's a bit at the top of the file to define the slide title and
  layout.

  `framework` defines the slide style. `highlighter` is the
  method to give syntax highlighting. With `mode` "standalone,"
  some otherwise-external files are embedded in the html file.

  YAML is a "human-readable data serialization format."
  (Serialization means it can be easily transmitted over a network.)
  It's a well-defined way of describing potentially complex
  data objects.





## Change the title slide colors



```
<style>
.title-slide {
  background-color: #EEE;
}

.title-slide hgroup > h1,
.title-slide hgroup > h2 {
  color: #005;
}
</style>
```


  The default colors for the title slide with framework `io2012`
  are really terrible. Include a bit of CSS code in your `.Rmd`
  file to fix that.

  There are a bunch of named colors in html, or you can use codes like
  "`\#005;`" or "`\#000055;`" for RGB (R=00, G=00, B=55).




## Beamer-based posters





\figh{Figs/mathbio2011.png}{0.75}



 [\tt
    \lolit \scriptsize github.com/kbroman/Poster_SampleMixups](https://github.com/kbroman/Poster_SampleMixups)


## Beamer-based posters


\addtocounter{framenumber}{-1}



\figh{Figs/enar2014.png}{0.75}



 [\tt
    \lolit \scriptsize github.com/kbroman/Poster_ENAR2014](https://github.com/kbroman/Poster_ENAR2014)



## Beamer-based posters


\addtocounter{framenumber}{-1}

```
\documentclass[final,plain]{beamer}
\usepackage[size=custom,width=152.4,height=91.44,scale=1.2]{%
    beamerposter}

\newlength{\sepwid}
\newlength{\onecolwid}
\newlength{\halfcolwid}
\newlength{\twocolwid}
\newlength{\threecolwid}

\setlength{\sepwid}{0.0192\paperwidth}
\setlength{\onecolwid}{0.176\paperwidth}
\setlength{\halfcolwid}{0.0784\paperwidth}
\setlength{\twocolwid}{0.3712\paperwidth}
\setlength{\threecolwid}{0.5664\paperwidth}
\setlength{\topmargin}{-0.5in}
\usetheme{confposter}
```



  Beamer can be used to make posters, too. It's a lot of work, but
  with my latest poster, I'm finally convinced of the value of these
  large-format posters.

  At UW-Madison, the Digital Media Center will print posters for you
  (\$5 per square foot for paper; \$7 per square foot for cloth). The
  cloth ones eliminate the need to carry a tube, but they need to be
  packed gently and probably still require a bit of ironing on the
  other end.

  `width` and `height` are in centimeters. Use `scale` to
  increase the font sizes overall. Then carefully calculate the {\tt
    sepwid, `onecolwid`, etc., so that everything fits just right.
}


% this is to get  within the lstlisting environment
% See http://tex.stackexchange.com/questions/73366/
\newsavebox{\codeboxseven}
\begin{lrbox}{\codeboxseven}
```
\title{Data visualizations should be more interactive}
\author{Karl W Broman}
\institute{University of Wisconsin--Madison}

## columns

[t]
  \begin{column}{\sepwid}\end{column} % empty spacer column
  \begin{column}{\onecolwid}
    \begin{exampleblock}{\Large Introduction}{
      \begin{itemize} * sep18pt
        *  Bullet 1
        *  Bullet 2
      \end{itemize}
    }
  \colonevsep % between blocks
    \begin{block}{Barriers}{
    }
  \end{column}
\end{columns}

```
\end{lrbox}

## Basic code for a poster



\usebox{\codeboxseven}


  The whole thing is within a single `frame` environment, and then
  with `columns` and `column`.

  The blocks within a column are within `exampleblock` or `block`
  environments.





## Between-block spacing



```
\newcommand{\colonevsep}{}
\newcommand{\coltwovsep}{}
\newcommand{\colthreevsep}{}
\newcommand{\colfourvsep}{}
\newcommand{\colfivevsep}{}
```


  I define different between-block spacings for each column, to get
  them all to have the same length.



## Summary



*  Use LaTeX/Beamer or Slidify to create reproducible slides.
*  Use LaTeX/Beamer to create reproducible posters.
*  Include KnitR code chunks to create figures directly.
*  Or keep the code for figures separate.

  To make reproducible slides/posters, you need to dump PowerPoint.

  With each of these approaches, you can use KnitR code chunks. But I
  still tend to produce the figures separately and include them with
  `{/`includegraphics.
}






