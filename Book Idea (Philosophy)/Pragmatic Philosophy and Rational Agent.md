
3 cores:

Beliefs/Knowledge

Goals/Preferences

Intentions/Actions

Then simulate some agents with different properties
Properties:

- Belief System
	- Credence based (precice, imprecise)
		- Bayesian
		- Bayesian with Czech book exceptions
	- AGM (Different inference rules)
	- Comparative beliefs (doxastic logic)
	- Neural Network (many many types here)
	- Logical Omniscience
	- Incomplete/Complete Information about world state
	- **No Drop** If one proposition entails another, then your degree of belief in the first should not exceed your degree of belief in the second.
- Preference:
	- Transitive
	- Complete
	- Irrelevant Alternatives
	- Continuity
- Decision Theoretic framework:
	- Causal
	- Causal with Newcomb's problem exceptions
	- Evidential
	- Decision theoretical dominance of any alternative
- Risks:
	- Risk Averse
	- Risk seeking
	- Expected utility maximiser

Agents who fail to uphold some of those characteristics may be subject too
- Dutch Books
- Money Pumps
- Sunken cost
- Chzeck books
- Aversion to free information
- "Fail to reduce objective compound lotteries"
- Taking dominated choices


## Worlds/States

Most things below are defined using possible worlds in some ways. 

Annihilation state: A $W_{annihilation}$ such that it with 100% probability of entering $W_{annihilation}$.




## Belief/Knowledge

Scepticism/Sceptical scenarios

Belief function $B$ over possible worlds $\{w1,\dots w_n\}$. Should generally follow the probability axioms. 

Empiricist Foundherentism (make blog post about that first, extract what's already written). 

Conditionalize beliefs on evidence (evidence can be formally defined in formal phenomenology).

Bayesian empirical beliefs, AGM for non-empirical/philosophical beliefs.

## Goals/Preferences

Preference relation $R$ over possible worlds $\{w1,\dots w_n\}$. 
Probability distribution over preferences (preferences are acually kinda unknown) $R^*$. 

Transitivity, Completeness, Independence of alternatives?

Dynamic preference relation. Getting rid of intransitivity over time due to money pump arguments. Changing preferences of worlds due to new beliefs about preferences.

So there are prefered preference relations? i.e $R_1 \succ R_2$? Meta-level preference? Need to make sure to avoid that, as it's meant to be dynamic. But I suppose it's not entirely wrong.
And then what about the transitivity of those? Why is that one static? If it's also dynamic, is there a third level?



## Intentions/Actions

Risk aversion. Can be defined as out of any set of gambles, pick the one with the highest lowest utility payout (i.e maxmin). This might not work due to the [something] principle which states that all possibilities has a non-zero probability of occurring. Even conditioned under some action a maybe.

Taking actions under uncertain beliefs and uncertain preferences

Changing beliefs and preferences are actions

SEP logic of action "see to it that" at some moment a history diverges and $\phi$ becomes true at that moment. 


## Caveat: Free will is not needed

Free will not needed for making sense of actions, preferences and beliefs, even if we cannot choose our actions, preference and beliefs freely. We can represent them as subset of phenomena. They are not metaphysical in that sense.


## Caveat: Folk psychology and physicalism

Physicalists can claim that the entire system is not a part of a future reduced mental objects. With new terms. I am prepared to change to this, once such a reductive programme is successful. 

## Caveat: Doxastic Voluntarism
To what extent can we control our beliefs? Well I dunno tbh. 


## Mathematical formalism only


Propositional symbols $\{p,q,\dots\}$
Predicate symbols $\{F, G,\dots\}$
Object symbols $\{x,y,\dots\}$
Logical connectives and quantifiers

Preference relation on worlds $P$
Epistemic modal operators $\{K, B, C\}$
Coherent and incoherent belief relations

Possible worlds (maximally consistent sets of propositions) $\{W_1, W_2\dots\}$
Actions are functions from worlds to worlds $a_i : W \rightarrow W$.

Dynamic single-agent epistemic logic with a preference relation over worlds

$$BE(a) = \sum_{i=1}^{n}\sum_{j=1}^{m}C(W_i|a\wedge W_j)C(W_j)BU(W_i)$$

Assuming transitive, complete preference relation such that it can be described by a utility function $U$.

Dynamic preferences: Intransitive preference removal:

If
$B(P(a,b)\wedge P(b,c) \wedge P(c,a)))$

$B(a>b\wedge b > c \wedge  c > a))$

Then the strict preference is removed
$B(a\equiv b \equiv c)$ 

So then $P_{i+1}$ will have removed one intransitive section of itself. 


Changing beliefs is an action. Not AGM, bayesian conditionalization instead (sometimes)


Perfection and Perfect horror 
Let there be a world $W_a$ such that $\forall W. W \preceq W_a$. Then $W_a$ is a perfect world (or atleast, most preferred, out of the one's currently known). Then $W_b$ such that $\forall W. W \succeq W_b$ makes $W_b$ really awful (or atleast, least preferred).

We could even have a set of such worlds. Call the good one's "paradise worlds" and call the other "horror worlds". 

With incompleteness, this might not be the case:
   o
 /   \
o    o


## Logical omniscience cannot be implemented due to Gödel's Incompleteness theorem

Self-explanatory, can't know all tautologies if some tautologies are unprovable. 

But how do we avoid falling for dutch books, specifically since axiom 2 no longer works? I.e the axiom that $C(p) + C(\neg p) = 1$, i.e all tautologies have probability one. 

What should you bet on the Continuum hypothesis?

[Bounded Rationality (Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/entries/bounded-rationality/#LimiLogiOmni)

"The notion of _apparently possible_ refers to a procedure for determining inconsistency, which is a form of bounded procedural rationality ([section 2](https://plato.stanford.edu/entries/bounded-rationality/#EmerProcRati)). The challenges of avoiding paradox, which Savage alludes to, are formidable. However, work on bounded fragments of Peano arithmetic (Parikh 1971) provide coherent foundations for exploring these ideas, which have been taken up specifically to formulate bounded-extensions of default logic for _apparent possibility_ (Wheeler 2004) and more generally in models of _computational rationality_ (Lewis, Howes, & Singh 2014)."

## The cost of optimizing 

  [Bounded Rationality (Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/entries/bounded-rationality/#LimiLogiOmni)
"The analysis should be careful not to prove too much; for some departures from theory are inevitable, and some even laudable. For example, a person required to risk money on a remote digit of π� would, in order to comply fully with the theory, have to compute that digit, though this would really be wasteful if the cost of computation were more than the prize involved. For the postulates of the theory imply that you should behave in accordance with the logical implication of all that you know. Is it possible to improve the theory in this respect, making allowances within it for the cost of thinking, or would that entail paradox, as I am inclined to believe but unable to demonstrate? (Savage 1967 excerpted from Savage’s prepublished draft; see notes in Seidenfeld et al. 2012)"