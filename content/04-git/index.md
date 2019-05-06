---
title: Version Control with Git and GitHub
---

Version control is not strictly necessary for reproducible
research, and it's admittedly a lot of work (to learn and to use) in
the short term, but the long term benefits are enormous.

The advantages are: you'll save the entire history of changes to a
project, you can go back to any point in time (and see what has
changed between any two points in time), you don't have to worry
about breaking things that work, and you can easily merge changes
from multiple people.

I now use version control for basically everything: software, data
analysis projects, papers, talks, and web sites.

People are more resistant to version control than to any other
tool, because of the short-term effort and the lack of recognition
of the long-term benefits.

- - - - -

![pic](phd101212s.gif)

This is typical. And never use "final" in a file name.

## Methods for tracking versions

* Don't keep track
  * good luck!
* Save numbered zip files
  * Unzip versions and `diff`
* Formal version control
  * Easy to study changes back in time
  * Easy to jump back and test
  
- - - - -

There are three methods for keeping track of changes: don't keep
track, periodically zip/tar a directory with a version number, or
use formal version control.

Imagine that some aspect of your code has stopped working at some
point. You know it was working in the past, but it's not working
now. How easy is it to figure out where the problem was introduced?


## Why use formal version control?

* History of changes
* Able to go back
* No worries about breaking things that work
* Merging changes from multiple people

- - - - -

With formal version control, you'll save the entire history of
changes to the project, and you can easily go back to any
point in the history of the project, to see how things were behaving
at that point.

You'll be able to make modifications (e.g., to try out a new
feature) without worrying about breaking things that work.

And version control is especially useful for collaboration. If a
collaborator has made a bunch of changes, it'll be much easier to
see what was changed and to incorporate those changes.


## Example repository

TODO: Include image of GitHub repo

This is a snapshot of a repository on GitHub: a set of files and
subdirectories with more files. You can easily explore the contents.


## Example history

TODO: Include picture of commit log from GitHub

This is a short view of the history of changes to the
repository: a series of ``commits.''


## Example commit

TODO: Picture of git diff from GitHub

This is an example of one of those commits, highlighting what
lines were added and what lines were removed.


## What is git?

* Formal version control system
* Developed by Linus Torvalds (developer of Linux)
  * used to manage the source code for Linux
* Tracks any content (but mostly plain text files)
  * source code
  * data analysis projects
  * manuscripts
  * websites
  * presentations

We're going to focus on git, the version control system
developed by Linus Torvalds for managing the source code for Linux.

You can track any content, but it's mostly for tracking plain text
files, but that can be most anything (source code, data analysis
projects, manuscripts, websites, presentations).


## Why use git?

* It's fast
* You don't need access to a server
* Amazingly good at merging simultaneous changes
* Everyone's using it

Git is fast, you can use it locally on your own computer, it's
amazingly good at merging changes, and there are lots of people
using it.


## What is GitHub?

* A home for git repositories
* Interface for exploring git repositories
* {\hilit Real} open source
  * immediate, easy access to the code
* Like facebook for programmers
* Free 2-year "micro" account for students
  * \href{http://education.github.com}{education.github.com}
* (Bitbucket.org is an alternative)
  * free private repositories

GitHub is a website that hosts git repositories, with a nice
graphical user interface for exploring git repositories.

Source code on GitHub is real open source: anyone can
study it and grab it.

GitHub is sort of like Facebook for programmers: you can see what
people are up to, and easily collaborate on shared projects.

It's free to have public repositories on GitHub; if you want private
repositories, you generally have to pay, but I understand that
students can get a two-year account that allows 5 private
repositories.

Bitbucket.org is an alternative; it allows unlimited private
repositories. I'm cheap, so I use Bitbucket for my private
repositories.


## Why use GitHub?

* It takes care of the server aspects of git
* Graphical user interface for git
  * Exploring code and its history
  * Tracking issues
* Facilitates:
  * Learning from others
  * Seeing what people are up to
  * Contributing to others' code
* Lowers the barrier to collaboration
  * "There's a typo in your documentation." vs. "Here's a correction for your documentation."

GitHub takes care of the server aspects of git, and you get a
great GUI for exploring your repositories.

GitHub is great for browsing others' code, for learning; you don't
even have to download it to your computer. And it's really easy to
contribute to others' code (e.g., to report typos in their
documentation).


