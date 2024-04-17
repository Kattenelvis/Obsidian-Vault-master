
- Physical Computation
	- Unlimited Pancomputationalism
	- Limited Pancomputationalism
	- Computational Universe Hypothesis
	- Physical Church-Turing thesis
	- Quantum Computing
	- Computonium
- Beyond computational aspects of reality?
- Simulation Hypothesis (Boström argument)
- Omega Point Cosmology





# Physical Realization of Computation

With the theory of computation out of the way, the question become how does one realize computation in physical (or as we'll see, even mental) systems? 

Mapping accounts/Simple mapping account 


So as we saw in [section], a machine in state $a$ goes to $b$ over time. We can also see that physical systems change over time from state $A$ to $B$ (for instance, a rock falling or a gear turning or a magnet moving through an electric field or the wave function propagating through some potential etc.). 

As such, assuming the physical system only has a countable set of states, we can set up a mapping from physical states to computational states. We get that $f$ maps $a$ to $A$ and $b$ to $B$. 

"One difficulty with the formulation above is that ordinary physical systems admit of uncountably many physical states, whereas ordinary computational descriptions, such as TM tables, consist of countably many states. Thus, there are not enough computational states for the physical states to map onto. One solution to this problem is to reverse the direction of the mapping, requiring a mapping of the computational states onto (a subset of) the physical states. Another, more common solution to this problem—often implicit—is to select either a subset of the physical states or equivalence classes of the physical states and map those onto the computational states. When this is done, clause (i) is replaced by the following: (i′) there is a mapping from _a subset of_ (or _equivalence classes of_) the physical states of _S_ to the states of computational description _C_."[Computation in Physical Systems (Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/entries/computation-physicalsystems/)

But what's important to note here is that the necessity of $a$ to $b$ may not be the same as the necessity from $A$ to $B$ in all physical systems. 

"Consider a rock under the sun, early in the morning. During any time interval, the rock’s temperature rises, going from _T_ to _T_+1, to _T_+2, to _T_+3. Now consider a NOT gate that feeds its output back to itself. At first, suppose the NOT gate receives ‘0’ as an input; it then returns a ‘1’. After the ‘1’ is fed back to the NOT gate, the gate returns a ‘0’ again, and so on. The NOT gate goes back and forth between outputting a ‘0’ and outputting a ‘1’. Now map physical states _T_ and _T_+2 onto ‘0’; then map _T_+1 and _T_+3 onto ‘1’.

According to the simple mapping account, the rock implements a NOT gate undergoing the computation represented by ‘0101’."

So Putnam argues that blah blah blah Chalmers responds

"The simple mapping account turns out to be very liberal: it attributes many computations to many systems. In the absence of restrictions on which mappings are acceptable, such mappings are relatively easy to come by. As a consequence, some have argued that every physical system implements every computation (Putnam 1988, Searle 1992)."

# Physical Computation



We've discussed the [Church Turing thesis] earlier, but David Deutsch developed a physical version of it. Noticing the universal realiziability of turing machines in physical systems, he was able to something something.



So, are we merely using computability mathematics to model and predict the behavior of a physical system, or are we explaining that the system works it way it works because it is computational? Is reality itself computational?





## Pancomputationalism

The view that the universe is a computation

We have to perhaps be a bit careful in how we interpret this notion. We may believe that even a rock is performing computation, by modelling it being bright, during the day, reflecting the suns rays, and it being dark, as 1 and 0 respectively, and that it is computing a one-bit signal clock. 


### Unlimited Pancomputationalism

The mapping account thus states that any computation is arbitrarily mapped to any physical system. This has been deemed problematic for some, as it makes the entire hypothesis vacuous

Instead, some argue that without properly addressing the fact that computations are implemented will also predict the future of the physical system, then they can only be said to implement a particular computation

Idea: Grue --> What if some physical system is modelled with machine $T$ however say, compared to the model where it is $T$ until time $t$ but then changes into $T'$. New problem of induction applies here

Instrumentalism vs non-natural realism vs naturalist realism



### Limited Pancomputationalism

Instead you can limit it to causal, 

Counterfactual account
Causal account
Dispositional account


"In the face of these objections, limited pancomputationalists are likely to maintain that the explanatory force of computational explanations does not come from the claim that a system is computational simpliciter. Rather, explanatory force comes from the _specific_ computations that a system is said to perform. Thus, while a rock and a digital computer both perform computations, the fact that they perform radically different computations explains the difference between them. As to the objection that there are still too many computations performed by each system, limited pancomputationalists have two main options: either to bite the bullet and accept that every system implements indefinitely many computations, or to find a way to single out, among the many computational descriptions satisfied by each system, the one that is ontologically privileged—the one that captures _the_ computation performed by the system. One way to do this is to postulate a fundamental physical level, whose most accurate computational description identifies the (most fundamental) computation performed by the system. This response is built into the view that the physical world is fundamentally computational (explored in the next section)."

# Examples of physical computation



Here is a hydrocomputer which realizes fluidic logic gates


Examples, such as hydrologic and woodlogic

## Quantum Computing

[Quantum Computing (Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/entries/qt-quantcomp/)
"Setting aside “hypercomputers”, even if we restrict ourselves only to Turing-computable functions, one can still find many proposals in the literature that purport to display “short-cuts” in computational resources. Consider, e.g., the DNA model of computation that was claimed (Adleman 1994; Lipton 1995) to solve **NP**-complete problems in polynomial time. A closer inspection shows that the cost of the computation in this model is still exponential since the number of molecules in the physical system grows exponentially with the size of the problem. Or take an allegedly instantaneous solution to another **NP**-complete problem using a construction of rods and balls (Vergis, Steiglitz, and Dickinson 1986) that unfortunately ignores the accumulating time-delays in the rigid rods that result in an exponential overall slowdown. It appears that these and other similar models cannot serve as counter-examples to the physical Church-Turing thesis (as far as complexity is concerned) since they all require some exponential physical resource. Note, however, that all these models are based on classical physics, hence the unavoidable question: Can the shift to quantum physics allow us to find “short-cuts” in computational resources? The quest for the quantum computer began with the possibility of giving a positive answer to this question."

Hadamard gate
![[Pasted image 20240216235344.png]]


# Implementing Hypercomputers


"Some authors have questioned whether the mainstream quantum computing paradigm is general enough and, if not, whether some aspects of quantum mechanics may be exploited to design a quantum hypercomputer (Nielsen 1997, Calude and Pavlov 2002). The most prominent proposal for a quantum hypercomputer is due to Tien Kieu (2002, 2003, 2004, 2005). He argues that an appropriately constructed quantum system can decide whether an arbitrary Diophantine equation has an integral solution—a problem which is known to be unsolvable by TMs. Kieu’s method involves encoding a specific instance of the problem in an appropriate Hamiltonian, which represents the total energy of a quantum system. Kieu shows that such a system can dynamically evolve over time into an energy ground state that encodes the desired solution. Unfortunately, Kieu’s scheme does not appear to be workable. For one thing, it requires infinite precision in setting up and maintaining the system (Hodges 2005). For another, Kieu does not provide a successful criterion for knowing _when_ the system has evolved into the solution state, and the problem of determining when the solution state is reached is Turing-uncomputable (Smith 2006b, Hagar and Korolev 2007). Thus, operating Kieu’s proposed hypercomputer would require already possessing hypercomputational powers."


But it seems given current physics that it is impossible:

Closed timelike curves can build a hypercomputer!

CTC's are nomonologically impossible:

Gödel metric [insert Gödel story here, no Gödel, no spinningfound!]

Generalized Entropy


# Computonium

A configuration of matter that is the most efficient for computation. See: Hedonium



# Computational Universe?


CUH Tegmark

Do not use planc length as an argument that the universe is discrete, it is merely at that point where uncertianty reaches a breaking point in our ability to uilize QM. Smaller theories may still be the case. 


Cellullar automata interpretation of QM

Wolfram Physics and Computational Quantum Gravity


# Junk, Gunk and Funk

In metaphysics, the idea of whether or not space or time is divisible forever or discrete at some step has been a major topic of discussion ever since the ancient Greeks[source]. It turns out to be relevant for the question on whether or not the universe is computational.

Is the universe infinitely large/infinitely divisible? If tey are atleast one of them, that spells some trouble for computational physics. 

Analog computation vs Digital Computation



# Simulation Hypothesis

The simulation hypothesis states that we, as in humanity, are in a computer simulation ran by some unknown entity. 


### Why the SH may be likely
Nick Boström makes an interesting argument beyond just mere speculation, and gives reasons for why SH is likely. 

1. Future civilizations will have some minimal interest in past generations and knowing the past, and thus set some tiny percentage $\epsilon > 0$ of their computer simulations on working on simulations.
2. Future civilizations will have vast computational resources through building Dyson sphere's and computers around every star, and have access to $K$ flops of computing power
3. So $\epsilon\times K$ is still a huge number
4. There would be so many simulations that the probability of being in one, assuming there's a uniform distribution over all simulations + "the main world", would be very large.
5. We're very likely living in a simulation



Simulations within simulations are possible


Idea (Tomas): We have a good reason to believe that we are at the top layer of the simulation: The size of the current simulation. It has so much energy and matter, and each iteration will only use a small subset of all availible energy and matter in their respective universes, such that the simulations somewhat quickly become low resolution. 


Our actions may be shaped by this. If there's a non-zero percent probability of the simulators shutting down the simulation, then it's less rational to plan for long term actions. This lowers our time-preference and increases discounting rate for all of our actions. However, assuming memory is reliable, the simulation started atleast 23 years ago (for me) but may be much older if we assume that other individuals have been simulated for thousands, even millions of years. This might mean that for any long-term entropic plans such as being at a rotating supermassive blackhole to keep my uploaded consciousness alive for a ridicilious amoun of time may not be as important to achieve anymore [see chapter on end-time civilizations].


# Omega Point Cosmology


Omega point cosmology (OPC) is a very wild, out-there idea that has recieved a lot of criticism. I believe it has a very low probability of being true, but is worth investigating anyways just because of how mind-boggingly insanse the idea is. 


![[Pasted image 20240414231023.png]]

