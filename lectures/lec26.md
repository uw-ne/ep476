# Lecture #25: 3D in matplotlib, testing and continuous integration

## Lecture Objectives


## Textbook Reference

## Activities

* jupyter notebook with:
  * seq_driver imported and `seq_dict = seq_driver.seq_driver_incr(length, length)`
```
import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np

fig = plt.figure()
ax = p3.Axes3D(fig)

for key, seq in seq_dict.items():
   ax.plot(key[0]*np.ones(length),range(length),seq, label=str(key))

ax.legend()
```

* surface plot
  * re-arrange data into a matrix
```
Z = np.ndarray((len(initial),length))
for key, seq in seq_dict.items():
    Z[key[0]-2,:] = seq
```
  * X & Y grid data for each point in matrix
```
initial = [key[0] for key in seq_dict]
X,Y = np.meshgrid(range(length),initial)
```
  * plot surface:
```
fig = plt.figure()
ax = p3.Axes3D(fig)

ax.plot_surface(X,Y,Z)
```

* testing
  * testing is a vital part of all modern software projects
    * confirms/demonstrates/defines expected behavior
    * demontrates bugs and then demonstrates that bugs have been fixed
    * prevents regression
  * unit tests
    * specific to individual functions 
    * test behavior under many possible conditions, including error conditions
      if errors are a possible response
    * should be fast and automated so that there is no disincentive for running them often
    * can include input/output of files
  * consider a function you are writing and describe some tests
  * integration tests
    * ensure that an complete software project does what is expected
    * often related to verification and validation
  * verification
    * are the equations implemented correctly
  * validation
    * are the correct equations implemented
  * uncertainty quantification
    * characterization of the uncertainty in the result of a simulation
    * related to validation

* Continuous integration
  * fundamentally: merging updates to the mainline on a frequent basis
  * key requirement:
    * automated building of software (less relevant for Python)
    * automated testing of software as it's proposed
    * testing in a realistic environment
  * services exist to assist with this, e.g. CircleCI