## Basic use

* Change some files
* See what you've changed
  * `git status`
  * `git diff`
  * `git log`
* Indicate what changes to save
  * `git add`
* Commit to those changes
  * `git commit`
* Push the changes to GitHub
  * `git push`
* Pull changes from your collaborator
  * `git pull`
  * `git fetch`
  * `git merge`

These are the basic git commands you'll use day-to-day.

{\tt git status} to see the current state of things,
{\tt git diff} to see what's changed, and {\tt git log} to look at
the history.

After you've made some changes, you'll use {\tt git add} to indicate
which changes you want to commit to, and {\tt git commit} to commit
to them (to add them to the repository).

You use {\tt git push} to push changes to GitHub, and {\tt git pull}
(or {\tt git fetch} and {\tt git merge}) to pull changes from a
collaborator's repository, or if you're synchronizing a repository
between two computers.


## Initialize repository

* Create {\lolit (and {\tt cd} to)} a working directory
  * For example, {\tt {\textasciitilde}/Docs/Talks/Graphs}
* Initialize it to be a git repository
  * {\tt \hilit git init}
  * Creates subdirectory {\tt {\textasciitilde}/Docs/Talks/Graphs/.git}

```
$ mkdir ~/Docs/Talks/Graphs
$ cd ~/Docs/Talks/Graphs
$ git init
Initialized empty Git repository in ~/Docs/Talks/Graphs/.git/
```

If you're starting a new, fresh project, you make a directory
for it and go into that directory, and then you type {\tt git
init}. This creates a {\tt .git} subdirectory.


## Produce content

* Create a `README.md` file

```
# Talk on "How to display data badly"

These are slides for a talk that I give as often as possible, because
it's fun.

This was inspired by Howard Wainer's article, whose title I stole: H
Wainer (1984) How to display data badly. American Statistician
38:137-147

A recent PDF is
[here](http://www.biostat.wisc.edu/~kbroman/talks/graphs2013.pdf).
```

Start creating a bit of content, such as a Readme file. You can
use Markdown to make it look nicer.


## Incorporate into repository

* Stage the changes using `git add`

```
$ git add README.md
```

Use {\tt git add} to tell git that you want to start keeping
track of this file.  This is called ``staging,'' or you say the file
is ``staged.''


# Incorporate into repository

* Now commit using {\tt \hilit git commit}

```
$ git commit -m "Initial commit of README.md file"
[master (root-commit) 32c9d01] Initial commit of README.md file
 1 file changed, 14 insertions(+)
 create mode 100644 README.md
```

* The \texttt{-m} argument allows one to enter a message
* Without \texttt{-m}, \texttt{git} will spawn a text editor
* Use a meaningful message
* Message can have multiple lines, but make 1st line an overview

Use {\tt git commit} to add the file to the repository.


## A few points on commits

* Use frequent, small commits
* Don't get out of sync with your collaborators
* Commit the sources, not the derived files
  * (R code not images)
* Use a {\tt .gitignore} file to indicate files to be ignored

```
*~
manuscript.pdf
Figs/*.pdf
.RData
.RHistory
*.Rout
*.aux
*.log
*.out
```

- - - - -

I recommend using frequent, small commits. I'll make a batch of
changes with a common theme, make sure things are working, then add
and commit.

In projects with collabotors, be sure to pull any changes from them
before starting to make your own changes, and encourage your
collaborators to do the same. If you both make a month's changes
in parallel, merging the changes will be harder.

I commit only the source, and not files that are derived from those
sources. For a manuscript, though, I might include the pdf at major
milestones (at submission, after revision, and upon acceptance), so
that I don't have to work as hard to reconstruct them.

