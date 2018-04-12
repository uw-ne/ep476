# Lecture #22: Working with files, Debugging and Output Formats

## Lecture Objectives


## Textbook Reference

## Activities

* openning files
  * `with open() as f:`

* writing to files
  * f.write()

* reading from files
  * for line in f.readlines():

* using the debugger (pdb)
  * import pdb
  * pdb.set_trace()
  * commands: step, next, print, list

* writing other output formats
  * start from sequence generator
  * add method to write text file:
     * argument to set filename
  * add method to write CSV file:
     * argument to set format
     * conditional to call correct output method
     * import csv
     * writerow
  * add method to write HDF5 file:
    * extend list of allowable formats
    * extend conditional
    * import tables
    * variout pytables syntax
    
