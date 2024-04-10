- **[Bremermann's Limit](https://www.orionsarm.com/eg-article/4611947064514)**  - Text by [Mike Parisi](https://www.orionsarm.com/xcms.php?r=oa-people#person23)  
    The maximum limit allowed for computation under the laws of physics.

https://en.wikipedia.org/wiki/Mathematical_universe_hypothesis


This post does not argue for nor against the computational unvierse hypothesis (CUH), but it clarifies and lays out the philosophical assumptions and consequences for CUH. 

The general form of a computation is the following:

A state $S_i$ follow a ruleset $R$ and produces $S_j$ as output. The most common example of a computation is a Turing machine, which is more complicated. 

We will use Turing machines in this blog post, even though there are equivalent notions (like lambda calculus, recursive functions e.t.c), this is because the state of the universe can be easily representable on the tape.

"This is very explicit in Section 9 of Turing 1936–7 where he shows that Turing machines are a ‘natural’ model of (human) computation by analyzing the process of human computation."
2.5 https://plato.stanford.edu/entries/turing-machine/

Since I can simulate a turing machine (or atleast, a finitely taped turing machine) then the universe is atleast partially computational. 



We can now state the conditions. The universe is computational iff

2. Time is discrete 

If time is continuous, then between any two state changes, there exists another state change. This means that between any two state changes there's an infinite number of state changes, which is an infinite computation which leads to contradictions. 

3. Naturalism

A key point of computation is the adherence to specific rules that update the state of the universe at every timestep. This implies a specific set of natural laws that cannot be changed from inside the system. 


1. Finite number of substance particulars 

In philosophical jargon, this means that whatever substance(s) the universe is constituated by, there's a finite number of such particulars. An implication of this is that there's a smallest indivisible substance particular. Another requirement is that each substance particular has a finite number of properties.

Example: Materialism. Quarks, Photons e.t.c are constituated by a finite number of some particular substance with a finite number of properties.

Example: Idealism. The visual field is constituated by a finite number of experiential points, like a two-dimensional pixel screen. This applies to all sense-perception just in case auditory and visual particulars are of different substance.   

This can be extended to Dualism (both previously mentioned at once), physicalist panpsychism (each particular material substance has an experiantial property), neutral monism and actor models for free will that posit a separate substance for free actions, (non-deterministic non-random automata). 

Free will substance agent-model cannot be allowed however since it's non-deterministic and non-probabilistic.

Formalism: Let $B$ be the set of substances in the universe, then there exists a set of particulars $P = \{x : F\in B \wedge F(x) \}$. 
Then the state of the universe is the set of particulars and their relations to other particulars
$S=P\cup\{<x,y>, R(x,y)\}$

The sets aboved can be indexed by time and possible worlds.

Requirement, $P$ and $S$ is less than a countable infinity:
$|P|<\aleph_0$
$|S|<\aleph_0$

The main reason for this requirement is that an infinite computation done in finite time, such as an oracle, leads to contradictions [SOURCE?!]. If the world was computational without this requirement, then the next time step could never occurr. 


Axiology:
"Should be $S_1$" is an ethical statement on how the configuration of the universe should be. An axiological function inputs states of the universe and outputs a value that is how "good" these states are, given some value system (axiology). 
$A: S \rightarrow N$


4. God doesn't exist or god is outside the universe

Wait what!


Consequences

1. Simulation hypothesis becomes possible

The simulators lack some god-like properties such as omnipresence, omnipotence e.t.c. A god could still exist that encompassess both the simulation and simulations, or outside either. 

AGI ancestor simulation

2. Some Physical Church-Turing thesis Thesis is true

Every physical process is computational.

From the last paragraph section 3.1 https://plato.stanford.edu/entries/turing-machine/:
"The focus on human computation in Turing’s analysis of computation, has led researchers to extend Turing’s analysis to computation by physical devices. This results in (versions of) the physical Church-Turing thesis. Robin Gandy focused on extending Turing’s analysis to discrete mechanical devices (note that he did not consider analog machines). More particularly, like Turing, Gandy starts from a basic set of restrictions of computation by discrete mechanical devices and, on that basis, develops a new model which he proved to be reducible to the Turing machine model. This work is continued by Wilfried Sieg who proposed the framework of Computable Dynamical Systems (Sieg 2008). Others have considered the possibility of “reasonable” models from physics which “compute” something that is not Turing computable. See for instance Aaronson, Bavarian, & Gueltrini 2016 https://arxiv.org/pdf/1609.05507.pdf  (also that powerpoint presentation) in which it is shown that _if_ closed timelike curves would exist, the halting problem would become solvable with finite resources. Others have proposed alternative models for computation which are inspired by the Turing machine model but capture specific aspects of current computing practices for which the Turing machine model is considered less suited. One example here are the persistent Turing machines intended to capture interactive processes. Note however that these results do not show that there are “computable” problems that are not Turing computable. These and other related proposals have been considered by some authors as reasonable models of computation that somehow compute more than Turing machines. It is the latter kind of statements that became affiliated with research on so-called hypercomputation resulting in the early 2000s in a rather fierce debate in the computer science community, see, e.g., Teuscher 2004 for various positions."

Summary. In complet e aspects of Turing's work are surveyed, with particular reference to his late interest in t he foundations of qu antum mechanics, and refuting t he assertion t hat his work raised the prospect of constructing physical "oraclemachines." (Hodges "What Would Alan Turing Have Done After 1954?")

Hypercomputational Models Mike Stannett

"There have been a number of purely mathematical demonstrations of non-recursive, physically reasonable, behaviors - and some of these might feasibly be implemented. The constructions of Pour-El and Richards are familiar to many researchers in the field , but t hat of Myhill seems to be less well known."

Keep in mind the Church-Turing thesis states (or implies?) that all recursive functions are computible. The existence of non-recursive behaviours in the physical world could imply behaviour that is not simulatable by a Turing machine.

"P our-El demonstrated as early as 1970 t hat a real-valued function of the reals is "analog-generable" precisely when it can be expressed in terms of certain non-linear differential equations (Pour-EI [55,56]) . He then showed that there are necessarily recursive functions that are not analog generable. This seems to suggest t hat analog computability is incomparable with its digital counterpart, and in [79] we took Pour-El's comments to mean that the class of recursive functions is not wholly included within that of functions computable by analog means. But our logic in this respect was flawed - Pour-El's result says only that the analog syste ms under discussion aren' t capable of generat ing all recursive fun ctions. In fact , other analog models (for example, analog recursive neural networks) are indeed powerful enough to compute all rec ursive fun ct ions [75]."

3. Relational Biology is false

4. Determinism becomes more parsemonious than Indeterminism.
   
Every nondeterministic turing machine can be reconstructed to a deterministic turing machine

Probabilistic Turing machine and indeterminism

This in turn might imply Superdeterminism in the philosophy of quantum mechanics. 

https://plato.stanford.edu/entries/computation-physicalsystems/