Use a {\tt .gitignore} file so that untracked files don't show up with
{\tt git status}. You can have a global ignore file, {\tt
{\textasciitilde}/.gitignore\_global}.

But leaving off critical files is a common mistake.


## Using git on an existing project

* {\tt git init}
* Set up {\tt .gitignore} file
* {\tt git status} {\footnotesize \lolit (did you miss any?)}
* {\tt git add .} {\footnotesize \lolit (or name files individually)}
* {\tt git status} {\footnotesize \lolit (did you miss any?)}
* {\tt git commit}

I recommend using git with all of your current projects.
Start with one.

Go into the directory and type {\tt git init}. Then use {\tt git
add} repeatedly, to indicate which files you want to add to the
repository.

Then use {\tt git commit} to make an initial commit.


## Removing/moving files

For files that are being tracked by git:

* Use {\tt \hilit git rm} instead of just {\tt rm}

* Use {\tt \hilit git mv} instead of just {\tt mv}

```
$ git rm myfile
$ git mv myfile newname
$ git mv myfile SubDir/
$ git commit
```

For files that are being tracked by git: If you want to change
the name of a file, or if you want to move it to a subdirectory, you
can't just use {\tt mv}, you need to use {\tt git mv}.

If you want to remove a file from the project, don't use just {\tt
rm}, use {\tt git rm}. Note that the file won't be
completely removed; it'll still be within the history.


## First use of git

```
$ git config --global user.name "Jane Doe"
$ git config --global user.email "janedoe@wisc.edu"

$ git config --global color.ui true

$ git config --global core.editor emacs

$ git config --global core.excludesfile ~/.gitignore_global
```

The very first time you use git, you need to do a bit of
configuration.

All of this stuff gets added to a {\tt {\textasciitilde}/.gitconfig} file


## Set up GitHub repository

