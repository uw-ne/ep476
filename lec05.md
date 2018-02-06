# Lecture #5: Introduction to Version Control with Git

## Lecture Objectives

## Textbook Reference

Chapter 15, Pgaes 349-365

## Activities

1. Introduction to version control

   a. What is version control

      * backup a changing set of files
      * store and access an annotated history of those files
      * manage merging of changes between different set of changes

   b. Centralized vs Distributed 

1. Configuring `git`

   * set user name, email and editor

1. Why git in pure local configuration

1. Make your first git repository

   * go to your `ep476-sandbox`
   * make a new directory `planets` and change to that directory
   * initialize with `git init`
   * explore what changed: `ls -a` & `git status`

1. Discuss typical git workflow: edit, add, commit

1. Make your first commit

   * make a file `mars.txt` that says "Cold and dry, but everything is my favorite color"
   * check the status - discuss
   * add the file
   * check the status - discuss
   * commit the file
   * check the status - discuss

1. Review all changes

   * git log - discuss

1. Make your first changes

   * edit `mars.txt` to add "Two moons will make for interesting tides."
   * check the status - discuss
   * `git diff` - discuss
   * `git commit` - does nothing - why?
   * `git add`
   * `git commit`
   * `git status` - discuss
   * `git log`

1. Make another change

   * edit `mars.txt` to add "Low humidity may make it hard to grow plants"
   * `git add`
   * `git status`
   * `git diff` - where are the changes
   * `git diff --staged`
   * `git commit`
   * `git log` - different variations: `--oneline` and `--oneline --graph --all --decorate`

1. Exploring the history

   * commit hashes
   * diff from a specific hash
   * `HEAD` and `HEAD~n` as shortcuts
   * show a specific commit

1. Undoing changes

   * fresh changes - checkout
   * staged changes - reset
   * commited changes - revert

1. Ignoring files (removing clutter, avoiding mistakes)

   * add a file called 'mars.dat'
   * assuming we don't want to include these files in the repo
   * create a file called '.gitignore'
   * `git status`
   * add `*.dat` to this file
   
   
