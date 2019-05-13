---
title: Version Control with Git and GitHub
---

## Introduction

### Version control and reproducible research

Version control is not strictly necessary for reproducible research,
and in the short term it's a lot of work (to learn and to use), but
**the long term benefits are enormous**.

<!-- NOTES -->

I use version control for: software, data analysis projects, papers,
talks, and web sites.

People are more resistant to version control than to any other tool
because of the short-term effort and the lack of recognition of the
long-term benefits.


### Why use formal version control?

* Maintain a history of all changes
  * Able to go back in time
  * See what changed between two time points
* No worries about breaking things
* Merge changes from multiple people

<!-- NOTES -->

With formal version control, you'll save the entire history of
changes to the project, and you can easily go back to any
point in the history of the project, to see how things were behaving
at that point.

You'll be able to make modifications (e.g., to try out a new
feature) without worrying about breaking things that work.

And version control is especially useful for collaboration. If a
collaborator has made a bunch of changes, it'll be much easier to
see what was changed and to incorporate those changes.


### What is Git?

* Formal version control system
* Designed for managing code
* Tracks any content (but best for plain text files)
  * source code
  * data analysis projects
  * manuscripts
  * websites
  * presentations
* Excellent for asynchronous collaboration

<!-- NOTES -->

We're going to focus on Git, the version control system developed by
Linus Torvalds for managing the source code for Linux.

You can track any content, but it's mostly for tracking plain text
files, but that can be most anything (source code, data analysis
projects, manuscripts, websites, presentations).


### Why use Git?

* It's fast
* You don't need access to a server
* Amazingly good at merging simultaneous changes
* Everyone's using it

<!-- NOTES -->

Git is fast, you can use it locally on your own computer, it's
amazingly good at merging changes, and there are lots of people using
it.


### What is GitHub?

* A home for git repositories
* Web interface for exploring git repositories
* **Real** open source
  * Immediate, easy access to the code
* Like facebook for programmers

<!-- NOTES -->

GitHub is a website that hosts git repositories, with a nice
graphical user interface for exploring git repositories.

Source code on GitHub is real open source: anyone can
study it and grab it.

GitHub is sort of like Facebook for programmers: you can see what
people are up to, and easily collaborate on shared projects.


### Why use GitHub?

* Handles the server aspects of Git
* Graphical user interface for Git
  * For exploring code and its history
* Provides issue tracking
* Facilitates:
  * Learning from others
  * Seeing what people are up to
  * Contributing to others' code
* Lowers the barrier to collaboration
  * "You have a typo" vs. "Here's a correction for that typo"

<!-- NOTES -->

GitHub takes care of the server aspects of Git, and you get a
great GUI for exploring your repositories.

GitHub is great for browsing others' code, for learning; you don't
even have to download it to your computer. And it's really easy to
contribute to others' code (e.g., to report typos in their
documentation).


## How to use Git

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

* Create a `README.md` file

```
How to display data badly
=========================

Karl Broman gives a talk inspired by Howard Wainer's
article by the same name: H Wainer (1984) How to
display data badly. American Statistician 38:137-147

A recent PDF is [here][1].

[1]: http://www.biostat.wisc.edu/~kbroman/talks/graphs2013.pdf
```

<!-- NOTES -->

A README file is a great place to start a new project. It can give
readers of your files a high-level overview of the project.


### Incorporate into repository: part 1 of 2

* Stage the changes using `git add`

```
$ git add README.md
```

Use `git add` to tell git that you want to start keeping
track of this file.  This is called "staging", or you say the file
is "staged".


### Incorporate into repository: part 2 of 2

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

This will remove/move the file/directory **and** stage the change.

<!-- NOTES -->

For files that are being tracked by git: If you want to change
the name of a file, or if you want to move it to a subdirectory, you
can't just use `mv`, you need to use `git mv`.

If you want to remove a file from the project, don't use just
`rm`, use `git rm`. Note that the file won't be
completely removed; it'll still be within the history.


### First use of Git

```
$ git config --global user.name "Jane Doe"
$ git config --global user.email "jdoe@hbs.edu"
$ git config --global color.ui true
$ git config --global core.editor emacs
$ git config --global core.excludesfile ~/.gitignore_global
```

