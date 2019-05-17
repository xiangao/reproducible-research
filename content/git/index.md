---
title: Version Control with Git and GitHub
---

## Introduction

This lesson aims to introduce you to using Git and GitHub for
reproducible research. The first draft of these materials was a
little intimidating and unclear about how to use these tools in
practice. Git and GitHub are valuable tools; I want to show you how to
use the tools, and you can decide whether you want to use them in your
work.

Version control software is not strictly
necessary for reproducible research. In the short-term it can be a lot
of work to learn and to use. But, it has some pretty awesome long-term
benefits. I want to ease the short-term pain of learning Git/GitHub
and illustrate the long-term gain of adding Git/GitHub to your
toolbox.

### Why use Git?

For the moment, think of Git like a camera. You can use Git to take
snapshots of your code over time. This is valuable because it lets
you:

* see how a project has evolved,
* restore your code to an old snapshot (this is super useful if you
  break something, it encourages you to experiment more freely), and
* see what changed between two snapshots.

At the same time, Git is like Adobe Photoshop. You can use Git to
combine snapshots together. This is great for collaborating with other
people.

It's worth mentioning that Git works best with plain text files (code,
markdown, csv, ...). It's less helpful when working with binary files
like Microsoft Word or Excel documents.

### Why use GitHub?

GitHub is a web application that facilitates collaboration.

* GitHub is a website that hosts Git repositories.

* It provides a nice graphical user interface (GUI) for exploring Git
  repositories.

* Source code on GitHub is **real** open source: anyone can study it
  and grab it.

* GitHub provides issue tracking.

* GitHub makes it easy to suggest changes to anyone (pull requests).

[^dvcs]: Git is a distributed version control system (DVCS). Imagine that
    you and I are working on a project together and were using GitHub
    to coordinate our work. There will be at least three copies of the
    project: one on your computer, one on my computer, and one on
    GitHub. These copies can look different. You might be working on
    adding a widget to the project and I might be working on the
    documentation. If someone asks for the current version of the
    code, what should we give them? The typical convention is the
    "master" branch on GitHub is the latest stable version.

[^facebook]: GitHub is sort of like Facebook for programmers. You can
    see what people are up to.

### Installation

