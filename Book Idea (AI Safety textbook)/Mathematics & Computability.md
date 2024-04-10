
AI's are computational. But what really is computation? 

This chapter is more technical than the average chapter. This chapter will be technical, but will be useful for many future chapters.



## Foundations of computation/Grammar


We begin with formalising the notion of language. We're not necessarily talking about the English language, or the French language, known as natural languages. We're talking about formal languages. Formal languages are constructed from simple rules that determine the vocabulary of the language. 

With the rule that $A \rightarrow qA$ we can get the vocabulary (using $A$ as a starting vocabulary)

$A$
$qA$
$qqA$
$qqqA$
$qqqqA$
...

One can notice that even with simple rules, the language can easily be infinite. Creating finite languages can be more difficult than creating finite languages using non-ad hoc rules. 

$A\rightarrow Bb$
$B\rightarrow c$

Then we get
$A$
$Bb$
$cb$

And it terminates.


## Finite state machines 


a --> b

They can be used to generate a vocabulary, and the finish states determine correctly formed formula




Indeterministic

## Push down automata

Now with memory!

## Turing machines


More complicated rule set

Multiple formalisms



## Example Algorithms (AI related?)





## Universal Turing Computing

"Turing also showed that there are universal TMs—machines that can compute any function computable by any other TM. Universal machines do this by executing instructions that encode the behavior of the machine they simulate. Assuming the Church-Turing thesis, universal TMs can compute any function computable by algorithm. This result is significant for computer science: you don’t need to build different computers for different functions; one universal computer will suffice to compute any computable function. Modern digital computers are universal in this sense: digital computers can compute any function computable by algorithm for as long as they have time and memory. (Strictly speaking, a universal machine has an unbounded memory, whereas digital computer memories can be extended but not indefinitely, so they are not unbounded.)"

"The above result should not be confused with the common claim that computers can compute _anything_. This claim is false: another important result of computability theory is that most functions are _not_ computable by TMs (and hence, by digital computers). TMs compute functions defined over denumerable domains, such as strings of letters from a finite alphabet. There are uncountably many such functions. But there are only countably many TMs; you can enumerate TMs by listing each TM specification (which is some finite string). Since an uncountable infinity is much larger than a countable one, it follows that TMs (and hence digital computers) can compute only a tiny portion of all functions (over denumerable domains, such as natural numbers or strings of letters)."
[Computation in Physical Systems (Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/ENTRIES/computation-physicalsystems/)



## Undecidability, Halting Problem and the limits of computation

Limits of computation
Turing's undecidability thesis

Similar to Liar's Paradox, Russell's Paradox, Gödel's incompleteness theorem's (note to self: the SEP page does make notes that it's a bit more complicated than just "self-reference"), Tarski's undefinability of truth and the Nelson-Grayling paradox, who all have in common the notion of self-referentiality, there exist a similar problem for computability which is also highly connected and even a lemma of the above one's

Proof:

Imagine a computation C that computes whether or not computations halt. If it feeds itself, it can either say "halts", in which case it halts, but it will never say "halts" if it doesn't halt, it will keep going forever. 


Keep in mind this is only for a general algorithm. Some algorithms do exist that can test the halting of certain algorithms. Just like how Russell's Type theory disallowed Russell's paradox in axiomatic set theory, so can algorithms which specify input types[source]




## Computational Complexity: Can a big enough computer with enough time just solve any problem?



P = NP discussion

ExpSpace

Quantum Complexty and quantum supremacy?

Brute force

AI as a P-algorithm heuristic that's a "good enough" approximation of solutions to NP-complete problems.

[Computability and Complexity (Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/entries/computability/)
"With a very few exceptions, when a natural problem is in NP, it turns out to be either NP complete, or in P. People wondered whether this was always the case. Ladner proved that if P ≠≠ NP, then there is an intermediate problem I� that is in NP but not in P and not NP complete [Ladner, 1975]."

"Ladner’s proof method is called delayed diagonalization. He generalized his result to show that for any two well-behaved complexity classes, C, E such that C is strictly contained in E, there is an intermediate class, D such that C is strictly contained in D and D is strictly contained in E. Thus the ordering of complexity classes is dense."

"However, these intermediate problems don’t tend to show up."

Idea: Similar to the Continuum hypothesis, given that we don't see sets between $\aleph_0$ and $\aleph_1$. 

## Hypercomputation

If hypercomputers existed however, we'd just use brute force algorithms and even do uncomputable algorithms such as AIXI. Of course, how to align an AIXI would still have to be debated, but it would be really easy to have vastly smarter-than-human intelligence.





# Logic - Computation correspondences

Logic, such as first order logic- has an equivalent computation that proves all theorems in that system. Proof systems are in that sense computational. 

## Curry Howard Correspondence
As such, the lambda calculus has a correspondence with first order intuitionistic logic.



## Basic Programming Theory




# Gödel

This won't be brought up until the chapter in [[Mind]], so it's safe to skip this chapter for now if you wanna read about physical realizability of computation. 

Gödel's incompleteness theorem's are 2 very important theorems that proove certain metalogical conditions that logical systems are must abide by. They state that all logical systems, who are $\omega-$consistent with sufficient arithmetic (we'll go back to what exactly this means), have true sentences that are unprovable withing the system. The second incompleteness theorem states that such systems cannot prove that they are themselves consistent. 

It's worth noting that this does *not* entail *all* of mathematics is incomplete, only certain logical systems. There's a list [on wikipedia] on all provably complete and consistent systems, such as finitist set theory, the theory of random graphs and Robinson arithmetic. 


 
## Brief, informal overview
Yes (probably more logic than math but whatever, we'll see how I organize the chapters)

Needs to be atleast arithmetic $Q$ for gödel numbering (given that it requires the prime factorization theorem)

Needs to be $\omega-$consistent

Needs to be recursively axiomatizable (i.e there exists a program $P$ that decides $P(ax)$ is true iff $ax$ is an axiom)

Diagonalization lemma states that for all gödel-numbered predicates $A$, it is the case that a propsosition $G$ can be created such that 
$F\vdash G\leftrightarrow A([G])$

Apply it to the "not provable" predicate

$F\vdash G\leftrightarrow \neg PROV([G])$

BOOM!
Assume it's not provable yada yada
Assume it is yada yada





# Probability Theory


This will be an important reference for some future chapters

Kolmogorov Axioms
1. Non-negativity
2. Sum to 1
3. Stuff

Borel Algebra $A$ on an outcome space $\Omega$ and measure $P$.

Bayes' formula: Proof

This formula will be useful in rationality chapter

Law of Large numbers: Proof

Imprecise probabilities

## Information Theory

Information! $I=1/log(p)$
Entropy $H$. 

Opposite of uncertianty, unknown systems
Entropy in Physics

