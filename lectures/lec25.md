# Lecture #25: HDF5, Dictionary of functions, Intro to matplotlib

## Lecture Objectives


## Textbook Reference

## Activities

* add command-line argument to select output format

* add method to write HDF5 file:
  * extend list of allowable formats
  * extend conditional
  * import tables
  * various pytables syntax
    
* create a dictionary of functions to perform output
  * empty dictionary `output_method` before first output function
  * for each output function `write_seq_dict_<format>` add to dictionary:
    * `output_method['format'] = write_seq_dict_<format>`
  * populate valud choices for format command line argument with `output_method.keys()`
  * call `output_method[args.format](args.filename, seq_dict)`

* simple 2-D plots in Jupyter Notebook
  * new notebook
  * import `seq_driver` and generate a dictionary `seq_dict = seq_driver.seq_driver_incr(10,10)`
    * NOTE: this dictionary contains 9 entries, each with a list of 10 entries
  * `import matplotlib.pyplot as plt`
  * make new plot with some data
    * `plt.plot(seq_dict[(2,10)])`
    * `plt.show()`
  * add another curve (insert before `plt.show()`)
    * `plot.plot(seq_dict[(5,10)])`
  * add legend
    * add label to each plot: e.g. `plt.plot(seq_dict[(2,10)], label=str((2,10)))`
    * add legend: `plt.legend()`
  * add loop to plot all data
```
for key, seq in seq_dict.items():
   plt.plot(seq, label=str(key))
plt.legent()
plt.show()
```
