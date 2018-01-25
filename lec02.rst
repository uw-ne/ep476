Lecture #2: Working with files and your environment
===================================================

Learning objectives
---------------------

#. Unix/Linux Command-line

   #. Differentiate between the terminal window and the shell

   #. List the aspecst of a shell that make it a programming language
   
   #. Draw a filespace as a tree of directories

   #. Identify the current working directory with ``pwd``

   #. Define the meaning of ``.``, ``..`` and ``~``

   #. Recognize whether a path is an absolute path or a relative path

   #. Use different options to render different formats of file list with ``ls``

   #. Use ``man`` to learn more about a command by recognizing the components
      of a command from a ``man`` page
      
   #. Change directories using ``cd`` using both absolute and relative paths

   #. Make new directories using ``mkdir``
   
   #. Use tab completion to navigate a filesystem more effectively

   #. Look at files with ``head``, ``tail``, ``cat`` and ``less``

   #. Create files with ``touch``, ``cat`` and ``nano``

   #. Copy and move single files and multiple files with ``cp`` and ``mv``, respectively

   #. Be aware of the risks when copying and moving files

   #. Delete single files, multiple files, and directories with ``rm``

   #. Be aware of the risks when deleting files

   #. Use wildcards to represent sets of files in commands
      
   #. Use relative paths in shell commands to access other directories without
      going to that directory

   #. Combine shell concepts with redirection and pipes

   #. Read and change permissions on files to share with others


Activities
----------        
      
#. open a terminal

#. ``pwd``

   * type ``pwd`` and interpret results

   * draw the branch of the filesystem tree that includes your home directory, starting from the root
     
#. ``ls``

   * type ``ls`` and interpret the results

   * type ``ls .`` and interpret the results
  
   * type ``ls ..`` and interpret the results
  
   * type ``ls -l`` and interpret the results

   * for a subdirectory, ``dir``, from your current working directory, type
     ``ls <dir>`` and interpret the results
     
#. ``man``

   * type ``man ls`` and discuss what you see with your neighbor

   * find a way to list all your files in one column

   * find a way to sort your file listing by the age of the file

   * find a way to sort your file listing by the size of the file
     
#. ``cd``

   * change to the parent of your home directory

   * change back to your home directory

   * use a relative path to change to the "grand-parent" of your home directory

   * change back to your home directory with a relative path

   * repeat and change back to your home directory with no path

   * explore the ``/bin`` directory

   * use tab completion to be more effective when moving around the file system

   * draw a partial picture of the file tree that includes your home directory
     
#. ``mkdir``

   * make a new directory called ``ep476-sandbox`` - we will use this
     directory as a place that we can freely delete and clean out on various
     occasions, so don't put important things here.

   * change to that directory

   * download `this zip file
     <https://github.com/gonuke/ep476/raw/master/ecp-sample-filespace.zip>`_
     and save it in the current directory

     * BONUS: use the command-line tool ``wget`` to accomplish this

   * unpack the zip file with the command: ``unzip ecp-sample-filespace.zip``
     (Hint: use tab completion)

   * chage to the ``textbook-examples/filespace`` directory

   * draw a tree that represents this filespace
     
#. ``cat``

   * go to the ``fission/applications/power`` in Lise Meitner's directory

   * type ``cat reactor.txt`` and interpret the results

#. ``head``

   * look at the beginning of the file with ``head reactor.txt``

   * use the ``man`` pages to learn how to show only the first 5 lines
     
#. ``tail``

   * look at the end of the file with ``tail reactor.txt``

#. ``wc``

   * count the number of lines in the file with ``wc reactor.txt``

#. ``touch``

   * create a new empty file with ``touch new_file.txt``

   * check the timestamnp of ``reactor.txt`` and then update the timestamp of
     a file with ``touch reactor.txt``

#. ``nano``

   * open a file for editing with ``nano reactor.txt``

#. ``cp``

   * copy a file with ``cp reactors.txt heaters.txt`` - note: within the same directory

   * explore different patterns for different combinations:

     * one file to new file within this directory

     * one file to new file with the same name in a different directory

     * one file to new file with different name in a different directory

     * many files to a different directory, all with the same names

     * many files to a different directory, each with a new name - is this possible?

#. ``mv``

   * change to the propulsion directory

   * move a file with ``mv nuclear_plane.txt bad_idea.txt``

   * explore different patterns for different combinations:
     
     * one file to new file with the same name in a different directory

     * one file to new file with different name in a different directory

     * many files to a different directory, all with the same names

     * many files to a different directory, each with a new name - is this possible?

#. ``rm``

   * make a copy of ``bad_idea.txt`` called ``another_bad_idea.txt``

   * delete that copy with ``rm another_bad_idea.txt``

   * delete the ``propulsion`` directory with ``rm propulsion`` - does this work?

   * try ``rm -r propulsion`` - does that work?

  
  
`Command-line Cheat Sheet <http://www.catonmat.net/download/gnu-coreutils-cheat-sheet.pdf>`_

