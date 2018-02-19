# Project Scope and Design

## Learning Objectives

* develop a detailed specification for a software project
* develop a project plan for a software projecct including:
    * different stages of development
    * a decomposition of the problem at each stage

## Textbook

N/A

## Activities

1. Proposal ideas
   * parametric calling of other software: FCI, MCNP, lattice physics
   * simplified interface (GUI) for other software
   * Monte Carlo radiation transport
   * PDE/eigenvalue problems:
      * transient thermal conduction in a fuel pebble
      * vibration in a guitar string
      * CFD along shark skin
      * time-dependent neutron diffusion
      * finite element electrostatics/dynamics

1. Understanding requirements
   1. formal processes
   1. research software
      * initial requirements
      * planning for future requirements
   1. demonstrate with project ideas
       * pick 2: time-dependent neutron diffusion & parametric FCI

1. Developing project plan
   1. Stages of development
      * scope - dimensionality, types of boundary/interface conditions, etc
      * complexity - physics approximations, linearity, etx
      * algorithmic breakdown - input, processing steps, output
   1. demonstrate with project ideas
      * same two projects as above

1. Designing data models and interfaces
   1. Many reason to break project into distinct pieces with well-defined
      interfaces
      * division of labor
      * separation of concerns
      * reviewability
   1. all components must share the same data model
      * how will data be shared among components
      * balance between flexibility and simplicity
      * depends heavily on features of language
        * object-oriented
        * advanced containers
   1. define interfaces
      * input, output, behavior
