KIB
===

Code and scripts for wavefunction projections

Usage
===

Compile the code on your machine using the makefile.

Then go into the iota directory. Here you will find the real and imaginary part of a wavefunction on a real space grid. The actual electronic structure problem was solved with planewaves, but has since been backtransformed into real space.

To run the executable, from this iota directory type

../exe.osx WR.01.001.00001.dx WI.01.001.00001.dx

For the code I used, the real and imaginary part of the wavefunction was actually stored in two different files. Really we are feeding it _one_ complex wfn.

You should see the following output:

 # The norm of the isolated state is   3455999.9821567237     
 # I think there should be     3456000 i.e.    99.99 %
 1 -0.46954201505784937       0.87873213954149121     
 2 -7.04689635864237055E-003  1.31880306517494130E-002

The first two lines are the header, and are a basic sanity check. If you don't see a value close to 100%, it means there is probably a mismatch between the gridpoints between your iota and kappa wavefunctions, or the number of gridpoints in the file has not been understood by the code. Having that number be close to 100% is a necessary though not sufficient condition for normal operation.

What follows is the main output of the code. Each line is the projection of the iota you specificed in the command line arguement with the kappa states in the other directory.

In this example, there is a significant weight on the 1st kappa state, and none on the second. 
