# Lecture #6: Collaborative development with git and Github

## Lecture Objectives

1. use branching & merging to isolate changes to code
1. describe the benefits of a cloud-based git service
1. describe a situation in which a local server-based repo is sufficient
1. clone a github based repo
1. push changes from a local clone of a repo to the cloud-based repo
1. add remote repos to your local clone
1. create a pull request
1. comment on a pull request
1. ensure that your fork (and clone) are syncronized with changes in the
   "upstream" repo
1. amend a pull request based on feedback

## Textbook Reference

Chapter 12, pages 371-380

## Activiteis

1. Add a layer to the onion with branching (10 min)

   * describe branching workflow
   * go to `planets` directory
   * create a new branch called `venus`
   * change to that branch
   * create/edit a file named `venus.txt` that says "Kind of cloudy and hard to breath"
   * add/commit that file to this branch
   * complete another edit/add/commit cycle to this file that says "Maybe we
   can build cities in the clouds"
   * change to the `master` branch
   * look at differences between branches
   * merge `venus` into `master`

1. Introduce rebase (15 min)

   * from `master` create and switch to a new branch `earth`
   * create/add/commit a file `earth.txt` with some interesting fact about earth
   * switch back to `master`
   * repeat with `jupiter`
   * switch back to `master`
   * compare `master` vs `earth` and `master` vs `jupiter`
   * merge `earth` into `master`
   * switch to `jupiter`
   * discuss rebase vs merge
   * rebase `jupiter` onto `master`
   * switch back to `master`
   * compare `master` vs `jupiter`
   * merge `jupiter` into `master`

1. discuss differences between simple server and cloud service

   * Code browsing with syntax highlighting
   * Collaboration & access control
   * Issue tracking
   * Code review for new contributions
   * Project management

1. discuss different options: esp. bitbucket & github (1 min)

1. dicuss **basic** workflow of remote interaction (5 min)

   * simple server or cloud service

     * clone once
     * fetch, merge/rebase, (edit, add, commit) x many, push 

1. fork/clone/add element to Chart of Nuclides  (8 min)
   1. browse to CoN site
      * explore GH repo
   1. fork repo
      * explore their fork - how is it different from the parent
   1. clone repo
   1. choose an element (randomize) and create a branch with that name
      * discuss why a branch
   1. use a number of edit/add/commit cycles to populate your element - at least partially
   1. push your changed branch back to your repo
      * explore your changed repo

1. connect to someone else's Chart of Nuclides repo  (8 min)
   1. add gonuke as remote
   1. fetch gonuke's repo
   1. look at branches
   1. compare branches
   1. add uw-ne as remote
   1. fetch uw-ne
   1. look at branches
   1. compare branches: esp. `master` vs `uw-ne/master`

1. Pull requests (12 min)
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

1. Keeping your repo in sync  (8 min)
   1. merge `gonuke` pull request
   1. review your PR - has it changed?
   1. fetch from `uw-ne` again
      * notice what has changed
   1. compare `master` vs `uw-ne/master`
   1. rebase `master` onto `uw-ne/master`
   1. push your `master` branch to your repo to keep it sync'ed
   1. switch to your element branch
   1. rebase your branch onto `uw-ne/master` (or `master`)
   1. push your element branch to your repo now that it's rebased
   1. review your PR - has it changed?

1. Update your PR (8 min)
   1. switch to your element branch
   1. make (at least) one edit/add/commit cycle (perhaps respond to comment?)
   1. push your branch to your repo
   1. review your PR - has it changed?

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
