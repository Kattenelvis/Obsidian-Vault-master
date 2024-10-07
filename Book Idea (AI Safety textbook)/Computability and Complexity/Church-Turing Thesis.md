a
Not the physical version


Assumption, taken to be true, might not be. 
[DaylightCTTsabamDec2018.pdf (dijkstrascry.com)](https://dijkstrascry.com/sites/default/files/papers/DaylightCTTsabamDec2018.pdf)
[The Church-Turing Thesis (Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/entries/church-turing/)

Lambda calculus and Turing machines are equivalent. 


"Modern reimaginings of the Church-Turing thesis transform it, extending it to fundamental physics, complexity theory, exotic algorithms, and cognitive science. It is important to be aware though that some of the theses nowadays referred to as the Church-Turing thesis are at best _very_ distant relatives of the thesis advanced by Church and Turing."





# Church-Turing Thesis

## Church Thesis
It has been postulated that the intuitive notion of "computability" by a human is all there is to computability. There have been a few empirical reasons to believe this, for instance finding many different equivalent notions of computability, from Turing machines, the lambda calculus, and the recursive functions. 

Church's Thesis has since found to be provable from other axioms 
[A Natural Axiomatization of Computability and Proof of Church's Thesis Author(s): Nachum Dershowitz and Yuri Gurevich]

## Turing Thesis




# Universal Turing Computing

"Turing also showed that there are universal TMs—machines that can compute any function computable by any other TM. Universal machines do this by executing instructions that encode the behavior of the machine they simulate. Assuming the Church-Turing thesis, universal TMs can compute any function computable by algorithm. This result is significant for computer science: you don’t need to build different computers for different functions; one universal computer will suffice to compute any computable function. Modern digital computers are universal in this sense: digital computers can compute any function computable by algorithm for as long as they have time and memory. (Strictly speaking, a universal machine has an unbounded memory, whereas digital computer memories can be extended but not indefinitely, so they are not unbounded.)"

"The above result should not be confused with the common claim that computers can compute _anything_. This claim is false: another important result of computability theory is that most functions are _not_ computable by TMs (and hence, by digital computers). TMs compute functions defined over denumerable domains, such as strings of letters from a finite alphabet. There are uncountably many such functions. But there are only countably many TMs; you can enumerate TMs by listing each TM specification (which is some finite string). Since an uncountable infinity is much larger than a countable one, it follows that TMs (and hence digital computers) can compute only a tiny portion of all functions (over denumerable domains, such as natural numbers or strings of letters)."
[Computation in Physical Systems (Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/ENTRIES/computation-physicalsystems/)


Finite bounded TM's can still simulate larger ones





An pseudo-empirical hypothesis!?

$\lambda$-functions are effectively calculable by a Turing machine
The recursive functions are calculable by a Turing machine (MAYBE NOT?)
https://en.wikipedia.org/wiki/Ackermann_function effectively calculable function that is cannot be a recursive function. Atleast one's built up from the primitive recursive functions. 

by induction...
Every effectively calculable procedure is calculable on a Turing machine.


Hypercomputation is most likely false as we'll see that it's empirically not the case that we live in as olution to einsteins field equations which allows for closed-timelike curves which could in principle build hypercomputation. But it's controversial to what extent hypercomputation is possible. 


Gödel wanted to generalize the incompleteness theorem from principica mathematica. He apparently could use Turing machines for this as a way to model the very general system of effective procedure, allowing for the fully general theorem which states that consistent systems with sufficient arithmetic (and finitely axiomatizable?) can have true but unprovable propositions. 
Source: Section 3.1 SEP page churc-turing thesis



Rosser's Theorem via Turing machines, connections with Gödel incompleteness theorem.
https://scottaaronson.blog/?p=710
[Shtetl-Optimized » Blog Archive » Rosser’s Theorem via Turing machines (scottaaronson.blog)](https://scottaaronson.blog/?p=710)


"For those of you who’ve never seen the connection between these two triumphs of human thought: suppose we had a sound and complete (and recursively-axiomatizable, yadda yadda yadda) formal system F, which was powerful enough to reason about Turing machines.  Then I claim that, using such an F, we could easily solve the halting problem.  For suppose we’re given a Turing machine M, and we want to know whether it halts on a blank tape.  Then we’d simply have to enumerate all possible proofs in F, until we found _either_ a proof that M halts, _or_ a proof that M runs forever.  Because F is complete, we’d eventually find one or the other, and because F is sound, the proof’s conclusion would be _true_.  So we’d decide whether M halts.  But since we already know (thanks to Mr. T) that the halting problem is undecidable, we conclude that F can’t have existed."

“Look ma, no Gödel numbers!”



Connections with Lucas argument?

It states in the SEP page for the Church-Turing thesis that every effective procedure can "Without exercising any insight, intuition, or ingenuity, a human being can work through the instructions in the program and carry out the required operations.". This is not the case for seeing the truth of a Gödel sentence of a system, according to the Lucas-Penrose argument. If that argument succeeds, is it a counter-example?

https://reducing-suffering.org/replies-lucas-penrose-argument/

"Roger Penrose (1989; 1994) conjectured that some mathematical insights are non-
recursive. Assuming that this mathematical thinking is carried out by some physical processes in
the brain, the bold thesis must then be false. But Penrose’s conjecture is highly controversial."
https://oronshagrir.huji.ac.il/sites/default/files/oronshagrir/files/ver19_physical_computability_theses.pdf





## Arguments for the thesis

### Inductive argument
Look at all these effectively calculable functions that just so happen to also be Turing machine computable!


### Turing argument I
Humans can be a bit like a Turing machine
We intuit what is effectively calculable by calculating it
Therefore what is effectively calculable is calculable by a turing machine

The human is a bit different though, like being able to hold multiple states (compared to the FST inside the TM) and keep track of a longer tape in more dimensions.

"I think it will be agreed that the two-dimensional character of paper is no essential of computation. (Turing 1936 [2004: 75])"

"It is not totally obvious that calculations carried out in two (or three) dimensions can be put on a one-dimensional tape and yet preserve the “local” properties. (Gandy 1988: 81, 82–83)"

**Turing’s computation theorem**:  
This account of the essential features of human computation implies Turing’s thesis.

### Turing argument II

Kripke's version:
All mathematical derivations/effective calculations(?) can be described in first order logic with identity ("Hilberts thesis")
Every human can perform such derivations ("Turings Thesis")
By the Completeness theorem, everything derivable is valid

### Turing argument III
Modified argument I



## **Deutsch-Wolfram Thesis**:  
Every finite physical system can be simulated to any specified degree of accuracy by a universal Turing machine. (Copeland & Shagrir 2019)




The _Extended Church-Turing Thesis (ECT)_ makes the … assertion that the Turing machine model is also as efficient as any computing device can be. That is, if a function is computable by some hardware device in time T(n) for input of size n, then it is computable by a Turing machine in time (T(n))k for some fixed k (dependent on the problem). (Yao 2003: 100–101)



# The Gandy Argument


Improved and generalized version of Turing's argument I. 

"Gandy (Turing’s only PhD student) pointed out that Turing’s analysis of human computation does not immediately apply to computing machines strongly dissimilar from Turing machines. (See [Section 4.3](https://plato.stanford.edu/entries/church-turing/#TuriArguI) below for details of Turing’s analysis.) For example, Turing’s analysis does not obviously apply to parallel machines which, unlike a Turing machine, are able to process an arbitrary number of symbols simultaneously. Seeking a generalized form of Turing’s analysis that applies equally well to Turing machines and massively parallel machines, Gandy (1980) stated four axioms governing the behaviour of what he called _discrete deterministic mechanical devices_. (He formulated the axioms in terms of hereditarily finite sets.) Gandy was then able to prove that every device satisfying these axioms can be simulated by a Turing machine: **Discrete deterministic mechanical devices, even massively parallel ones, are no more powerful than Turing machines**, in the sense that whatever computations such a device is able to perform can also be done by the universal Turing machine. (For more on Gandy’s analysis, see [Section 6.4.2](https://plato.stanford.edu/entries/church-turing/#GandArgu).)"


1. “A discrete deterministic mechanical device satisfies principles I-IV” (he called this “Thesis P”; Gandy 1980: 126), and
   
2. “What can be calculated by a device satisfying principles I-IV is computable” (he labelled this “Theorem”).


"However, the Németi computer is a discrete, deterministic mechanical device, and yet is able to calculate functions that are not Turing-machine computable. That is to say, relativistic computers are counterexamples to Gandy’s Thesis P. In brief, the reason for this is that the sense of “deterministic” implicitly specified in Gandy’s Principles (“Gandy-deterministic”) is narrower than the intuitive sense of “deterministic”, where a deterministic system is one obeying laws that involve no randomness or stochasticity. Relativistic computers are deterministic but not Gandy-deterministic. (For a fuller discussion, see Copeland, Shagrir, & Sprevak 2018.)"

"**In conclusion, Gandy’s analysis has made a considerable contribution to the current understanding of machine computation. But, important and illuminating though the Gandy argument is, it certainly does not settle the question whether the Deutsch-Wolfram thesis is true.**"




# A phenomenological version?


Let's apply formal phenomenology! Here's how a mind based turing machine could look like

One pixel determines the state. Different colors indicate different states 
🟥🟦

A one-dimensional band of black and white pixels determine the tape, we can imagine that white = 1 and black = 0.
◻️⬛◻️◻️◻️⬛⬛⬛◻️

We then have a pixel next to the indicated head position. We can put it on the left as a convention, but it could just as well be placed on the right. We denote it with ⭐

Lastly, the set of rules can be stored as pixel values aswell. A yellow pixel separates the tape from the ruleset, which is also specified by pixels.

Example rule:
🟥◻️⬅️⤴️🟥⬛⬅️

Many rules in a row:
🟥◻️⬅️⤴️🟥⬛⬅️🟨🟥◻️⬅️⤴️🟥◻️➡️



In the end, we can get a phenomenal experience that looks like this:

🟥⬅️◻️⬛◻️⭐◻️◻️⬛⬛⬛◻️🟨🟥◻️⬅️⤴️🟥⬛⬅️🟨🟥◻️⬅️⤴️🟥◻️➡️

One computation step later:

🟥⬅️◻️⬛⭐◻️⬛◻️⬛⬛⬛◻️🟨🟥◻️⬅️⤴️🟥⬛⬅️🟨🟥◻️⬅️⤴️🟥◻️➡️


🟥⬅️◻️⭐⬛⬛⬛◻️⬛⬛⬛◻️🟨🟥◻️⬅️⤴️🟥⬛⬅️🟨🟥◻️⬅️⤴️🟥◻️➡️

Where it runs out of instructions and halts. We could extend this to an infinite tape by having it "scroll" by having new experiences come in from the side, like this:
◻️◻️◻️◻️⬛
Scroll step:s (to the left)
◻️◻️◻️⬛◻️
◻️◻️⬛◻️◻️
◻️⬛◻️◻️⬛

Where in the last step a 0 tape comes in. Likely that information is stored somewhere else in the universe, perhaps similarly the way it does for our experiences as they change over time.

While it might be clear with pixels or atleast for the average human reading this, regions of colors, the symbolic systems in typical descriptions of turing machines are not at all very different, since they are also experiences updating over time.

The idea might be that, given that idealism, or (something like "metaphysical phenomenalism" where all that exists is phenomenal experience) and the phenomenal experiences of the world update following some rule, in discrete steps, then pancomputationalism, i.e the view that everything is computational, is true. 

Putnam multiple computations blah blah Chalmers response. 



# Hilbert's Thesis

[Is there a hillberts thesis.pdf](file:///C:/Users/Katte/Documents/Academic/Philosophy/Is%20there%20a%20hillberts%20thesis.pdf)
Reinhard Kahle
https://www.jstor.org/stable/45096844


