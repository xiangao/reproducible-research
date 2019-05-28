---
date: 2016-03-08T21:07:13+01:00
title: Tools for Reproducible Research
type: index
weight: 1
---

This is Andrew Marder's adaptation of Karl Broman's [Tools for
Reproducible Research](https://github.com/kbroman/Tools4RR).

A minimal standard for data analysis and other scientific computations
is that they be **reproducible**: that the **code and data are
assembled in a way so that another group can re-create all of the
results** (e.g., the figures in a paper). The importance of such
reproducibility is now widely recognized, but it is still not as
widely practiced as it should be, in large part because many
computational scientists (and particularly statisticians) have not
fully adopted the required tools for reproducible research.

In this course, we will discuss general principles for reproducible
research but will focus primarily on the use of relevant tools
(particularly [Make](https://www.gnu.org/software/make/),
[Git](https://git-scm.org/), and
[R Markdown](https://rmarkdown.rstudio.com/)), with the goal that the
students leave the course ready and willing to ensure that all aspects
of their computational research (software, data analyses, papers,
presentations, posters) are reproducible.

## Details

Prerequisite: Some knowledge of R.

The source for this website is on
[GitHub](https://github.com/hbs-rcs/reproducible-research).

## Recommended Books

* Christopher Gandrud's [Reproducible Research with R and RStudio](https://www.amazon.com/gp/product/1498715370?ie=UTF8&tag=7210-20)

* Yihui Xie's [Dynamic Documents with R and knitr](https://www.amazon.com/gp/product/1498716962?ie=UTF8&tag=7210-20)

## Project

By the end of the course, each student will have designed and
completed a small project:

* Implement something in R (e.g., simulation + fancy plot).
* Develop it in a Git repository on GitHub.
* Make it an R package.
* Use `rmarkdown` to make a vignette.
* Use `testthat` to include a unit test.
* Make sure it passes `R CMD check`.
