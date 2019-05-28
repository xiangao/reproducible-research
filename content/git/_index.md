---
title: Git and GitHub
weight: 40
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

**Open source**

* Open source means everyone can see my stupid mistakes.

* Version control means everyone can see every stupid mistake I've
  ever made.

If you store your code on GitHub, everyone can see everything.
They can even see everything that ever was.

I think this openness is a good thing. You may be shy about your
code, but probably no one is looking. And if they are looking, that
is actually a good thing.

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
help you clear this hurdle, I've copied installation instructions from [The
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
   3. Keep "Use Git from the Windows Command Prompt" selected and click on
      "Next". If you forgot to do this programs that you need for the workshop
      will not work properly. If this happens rerun the installer and select
      the appropriate option.
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


## Git: Linear Workflow

The plan for this section is to show you how to take snapshots of your project
in a linear fashion. Imagine your project is a mountain. As you make your way
up the mountain it makes sense to place anchors along the way, that way if you
ever lose your footing you'll only fall to the last anchor not the bottom of
the mountain!

### Set up your camera

Before you can take pictures of your code, you'll need to initialize
your repository using `git init`. Let's create a new project folder on
your desktop and initialize it to be a git repository.

```shell
$ mkdir ~/Desktop/my-project
$ cd ~/Desktop/my-project
$ git init
Initialized empty Git repository in /Users/amarder/Desktop/my-project/.git/
```

Note that `git init` creates a `.git/` subdirectory in your current
working directory. This is where Git saves all your snapshots.

### Take a snapshot

Taking a snapshot is a two-step process. We use `git add` to stage
changes and `git commit` save the snapshot in the hidden `.git/`
subdirectory.

Let's do an example. In your project folder create a `README.md`
file.

```md
# My Example Project

Let's see if Andrew has any cool tricks to show us...
```

After you've saved that file use `git add` and `git commit` to take a
snapshot.

```shell
$ git add README.md 
$ git commit -m "Add README"
[master (root-commit) d950cb5] Add README
 1 file changed, 3 insertions(+)
 create mode 100644 README.md
```

Use `git add` to tell Git that you want to start keeping track of this
file.  This is called "staging", or you say the file is "staged". Use
`git commit` to add the file to the history of the project. The `-m`
argument allows one to enter a message. Without `-m`, `git` will spawn
a text editor. Use a meaningful message. Message can have multiple
lines, but make 1st line like the subject of an email.[^add-commit]

[^add-commit]: Why is committing a two-step process? Sometimes you'll
    be editing a whole bunch of files at once and you want to take a
    few different photos so the project history is easier to
    read. It's a non-intuitive process but the flexibility is a plus
    for many Git users.

### Take any snapshot

Let's create a Bash script to list all the files in your `.git/`
subdirectory, call it `git_list.sh`:

```bash
find .git/ -type f
```

After you save your new script you can print the results into a new
file:

```shell
$ ls
README.md	git_list.sh
$ bash git_list.sh > files.txt
$ ls
README.md	files.txt	git_list.sh
```

You can use `git add -A` to stage all changed files in this directory
and then use `git commit` to save your second snapshot.

```shell
$ git add -A && git commit -m "Wrote a bash script"
[master 7b620ba] Wrote a bash script
 2 files changed, 23 insertions(+)
 create mode 100644 files.txt
 create mode 100644 git_list.sh
```

### What files to include?

As you work with Git, you'll start to notice files that haven't
been on your radar before. For instance, when you're working
interactively in R, R will create an `.Rhistory` file to record all
the commands you type at the console. I suggest that you omit files
like these from your snapshots. That way your photos will be easier to
read, there won't be a bunch of superfluous files. Git offers a
mechanism to handle this. Create a `.gitignore` file in your project
directory and Git will ignore any file that matches a pattern in that
file, here's an example file:
```
.Rhistory
*.Rout
```
You can even set up a global ignore file using the `git config`
command.
```shell
$ git config --global core.excludesfile ~/.gitignore_global
```

The general rule for what files to include is to commit the source
files, not the derived files (R code not images).
  
