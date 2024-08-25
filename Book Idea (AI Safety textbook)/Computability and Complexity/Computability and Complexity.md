
AI's are computational. But what really is computation? 

This chapter is more technical than the average chapter. This chapter will be technical, but will be useful for many future chapters.

The intuitive notion of a computation is that of a some *starting symbols*  with some *symbol manipulation system* which transforms those symbols into new symbols. This seemingly simple idea has extremely deep consequences, and has is foundational for entire fields of study and parts of every field of study (to some extent atleast). 

How this idea works more formally is what will be explicated in this chapter. We will also dive into results which shape this field into something truly spectacular. 

## Foundations of computation

We begin by considering symbols, and an alphabet. This is foundational for all of logic. We introduce symbols as the first principle

**Principle 1:** Symbols exist. We will not consider any kind of semiotic[pierce] framework, as the symbols we begin with do not represent or denote anything. They are merely some kind of pattern.

The most common example of symbols in theoretical computer science is the symbol "1" and the symbol "0".

**Definition 1:** An alphabet is a set of symbols

But any arbitrary symbol set can be used. To enable computation we must also allow change in symbols, changing 1's to 0's

**Principle 2:** Algorithmic rules can be used to manipulate symbols

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

Whether or not an algorithm terminates or not turns out to be very important for computer science in general, and we'll explore it in the multiple future sections.

## Finite state machines 

One way to represent state changes is with a finite state machine. They are generally visualized as many circles with various arrows going between the circles, as a kind of labeled directed graph with 2 special nodes and where the labeling can repeat.

-->a --> (b)

Here, state a is the starting node, and b is the final node. If some input ends at b, it terminates as "yes". Otherwise no. 


They can be used to generate a language, and the finish states determine correctly formed formula.


#### Indeterministic

They can also be non-deterministic, probabilistic and quantum. Each with their own QUIRKS. 

a -->b
   --> c

Same input from a to b and c. How is this resolved? Generally by going over all of the options.


## Push down automata

Now with memory!

## Turing machines


More complicated rule set

Multiple formalisms

TAPE

The Turing machine is a mathematical construct that has found itself being useful all over the place. Here is a definition
Let $X$ be a list of symbols, whose kleene star operation $X$ denotes a vocabulary, and let $L$ be left, $R$ be right, let $\sigma: \{L, R\}\times X\rightarrow \{L, R\}\times X$ be a function that takes some input and output



Turing machines can also be represented as a machine table 





## Example Algorithms (AI related?)



## Lambda Calculus

Identity function
$\lambda x.x$

Wow! Everything, including numbers, is a function! Based on a long row of successors!




## Undecidability, Halting Problem and the limits of computation

Limits of computation
Turing's undecidability thesis

Similar to Liar's Paradox, Russell's Paradox, Gödel's incompleteness theorem's (note to self: the SEP page does make notes that it's a bit more complicated than just "self-reference"), Tarski's undefinability of truth and the Nelson-Grayling paradox, who all have in common the notion of self-referentiality, there exist a similar problem for computability which is also highly connected and even a lemma of the above one's

Proof:

Imagine a computation C that computes whether or not computations halt. If it feeds itself, it can either say "halts", in which case it halts, but it will never say "halts" if it doesn't halt, it will keep going forever. 


Keep in mind this is only for a general algorithm. Some algorithms do exist that can test the halting of certain algorithms. Just like how Russell's Type theory disallowed Russell's paradox in axiomatic set theory, so can algorithms which specify input types[source]


All of these self-referential paradoxes can be generalized into the fixed point theorem in category theory. 



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



[philos.pdf (scottaaronson.com)](https://www.scottaaronson.com/papers/philos.pdf)
![[Pasted image 20240808213558.png]]


![[Pasted image 20240809141903.png]]

![[Pasted image 20240809142446.png]]

Look up tables for Searle's chinese room thought experiment. Grows exponentially with conversation length $n$. Humans may have evolved/developed efficient algorithms for language.

Waterfal/Putnam all possible computations thingy

## Hypercomputation

If hypercomputers existed however, we'd just use brute force algorithms and even do uncomputable algorithms such as AIXI. Of course, how to align an AIXI would still have to be debated, but it would be really easy to have vastly smarter-than-human intelligence.


[Zeno machine - Wikipedia](https://en.wikipedia.org/wiki/Zeno_machine)




# Logic - Computation correspondences
Do I need this section?

Logic, such as first order logic- has an equivalent computation that proves all theorems in that system. Proof systems are in that sense computational. 

## Curry Howard Correspondence
As such, the lambda calculus has a correspondence with first order intuitionistic logic.



## Basic Programming Theory



# Metalogic

## Compactness

## Completeness
## Incompleteness Theorems

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

This formula will be useful in rationality chapter: Bayes' formula: Proof


Useful for Jury Theorems: Law of Large numbers: Proof



## Imprecise probabilities

One way to avoid utilizing just a single value for the probability of an event, we may choose to have a whole range of probabilities $P\subseteq[0,1]$. When performing calculations then, one may need a specific value, and there are multiple kinds of algorithms that have been developed for that. Some basic one's include averaging, taking the lowest one, or the maximum one. 

We will get back to this later, but it turns out that imprecise probabilities for rational decision theory leads to sunk costs and other nasty consequences. 



## Information Theory

Information! $I=1/log(p)$
Entropy $H$. 

Opposite of uncertianty, unknown systems
Entropy in Physics





# Relation Theory

$R$

RELATIONS! 


# Formalism

Theorem proovers, math is bad, people rush through and fail often. Sometimes for decades.

If this happends to proofs regarding AI safety, we could put all of humanity into danger.

We have to apply rigirious use of theorem prooving machines before for safety standards!

