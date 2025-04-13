


[DaylightCTTsabamDec2018.pdf (dijkstrascry.com)](https://dijkstrascry.com/sites/default/files/papers/DaylightCTTsabamDec2018.pdf)
[The Church-Turing Thesis (Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/entries/church-turing/)

It's worth noting that there are many different accounts of the Church-Turing thesis, as described by the SEP:

> "Modern reimaginings of the Church-Turing thesis transform it, extending it to fundamental physics, complexity theory, exotic algorithms, and cognitive science. It is important to be aware though that some of the theses nowadays referred to as the Church-Turing thesis are at best _very_ distant relatives of the thesis advanced by Church and Turing."

In general, the classical CTT is about an equivalence between the intuitive notion of computation and Turing machines, positing that all other formalizations of the intuitive notion of computation are equivalent to Turing machines. For instance that lambda calculus and Turing machines are equally powerful in terms of what they can compute, meaning that any function that is computable in one system is also computable in the other. This equivalence extends to other formal models of computation like recursive functions, Post machines, and register machines.

**Church-Turing Thesis:** All models of computation are equivalent to Turing machines.

It is often taken as an assumption by computer scientists, taken to be true, but might not be. So far, by 2024, no one has found a counter-example in a way relevant to the classical CTT. 

## Church Thesis
It has been postulated that the intuitive notion of "computability" by a human is all there is to computability. There have been a few empirical reasons to believe this, for instance finding many different equivalent notions of computability, from Turing machines, the lambda calculus, and the recursive functions. 

Church's Thesis has since found to be provable from other axioms 
[A Natural Axiomatization of Computability and Proof of Church's Thesis Author(s): Nachum Dershowitz and Yuri Gurevich]

# Arguments for the thesis

## Inductive argument
One way to argue for the thesis is to consider it an empirical hypothesis with predictive power. Just look at all these effectively calculable functions that just so happen to also be Turing machine computable! One (potentially naive) way to characterize induction is that given a set of observations with no counter-examples, one can tentatively assume a universal statement about them. 

**Principle 4, Induction**: $O(a_1),O(a_2)...O(a_n),\neg\exists x\neg O(x) \vDash \forall x O(x)$ 

So from Principle 4 and a long finite set of effectively computable functions which are also Turing computable with no counter-examples we can derive that all effectively computable functions are Turing computable.

We can strengthen this even more by seeing how other definitions of effectively computable all turn out to be equivalent. Take for instance the lambda calculus. Everything, including numbers, are functions, based on a long row of successors. It turns out that $\lambda$-functions are effectively calculable by a Turing machine, i.e equivalent. Atleast, so far, we only have evidence of effectively computable functions which are both lambda calculable and Turing machine calculable. There have been examples of delayed discovery of the primitive recursive functions which showed that they it could not calculate all effective computations. 
## Turing argument I and III
For a stronger argument in such a way where can be more certain in the conclusion, we instead consider some "psychological" aspects of humans (or perhaps certain kinds of creatures which can do rule driven activities) which is reminiscent of Turing machine computation. In this sense, it would turn out that all intuitively computable functions for a human is Turing computable. 

A human can look at a finite 2-dimensional sheet of paper, alternatively, there exists some experience $E$ such that $E$ consists of nothing but white squares. 

These squares can have symbols on them, and the symbols can be manipulated given one's *state of mind*, (and for argument III: with a note on the side). 

The human is a bit different though, like being able to hold multiple states and keep track of a longer tape in more dimensions, and as Gandy argues, we can perform many computations at once.

"I think it will be agreed that the two-dimensional character of paper is no essential of computation. (Turing 1936 [2004: 75])"

But this might turn out to be faulty. 

"It is not totally obvious that calculations carried out in two (or three) dimensions can be put on a one-dimensional tape and yet preserve the “local” properties. (Gandy 1988: 81, 82–83)"

**Turing’s computation theorem**:  
This account of the essential features of human computation implies Turing’s thesis. Human minds are at a minimum capable of simulating B-L Turing machines.


### Turing argument II

Kripke's version:
All mathematical derivations/effective calculations(?) can be described in first order logic with identity ("Hilberts thesis")
Every human can perform such derivations ("Turings Thesis")
By the Completeness theorem, everything derivable is valid




# Gandy's Argument


Generalized version of Turing's argument I. 

"Gandy (Turing’s only PhD student) pointed out that Turing’s analysis of human computation does not immediately apply to computing machines strongly dissimilar from Turing machines. (See [Section 4.3](https://plato.stanford.edu/entries/church-turing/#TuriArguI) below for details of Turing’s analysis.) For example, Turing’s analysis does not obviously apply to parallel machines which, unlike a Turing machine, are able to process an arbitrary number of symbols simultaneously. Seeking a generalized form of Turing’s analysis that applies equally well to Turing machines and massively parallel machines, Gandy (1980) stated four axioms governing the behaviour of what he called _discrete deterministic mechanical devices_. (He formulated the axioms in terms of hereditarily finite sets.) Gandy was then able to prove that every device satisfying these axioms can be simulated by a Turing machine: **Discrete deterministic mechanical devices, even massively parallel ones, are no more powerful than Turing machines**, in the sense that whatever computations such a device is able to perform can also be done by the universal Turing machine. (For more on Gandy’s analysis, see [Section 6.4.2](https://plato.stanford.edu/entries/church-turing/#GandArgu).)"


1. “A discrete deterministic mechanical device satisfies principles I-IV” (he called this “Thesis P”; Gandy 1980: 126), and
   
2. “What can be calculated by a device satisfying principles I-IV is computable” (he labelled this “Theorem”).


"However, the Németi computer is a discrete, deterministic mechanical device, and yet is able to calculate functions that are not Turing-machine computable. That is to say, relativistic computers are counterexamples to Gandy’s Thesis P. In brief, the reason for this is that the sense of “deterministic” implicitly specified in Gandy’s Principles (“Gandy-deterministic”) is narrower than the intuitive sense of “deterministic”, where a deterministic system is one obeying laws that involve no randomness or stochasticity. Relativistic computers are deterministic but not Gandy-deterministic. (For a fuller discussion, see Copeland, Shagrir, & Sprevak 2018.)"

"**In conclusion, Gandy’s analysis has made a considerable contribution to the current understanding of machine computation. But, important and illuminating though the Gandy argument is, it certainly does not settle the question whether the Deutsch-Wolfram thesis is true.**"




# A phenomenological version of argument I


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

# Hilbert's Thesis

An interesting parallel is Hilbert's thesis, which involve similar arguments in the sense that first order logic has equivalent proof systems.

> 	**Leibniz's Thesis**
> 	(i) Every acceptable argument of (informal) mathematics is a proof.
> 	(ii) Every proof can be formalized as a derivation. 
> 	
> 	**Frege's Thesis.**
> 	 (i) Leibniz's thesis is true. 
> 	 (ii) There is a formal language and a set of rules of inference that can be used to formalize adequately all proofs. 
> 	 
> 	 **Frege's Thesis**: 
> 	 (i) Frege's thesis is true.
> 	 (ii) All arguments of informal mathematics can be formulated adequately using only the first-order predicate calculus.


The arguments which are similar include the following:

>The fact that a "Hilbert's Thesis" tries to give a formal definition (formal ized proof) of an informal notion (mathematical proof) is a rather superficial parallel with Church's Thesis. An association of them would be better sup ported by analogous justifications. Kleene, in his book, gives four arguments, under the following titles (of course, with substantial arguments spelled out in detail): 
>(A) Heuristic evidence. 
>(B) Equivalence of diverse formulations. 
>(C) Turing's concept of a computing machine. 
>(D) Symbolic logics and symbolic algorithms.

Kahle then goes on to discuss the parallel arguments and how they differ. 

[Is there a hillberts thesis.pdf](file:///C:/Users/Katte/Documents/Academic/Philosophy/Is%20there%20a%20hillberts%20thesis.pdf)
Reinhard Kahle
https://www.jstor.org/stable/45096844