A common hurdle when working with new software is installation! To
help you clear this hurdle, I've copied installation from [The
Carpentries](https://carpentries.org/). If these instructions don't
work for you, please let me know in the comments at the bottom of this
page.

#### Install Git on Windows

[Video Tutorial](https://www.youtube.com/watch?v=339AEqk9c-8)


1. Download the Git for Windows [installer](https://git-for-windows.github.io/).
2. Run the installer and follow the steps below:
   1. Click on "Next" four times (two times if you've previously
      installed Git).  You don't need to change anything
      in the Information, location, components, and start menu screens.
   2. **Select "Use the nano editor by default" and click on "Next".**
   3. Keep "Use Git from the Windows Command Prompt" selected and click on "Next".
                If you forgot to do this programs that you need for the workshop will not work properly.
                If this happens rerun the installer and select the appropriate option.
   4. Click on "Next".
   5. Keep "Checkout Windows-style, commit Unix-style line endings"
      selected and click on "Next".
   6. **Select "Use Windows' default console window" and click on "Next".**
   7. Click on "Install".
   8. Click on "Finish".

3. If your "HOME" environment variable is not set (or you don't know what this is):
   1. Open command prompt (Open Start Menu then type `cmd` and press <kbd>Enter</kbd>)
   2. Type the following line into the command prompt window exactly as shown:
      ```
      setx HOME "%USERPROFILE%"
      ```
   3. Press <kbd>Enter</kbd>, you should see `SUCCESS: Specified value was saved.`
   4. Quit command prompt by typing `exit` then pressing <kbd>Enter</kbd>.

This will provide you with both Git and Git Bash (a command line
interface).

#### Install Git on macOS

[Video Tutorial](https://www.youtube.com/watch?v=9LQhwETCdwY)

**For OS X 10.9 and higher**, install Git for Mac
by downloading and running the most recent "mavericks" installer from [this list](http://sourceforge.net/projects/git-osx-installer/files/).
Because this installer is not signed by the developer, you may have to
right click (control click) on the .pkg file, click Open, and click
Open on the pop up window. 
After installing Git, there will not be anything in your `/Applications` folder,
as Git is a command line program.
**For older versions of OS X (10.5-10.8)** use the
most recent available installer labelled "snow-leopard"
[available here](http://sourceforge.net/projects/git-osx-installer/files/).

#### Install Git on Linux

If Git is not already available on your machine you can try to
install it via your distro's package manager. For Debian/Ubuntu run
`sudo apt-get install git` and for Fedora run
`sudo dnf install git`.

### The command line

This lesson focuses on using Git at the command line. (Ideally, we
would have gone through the [Unix](../unix/) lesson and you'd be
feeling good about using command line tools. In reality, we haven't
done that. I'll try make things accessible and be responsive to any
issues you might run into.)

* These materials focus on using Git at the command line (rather
  than using a GUI) to help you understand how Git works.
  
* You might find that a GUI works better for you than the command
  line.
  
* I'm focusing on the command line because it's the same for everyone,
  and it will help you understand what GUIs are doing under the hood.
  
Back in the Unix lesson, there should be a section discussing shells.

> In computing, a shell is a user interface for access to an operating
> system's services. In general, operating system shells use either a
> command-line interface (CLI) or graphical user interface (GUI),
> depending on a computer's role and particular operation. It is named
> a shell because it is the outermost layer around the operating
> system kernel.

We are going to use Bash as our CLI shell. Bash is a commonly-used
shell that gives you the power to do simple tasks more quickly.

* On Windows, I suggest using Git Bash, which was installed when you
  installed Git.
  
* The default shell in all versions of macOS is Bash, so no need to
  install anything. You access Bash from the Terminal (found in
  `/Applications/Utilities/`).

* On Unix-like operating systems, the default shell is usually Bash,
  but if your machine is set up differently you can run it by opening
  a terminal and typing bash. There is no need to install anything.

### Git global configuration

When you first install Git, it's helpful to configure some global
variables. For instance, tell Git your name and email address for it
to use when you take snapshots of your code:

```
$ git config --global user.name "Jane Doe"
$ git config --global user.email "jdoe@hbs.edu"
```

Tell it to use nice colors when printing to the command line so it's
easier to read:

```
$ git config --global color.ui true
```

All of this information gets written to a file in your home directory
`~/.gitconfig`.

### Sign up for GitHub

If you don't already have a GitHub account...

You will need an account at [github.com](https://github.com/) for
parts of this lesson. The free account for individuals should be fine
for most users (you can always upgrade later if you want). It's worth
considering what personal information you'd like to reveal. For
example, you may want to review these [instructions for keeping your
email address
private](https://help.github.com/articles/keeping-your-email-address-private/).


## Git

### Basic use

* Change some files
* See what you've changed
  * `git status`
  * `git diff`
  * `git log`
* Indicate what changes to save
  * `git add`
* Commit to those changes
  * `git commit`

<!-- NOTES -->

These are the basic git commands you'll use day-to-day.

`git status` to see the current state of things,
`git diff` to see what's changed, and `git log` to look at
the history.

After you've made some changes, you'll use `git add` to indicate
which changes you want to commit to, and `git commit` to commit
to them (to add them to the repository).


### Initialize a repository

* Create a working directory (e.g., `~/my-project`)
* `cd` into your working directory
* Initialize it to be a git repository using `git init`
  * This creates a subdirectory `~/my-project/.git`

```
$ mkdir ~/my-project
$ cd ~/my-project
$ git init
Initialized empty Git repository in ~/my-project/.git/
```

<!-- NOTES -->

If you're starting a new, fresh project, you make a directory
for it and go into that directory, and then you type `git
init`. This creates a `.git` subdirectory.


### Produce content

* Create a short `README.md` file

```md
R for Data Science
==================

This repository contains the source of [R for Data Science][r4ds]
book. The book is built using [bookdown][bookdown].

The R packages used in this book can be installed via

    devtools::install_github("hadley/r4ds")
    
[r4ds]: http://r4ds.had.co.nz
[bookdown]: https://github.com/rstudio/bookdown
```

<!-- NOTES -->

A README file is a great place to start a new project. It can give
readers of your code a high-level overview of the project.


### Incorporate into repository (part 1 of 2)

* Stage the changes using `git add`

```
$ git add README.md
```

Use `git add` to tell git that you want to start keeping
track of this file.  This is called "staging", or you say the file
is "staged".


### Incorporate into repository (part 2 of 2)

* Now commit using ` git commit`

```
$ git commit -m "Initial commit of README.md file"
[master (root-commit) 32c9d01] Initial commit of README.md file
 1 file changed, 14 insertions(+)
 create mode 100644 README.md
```

* The `-m` argument allows one to enter a message
* Without `-m`, `git` will spawn a text editor
* Use a meaningful message
* Message can have multiple lines, but make 1st line an overview

Use `git commit` to add the file to the history of the project.


### A few points on commits

* Use frequent, small commits
* Don't get out of sync with your collaborators
* Commit the sources, not the derived files
  * (R code not images)
* Use a `.gitignore` file to indicate files to be ignored

```
.Rhistory
*.Rout
manuscript.pdf
figures/*.pdf
```

<!-- NOTES -->

I recommend using frequent, small commits. I'll make a batch of
changes with a common theme, make sure things are working, then add
and commit.

I commit only the source, and not files that are derived from those
sources. For a manuscript, though, I might include the pdf at major
milestones (at submission, after revision, and upon acceptance), so
that I don't have to work as hard to reconstruct them.

Use a `.gitignore` file so that untracked files don't show up with
`git status`. You can have a global ignore file, `~/.gitignore_global`.

```
$ git config --global core.excludesfile ~/.gitignore_global
```

But leaving off critical files is a common mistake.


### Using Git on an existing project

* `cd` into your project directory
* `git init`
* Set up a `.gitignore` file (optional)
* `git status`
* `git add`
* `git status`
* `git commit`

<!-- NOTES -->

I recommend using git with all of your current projects.
Start with one.

Go into the directory and type `git init`. Then use `git
add` repeatedly, to indicate which files you want to add to the
repository.

Then use `git commit` to make an initial commit.


### Removing/moving files

For files that are being tracked by git:

* Use `git rm` instead of just `rm`

* Use `git mv` instead of just `mv`

<!-- NOTES -->

For files that are being tracked by git: If you want to change
the name of a file, or if you want to move it to a subdirectory, you
can't just use `mv`, you need to use `git mv`.

If you want to remove a file from the project, don't use just
`rm`, use `git rm`. Note that the file won't be
completely removed; it'll still be within the history.


## GitHub

### Basic use

* Push changes to GitHub
  * `git push`
* Pull changes from your collaborator
  * `git pull` or
  * `git fetch` and `git merge`

<!-- NOTES -->

You use `git push` to push changes to GitHub, and `git pull`
(or `git fetch` and `git merge`) to pull changes from a
collaborator's repository, or if you're synchronizing a repository
between two computers.

In projects with collabotors, be sure to pull any changes from them
before starting to make your own changes, and encourage your
collaborators to do the same. If you both make a month's changes
in parallel, merging the changes will be harder.


### Set up GitHub repository

* Sign up for a GitHub account
* Click the "Create a new repo" button
* Give it a name (and description)
* Click the "Create repository" button
* Back at the command line:

  ```
  git remote add origin git@github.com:user/repo.git
  git push -u origin master
  ```

<!-- NOTES -->

To create a GitHub repository, I generally first set things up
locally (using `git init` and then a bit of `git add` and
`git commit`).

Then go to GitHub and click the "Create a new repo" button. Give
it a name and description and click "Create repository".

Then back at the command line, you use `git remote add` to
indicate the github address; then `git push` to push everything
to GitHub.


### Configuration file (part 1 of 2)

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

The `git remote add` commands adds stuff to the
`.git/config` file; if you've made a mistake, you can just edit
this file.

### Configuration file (part 2 of 2)

There are three different constructions for the url:

1.  `https://github.com/user/repo`
2.  `git://github.com/user/repo`
3.  `git@github.com:user/repo`

With `https://`, you'll need to enter your GitHub login and password each
time. With `git://`, you'll have read-only access. With `git@`, you
need to set up ssh (more work initially, but you'll get write access
without having to enter your login and password).


### Branching and merging

* Use branches to test out new features without breaking the working code.
  * `git branch devel`
  * `git branch`
  * `git checkout devel`
* When you're happy with the work, merge it back into your master branch.
  * `git checkout master`
  * `git merge devel`

<!-- NOTES -->

Branching is a great feature of Git. Create a branch
to test out some new features without breaking your working
software.

`git branch` is used to create branches and to see what branches
you have.

`git checkout` is used to switch among branches.

`git merge` is used to merge a different branch into your
current one.


### Issues and pull requests

If you have a problem with or a suggestion for someone's code:

* Point it out as an Issue
* Even better, provide a fix
  * Fork
  * Clone
  * Modify
  * Commit
  * Push
  * Submit a Pull Request

<!-- NOTES -->

One of the best features of GitHub is the ease with which you can
suggest changes to others' code, either via an Issue, or best of all
via a Pull Request.


### Suggest a change to a repo

* Go to the repository: `http://github.com/someone/repo`
* **Fork** the repository (click the "Fork" button)
* **Clone** your version of it: `git clone https://github.com/username/repo`
* Change things locally: `git  add`, `git  commit`
* Push the changes to **your** GitHub repository: `git  push`
* Go to **your** GitHub repository: `http://github.com/username/repo`
* Click "New pull request"

<!-- NOTES -->

To suggest a change to someone's repository, go to their
repository and click the "Fork" button. This makes a copy of the
repo in your GitHub account.

Then go back to the command line and `clone` your version of the
repository.

Make changes, test them, `add`, and `commit` them, and `push` them to your
GitHub repository.

Then go back to your GitHub repository and click "New pull request".


### Pulling a friend's changes

* Add a connection
  ```
  git remote add friend git://github.com/friend/repo
  ```
* If you trust them, just pull the changes
  ```
  git pull friend master
  ```
* Alternatively, fetch the changes, test them, and then merge them.

  ```
  git fetch friend master
  git branch -a
  git checkout remotes/friend/master
  git checkout -b friend
  git checkout master
  git merge friend
  ```
* Push them back to your GitHub repo
  ```
  git push
  ```

<!-- NOTES -->

If a friend (or perhaps someone you don't even know) has
suggested changes to your repository by a Pull Request, you'll get
an email and it will show up on your GitHub repository.

On the command line, use `git remote add` to make a connection
to their repository.

Then use `git pull`, or (better) use `git fetch`, test them
out, and then use `git merge`.

Finally, `push` the changes back to your GitHub repository.


### Merge conflicts

Sometimes after `git pull friend master`

```
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
```

Inside the file you'll see:

```
<<<<<<< HEAD
A line in my file.
=======
A line in my friend's file
>>>>>>> 031389f2cd2acde08e32f0beb084b2f7c3257fff
```

Edit, add, commit, push, submit pull request.

<!-- NOTES -->

Sometimes there will be conflicts: you and your collaborator
will have been making changes to the same portion of a file and
you'll have to resolve the differences.

It's perhaps surprising how seldom this happens. Git is really good
at merging changes.

If there's a merge conflict, there'll be a big warning message on
`git pull` or `git merge`,
When you open the offending file in an editor, look for
lines with `<<<<<<<`, `=======`, and `>>>>>>>`. Pick and
choose and make the file just as you want it.

Then, `git add`, `git commit`, and `git push`.


### Delete a repo

To learn Git and GitHub, you'll want to create some test
repositories and play around with them for a while. You may want to
delete them later.

* On your computer, if you delete the `.git` subdirectory, the folder
  will no longer be a Git repository.

* On GitHub, go to the settings for the repository and head down to
  the "Danger Zone".


### Open source

* Open source means everyone can see my stupid mistakes.

* Version control means everyone can see every stupid mistake I've
  ever made.

If you store your code on GitHub, everyone can see everything.
They can even see everything that ever was.

I think this openness is a good thing. You may be shy about your
code, but probably no one is looking. And if they are looking, that
is actually a good thing.

## Lab

### Objective

* I want help from **you**.
* Let's improve this documentation together.

### Process

We'll be following the
[GitHub Flow](https://guides.github.com/introduction/flow/) approach
to collaboration.

### Decide where to contribute (step 1 of 5)

* Browse through the documentation and determine where you'd like to
  help.
  
* I need help with: typos, writing, formatting, and content.

* Pick something small you can complete in a few minutes.

### Installation (step 2 of 5)

Go to [my GitHub
repository](https://github.com/amarder/reproducible-research) and
follow the Installation instructions.

(Notice that those instructions involve forking my repository and
using `git clone` to set up a local copy on your computer)

### Edit the documentation locally (step 3 of 5)

1. Use `git branch` to create a branch to experiment on.

2. Use `git checkout` to switch to your new branch.

3. Make your edits.

4. Use `git add` and `git commit` to commit those edits to your
   branch.
   
### Create a pull request (step 4 of 5)

1. Use `git push` to push your branch up to GitHub.

2. Open a Pull Request on GitHub.

### I respond to your pull request (step 5 of 5)

I will either:

* comment on your pull request, and/or

* merge it into `master`.

## Additional Tools

### RStudio integration

* RStudio has great features for using Git and GitHub from within the IDE.

* See [RStudio's documentation](https://support.rstudio.com/hc/en-us/articles/200532077-Version-Control-with-Git-and-SVN).

* Check out the [RStudio IDE Cheat Sheet](https://www.rstudio.com/resources/cheatsheets/#ide).

<!-- NOTES -->

The key thing is that a Project in RStudio is a directory (with an
RStudio configuration file, `blah.Rproj`) your `.git` folder will be
stored in this same directory.

### code.harvard.edu

* https://code.harvard.edu/
* Enterprise GitHub
* Private collaboration for teams

<!-- NOTES -->

Free accounts on [github.com](https://github.com/) now get unlimited
private repositories, but they are limited to 3 collaborators.

[code.harvard.edu](https://code.harvard.edu/) is great for teams at
Harvard that want to keep their work private.

### Graphical User Interfaces (GUIs)

* [GitHub Desktop](https://desktop.github.com/) is user-friendly
* [GitKraken](https://www.gitkraken.com/) is cross-platform

<!-- NOTES -->

Personally, I want my editor to have Git integration. I don't like
having a separate GUI for dealing with Git.

If you are working with Git at the command line a lot, I have enjoyed
[Bash-it](https://github.com/Bash-it/bash-it). Their [git
aliases](https://itsfoss.com/bash-it-terminal-tool/) save a lot of
typing.

### References

* [git - the simple guide](https://rogerdudler.github.io/git-guide/)
* [Git is a Directed Acyclic Graph and What the Heck Does That Mean?](https://medium.com/girl-writes-code/git-is-a-directed-acyclic-graph-and-what-the-heck-does-that-mean-b6c8dec65059)
* [4 branching workflows for Git](https://medium.com/@patrickporto/4-branching-workflows-for-git-30d0aaee7bf)
* [GitHub Help](https://help.github.com/en)
* [Git - Documentation](https://git-scm.com/doc)
* [Oh shit, git!](https://wizardzines.com/zines/oh-shit-git/)
* [What is version control: centralized vs. DVCS](https://www.atlassian.com/blog/software-teams/version-control-centralized-dvcs)


### FAQ

> If people were going to adopt version control only for particular
> projects (e.g., those that were especially complicated, had many
> collaborators, etc.) is there any rule of thumb that you’d give
> people for when a project gets big enough that it really should be
> version controlled? I know you version control for all projects, but
> I think people will likely use some combination of version
> controlling (project dependent) and not.

I don't have a clear-cut answer here. The advantage of focusing on
small projects is that it's a great opportunity to get familiar with
Git. The advantage to focusing on larger projects is they're likely to
have longer histories so the benefits of working with version control
will become more apparent.

> Can you add commit statements to your code so that it commits as you
> initialize a session or at various points along the way in a program
> (not sure if that makes sense as written out)?

Yes, but this is dangerous. You want to be very explicit with
Git. Tell it exactly when you want to take a snapshot of your code. If
you start automating that process, you'll likely end up with a less
useful history.

> Because people were generally very apprehensive about Git, I’m
> wondering whether it might help to divide up the sections by the
> very very basic commands and then the more advanced commands that
> might or might not come up in RCS work so they can focus on at least
> knowing the basics. People conveyed that they got especially
> confused when dealing with branching, merging, forking, etc.

Absolutely! I tried to do this by dividing commands between the
[Git](#git) and [GitHub](#github) sections.

In the Git section, we cover `status`, `diff`, `log`, `add`, `commit`,
`mv`, and `rm`. These commands are necessary for keeping a completely
linear history.

In the GitHub section, we cover `push`, `pull`, `fetch`, and
`merge`. These are necessary for collaborating with others. We also
cover `branch` and `checkout` in this section. But, maybe it makes
sense to cover branches separately because they're freaking people
out.

> I really like the idea of doing some hands on work during the
> session as you’ve added at the end. (confession: I am intimidated by
> forking, cloning, etc. over command line, but I’m sure we’ll all be
> more comfortable by the end of the session)

No reason to be intimidated. You've got this!
