# Lecture #7: Managing collaborative contributions and conflicts

## Lecture Objectives

1. add remote repos to your local clone
1. create a pull request
1. comment on a pull request
1. ensure that your fork (and clone) are synchronized with changes in the
   "upstream" repo
1. amend a pull request based on feedback
1. identify and resolve conflicts

## Textbook Reference

Chapter 16, pages 379-384

## Activities

1. Pull requests (20 min)
   1. definition of pull request - cloud service specific
   1. launch pull request from your repo
   1. examine pull requests
   1. comment on someone else's pull request
      * opportunity to practice effective communication (e.g. please &
        thankyou)
      * comment on individual lines
      * comment on the pull request on the whole
   1. Notice access controls
   1. request a review from your pull request

1. Keeping your repo in sync  (15 min)
   1. merge `gonuke` pull request
   1. review your PR - has it changed?
   1. add uw-ne as remote
   1. fetch uw-ne
   1. look at branches
   1. compare branches: esp. `master` vs `uw-ne/master`
   1. rebase `master` onto `uw-ne/master`
   1. push your `master` branch to your repo to keep it sync'ed
   1. switch to your element branch
   1. rebase your branch onto `uw-ne/master` (or `master`)
   1. push your element branch to your repo now that it's rebased
   1. review your PR - has it changed?

1. Update your PR (10 min)
   1. switch to your element branch
   1. make (at least) one edit/add/commit cycle (perhaps respond to comment?)
   1. push your branch to your repo
   1. review your PR - has it changed?

1. Add a common file (10 min)
   1. add a file in the top directory called `completed.md`
   1. The first line should read "# List of completed elements"
   1. The third line should be the name of your element's directory and its
      english name.
   1. add/commit this new file
   1. push this branch to your repo and check the status of your PR

1. managing merge conflicts (merge additional PR causing conflict)
   1. check the status of your PR
   1. fetch `uw-ne`
   1. rebase your element branch onto `uw-ne`
   1. conflict - note options: abort, continue, skip
   1. open file with conflict and choose the correct final edits
   1. add that file (but do NOT commit)
   1. continue rebase
   1. push your branch to your repo
   1. check the status of your PR

1. connect to someone else's Chart of Nuclides repo  (15 min)
   1. add gonuke as remote
   1. fetch gonuke's repo
   1. look at branches
   1. compare branches

## Bonus topics

1. Change your prompt to constantly show you some git status information

   There are a number of different solutions shared on the internet for
   changing your bash prompt to show you the current branch you are in, and
   other information.  Here are just a few:
 
   * [Put Your Git Branch in Your Bash Prompt](http://code-worrier.com/blog/git-branch-in-bash-prompt/)
   * [git-prompt.sh from the git project](https://github.com/git/git/blob/master/contrib/completion/git-prompt.sh)
   * [bash-git-prompt adds additional info](https://github.com/magicmonty/bash-git-prompt)

1. Your life will be much simpler if you don't have to type your password
   every time you interact with github.  I encourage you to set up an ssh key
   for this:

    * [Connecting to GitHub with SSH](https://help.github.com/articles/connecting-to-github-with-ssh/)
