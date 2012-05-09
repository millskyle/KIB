KIB
===

Code and scripts for wavefunction projections

Usage
===

Compile the code on your machine using the makefile.

Then go into the iota directory. Here you will find the real and imaginary part of a wavefunction on a real space grid. The actual electronic structure problem was solved with planewaves, but has since been backtransformed into real space.

To run the executable, from this iota directory type

@code@ ../exe.osx WR.01.001.00001.dx WI.01.001.00001.dx

For the code I used, the real and imaginary part of the wavefunction was actually stored in two different files. Really we are feeding it _one_ complex wfn.

You should see the following output:

 # The norm of the isolated state is   3455999.9821567237     
 # I think there should be     3456000 i.e.    99.99 \%
 1 -0.46954201505784937       0.87873213954149121     
 2 -7.04689635864237055E-003  1.31880306517494130E-002

The first two lines are the header, and are a basic sanity check. If you don't see a value close to 100%, it means there is probably a mismatch between the gridpoints between your iota and kappa wavefunctions, or the number of gridpoints in the file has not been understood by the code. Having that number be close to 100\% is a necessary though not sufficient condition for normal operation.

What follows is the main output of the code. Each line is the projection of the iota you specified in the command line argument with the kappa states in the other directory.

In this example, there is a significant weight on the 1st kappa state, and none on the second.

Due to file sizes, only two kappa states and one iota state have been included in this example. Normally, one would include all occupied kappa states and some number of unoccupied states in the kappa directory. The exact number of unoccupied states to include is system specific, and is essientially a controlled approximation. The more unoccupied states you include, the more flexible your basis will be and the better you will span the vector space. Fortunately, one can check if a sufficient number of kappas have been included in the expansion by evaluating the inner product of an iota _expressed in the basis of kappa_. In the iota directory, there is an additional directory called precomputed. Here are the results of using the code on several iota states (iota001 corresponds to the dx files we just used), where the projection was done using 1244 kappa states (rather than just two as per the example).

From this directory, the script ../../getNorm.sh can be called. This will compute the inner product and gives the following output:

iota001  0.999863
iota002  0.999826
iota003  0.999909
iota004  0.999999
iota005  0.999874
iota006  0.999991
iota007  0.999881
iota009  0.999928
iota010  0.999857
iota011  0.999884
iota012  0.999977
iota013  0.999984
iota014  0.999953
iota015  0.999185
iota016  0.999856
iota017  0.9999
iota018  0.997309
iota019  0.994961
iota020  0.999993
iota021  0.995398
iota022  0.999823
iota023  0.981272

For all but iota023, more than 99% of the wavefunction is accounted for, meaning we used enough kappa states in our expansion. If you find that you are not getting a norm close to 1.0, you probably need to include more kappas.

Since we have a decent expansion, we can now used these states to look at how strongly coupled our system is.

One thing to look at is < iota | kappa_i > < i_ kappa |

Using gnuplot (for example), we can plot the projection:

plot "iota021" u 1:($2**2 + $3**2)

Using that command will give square modulus.

To get a matrix element of the form < iota_i | H(\kappa) | iota_j >

use the command 

../../get_matrix_element.py iota021 iota022 ../../kappa/eigenvalues

This will print the real and imaginary part of the matrix element. Essientially this tells you what the coupling between iota021 and iota022 is when they are _in the presence of the combined Hamiltonian_

Cool right?
