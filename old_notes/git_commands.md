#About Git 
###Git - open source distributed version control tool.

> Install Git On Windows
[Download Git for Windows]:https://git-scm.com/download/win

> Let us proceed with configuring Git with your username and email. In order to do that, type the following commands in your Git Bash:

```sh
git config - - global user.name "<your name>"

git config - - global user.email "<your email>"
```

##Git Commands
> **git config:** This command used to configure Git with your username and email

```sh
git config - - global user.name "<your name>"

git config - - global user.email "<your email>"
```

> **git init:** used to start a new repository
```sh
git init [repository name]
```

> **git clone:** This command used to obtain a repository from an existing URL
```sh
git clone [url]
```
> **git add:** This command adds a file to the staging area
```sh
git add [file]
git add *
```

> **git commit:** This command records or snapshots the file permanently in the version history.
```sh
git commit -m “[ Type in the commit message]”
git commit -a
git commit -am “[ Type in the commit message]”
```
> **git diff:** This command shows the file differences which are not yet staged.
```sh
git diff
git diff [first branch] [second branch]
```

> **git reset** This command undoes all the commits after the specified commit and preserves the changes locally.

> **git reset –hard [commit]** This command discards all history and goes back to the specified commit.
```sh
git reset –hard [commit]
```

> **git status** This command lists all the files that have to be committed.
```sh
git status
```

> **git rm** This command deletes the file from your working directory and stages the deletion
```sh
git rm [file]
```

> **git log** This command lists version history for a file, including the renaming of files also.
```sh
git log –follow[file]
```

> **git show** This command shows the metadata and content changes of the specified commit.
```sh
git show [commit]
```

> **git branch** This command lists all the local branches in the current repository.
```sh
git branch
git branch [branch name] - Creates a new branch
git branch -d [branch name] - Deletes the feature branch
```
> **git checkout** This command is used to switch from one branch to another.
```sh
git checkout [branch name]
```

> **git merge** This command merges the specified branch’s history into the current branch.
```sh
git merge [branch name]
```

> **git push** This command sends the branch commits to your current remote repository.
```sh
git push
git push [variable name] [branch]
git push –all [variable name] -Pushes all branches to your remote repository.
git push [variable name] :[branch name] -Deletes a branch on remote repository.
```
> **git pull** This command fetches changes into your local directory
```sh
git pull**
```


