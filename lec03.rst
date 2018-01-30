Lecture #2: Working with files and your environment
===================================================

Learning objectives
---------------------

#. Unix/Linux Command-line

   #. Copy and move single files and multiple files with ``cp`` and ``mv``, respectively

   #. Be aware of the risks when copying and moving files

   #. Delete single files, multiple files, and directories with ``rm``

   #. Be aware of the risks when deleting files

   #. Make symbolic links with ``ln``

   #. Describe when you might want to use a symbolic link
      
   #. Use wildcards to represent sets of files in commands
      
   #. Use relative paths in shell commands to access other directories without
      going to that directory

   #. Combine shell concepts with redirection and pipes

   #. Read and change permissions on files to share with others

   #. read and change environment variables and aliases

   #. configure the environment by chaning the ``.bashrc`` file


Activities
----------        
      
#. open a terminal

#. download `a new set of sandbox files
   <http://swcarpentry.github.io/shell-novice/data/shell-novice-data.zip>`_

#. unzip those files in your sandbox

#. find those files in your sandbox

#. make a directory called ``hobbies``

#. open a new file named ``sports.txt`` in that directory with ``nano`` and list
   some of your favorite sports or other physical activities, either to play
   or to watch.
   
#. ``cp``

   * copy a file with ``cp sports.txt movement.txt`` - note: within the same directory

   * explore different patterns for different combinations:

     * one file to new file within this directory (see above)

     * one file to new file with the same name in a different directory

       * ``mkdir ../memoirs``

       * ``cp sports.txt ../memoirs/.``
       
     * one file to new file with different name in a different directory

       * ``cp sports.txt ../memoirs/family_sports.txt``

     * many files to a different directory, all with the same names

       * ``mkdir ../family``

       * ``cp sports.txt movement.txt ../family/.``

     * many files to a different directory, each with a new name - is this possible?

#. ``mv``

   * change to the ``memoirs`` directory

   * move a file with ``mv sports.txt movement.txt``

   * explore different patterns for different combinations:
     
     * one file to new file with the same name in a different directory

       * ``mkdir ../youth``

       * ``mv movement.txt ../youth/.``
         
       * ``mv ../youth/movement.txt .``
         
     * one file to new file with different name in a different directory

       * ``mv movement.txt ../youth/sport.txt``

       * ``mv ../youth/sport.txt .``

     * many files to a different directory, all with the same names

       * ``cp sport.txt movement.txt``

       * ``mv movement.txt sport.txt ../youth/.``
         
     * many files to a different directory, each with a new name - is this possible?

#. ``rm``

   * delete a file with ``rm movement.txt``

   * go up one directory
  
   * delete the ``youth`` directory with ``rm youth`` - does this work?

   * try ``rm -r youth`` - does that work?

#. ``ln``

   * return to your ``hobbies`` directory

   * edit the file ``sports.txt`` in your editor
     
   * return to your ``memoirs`` directory - has the file ``family_sports.txt`` changed?

   * delete the ``family_sports.txt`` file

   * make a symlink to a the original file with ``ln -s ../hobbies/sports.txt family_sports.txt``

   * open ``../hobbies/sports.txt`` in your editor and change a line = has the
     file ``family_sports.txt`` changed?

   * open ``family_sports.txt`` in your editor and change a line - has ``../hobies/sports.txt`` changed?
     
   * replace both the files in the ``family`` directory like this
   
#. Flags and wildcards

   * change to the ``data/elements`` directory in sandbox files

   * examine the file names - what do you notice?

   * make a listing of all the files and their sizes

   * make a listing of only the files that begin with ``S`` with ``ls S*``

     * is it any different if you type ``ls S*.xml``?

     * Use this to determine which vowel is the most common 2nd letter in an
       element name

   * make a listing of only the files that have a single letter with ``ls ?.xml``

     * make a listing of only the files that have two letters

   * make a new directories parallel to this one called ``periodic_table_1``
     and ``periodic_table_2``

   * copy all the 1-letter elements to ``periodic_table_1`` and all the
     2-letter elements to ``periodic_table_2``

   * go up to the ``data`` directory directory

   * copy the whole ``north-pacific-gyre`` directory to make a copies called
     ``south-pacific-gyre`` and ``north-atlantic-gyre``

   * in each copy, delete all the text files in the ``2012-07-03`` directory

#. Pipes and redirection

   * It is possible to send the output of one command into the input of another command

   * ``stdin`` and ``stdout``

   * go to the ``data/pdb`` directory in the sandbox

   * look at the top of ``lanoxin.pdb`` using ``head``

   * extract lines 2-4 of ``lanoxin.pdb`` using ``head -n 4 lanoxin.pdb |
     tail -n 3``

   * It is possible to send the output of one command to a file

   * save lines 2-4 of ``lanoxin.pdb`` using ``head -n 4 lanoxin.pdb | tail -n
     3 > AUTHOR.txt``

   * look at ``ethylcyclohexane.pdb``, determine which lines begin with
     ``AUTHOR`` and append those lines to ``AUTHOR.txt``
     
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

#. managing your environment

   * important environment variables

     * ``env`` to see them all

     * ``echo`` to see the values of each one: ``$USERNAME, $PWD, $PATH, $GROUP, $HOME, $PS1``

   * set an environment variable with ``export bestClass=EP476`` - note: no ``$``

   * set the prompt with ``export PS1="Have a great day <name>: [\w]"

   * make an alias to ``ls -ltr`` with ``alias lT='ls -ltr'``

   * save your environment by editing ``.bashrc``

     * new prompt

     * alias ``ls`` to be ``ls --color=auto``

#. ``history``

   * review the history of your commands using ``history``

   * save the last 5 lines of your history to a file using ``history | tail -n 5 > recent_history.txt``
     
  

        
`Command-line Cheat Sheet <http://www.catonmat.net/download/gnu-coreutils-cheat-sheet.pdf>`_