The very first time you use git, you need to do a bit of
configuration.

All of this stuff gets added to a `~/.gitconfig` file


## How to use GitHub

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

The back at the command line, you use `git remote add` to
indicate the github address; then `git push` to push everything
to GitHub.


### Configuration file: part 1 of 2

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

### Configuration file: part 2 of 2

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

Branching is a great feature of git. Create a branch
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
repo in your part of GitHub.

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

If a friend (or perhaps someone you don't even know) has made
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

It's perhaps surprising how seldom this happens. git is really good
at merging changes.

If there's a merge conflict, there'll be a big warning message on
`git pull` or `git merge`,
When you open the offending file in an editor, look for
lines with `<<<<<<<`, `=======`, and `>>>>>>>`. Pick and
choose and make the file just as you want it.

Then, `git add`, `git commit`, and `git push`.


### Delete a repo

To learn git and GitHub, you'll want to create some test
repositories and play around with them for a while. You may want to
delete them later.

* On your computer, if you delete the `.git` subdirectory, it'll no
  longer be a git repository.

* On GitHub, go to the settings for the repository and head down to
  the "Danger Zone".


### Open Source

* Open source means everyone can see my stupid mistakes.

* Version control means everyone can see every stupid mistake I've
  ever made.

If you store your code on GitHub, everyone can see everything.
They can even see everything that ever was.

hi

I think this openness is a Good Thing. You may be shy about your
code, but probably no one is looking. And if they are looking, that
is actually a Good Thing.

## Lab

### 1. User A

- Set up a new repository, locally

        mkdir TestRepo
        cd TestRepo
        git init

- Create or copy over a file or two and add them to the repository.

        touch ReadMe.md
        [edit the file]
        git add ReadMe.md
        git commit

- Go to your GitHub account and create a new repository

- Connect your local repository to GitHub

        git remote add origin https://github.com/userA/TestRepo

- Push your local repository to GitHub

        git push -u origin master

### 2. User B

- Fork user A's repository on GitHub: go to
  `http://github.com/userA/TestRepo` and click the "Fork" button.

- Clone _your_ version of that repository locally

        git clone https://github.com/userB/TestRepo

- Change a file, and another file

        cd TestRepo
        [change/copy files]
        git add [filenames]
        git commit

- Push the changes to GitHub

        git push

- Make a pull request:

    - Go to _your_ version of the repository on GitHub
      (`http://github.com/userB/TestRepo`)
    - Click "Pull requests"
    - Click "New pull request"
    - Click "Create pull request"
    - Optionally add a comment
    - Click "Create pull request"

### 3. User A

- Connect to User B's repository

        git remote add userB git://github.com/userB/TestRepo

- Fetch the changes from User B

        git fetch userB

- Checkout their version of the repository as a local branch

        git checkout -b userB userB/master

- Check that you like the changes

- Use `git branch` to see your branches; the asterisk indicates the
  one you're currently on.

- Switch back to ("`checkout`") your master branch

        git checkout master

- Note that the files are in the state that _you_ left them.

- Merge their work into your master branch.

        git merge userB

- Push the work to github.

        git push

- Make another change to the file; then `add`, `commit`, and `push`.

### 4. User B

- Add a connection to User A's repository

        git remote add userA git://github.com/userA/TestRepo

- Fetch User A's latest

        git fetch userA

- Check it out as a local branch

        git checkout -b userA userA/master

- Test things

- Checkout your master, merge the change from User A, and push to
  github.

        git checkout master
        git merge userA
        git push

### 5. Users A and B

- Make simulateneous changes, then `add`, `commit`, and `push`.

### 6. User B

- Pull User A's change

        git checkout userA
        git pull userA master

- Go back to your master branch and merge the change from User A.

        git checkout master
        git merge userA

- Fix the merge conflict; then `add`, `commit`, `push`.

- Make another pull request

### 7. User A

- Fetch User B's repository

        git checkout userB
        git pull userB master

- Merge into your master branch

        git checkout master
        git merge userB

- Push back to github

        git push


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
