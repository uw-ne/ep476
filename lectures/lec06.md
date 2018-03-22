# Lecture #6: Branching and working with remote repositories

## Lecture Objectives

1. use branching & merging to isolate changes to code
1. describe the benefits of a cloud-based git service
1. describe a situation in which a local server-based repo is sufficient
1. clone a github based repo
1. push changes from a local clone of a repo to the cloud-based repo
1. add remote repos to your local clone
1. create a pull request
1. comment on a pull request
1. ensure that your fork (and clone) are synchronized with changes in the
   "upstream" repo
1. amend a pull request based on feedback

## Textbook Reference

Chapter 15, pages 365-367

Chapter 16, pages 

Extra resource: [A visual representation of the layers of workflows with git][workflow]

## Activities

1. Add a layer to the onion with branching (20 min)

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

1. Introduce rebase (20 min)

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

1. discuss differences between simple server and cloud service (4 min)

   * Code browsing with syntax highlighting
   * Collaboration & access control
   * Issue tracking
   * Code review for new contributions
   * Project management

1. discuss different options: esp. bitbucket & github (1 min)

1. discuss **basic** workflow of remote interaction (5 min)

   * simple server or cloud service

     * clone once
     * fetch, merge/rebase, (edit, add, commit) x many, push 

1. fork/clone/add element to Chart of Nuclides  (15 min)
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

[workflow]: https://docs.google.com/presentation/d/1zWa5y-BUZVvR0jKCtG6ueDxPYoODKTP8xeyhZYP_eGo/edit#slide=id.g30ae4d994d_0_339
