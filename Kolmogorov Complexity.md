[BASIC CONCEPTS (idsia.ch)](https://people.idsia.ch/~juergen/locoart/node2.html)

# BASIC CONCEPTS

The following are a few basic concepts of the theory of Kolmogorov complexity (see the Appendix for formal details):

**Compiler theorem.** Informally, this theorem says that any program for a given computer can be compiled into an equivalent program for a given universal computer by a compiler program whose length does not depend on the programs it compiles.

**Kolmogorov complexity.** The Kolmogorov complexity of a computable object is the length of the shortest program that computes it on a universal computer and halts.

**Invariance theorem**. Essentially, the invariance theorem says that the Kolmogorov complexity of some object does not depend of the particular computer used, leaving aside an additive, machine-specific, object-independent constant. This objectivity is due to the compiler theorem.

**Noncomputability of Kolmogorov complexity.** It can be shown that there is no single algorithm that can generate the shortest program for computing arbitrary given data on a given computer [4].