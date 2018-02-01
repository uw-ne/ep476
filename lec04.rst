Lecture #2: Managing your environment & searching your files
=============================================================

Learning objectives
---------------------

#. Unix/Linux Command-line

   #. Read and change permissions on files to share with others

   #. read and change environment variables and aliases

   #. configure the environment by chaning the ``.bashrc`` file


Activities
----------        
      
#. open a terminal

#. managing your environment

   * important environment variables

     * ``echo`` to see the values of each one: ``$USERNAME, $PWD, $PATH, $GROUP, $HOME, $PS1``

     * ``env`` to see them all

   * set an environment variable with ``export bestClass=EP476`` - note: no ``$``

     * use ``echco`` to test that you set it correctly
     
   * set the prompt with ``export PS1="Have a great day <name>: [\w]"``

   * make an alias to ``ls -ltr`` with ``alias lT='ls -ltr'``

   * save your environment by editing ``.bashrc``

     * new prompt

     * alias ``ls`` to be ``ls --color=auto``

#. permissions

   * find a partner and log in to each other's computer using ``ssh <username>@tux-??`

   * change to the ``/tmp`` directory

   * make a directory there with your username and copy your ``sports.txt``
     file to there

   * can you access each other's directories?

   * examine the permissions of those directories

   * change the permissions to allow ``cd`` but not ``ls``

     * ``chmod o+x .`` or ``chmod a+x .`` or ``chmod o+x /tmp/<username>``

   * make a subdirectory there with the other person's username

   * who can see that new directory?

   * change the permissions to allow ``cd`` and ``ls`` of the new directory

   * place a copy of ``sport.txt`` into the new directory

   * change the permissions of ``sport.txt`` to allow the other person to read it

   * copy the other person's ``sport.txt`` file to your own directory in ``/tmp``

   * who can read/see which files?

#. ``history``

   * review the history of your commands using ``history``

   * save the last 5 lines of your history to a file using ``history | tail -n 5 > recent_history.txt``


#. Searching in files: ``grep``

   * go to the ``data/elements`` directory in the sandbox data

   * find the oxidization states of all elements with ``grep oxidization *``

   * count the number of times that ``melting`` occurs in each file with ``grep -c melting *``

   * find the files that do not have melting points with ``grep -c melting * | grep :0``

#. Searching for files: ``find``

   * find all the files in the ``data`` directory that:

     * have ``ane`` in their name: ``find . -name "*ane*"``

     * have a size larger than 1000 bytes: ``find . -size +1000c``

     * have a size between 1000 and 10000 bytes: ``find . -size +1000c -size -10000c``

     * have a size between 1000 and 10000 bytes and have ``ane`` in their name:
       ``find . -size +1000c -size -10000c -name "*ane*"``

#. Loops

   * basic syntax/construct:  ``for <loop variable> in <list of values>; do ....  ;done``

   * go to ``data/elements`` directory

   * make a subdirectory ``tmp``

   * copy all the elements to the ``tmp`` directory with ``new.`` prepended to its name

     * ``for element in *.xml; do cp $element tmp/new.$element; done``

   * there are many ways to create a list of values, best to think of a string
     converted to items separated by whitespace

     * wildcards are interpretted as lists of files in the local directory,
       e.g. ``*.xml`` for all the files in this directory that match that
       pattern

     * surrounding a command with backticks (`````) makes the output of that
       command useable as a string, e.g. ```find . -name "*.xml"``` for all
       the files in this directory or any subdirectory that match that string

#. Conditionals

   * basic syntax/construct:   ``if <test>; then ....; fi``
       
`Command-line Cheat Sheet <http://www.catonmat.net/download/gnu-coreutils-cheat-sheet.pdf>`_