Like any good rule, this one is often broken. For a manuscript, I
might include the pdf at major milestones (at submission, after
revision, and upon acceptance), so that I don't have to work as hard
to reconstruct them.

Warning: Ignoring critical files is a common mistake.

### Extras

So, you're fully equipped to snapshot your project in a linear
fashion. Here's the workflow:

1. Edit files
2. Snapshot using `git add -A && git commit -m "<insert-message>"`
3. Repeat

There are a whole bunch of additional tools I want to introduce but
are not mission-critical.

* When you've edited files but haven't taken a snapshot yet,
  `git status` will show you what files have changed.

* `git diff` will give you even more information showing what lines
  have been added/removed to each file.
  
* To list all your snapshots use `git log`.

For files that are being tracked by git:

* Use `git rm` instead of just `rm`. `git rm` removes the file and
  stages that change.

* Use `git mv` instead of just `mv`. `git mv` moves the file and
  stages that change.

A general best practice: **Use frequent, small commits.**


## Git: Nonlinear Workflow

So, your project is in good shape. You've been taking linear snapshots
and everything's working fine. You're thinking about adding this new
feature. It's going to be very complicated, require a bunch of
commits, and you're not sure it's going to work out. This is where
branches can be helpful. So, let's see how to branch and merge!

Use branches to test out new features without breaking code that
works. Use the `git branch` command to create, list, or delete
branches. Use `git checkout` to switch between branches. Below we (1)
create a branch, (2) list all branches, and (3) switch to the new
branch.

```shell
$ git branch my-experiment
$ git branch
* master
  my-experiment
$ git checkout my-experiment
Switched to branch 'my-experiment'
```

Once you're on the new branch feel free to experiment freely. Nothing
you do here will affect the `master` branch until you merge it
back. Edit some files and create a new commit on the `my-experiment`
branch.

When you're happy with the work, merge it back into your `master`
branch. You do this by (1) switching to the `master` branch and (2)
merging the `my-experiment` branch into your current branch (`master`).

```shell
$ git checkout master
Switched to branch 'master'
$ git merge my-experiment
Updating 7b620ba..ead9d4c
Fast-forward
 README.md | 2 ++
 1 file changed, 2 insertions(+)
```

If you're working alone you probably won't see much value in using
branches. When you're working with others they become mission
critical...


## GitHub: Collaboration

I have posted this lesson on GitHub because I want to collaborate
with you to make these materials better. In this section, I will walk
through the tools you'll need so we can work together!

There are two different models for contributing to projects on GitHub:

1. In the **fork and pull model**, anyone can fork an existing
   repository and push changes to their personal fork without needing
   access to the source repository. The changes can be pulled into the
   source repository by the project maintainer. This model is
   popular with open source projects as it reduces the amount of
   friction for new contributors and allows people to work
   independently without upfront coordination.

2. In the **shared repository model**, collaborators are granted push
   access to a single shared repository and topic branches are created
   when changes need to be made. Pull requests are useful in this
   model as they initiate code review and general discussion about a
   set of changes before the changes are merged into the main
   development branch. This model is more prevalent with small teams
   and organizations collaborating on private projects.

Since I want this lesson to be open and allow anyone to suggest
changes, I will be focusing on the fork and pull model. 

### Suggest a change

One of the best features of GitHub is the ease with which you can
suggest changes to others' code, either via an Issue, or best of all
via a Pull Request.

* Issues = "Can you change this?"
* Pull Requests = "I changed this. Can you incorporate this change?"

Here's the process for submitting a pull request. 

