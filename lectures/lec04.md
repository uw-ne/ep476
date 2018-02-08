# Lecture #4: Managing your environment, searching your files, and bash scripts

## Learning objectives

### Unix/Linux Command-line

1. read and change environment variables and aliases
1. configure the environment by chaning the `.bashrc` file
1. Read and change permissions on files to share with others
1. Search within files with `grep`
1. Search among files with `find`
1. Construct loops with bash
1. Invoke conditionals with bash
1. Write a bash script for repetitive tasks

## Textbook Reference

Chapter 1, Pages 29-38

## Activities
      
1. open a terminal
1. managing your environment

   * important environment variables

     * `echo` to see the values of each one: `$USERNAME, $PWD, $PATH, $GROUP, $HOME, $PS1`
     * `env` to see them all

   * set an environment variable with `export bestClass=EP476` - note: no `$`

     * use `echco` to test that you set it correctly
     
   * set the prompt with `export PS1="Have a great day <name>: [\w]"`
   * make an alias to `ls -ltr` with `alias lT='ls -ltr'`
   * save your environment by editing `.bashrc`

     * new prompt
     * alias `ls` to be `ls --color=auto`

1. permissions

   * find a partner and log in to each other's computer using `ssh <username>@tux-??`
   * change to the `/tmp` directory
   * make a directory there with your username and copy your `sports.txt`
     file to there
   * can you access each other's directories?
   * examine the permissions of those directories
   * change the permissions to allow `cd` but not `ls`

     * `chmod o+x .` or `chmod a+x .` or `chmod o+x /tmp/<username>`

   * make a subdirectory there with the other person's username
   * who can see that new directory?
   * change the permissions to allow `cd` and `ls` of the new directory
   * place a copy of `sport.txt` into the new directory
   * change the permissions of `sport.txt` to allow the other person to read it
   * copy the other person's `sport.txt` file to your own directory in `/tmp`
   * who can read/see which files?

1. `history`

   * review the history of your commands using `history`
   * save the last 5 lines of your history to a file using `history | tail -n 5 > recent_history.txt`

1. Searching in files: `grep`

   * go to the `data/elements` directory in the sandbox data
   * find the oxidization states of all elements with `grep oxidization *`
   * count the number of times that `melting` occurs in each file with `grep -c melting *`
   * find the files that do not have melting points with `grep -c melting * | grep :0`

1. Searching for files: `find`

   * find all the files in the `data` directory that:

     * have `ane` in their name: `find . -name "*ane*"`
     * have a size larger than 1000 bytes: `find . -size +1000c`
     * have a size between 1000 and 10000 bytes: `find . -size +1000c -size -10000c`
     * have a size between 1000 and 10000 bytes and have `ane` in their name:
       `find . -size +1000c -size -10000c -name "*ane*"`

1. Loops - consider python

   * basic syntax/construct:  `for <loop variable> in <list of values>; do ....  ;done`
   * go to `data/elements` directory
   * make a subdirectory `tmp`
   * copy all the elements to the `tmp` directory with `new.` prepended to its name

     * `for element in *.xml; do cp $element tmp/new.$element; done`

   * there are many ways to create a list of values, best to think of a string
     converted to items separated by whitespace

     * wildcards are interpretted as lists of files in the local directory,
       e.g. `*.xml` for all the files in this directory that match that
       pattern

     * surrounding a command with backticks (```) makes the output of that
       command useable as a string, e.g. ``find . -name "*.xml"`` for all
       the files in this directory or any subdirectory that match that string

1. Conditionals

   * basic syntax/construct:   `if <test>; then ....; fi`
   * `many ways to format tests<http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_07_01.html>`_
   * some common examples for in scripts:

     * `if [ "$#" -ne 1 ]; then` will test whether there was 1 and only 1 argument
     * `if [ -a "$1" ]; then` will test whether the file name specified in the first argument exists

1. Making scripts

   * like any language:

     * set variables
     * execute commands
     * conditionals
     * loops

   * many ways to execute

     * change file permissions to be executable and run like any command
     * `source <filename>`
     
1. Getting help

   * It is very common for expert software engineers to rely on Google for assistance.
   * One of the best resources is [Stack
     Overflow](https://stackoverflow.com/) and Q&A posted there often comes
     up near the top of a Google search


   
[Command-line Cheat Sheet](http://www.catonmat.net/download/gnu-coreutils-cheat-sheet.pdf)

