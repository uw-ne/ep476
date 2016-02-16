Lecture #3: Controlling your environment & version control
===========================================================

Reading:
  * Chapter 1, (pp 18-38)
  * Chapter 15, Section 1: What is Version Control? (pp 349-351)


1. Manipulating files
    * remove
    * links
    * mkdir
    * wildcards
         * asterisk
         * question mark
         * ranges
    * flags: e.g. cp -r, mv -f, rm -f
2. Customizing your environment
    * Environment variables
       * PATH
       * HOME
       * prompt - PS1
    * aliases
    * bashrc
3. Scripting & history
4. Git intro
    * git config
    * git init
    * git add
    * git status
    * git commit
    * git log
    * git diff
 
Some useful git stuff
-----------------------

Changing your prompt to show your git branch.
+++++++++++++++++++++++++++++++++++++++++++++

Add these functions to  your `.bashrc`

``` bash
function parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1) /'
    
}

function get_git_color() {

    isred=`git status -s 2> /dev/null | egrep "^.[^? ]" | wc | awk '{print $1}'`
    isorange=`git status -s 2> /dev/null | egrep "^[^? ]" | wc | awk '{print $1}'`

    git_prompt_color=32

    if [ $isorange -ne 0 ]
    then
	git_prompt_color=33
    fi
    if [ $isred -ne 0 ]
    then
	git_prompt_color=31
    fi
    
    echo "$git_prompt_color"
}
```

and then change your prompt to include:

```
export STD_PROMPT="\[\e[1;\$(get_git_color)m\] \$(parse_git_branch)\[\e[0m\]"
```


Print a pretty log of your git repo
++++++++++++++++++++++++++++++++++++++

The following set of options for `git log` will give a color coded log that shows branches.

```
log --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s%Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --graph --decorate --date=relative
```

You can add it to your git config file (~/.gitconfig) as an alias:

```
[alias]
     plog=log --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s%Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --graph --decorate --date=relative
```

and then use it as the comment `git plog`.

