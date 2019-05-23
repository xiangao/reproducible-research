---
title: R Markdown
weight: 30
---

Statisticians write a lot of reports, describing the results of
  data analyses. It's best if such reports are fully reproducible:
  that the data and code are available, and that there's a clear and
  automatic path from data and code to the final report.

  knitr is ideal for this effort. It's a system for combining code and
  text into a single document. Process the document, and the code is
  replaced with the results and figures that it generates.

  I've found it most efficient to produce informal analysis reports as
  web pages. Markdown is a system for writing simple,
  readable text, with the sort of marks that you might use in an email
  message, that gets converted to nicely formatted html-based web pages.

  My goal in this lecture is to show you how to use knitr with R
  Markdown (a variant of Markdown) to make such
  reproducible reports, and to convince you that this is the way that
  you should be constructing such analysis reports.

  I'd originally planned to also cover knitr with AsciiDoc, but I
  decided to drop it; it's best to focus on Markdown.


## knitr in a knutshell

\centerline{\Large [\tt kbroman.org/knitr_knutshell](http://kbroman.org/knitr_knutshell)}

I wrote a short tutorial on knitr, covering a bit more than I'll
  cover in this lecture.

  I'd be glad for suggestions, corrections, or questions.








## Data analysis reports





*  Figures/tables + email
*  Static \LaTeX\ or Word document
*  knitr/Sweave + \LaTeX\ -> PDF
*  knitr + Markdown -> Web page
Statisticians write a lot of reports. You do a bunch of
  analyses, create a bunch of figures and tables, and you want to
  describe what you've done to a collaborator.

  When I was first starting out, I'd create a bunch of figures and
  tables and email them to my collaborator with a description of the
  findings in the body of the email. That was cumbersome for me and
  for the collaborator. ("Which figure are we talking about, again?")

  I moved towards writing formal reports in
  \LaTeX\ and sending my collaborator a
  PDF. But that was a lot of work, and if I later wanted to re-run
  things (e.g., if additional data were added), it was a real hassle.

  Sweave + \LaTeX\ was a big help, but it's a pain to deal with page
  breaks.

  Web pages, produced with knitr and Markdown, are ideal. You can make
  super-tall multi-panel figures that show the full details, without
  worrying page breaks. And hyperlinks are more convenient, too.




\begin{frame}[c]{}

\centering
What if the data change?



What if you used the wrong version of the data?

If data are added, will it be easy to go back and re-do your
  analyses, or is there a lot of copying-and-pasting and editing to be
  done?

  I usually start an analysis report with a summary of the experiment,
  scientific questions, and the data. Recently, a collaborator noticed
  that I'd used an old version of the data. (I'd cited sample
  sizes, and so he could see that I didn't have the full set.)

  He said, "I'm really sorry you did all that work on the incomplete
  dataset."

  But actually, it didn't take long to find the right file, and the
  revised analysis was derived instantaneously, as I'd used knitr.





## knitr code chunks





[Input to knitr](https://github.com/kbroman/Tools4RR/blob/master/03_KnitrMarkdown/Examples/example1.Rmd):
```
We see that this is an intercross with `r nind(sug)`
individuals. There are `r nphe(sug)` phenotypes, and genotype
data at `r totmar(sug)` markers across the `r nchr(sug)`
autosomes.  The genotype data is quite complete.

"`{r summary_plot, fig.height=8}
plot(sug)
"`
```



[Output from knitr](https://github.com/kbroman/Tools4RR/blob/master/03_KnitrMarkdown/Examples/example1.md):
```
We see that this is an intercross with 163
individuals. There are 6 phenotypes, and genotype
data at 93 markers across the 19
autosomes.  The genotype data is quite complete.

"`r
plot(sug)
"`

![plot of chunk summary_plot](RmdFigs/summary_plot.png)
```


The basic idea in knitr is that your regular text document will
  be interrupted by chunks of code delimited in a special way.

  This example is with R Markdown.

  There are in-line bits of code indicated with backticks.
  When the document is processed by knitr, they'll be evaluated and
  replaced by the result.

  Larger code chunks with three backticks. This one will produce a
  plot. When processed by knitr, an image file will be created and a
  link to the image will be inserted at that location.

  In knitr, different types of text have different ways of delimiting
  code chunks, because it's basically going to do a
  search-and-replace and depending on the form of text, different
  patterns will be easier to find.




## html





```
<!DOCTYPE html>
<html>
<head>
  <meta charset=utf-8"/>
  <title>Example html file</title>
</head>

<body>
<h1>Markdown example</h1>

<p>Use a bit of <strong>bold</strong> or <em>italics</em>. Use
backticks to indicate <code>code</code> that will be rendered
in monospace.</p>

<ul>
<li>This is part of a list</li>
<li>another item</li>
</ul>

</body>
</html>
```



 [[Example](http://kbroman.github.io/knitr_knutshell/assets/markdown_example.html)]

It's helpful to know a bit of html, which is the markup
language that web pages are written in. html really isn't that hard;
it's just cumbersome.

An html document contains pairs of tags to indicate content, like
`<h1>` and `</h1>` to indicate that the enclosed text is a
"level one header", or `<em>` and `</em>` to indicate emphasis
(generally italics). A web browser will parse the html tags and
render the web page, often using a cascading style sheet (CSS) to
define the precise style of the different elements.

Note that there are six levels of headers, with tags
`<h1>`, `<h2>`, `<h3>`, \dots, `<h6>`.
Think of these as the title,
section, subsection, sub-subsection, \dots




## CSS





```
ul,ol {
  margin: 0 0 0 35px;
}

a {
  color: purple;
  text-decoration: none;
  background-color: transparent;
}

a:hover
{
  color: purple;
  background: #CAFFFF;
}
```



 {\footnotesize \lolit
[[Example](http://kevinburke.bitbucket.org/markdowncss/markdown.css)]}

I don't really want to talk about CSS, but I thought I should at
  least acknowledge its existence.

  CSS is really important for defining how your document will
  appear. Much of the time, you just want to find someone else's CSS
  document that is satisfactory to you.




## Markdown





```
# Markdown example

Use a bit of **bold** or _italics_. Use backticks to indicate
`code` that will be rendered in monospace.

- This is part of a list
- another item

Include blocks of code using three backticks:

"`
x <- rnorm(100)
"`

Or indent four spaces:

    mean(x)
    sd(x)

And it's easy to create links, like to
[Markdown](http://daringfireball.net/projects/markdown/).
```



 {\footnotesize \lolit
[[Example](http://kbroman.github.io/knitr_knutshell/assets/markdown_example.md) |
[MD cheat sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)]}

Markdown is a system for writing simple, readable text that is
  easily converted into html. The reason it's useful to know a bit of
  html is that then you have a better idea how the final product will
  look. (Plus, if you want to get fancy, you can just insert a bit of
  html within the Markdown document.)

  Markdown is just a system of marks that will get searched-and-
  replaced to create an html document. A big advantage of the Markdown
  marks is that the source document is much like what you might write
  in an email, and so it's much more human-readable.

  Github (which we'll talk about next week) automatically renders
  Markdown files as html, and you can use Markdown for ReadMe files.
  And the website for this course is mostly in Markdown.






## R Markdown





* sep12pt
*  [R Markdown](http://rmarkdown.rstudio.com) is a variant of Markdown, developed at
  [RStudio.com](http://www.rstudio.com)
*  Markdown + knitr + extras
*  A few extra marks
*  [\LaTeX\ equations](http://www.rstudio.com/ide/docs/authoring/using_markdown_equations)
*  Bundle images into the final html file
R Markdown is a variant of Markdown developed by the folks at
  RStudio.

  It's Markdown with knitr code chunks, but there are a number of
  added features,  most importantly the ability to use
  \LaTeX\ equations.




## Code chunks, again





```
"`{r knitr_options, include=FALSE}
knitr::opts_chunk$set(fig.width=12, fig.height=4,
                      fig.path='Figs/', warning=FALSE,
                      message=FALSE)
set.seed(53079239)
"`

### Preliminaries

Load the R/qtl package using the `library` function:

"`{r load_qtl}
library(qtl)
"`

To get help on the read.cross function in R, type the
following:

"`{r help, eval=FALSE}
?read.cross
"`
```



 {\footnotesize \lolit
[[Example](https://github.com/kbroman/knitr_knutshell/blob/gh-pages/assets/knitr_example.Rmd)]}


A couple of additional points about code chunks.

You can (and should) assign names to the code chunks. It will make it
easier to fix errors, and figure files will be named based on the
name of the chunk that produces them.

Code chunks can also have options, like `include=FALSE` and `eval=FALSE`.
And you can define global options, which will apply to all subsequent
chunks.




## Chunk options





\renewcommand{\arraystretch}{1.3}
\begin{tabular}{ll}
`echo=FALSE`     & \lolit Don't include the code \\
`results="hide"` & \lolit Don't include the output \\
`include=FALSE`  & \lolit Don't show code or output \\
`eval=FALSE`     & \lolit Don't evaluate the code at all \\
`warning=FALSE`  & \lolit Don't show R warnings \\
`message=FALSE`  & \lolit Don't show R messages \\
`fig.width=\#`   & \lolit Width of figure \\
`fig.height=\#`  & \lolit Height of figure \\
`fig.path="Figs/"` & \lolit Path for figure files \\
\end{tabular}



There are [lots of chunk options](http://yihui.name/knitr/options#chunk_options).

These are the chunk options that I use most, but there are lots
  more. Each should be valid R code, and can be basically any valid
  R code, so you can get pretty fancy.

  The ending slash in `fig.path` is important, as this is just pasted to
  the front of the figure file names. If not included, the figures
  would be in the main directory but with names starting with "`Figs`".





## Global chunk options





```
"`{r knitr_options, include=FALSE}
knitr::opts_chunk$set(fig.width=12, fig.height=4,
                      fig.path='Figs/', warning=FALSE,
                      message=FALSE, include=FALSE,
                      echo=FALSE)
set.seed(53079239)
"`

"`{r make_plot, fig.width=8, include=TRUE}
x <- rnorm(100)
y <- 2*x + rnorm(100)
plot(x, y)
"`
```



* sep12pt
*  Use global chunk options rather than repeat the same options over and over.
*  You can override the global values in specific chunks.
I'll often use `include=FALSE` and `echo=FALSE` in a report to a
  collaborator, as they won't want to see the code and raw
  results. I'll then use `include=TRUE` for the figure chunks.

  And I'll set some default choice for figure heights and widths but
  then adjust them a bit in particular figures.

  You may need to include `{/`library(knitr) before the
  `opts_chunk\$set()` (for example, within RStudio).
}






## Package options





```
"`{r package_options, include=FALSE}
knitr::opts_knit$set(progress = TRUE, verbose = TRUE)
"`
```


* sep12pt
*  It's easy to confuse global [chunk options](http://yihui.name/knitr/options#chunk_options) with
[package options](http://yihui.name/knitr/options#package_options).
*  I've not used package options.
*  So focus on ` opts_chunk\$set()` not {\tt
  \lolit opts_knit\$set()}.
If you are doing something fancy, you may need knitr package
  options, but I've not used them.

  I've gotten confused about them, though: `opts_chunk\$set`
  vs. `opts_knit\$set`.





## In-line code





```
We see that this is an intercross with `r nind(sug)`
individuals. There are `r nphe(sug)` phenotypes, and genotype
data at `r totmar(sug)` markers across the `r nchr(sug)`
autosomes.  The genotype data is quite complete.
```



* sep12pt
*  Each bit of in-line code needs to be within one line; they
  **can't**
  span across lines.
*  I'll often precede a paragraph with a code chunk with {\tt
  include=FALSE}, defining various variables, to simplify the in-line
  code.
*  Never hard-code a result or summary statistic again!
In-line code to insert summary statistics and such is a key
  feature of knitr.

  Even if you wanted the code for your figures or data analysis to be
  separate, you'd still want to make use of this feature.

  Remember my anecdote earlier in this lecture: if I hadn't mentioned
  sample sizes, my collaborator wouldn't have noticed that I was using
  an old version of the data.




## YAML header





```
---
title: "knitr/R Markdown example"
author: "Karl Broman"
date: "28 January 2015"
output: html_document
---
```




```
---
title: "Another knitr/R Markdown example"
author: "[Karl Broman](http://kbroman.org)"
date: "`r Sys.Date()`"
output: word_document
---
```



At the top of your Rmd file, it's best to include a header like
  the above examples. (YAML is a simple text-based format for
  specifying data, sort of like JSON but more human-readable.)

  You don't have to include any of these things, but it's good to at
  least specify `output:` (which can be also be {\tt
  pdf_document). There are a lot more options; see `rmarkdown.rstudio.com`.

  Note my use of a hyperlink and some R code in the second
  example. These will carry over to the final document.
}



## Rounding





* sep18pt
*  `cor(x,y)` might produce `\vhilit 0.8992877`, but
I want ` 0.90`.

*  `round(cor(x,y), 2)`, would give `\vhilit 0.9`, but I want
` 0.90`.

*  You could use `sprintf("\%.2f", cor(x,y))`, but
`sprintf("\%.2f", -0.001)` gives `\vhilit -0.00`.

*  Use the `myround` function in my
[R/broman](http://github.com/kbroman/broman) package.

*  `myround(cor(x,y), 2)` solves both issues.
I'm very particular about rounding. You should be too.

  If you're a C programmer, sprintf seems natural. No one else agrees.

  The R/broman package is on both github and CRAN.




## R Markdown -> html, in [RStudio](http://www.rstudio.com)





\centerline{\includegraphics[width=\textwidth]{Figs/rstudio_knitr.png}}

The easiest way to convert an R Markdown file to html is with
  RStudio.

  Open the R Markdown file in R Studio and click the "Knit HTML"
  button (with the ball of yarn and knitting needle).

  Note the little button with a question mark. Click that, and you'll
  get the "Markdown Quick Reference."

  What actually happens: The `knit` function in the knitr package
  processes all of the code chunks and in-line code and creates a
  Markdown file and possibly a bunch of figure files.
  The Markdown file (and any figure files) are sent to Pandoc, which
  converts them to an HTML file, with embedded figures.

  RStudio is especially useful when you're first learning R Markdown
  and knitr, as it's easy to create and view the corresponding html
  file, and you have access to that Markdown Quick Reference.





## R Markdown -> html, in [R](http://www.r-project.org)





```
> library(rmarkdown)
> render("knitr_example.Rmd")
```



```
> rmarkdown::render("knitr_example.Rmd")
```


When you click the "Knit HTML" button in RStudio, what it
  actually does is run `rmarkdown::render()`, which in turn calls
  `knitr::knit()` and then runs pandoc.

  You can do the same thing directly, in R. You do miss out on the
  immediate preview of the result.



## R Markdown -> html,
    [GNU make](http://www.gnu.org/software/make)





```
knitr_example.html: knitr_example.Rmd
    R -e "rmarkdown::render('knitr_example.Rmd')"
```

I prefer to do this from the command-line, using a Makefile.
  Then it's more obvious what's happening.

  In Windows, it's important that the double-quotes are on the outside
  and the single-quotes are on the inside.




## Need pandoc in your `PATH`





[RStudio](http://www.rstudio.com) includes pandoc; you just need
to add the relevant directory to your `PATH`.



 **Mac**:



 {\ttsm /Applications/RStudio.app/Contents/MacOS/pandoc}



 **Windows**:



 {\ttsm "c:{/}Program Files{/}RStudio{/}bin{/}pandoc"}

To use the rmarkdown package from the command line, you need
  access to pandoc. But if you've installed RStudio (and I {
  highly recommend that you do), you don't need to do a separate
  install, as pandoc is included with RStudio.

  You just need to add the relevant directory (listed above) to your
  `PATH`, for example in your `{~`/.bash_profile} file.

  At the command line, type `type pandoc` or
  `pandoc --version` to check that it's available.

}




## Reproducible knitr documents





* sep8pt
*  Don't use absolute paths like `\vhilit
  {~`/Data/blah.csv}
*  Keep all of the code and data in one directory (and its
  subdirectories)
*  If you {\vhilit must} use absolute paths, define the various directories
  with variables at the top of your document.
*  Use `R --vanilla` or perhaps \\
`\scriptsize R --no-save --no-restore --no-init-file --no-site-file`
*  Use GNU make to document the construction of the final product
   (tell future users what to do)
*  Include a final chunk with `getwd()` and
  `devtools::session_info()`.
*  For simulations, use `set.seed` in your first
   chunk.
That you've used knitr doesn't mean the work is really {\nvhilit
    reproducible.  The source and data need to be available to
  others, they need to know what packages were used and how to compile it,
  and then they need to be able to compile it on their system.

  The complicated alternative to `R --vanilla` is if you want to
  still load `{~`/.Renviron}, for example, to define
  `R_LIBS`.

  If you use `set.seed` at the top of the document, it should be that
  the random aspects will give exactly the same results.
  I'll use \\ `runif(1, 0, 10{\textasciicircum`8)} and then paste that big number
  within `set.seed()`.

  Two anecdotes: The github repository for the Reproducible Research
  with R and R Studio book uses some absolute paths that basically
  make it not reproducible.

  Earn et al. (2014) Proc Roy Soc B 281(1778):20132570 has a really
  nice supplement, written with knitr. But it says, "The source code
  is available upon request." It's not {\nvhilit really}
  reproducible, then.
}




## Controlling figures





```
"`{r test_figure, dev.args=list(pointsize=18)}
x <- rnorm(100)
y <- 2*x + rnorm(100)
plot(x,y)
"`
```



{\small
* sep8pt
*  The default is for knitr/R Markdown is to use the `png()`
  graphics device.
*  Use another graphics device with the chunk option `dev`.
*  Pass arguments to the graphics device via the chunk
  option `dev.args`.
}

Graphics in knitr are super easy. For the most part, you don't
  have to do anything! If a code chunk produces a figure, it will be
  inserted.

  But depending on the type of figure, you might want to try different
  graphics devices. And sometimes you want to pass arguments to the
  graphics device.

  Yesterday (6 Feb 2014), to change the size of axis
  labels, you couldn't just use the pointsize device argument; you'd also
  need to use something like `par(cex.lab=1.5)`. But I posted a
  question about it on StackOverflow, and Yihui Xie responded and then
  immediately fixed the problem. I used a bit of twitter in there too,
  to get his attention.

  To download and install the development version of knitr, you can
  use the `install_github` function in Hadley Wickham's devtools
  package. Use `install.packages("devtools")` if you don't already
  have it installed.  Then `library(devtools)` and
  `install_github("yihui/knitr")`.




## Tables



```
"`{r kable}
x <- rnorm(100)
y <- 2*x + rnorm(100)
out <- lm(y ~ x)
coef_tab <- summary(out)$coef
library(kable)
kable(coef_tab, digits=2)
"`
```



```
"`{r pander}
library(pander)
panderOptions("digits", 2)
pander(out, caption="Regression coefficients")
"`
```



```
"`{r xtable, results="asis"}
library(xtable)
tab <- xtable(coef_tab, digits=c(0, 2, 2, 1, 3))
print(tab, type="html")
"`
```




In informal reports, I'll often just print out a matrix or data
  frame, rather than create a formal table.

  But there are multiple ways to make tables with R Markdown that may
  look a bit nicer. I'm not **completely** happy with any of
  them, but maybe I've just not figured out the right set of options.

  `kable` in the knitr package is simple but can't be customized
  too much. But it can produce output as pandoc, markdown, html, or latex.

  The `pander` package produces pandoc-based tables, which even
  work if you're making a Word document, and has a bit more control
  than `kable`.

  The `xtable` package gives you quite complete control,
  but only produces latex or html output. You need to be sure to use
  `results="asis"` in the code chunk.





## Important principles



\centering
Modify your desires to match the defaults.



Focus your compulsive behavior on things that matter.

Focus on the text and the figures before worrying too much about
  fine details of how they appear on the page.

  And consider which is more important: a manuscript, web page, blog,
  grant, course slides, course handout, report to collaborator,
  scientific poster.

  You can spend a ton of time trying to get things to look just
  right. Ideally, you spend that time trying to construct a general
  solution.  Or you can modify your desires to more closely match what
  you get without any effort.






# KnitR + LaTeX -> paper

  This lecture is about how to create reproducible manuscripts, for
  journal articles. KnitR with R Markdown is great for informal
  reports. KnitR with AsciiDoc is great for somewhat fancier
  reports. There are a number of efforts, especially with Pandoc, to
  use R Markdown for journal articles. But if you want fine control
  over the appearance of a document, it's hard to beat \LaTeX, and so
  I'm just going to focus on that.

  I can't hope to explain \LaTeX/ properly in just this one
  lecture. My goals are to give the general gist, indicate resources
  and options, and show how to use KnitR with \LaTeX.

  I also want to discuss some more general strategies for ensuring that
  the results described in a journal article are fully reproducible.



## \LaTeX



```
\documentclass[12pt]{article}

\usepackage{graphicx}

\title{An example document}
\author{Karl Broman}

\begin{document}

\maketitle
\thispagestyle{empty}

\section{A section}

This is a simple example of a \LaTeX/ document for an article.
Here's some in-line math: $y = \beta_0 + \beta_1 x + \epsilon$.

And here's a display equation:

$$ \hat{\beta} = (X'X)^{-1} X'y $$


```


  \LaTeX/ is like html or Markdown: plain text with special codes to
  indicate how things are to appear.

  A \LaTeX/ document always starts with `{/`documentclass, then a
  bunch of overall controlling information. The actual document is
  between `{/`begin\{document\}} and `{/`end\{document\}}.

  `{/`usepackage\{\}} is like `library()` in R.

  Ideally, you focus on {\nhilit semantics} rather than {\nhilit
  style}: define the `{/`title\{\}} and `{/`author\{\}} and use
  `{/`maketitle} to have them included in the document, and
  indicate sections and subsections with `{/`section\{\}} and
  `{/`subsection\{\}}.

  For some reason, `{/`thispagestyle\{empty\}} ("don't
  show page number on this page") needs
  to be placed {\nhilit after} `{/`maketitle}.

  A key feature of \LaTeX/ is the mathematics typesetting. There's no
  better system. And your \LaTeX/ skills can be immediately
  transferred to your Markdown documents, with MathJax.
}



## What I actually do



```
\documentclass[12pt]{article}

\setlength{\headheight}{10pt}
\setlength{\headsep}{15pt}
\setlength{\topmargin}{-25pt}
\setlength{\topskip}{0in}
\setlength{\textheight}{8.7in}
\setlength{\footskip}{0.3in}
\setlength{\oddsidemargin}{0.0in}
\setlength{\evensidemargin}{0.0in}
\setlength{\textwidth}{6.5in}

\begin{document}
\begin{center}
\textbf{\large An example document}


Karl Broman
\end{center}


\textbf{\sffamily A section}
```


  In reality, for a paper, I don't use `{/`maketitle
  or `{/`section}, but rather just muck about,
  hard-coding the placement of things.

  But mine is not the recommended approach. If, for some reason, you
  need to change the style, it's easier if your document is defined in
  terms of {\nhilit semantics}.
}



## Why \LaTeX/?



*  Fine control of document appearance
*  Transparency of how that was achieved
*  Version control (diff/merge)
*  Typesetting equations
*  Markdown's not quite ready, or sufficiently rich
  * [] (but see the R package [rticles](https://github.com/rstudio/rticles))
  
  It's {\nhilit a lot of work to learn \LaTeX, so we need to be clear
  about why we'd want to devote the effort to it.

  For reproducible research, we need some sort of code-based document
  system (i.e., {\nvhilit not Word!}), and \LaTeX/ gives you the most
  fine-grained control, if you need it. Ultimately, I hope, Markdown
  will be sufficient, but for now, we often need \LaTeX/.

  The code-based control makes what you're trying to do
  transparent.  And you should treat \LaTeX/ like code: write clearly
  and simply, and comment the tricky bits.

  This sort of document also has the advantage of easy treatment of
  `diff` and `merge` in a version control system like git.

  The real power of \LaTeX/ is in the typesetting of mathematical
  equations. And what you learn on that aspect can be transferred to
  your Markdown documents, using MathJax. (But I already said that,
  didn't I?)
}



\begin{frame}[c]{}



\centerline{\Large simple \quad $\longleftrightarrow$ \quad flexible}



\onslide<2->{\centerline`\scriptsize \lolit {/`centerline\{{/}Large simple
{/}quad \${/}longleftrightarrow\$ {/}quad flexible\}}}


  \LaTeX/ sits at the right of the simple-to-flexible spectrum.





\begin{frame}[c]{}

\centering
Modify your desires to match the defaults.



Focus your compulsive behavior on things that matter.


  I've said this before, but I like to repeat it.

  Focus on the text and the figures before worrying too much about
  fine details of how they appear on the page.

  And consider which is more important: a manuscript, web page, blog,
  grant, course slides, course handout, report to collaborator,
  scientific poster.

  You can spend a ton of time trying to get things to look just
  right. Ideally, you spend that time trying to construct a general
  solution.  Or you can modify your desires to more closely match what
  you get without any effort.




## Stuff I use a lot



```
% other fonts
\usepackage{palatino}
\usepackage{times}

\setlength{\rightskip}{0pt plus 1fil} % makes ragged right

\newcommand{\LOD}{\text{LOD}}

\usepackage{setspace}
\setstretch{2.0}

\addtocounter{framenumber}{-1}

% make figures S1, S2, ...
\renewcommand{\thefigure}{\textbf{S\arabic{figure}}}
\renewcommand{\figurename}{\textbf{Figure}}

% bigger space between rows in tables
\renewcommand{\arraystretch}{1.5}

% paragraphs not indented but have space between
\setlength{\parskip}{6pt}
\setlength{\parindent}{0pt}
```



  These are bits of \LaTeX/ code that I use a lot.







## KnitR + \LaTeX -> Rnw



```
\documentclass[12pt]{article}

\title{An example Rnw document}
\author{Karl Broman}

\begin{document}
\maketitle

<<load_library, echo=FALSE, results="hide">>=
library(broman) # used for myround()
@

<<example_chunk>>=
x <- rnorm(100)
y <- 5*x + rnorm(100)
lm.out <- lm(y ~ x)
plot(x,y)
abline(lm.out$coef)
@

The estimated slope is \Sexpr{myround(lm.out$coef[2], 1)}.

```




## KnitR + \LaTeX -> Rnw


\addtocounter{framenumber}{-1}

```
\documentclass[12pt]{article}

\title{An example Rnw document}
\author{Karl Broman}

\begin{document}
\maketitle

<<load_library, echo=FALSE, results="hide">>=
library(broman) # used for myround()
@

<<example_chunk, out.width="0.8\\textwidth">>=
x <- rnorm(100)
y <- 5*x + rnorm(100)
lm.out <- lm(y ~ x)
plot(x,y)
abline(lm.out$coef)
@

The estimated slope is \Sexpr{myround(lm.out$coef[2], 1)}.

```


  KnitR works well with LaTeX.

  Most of what you learned about KnitR with R Markdown transfers
  directly to working with LaTeX.

  The main difference is the way in which code chunks are
  indicated. You use `<<>>=` and `@` for chunks, and
  `{/`Sexpr\{\} for in-line code.

  KnitR basically does a search-and-replace for code
  chunks. Different patterns will be easier, depending on the nature
  of the surrounding code.

  The chunk options are the same. Here, I used
  `out.width="0.8{/`textwidth"}
  to make the figure appear as 80\% of the width of the page.

  `out.width` and `out.height` need units as in \LaTeX/ (built into
  `{//`textwidth}; otherwise `"in"`
  or `"cm"` or `"pt"` or whatever).

  `fig.width` and `fig.height` are as in R, with implied units.
}


## LyX





\figh{Figs/lyx.png}{0.7}



 [lyx.org](http://www.lyx.org/)


  I create \LaTeX/ documents in emacs. If you want something WYSIWYG,
  consider LyX. KnitR is built in, and Yihui Xie strongly endorses
  it. (LyX is not really "WYSIWYG" but rather "WYSIWYM," but
  that's what you want most, anyway.)




## Also



*  [Overleaf](http://overleaf.com)
*  [ShareLaTeX](http://sharelatex.com)
*  [Authorea](http://authorea.com)
*  [Verbosus](http://verbosus.com)

  There are a bunch of online tools for creating LaTeX documents,
  collaboratively.

  I have no experience with these, but I've heard good things about
  Overleaf (formerly WriteLaTeX).






## Flavors of \LaTeX



*  [\LaTeX](http://www.latex-project.org/)
*  [pdflatex](http://en.wikipedia.org/wiki/PdfTeX)
*  [xelatex](http://en.wikipedia.org/wiki/XeTeX)
*  [lualatex](http://www.luatex.org/)

  In addition to regular \LaTeX, there's pdflatex (which I mostly
  use). It has the advantage of being able to include pdf, jpg, and
  png figures, and produces a PDF file directly.

  XeLaTeX and LuaLaTeX are great for fonts and Unicode.

  I've not mentioned that behind the scenes is \TeX, which is the
  source of all of this. Believe or not, \LaTeX/ exists because
  \TeX/ is even harder. PdfLaTeX, XeLaTeX, and LuoLaTeX, really
  derive from PdfTeX, XeTex, and LuoTex.





## Getting help



*  Google
*  [tex.stackexchange.com](tex.stackexchange.com)
*  Ask a friend
*  Look at others' documents
*  Resign yourself to something less-than-ideal

  There is {\nhilit a ton of online information about \LaTeX. Start
  with google. It's highly unlikely that you have a completely unique
  question or problem.

  My last point here is basically that one way to help yourself is by
  learning to let things go.
}




## Figure captions and floats



```
<<fig_with_caption, fig.cap="Scatterplot of $y$ vs $x$">>=
x <- rnorm(100)
y <- 5*x + rnorm(100)
lm.out <- lm(y ~ x)
plot(x,y)
abline(lm.out$coef)
@
```



```
\begin{figure}[]
\includegraphics{figure/fig_with_caption}

\caption{Scatterplot of $y$ vs $x$\label{fig:fig_with_caption}}
\end{figure}
```



  If you use the chunk option `fig.cap`, the figure will get a
  caption.

  But it will also be embedded within a `figure` "environment."
  (That is, between `{/`begin\{figure\} and
  `{/`end\{figure\}}.)

  This makes it a "float." \LaTeX/ decides where it's going to be
  placed. The placement of floats is {\nvhilit the biggest pain} in
  using \LaTeX.

  The figure also gets a label, from the chunk name. (The
  `{/`label\{\}} bit.) This allows you to
  cross-reference the figure, to have the figure number determined
  automatically.

  The cross reference would be with `{/`ref\{fig:fig_with_caption\}}.

  When you use cross references, you need to run \LaTeX/ twice: once
  to establish where things will sit on the page and how they are
  numbered, and a second time to insert the cross references.
}





## Tables in \LaTeX





```
\begin{tabular}{rrrrr} \hline
& Estimate & Std. Error & t value & Pr($>$$|$t$|$) \\  \hline
(Intercept) & 0.04 & 0.11 &  0.4 & 0.69 \\
      x     & 0.98 & 0.10 & 10.0 & 0.00 \\ \hline
\end{tabular}
```


  Tables in \LaTeX/ are a pain, but they offer extremely fine
  control.

  But writing this sort of code (`\&` indicates breaks between
  columns, `{/`{/} indicates the end of
  a row) {\nhilit reproducibly} is hard.
}




## xtable





```
<<generate_and_fit>>=
x <- rnorm(100)
y <- x + rnorm(100)
lm.out <- lm(y ~ x)
@

<<table, results="asis">>=
library(xtable)
xtable(lm.out, digits=c(0,2,2,1,2))
@


% a non-floating version
<<table, results="asis">>=
library(xtable)
xtab <- xtable(lm.out, digits=c(0,2,2,1,2))
print(xtab, floating=FALSE)
@
```


  xtable is a superb R package for producing \LaTeX/ tables.
  You don't have complete control, but you do have a ton of
  control. The xtableGallery vignette shows you much of what can be
  done.

  Note that a lot of the options are for `print.xtable`, so look
  at the help files for both `xtable` and `print.xtable`.

  For example, if you {\nhilit don't want a table to be "floating,"
  (within a `table` environment, between
  `{/`begin\{table\}} and
  `{/`end\{table\}}),
  you need to use `print.table` with `floating=FALSE`.
}



## Read proofs carefully





As submitted


\figw{Figs/rigenome_as_submitted.png}{0.5}

 

As printed


\figw{Figs/rigenome_error.png}{0.5}



\scriptsize Broman (2005) Genetics 169:1133{\textendash1146}


  Some journals re-type a bunch of your manuscript, sometimes
  introducing errors.

  So read proofs {\nhilit carefully. (What pain!) And post a
  preprint, say to arXiv.org or bioRxiv.org.

  The above is the most important equation in the paper, and I missed
  that they'd introduced a mistake.
}





## Re-type that!





\figh{Figs/preCC_table.png}{0.65}



\scriptsize Broman (2012) Genetics 190:403{\textendash412}


  I have a few papers with {\nhilit a lot of equations. I hope
  they're not trying to re-type these. I generated them from code.
}



## BibTeX for bibliographies



```
%bibliography format
\usepackage[authoryear]{natbib}
\bibpunct{(}{)}{;}{a}{}{,}

A number of investigators have developed methods for identifying
such sample mix-ups \citep{Westra2011, Schadt2012, Lynch2012,
Ekstrom2012}, and a similar approach was applied by
\citet{Baggerly2008, Baggerly2009} in their forensic...

\bibliographystyle{genetics}
\renewcommand*{\refname}{\centerline{\normalsize\sffamily
   \textbf{Literature Cited}}}
\bibliography{samplemixups}
```



```
@article{Baggerly2008,
author = {Baggerly, Keith A. and Coombes, Kevin R.},
journal = {J. Clin. Oncol.},
pages = {1186--1187},
title = {Run batch effects potentially compromise...},
volume = {26},
year = {2008} }
```



  References with \LaTeX/ are via BibTeX, which is fabulous once you
  get used to it. Most software to track references will produce
  BibTeX files for you.

  The formatting of citations and the reference listings, to match
  what the journal wants, can be painful. But I've figured out how to
  produce what **Genetics/ wants, and I send all of my papers
  there.

  The first box is the sort of code that would appear
  in your \LaTeX/ file: the bit at the top goes in the header (before
  `{/`begin\{document\**}). The bit in the middle
  shows how to cite papers: use `{/`citep} to get the
  whole thing in parentheses, and use `{/`citet} to
  get a reference like "...applied by Baggerly and Coombes (2008, 2009)..."
  The last bit in the first box produces the actual list of references.

  The second box is the BibTeX format for a particular reference.

  When you use BibTeX, you tend to run `pdflatex`, then {\tt
  bibtex}, and then `pdflatex` a couple of more times.
}



## Organizing analyses



*  Directory for the main analysis project
  * [] `{~`/Projects/Blah}
  *  Directory for a paper
  * [] `{~`/Docs/Papers/Blah}
  *  Paper directory may have an analysis directory
  * [] `{~`/Docs/Papers/Blah/Analysis}
  *  Symbolic links to `.RData` files
  * [] `ln -s {~`/Projects/Blah/DerivedData/blah.RData .}
  *  Each part well organized and fully reproducible.
*  R Markdown reports documenting different aspects.
*  Analysis with the paper may be re-done "properly."

  This is how I organize a paper related to a larger project.

  Some of the work in the main project may be re-done a bit
  differently (or cleaner) in the analysis with the paper.

  You don't want to re-do {\nhilit all analyses for the paper, but
  it'd also be nice to have the data and code related to the paper be
  a bit more self-contained.

  And usually when you're sitting down to write the paper, you have
  better ideas about how to re-do things properly, and so it might be
  a good idea to go ahead and re-do things.

  Ideally, you'd separate out each aspect of the analysis: data
  manipulation, data cleaning, and different parts of the analysis.

  Have an R Markdown document describing each aspect, with the
  actual manuscript and its figures and tables drawing from the
  results of those R Markdown documents.
}



## Make every number reproducible.



```
<<define_numbers, echo=FALSE>>=
numbers <- c("one", "two", "three", "four", "five",
             "six", "seven", "eight", "nine", "ten")
cap <- function(vec) paste0(toupper(substr(vec, 1, 1)),
                            substr(vec, 2, nchar(vec)))
Numbers <- cap(numbers)
n <- sample(1:10, 1)
@

Then if I want to talk about a number, like \Sexpr{n}, I can
refer to it by name: \Sexpr{numbers[n]}. And I can start a
sentence with it. \Sexpr{Numbers[n]} grasshoppers walked into a
bar\dots

But be careful about singular vs. plural, and so write
\Sexpr{Numbers[n]} grasshopper\Sexpr{ifelse(n>1, "s", "")}
walked\dots
```


  Every statistic, figure and table in your manuscript should be fully
  reproducible. So when you're citing statistics, use
  `{/`Sexpr\{\} liberally.

  This should inhibit you from writing numbers as words, though the
  \LaTeX/ code can get a bit ugly.

  There's a bit of fanciness here about capitalization and about
  ensuring that singular or plural nouns are correct. If
  `{/`Sexpr\{\}} produces a character string, it ends
  up as plain text in your document

  I'll use a lot of `myround()` from my R/broman package, too.

  Long explanations or descriptions of figures can't be fully
  reproducible, but the figures themselves and any statistics you
  mention should be.
}



## Keep the figures separate



```
# simple make file

mypaper.pdf: mypaper.tex Figs/fig1.pdf Figs/fig2.pdf
    pdflatex mypaper

Figs/fig1.pdf: R/fig1.R
    cd R;R CMD BATCH fig1.R fig1.Rout

Figs/fig2.pdf: R/fig2.R
    cd R;R CMD BATCH fig2.R fig2.Rout
```

 


```
\clearpage
\includegraphics{Figs/fig1.pdf}

\clearpage
\includegraphics{Figs/fig2.pdf}
```


  While you {\nhilit could include all code in your `.Rnw` file,
  I prefer to pull out the code for my figures as separate files, and
  then write a `Makefile` for the manuscript construction and
  include them with `{/`includegraphics}.

  The advantage of this is the ability to reuse the figures in
  talks or whatever. Also, journals will generally want the figures as
  separate files. Finally, the code for my figures is often incredibly
  long and ugly, so it's best to separate it out.

  Ideally, the code for a figure would be structured as a function and
  then a function call.  Put a bit more effort into the code, so that
  you can reuse it later for a similar figure with different data.
  At the very least, you should write the repeated bits as functions.

  If your function takes arguments that define the placement of
  things (padding for text and so forth), then the fine adjustments of the
  figure appearance would be easier.
}



## Version Control



*  Your manuscript is under version control, right?
\onslide<2->{*  Local or private repository for the whole thing
  *  including reviewers' reports and my response
  *  PDF of submitted and final manuscript
  *  Snapshot of the final version as a public repository
  *  I don't really want to show the whole history
  }

  Git is as good for tracking manuscripts and data analyses as it is
  for tracking code. Use it!

  But I don't want to make {\nhilit everything public, and I want to
  include private stuff in my repository.

  I've been using just a local repository, but I'm moving towards
  having a private repository hosted on BitBucket.

  I'll put a snapshot of the final version, and maybe a few final
  changes, on GitHub.
}



## Word



*  With papers led by a collaborator, I'm usually stuck with Word.
*  But my analyses and figures are fully reproducible.
*  Create an R Markdown document with the detailed results.

  Often, you'll be stuck with Word. And you can't reproducibly insert
  numbers into Word.

  So have a separate R Markdown report with the detailed results,
  including every statistic that will get inserted into Word.

  And take control of the figures and ensure that they are
  reproducible (and respectable).

  Teach your collaborators to at least have their figures be
  reproducible?





## Summary



*  \LaTeX/ is brilliant for fine control and for equations
*  Floating figures and tables can be a pain
*  You use KnitR with \LaTeX/ much the same way as you'd used it
  with Markdown.
*  Ensure that every statistic, figure, and table in your paper are
  fully reproducible.
*  Use xtable to make tables.
*  Separate out the code for the figures.
*  Use version control!

  Summaries are helpful.


# Presentations and posters

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


## Powerpoint/Keynote

* [+] Standard
* [+] Easy to share slides
* [+] WYSIWYG (mostly)
* [+] Fancy animations

- - - - -

* [-] Font problems
* [-] Lots of copy-paste
* [-] Hard to get equations
* [-] Not reproducible

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
\setbeamertemplate{itemize subitem}{{-}}
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
   UW{-}Madison}
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
