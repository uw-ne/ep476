# Lecture #5: Introduction to Version Control with Git

## Lecture Objectives

## Textbook Reference

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

1. fork/clone/add element to Chart of Nuclides
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

1. connect to someone else's Chart of Nuclides repo
   1. add gonuke as remote
   1. fetch gonuke's repo
   1. look at branches
   1. compare branches
   1. add uw-ne as remote
   1. fetch uw-ne