* Get a GitHub account
* Click the "Create a new repo" button
* Give it a {\hilit name} and description
* Click the "Create repository" button
* Back at the command line:
  *[] {\tt \hspace{-3em}  git remote add origin https://github.com/username/{\hilit repo}}
  *[] {\tt \hspace{-3em} git push -u origin master}

- - - - -

To create a GitHub repository, I generally first set things up
locally (using {\tt git init} and then a bit of {\tt git add} and
{\tt git commit}).

Then go to GitHub and click the ``Create a new repo'' button. Give
it a name and description and click ``Create repository.''

The back at the command line, you use {\tt git remote add} to
indicate the github address; then {\tt git push} to push everything
to GitHub.


## Configuration file

Part of a `.git/config` file:

```
[remote "origin"]
    url = https://github.com/kbroman/qtl.git
    fetch = +refs/heads/*:refs/remotes/origin/*

[branch "master"]
    remote = origin
    merge = refs/heads/master

[remote "brian"]
    url = git://github.com/byandell/qtl.git
    fetch = +refs/heads/*:refs/remotes/brian/*
```

The {\tt git remote add} commands adds stuff to the {\tt
.git/config} file; if you've made a mistake, you can just edit
this file.

There are three different constructions for the url: \\
{\tt https://github.com/username/repo} \\
{\tt git://github.com/username/repo} \\
{\tt git@github.com:username/repo}

With {\tt https}, you'll need to enter your GitHub login and
password each time. With {\tt git://}, you'll have only read
access. With {\tt git@github.com:}, you need to set up ssh. (More
work initially, but you'll get write access without having to enter your login and
password.)


## Branching and merging

* Use branches to test out new features without breaking the
  working code.
  *[] {\tt git branch devel}
  *[] {\tt git branch}
  *[] {\tt git checkout devel}
* When you're happy with the work, merge it back into your master
  branch.
  *[] {\tt git checkout master}
  *[] {\tt git merge devel}

- - - - -

Branching is a really important feature of git. Create a branch
to test out some new features without breaking your working
software.

{\tt git branch} is used to create branches and to see what branches
you have.

{\tt git checkout} is used to switch among branches.

{\tt git merge} is used to merge a different branch into your
current one.


## Issues and pull requests

\bbi
* Problem with or suggestion for someone's code?
\bi
* Point it out as an Issue
\ei
* Even better: Provide a fix
\bi
* Fork
* Clone
* Modify
* Commit
* Push
* Submit a Pull Request
\ei
\ei

\note{One of the best features of GitHub is the ease with which you
  can suggest changes to others' code, either via an Issue, or best of
  all via a Pull Request.
}
\end{frame}




\begin{frame}[fragile]{Suggest a change to a repo}
\bbi
* Go to the repository:
\bi
*[] {\tt http://github.com/someone/repo}
\ei
* {\hilit Fork} the repository
\bi
*[] Click the "Fork" button
\ei
* {\hilit Clone} your version of it
\bi
*[] {\tt git clone https://github.com/username/repo}
\ei
* Change things locally, {\tt git \hilit add}, {\tt git \hilit commit}
* Push your changes to \emph{your\/} GitHub repository
\bi
*[] {\tt git \hilit push}
\ei
* Go to \emph{your\/} GitHub repository
* Click "{\hilit Pull Requests}" and "New pull request"
\ei

\note{To suggest a change to someone's repository, go to their
  repository and click the ``Fork'' button. This makes a copy of the
  repo in your part of GitHub.

  Then go back to the command line and {\tt clone} your version of the
  repository.

  Make changes, test them, {\tt add}, and {\tt commit} them, and {\tt push} them to your
  GitHub repository.

  Then go back to your GitHub repository and click ``Pull Requests''
  and ``New pull request.''
}
\end{frame}


\begin{frame}[fragile]{Pulling a friend's changes}
\bbi
* Add a connection
\bi
*[] {\tt git remote add friend git://github.com/friend/repo}
\ei
* If you trust them, just pull the changes
\bi
*[] {\tt git pull friend master}
\ei
* Alternatively, fetch the changes, test them, and \emph{then\/}
  merge them.
\bi
*[] {\tt git fetch friend master}
*[] {\tt git branch -a}
*[] {\tt git checkout remotes/friend/master}
*[] {\tt git checkout -b friend}
*[] {\tt git checkout master}
*[] {\tt git merge friend}
\ei
* Push them back to your GitHub repo
\bi
*[] {\tt git push}
\ei
\ei

\note{If a friend (or perhaps someone you don't even know) has made
  suggested changes to your repository by a Pull Request, you'll get
  an email and it will show up on your GitHub repository.

  On the command line, use {\tt git remote add} to make a connection
  to their repository.

  Then use {\tt git pull}, or (better) use {\tt git fetch}, test them
  out, and then use {\tt git merge}.

  Finally, {\tt push} the changes back to your GitHub repository.
}
\end{frame}


\begin{frame}[fragile]{Merge conflicts}

\vspace{12pt}

Sometimes after {\hilit \tt git pull friend master}

\begin{lstlisting}
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
\end{lstlisting}

\bigskip

Inside the file you'll see:

\begin{lstlisting}
<<<<<<< HEAD
A line in my file.
=======
A line in my friend's file
>>>>>>> 031389f2cd2acde08e32f0beb084b2f7c3257fff
\end{lstlisting}

\bigskip

Edit, add, commit, push, submit pull request.

\note{Sometimes there will be conflicts: you and your collaborator
  will have been making changes to the same portion of a file and
  you'll have to resolve the differences.

  It's perhaps surprising how seldom this happens. git is really good
  at merging changes.

  If there's a merge conflict, there'll be a big warning message on
  {\tt git pull} or {\tt git merge},
  When you open the offending file in an editor, look for
  lines with {\tt <<<<<<<}, {\tt =======}, and {\tt >>>>>>>}. Pick and
  choose and make the file just as you want it.

  Then, {\tt git add}, {\tt git commit}, and {\tt git push}.
}
\end{frame}


\begin{frame}{git/GitHub with RStudio}

\vspace{24pt}

\figw{Images/RStudio04.png}{0.90}

\vspace{64pt}

\hfill
{\small \lolit
See \href{http://www.biostat.wisc.edu/~kbroman/presentations/GitPrimer.pdf}{GitPrimer.pdf}
or
\href{http://www.rstudio.com/ide/docs/version_control/overview}{RStudio page}}

\note{RStudio has great features for using git and GitHub.

  I'm not going to spend time talking about this here; google \\
  {\tt git site:rstudio.com}.

  The key thing is that a Project in RStudio is a directory (with some
  RStudio configuration file, {\tt blah.Proj})
  and will be your git repository.
}
\end{frame}

\begin{frame}[c]{Delete GitHub repo}

\figh{Images/RStudio12.png}{0.80}

\note{To learn git and GitHub, you'll want to create some test
  repositories and play around with them for a while. You may want to
  delete them later.

  On your computer, if you delete the {\tt .git} subdirectory, it'll
  no longer be a git repository.

  On GitHub, go to the settings for the repository and head down to
  the Danger Zone.
}
\end{frame}


\begin{frame}
\frametitle{Git at Statistics, UW-Madison}

\vspace{18pt}

\bbi
* Easy to use, free infinite private repositories.
* Not as nice of interface to review code: Rely on GUI or private web page.
* When your ssh account expires, your access to them expires.
\ei

\note{If you have an account on the UW-Madison Statistics server, you
  can use git there in place of GitHub.

  The advantage is that you can have as many private repositories as
  you want.

  The disadvantages are that you won't have the GitHub interface and
  you can only use this as long as you have a Statistics account.

  I haven't done this myself; these three slides were kindly provided
  by Tim Grilley.
}
\end{frame}


\begin{frame}
\frametitle{Git at Statistics, UW-Madison}

\vspace{18pt}

Setup (on server):
\bigskip

\bi
* Connect to server
    \bi
    *[] {\ttfn ssh bigmem01.stat.wisc.edu}
    *[] Consider using kinit + aklog if logging on frequently
    \ei
* Make Folder
    \bi
    *[] {\ttfn cd Repositories}
    *[] {\ttfn mkdir NewRepository}
    \ei
* Initialize Server Repository
    \bi
    *[] {\ttfn cd NewRepository}
    *[] {\ttfn git init}
    \ei
\ei

\note{To set up a repository you just log in
  to one of the Statistics computers, create a directory, and use {\tt
  git init}.
}
\end{frame}


\begin{frame}
\frametitle{Git at Statistics, UW-Madison}

\vspace{18pt}

Usage (on client, e.g. laptop):
\bigskip

\bi
* Clone/Pull onto other systems
    \bi
    *[] {\tt \tiny git clone ssh:{\textbackslash\textbackslash}bigmem01.stat.wisc.edu{\textbackslash\textasciitilde}[user]{\textbackslash}Repositories{\textbackslash}NewRepository}
    \ei
* Make changes, and commit
    \bi
    *[] {\ttfn git add -i}
    *[] {\ttfn git commit -m 'An informative message here.'}
    \ei
* Push changes back
    \bi
    *[] {\ttfn git push origin}
    \ei
\ei

\note{This is what you'd do on your local computer (e.g., a Windows
  laptop).

  On a Mac, you'd need to replace the backslashes with forward
  slashes.
}
\end{frame}






\begin{frame}{}

\vspace{25mm}

Open source means everyone can see my stupid mistakes.

\vspace{5mm}

Version control means everyone can see every stupid mistake I've ever
made.

\vspace{33mm}
\centerline{\scriptsize \tt \color{lolit} \href{http://bit.ly/stupidcode}{bit.ly/stupidcode}}

\note{If you store your code on GitHub, everyone can see everything.
  They can even see everything that ever was.

  I think this openness is a Good Thing. You may be shy about your
  code, but probably no one is looking. And if they are looking, that
  is actually a Good Thing.
}
\end{frame}

\end{document}
