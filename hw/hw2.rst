Homework #2
===========

EP476: Introduction to Scientific Computing for Engineering Physics
-------------------------------------------------------------------

**Due: Tuesday, February 23, 1:00 PM**

This homework is based on the concept of an event
log in a Monte Carlo radiation transport
application.  In this kind of application, a
particle moves around a system colliding with the
atoms in that system, losing energy, and changing
direction.  Each of these collisions is an event
and it is often necessary to keep a log of these
events.

1. Start a new repository for your EventLog manager

   a. Start a new repository on Github called "EventLog"
   b. Clone the repository to your local system (e.g. CAE).
   c. Write a README file with the introductory paragraph above.
   d. Commit this file to repository.
   e. Push the modified file to your Github repository.

2. Branch: Create a new branch to complete the
   next problem.  Put the answers to problem 3 in a
   text file.

3. Each event in an event log has the following information:

   * the numerical ID of the particle
   * the location of the event in 3-D space
   * the direction of the particle as it arrived
     at the event, normally expressed as a unit
     vector
   * the energy of the particle as it arrived at
     the collision
   * the type of atom involved in the collision,
     identified by its atomic number and its
     atomic mass
   * the type of reaction that occurred
   
   a. Consider particle 43 that has an event at a
      location of (3,4,5) traveling in a straight
      line from location (8,1,2), with an energy
      of 2.3 MeV, interacting with a deuterium atom,
      with reaction code 102.
      
      i. Write the python code to calculate the
         distance between this collision and the
         previous one.  (Hint: you may need the
         `math` module)
      ii. Write the python code to calculate the
         unit vector that describes the direction
         of the particle.
      iii. Write the python code to calculate the
           energy of the particle in units of eV.

   b. What kind of container would be best for
      storing all the information about an event?
      Describe why you chose this container by
      contrasting it with other container
      choices. Write the code to store this
      information in this container.  Note, you
      will need to carefully choose the data
      structure for each of pieces of information,
      and choose good names for these variables.
   c. What kind of container would be best for
      storing many events together in a 'log'?
      Describe why you chose this container by
      contrasting it with other container choices.
      Write the python code to store three copies
      of the above event in a single data
      structure
   d. Imagine an event log made of the data
      structures you have chosen above that is
      storing many events.

      i. Write the python code to determine the
         change in energy between the 5th and 6th
         event.
      ii. Write the python code to calculate the
          distance between the 7th and 8th event.
      iii. Write the python code to determine if
           the 4th event was more aligned with the
           z-axis than the 9th.

4. Merge: merge this branch with the new feature
   into the master branch your repository.
