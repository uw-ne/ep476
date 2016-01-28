Homework #1
===========

EP476: Introduction to Scientific Computing for Engineering Physics
-------------------------------------------------------------------

**Due: Thursday, February, 4, 1:00 PM**

Most of these questions are based on a common directory structure found at
~wilsonp/ep476-hw1.

Please turn in your solutions by email.  Some of your answers can be in the body of the message itself or in a standard text file.  If you are adding other attachments, please use PDF files.

1. Make a copy of this directory and all of its contents in your own
   filespace.

2. What is the command that will tell you the full path of your copy of this
   directory?  What is that full path?

3. Describe the contents of this subdirectory in a way that shows the
   hierarchy and indicates which are files, which are directories and which
   are symbolic links.

4. Write the commands that would accomplish the following in precisely this order:

      * change to the `fusion` directory
      * rename the `tokamak.rst` file to be `tokamak.txt`
      * make two directories: `magnetic` and `inertial`
      * move the `tokamak.txt` and `stellarator.txt` files to the `magnetic` directory
      * move the `iec.txt` and `laser.txt` files to the `inertial` directory
      * list the contents of the `thermal` subdirectory of the `fission` directory
      * create a symbolic link in your current directory (`fusion`) to the
        `hybrid.txt` file that is in the `fission` directory
      * create an environment variable called "NUCLEAR_PATH" that refers to
        the your copy of the top-level directory (you do NOT need to include
        this in your `.bashrc` file)
      
5. Repeat question #3 with the new directory structure.

6. What is the command to change your prompt and remove the username and
   hostname portion? (You may choose to do this by adding it to you `.bashrc`
   file, but you do not have to.)

7. Create an alias that will show you a long listing of the `fission`
   directory that you copied above.

8. In what ways does tab completion improve both accuracy and efficiency when
   working with the command-line?

9. What did you learn about the command-line that might affect the way that
   you work?
      