1.  **Go to the repository**
    
    Using your web browser, find the repository on GitHub you want to
    contribute to. Feel free to use [this
    repository](https://github.com/hbs-rcs/reproducible-research) for
    practice.
    
2.  **Fork the repository**
    
    This is done by clicking the "Fork" button. This copies the
    repository to your GitHub account.
    
3.  **Clone the repository**
    
    On the command line use the `git clone` command (be sure to
    insert your GitHub username and the correct repository name).
    ```
    $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
    ```
    This copies your repository from GitHub to your local machine.
    
4.  **Create a new branch**
    
    To create a new branch and switch to it with one command use
    `git checkout -b`.
    ```
    $ cd YOUR-REPOSITORY
    $ git checkout -b BRANCH-NAME
    ```
    Working on a new branch leaves the `master` branch
    unchanged. This will make it easier for you to make additional
    contributions in the future.
    
5.  **Create new commit(s)**

    Make your desired edits and commit them.
    ```
    $ git add -A && git commit -m "COMMIT-MESSAGE"
    ```
    
6.  **Push your changes to GitHub**
    
    Use `git push` to push your new branch up to GitHub.
    ```
    $ git push origin BRANCH-NAME
    ```
    This updates your copy of the repository on GitHub.
    
7.  **Create pull request**
    
    Go to your GitHub repository
    `https://github.com/YOUR-USERNAME/YOUR-REPOSITORY` and click "New
    pull request". The final steps on GitHub are (hopefully) pretty
    clear; let me know in the comments if you run into any
    difficulties. After the pull request has been created, it will be
    easy for the project maintainer to merge your modifications into
    the `master` branch of their repository.

Admittedly, this is a lot of work for you. The advantage of this
approach is it's very little work for the project maintainer, so
they'll be more likely to incorporate your work. Over time, you'll get
used to the process and it will be less work for you.

### Suggest another change

I want you to be a frequent collaborator on these materials. Ideally,
the `master` branch will be changing often. The
instructions in the previous section are great for your first pull
request, but I want you to be set up to make many more pull requests
in the future. To do this, we'll use the `git remote` command to tell
Git there's another repository you want to track.

```
git remote add rcs https://github.com/hbs-rcs/reproducible-research.git
```

This will add information to the `.git/config` file.[^remotes]

```
[remote "origin"]
	url = https://github.com/your_username/reproducible-research.git
	fetch = +refs/heads/*:refs/remotes/origin/*

[remote "rcs"]
	url = https://github.com/hbs-rcs/reproducible-research.git
	fetch = +refs/heads/*:refs/remotes/rcs/*
```

[^remotes]: Occasionally, I have had to edit this file to fix unwanted
    behavior. There are three different constructions for the url:
    
    1.  `https://github.com/user/repo`
    2.  `git://github.com/user/repo`
    3.  `git@github.com:user/repo`
    
    With `https://`, you'll need to enter your GitHub login and password each
    time. With `git://`, you'll have read-only access. With `git@`, you
    need to set up ssh (more work initially, but you'll get write access
    without having to enter your login and password).

Once you've set your remote the process for submitting pull requests
looks like this:

1. Update your `master` branch to match mine:
   ```
   git checkout master
   git pull rcs master
   ```
2. Create a new branch based off of `master` to work on:
   ```
   git branch new-feature
   git checkout new-feature
   ```
3. Make your changes and commit them (`git add`, `git commit`).
4. Push your branch to your GitHub repository:
   ```
   git push origin new-feature
   ```
5. Create a pull request.

### Merge conflicts

At some point in the future, you may be faced with a merge
conflict. Here's how they happen:

1. You're working on the project on your computer.
2. I'm also working on the project and I update the `master` branch.
3. You go to submit a pull request but your changes can't be merged
   into my `master` branch because we made conflicting edits.
   
Here's how to handle merge conflicts. Update your `master` branch to
match mine.

```
git checkout master
git pull rcs master
```

Merge `master` into the branch you've been working on.

```
git checkout new-feature
git merge master
```

You'll see a message letting you know there's a merge conflict.

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
A line in my RCS's file.
>>>>>>> 031389f2cd2acde08e32f0beb084b2f7c3257fff
```

Edit the file as you see fit (keep your line, keep my line, come up
with an entirely new line). Then you're ready for the typical process
(`git add`, `git commit`, `git push origin new-feature`).


## Lab

### Objective

* I want your help!
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
repository](https://github.com/hbs-rcs/reproducible-research) and
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

> How do I delete a repo?

* On your computer, if you delete the `.git` subdirectory, the folder
  will no longer be a Git repository.

* On GitHub, go to the settings for the repository and head down to
  the "Danger Zone".


