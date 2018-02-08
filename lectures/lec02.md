# Lecture #2: Navigating the file system


## Learning objectives


### Unix/Linux Command-line

1. Differentiate between the terminal window and the shell
1. Draw a filespace as a tree of directories
1. Identify the current working directory with `pwd`
1. Define the meaning of `.`, `..` and `~`
1. Recognize whether a path is an absolute path or a relative path
1. Use different options to render different formats of file list with `ls`
1. Use `man` to learn more about a command by recognizing the components
   of a command from a `man` page
1. Change directories using `cd` using both absolute and relative paths
1. Make new directories using `mkdir`
1. Use tab completion to navigate a filesystem more effectively
1. Look at files with `head`, `tail`, `cat` and `less`
1. Create files with `touch`, `cat` and `nano`

## Textbook Reference

Chapter 1, Pages 1-17

## Activities
      
1. open a terminal
1. `pwd`

   * type `pwd` and interpret results
   * draw the branch of the filesystem tree that includes your home directory, starting from the root
     
1. `ls`

   * type `ls` and interpret the results
   * type `ls .` and interpret the results
   * type `ls ..` and interpret the results
   * type `ls -l` and interpret the results
   * for a subdirectory, `dir`, from your current working directory, type
     `ls <dir>` and interpret the results
     
1. `man`

   * type `man ls` and discuss what you see with your neighbor
   * find a way to list all your files in one column
   * find a way to sort your file listing by the age of the file
   * find a way to sort your file listing by the size of the file
     
1. `cd`

   * change to the parent of your home directory
   * change back to your home directory
   * use a relative path to change to the "grand-parent" of your home directory
   * change back to your home directory with a relative path
   * repeat and change back to your home directory with no path
   * explore the `/bin` directory
   * use tab completion to be more effective when moving around the file system
   * draw a partial picture of the file tree that includes your home directory
     
1. `mkdir`

   * make a new directory called `ep476-sandbox` - we will use this
     directory as a place that we can freely delete and clean out on various
     occasions, so don't put important things here.
   * change to that directory
   * download [this zip file](https://github.com/uw-ne/ep476/raw/master/ecp-sample-filespace.zip)
     and save it in the current directory

     * BONUS: use the command-line tool `wget` to accomplish this

   * unpack the zip file with the command: `unzip ecp-sample-filespace.zip`
     (Hint: use tab completion)
   * chage to the `textbook-examples/filespace` directory
   * draw a tree that represents this filespace
     
1. `cat`

   * go to the `fission/applications/power` in Lise Meitner's directory
   * type `cat reactor.txt` and interpret the results

1. `head`

   * look at the beginning of the file with `head reactor.txt`
   * use the `man` pages to learn how to show only the first 5 lines
     
1. `tail`

   * look at the end of the file with `tail reactor.txt`

1. `wc`

   * count the number of lines in the file with `wc reactor.txt`

1. `touch`

   * create a new empty file with `touch new_file.txt`
   * check the timestamnp of `reactor.txt` and then update the timestamp of
     a file with `touch reactor.txt`

1. `nano`

   * open a file for editing with `nano reactor.txt`

[Command-line Cheat Sheet](http://www.catonmat.net/download/gnu-coreutils-cheat-sheet.pdf)

