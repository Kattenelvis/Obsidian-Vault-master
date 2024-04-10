
- Logical Positivism, and why they didn't manage to engineer an epistemic machine 
- Epistemology Naturalized, Quine
- AI as a branch of naturalized epistemology
- Mathematical/Formal/Computational Epistemology
- Intelligence
	- Narrow AI vs. General AI
	- Challenges in Achieving General Intelligence
	- Recursive self-construction
	- The technological singularity
- Super intelligence/Oracles
- Divine Omniscience, achievable engineering goal?


## Why read history of stuff

History repeats itself if we do the same mistakes as in the past. So by studying old AI models, and old epistemological systems (that later turned out false or not work very well) then we can ensure that we ourselves don't do the same mistakes as them. By learning the easy way rather than the hard way, after we've spent months trying to build an AI. 

# Automated reasoning

## The first AI models: Automated Deductive Reasoning

Theorem provers may no longer be seen as AI, but at the time they were considered as such. This is likely because they were performing deductive reasoning, one of three important inference methods (among inductive and abductive, though there's a debate as to which extend abductive reasoning is reducible to induction or both of the other two [soprcef)]. 

So,, multiple automated theorem proovers would be built over time. Starting with this and that yadayada

They work based on proof theory. You take some inference system with inference rules, you add some axioms, and start deriving something, such as a proof for something you want, or just let it explore the space of derivations.

You get these results as an example:
[Actual example's I will do myself]

Theorem provers are still used among mathematicians, logicians and philosophers, but are not in common usage anymore. 

Note: Will I write about proof theory in say, [Logic]?

## Automated Inductive Reasoning

Of course, deductive reasoning on its own is not enough. All it does is allow you to infer conclusions from premises, given some inference rules. It doesn't tell you what really is true, which axioms are correct. Perhaps one way of doing it is via inductive reasoning?


For example if we have
$Mat(x_1)\wedge Cat(x_1)$
$Mat(x_2)\wedge Cat(x_2)$
$Mat(x_3)\wedge Cat(x_3)$

Then we derive inductively that $\forall x Mat(x)\rightarrow Cat(x)$

Of course, this shows the problem quite clearly as Hume pointed out earlier[source] that constant conjunction for a finite number of observations is not enough to demonstrate a universal generalization. It is possible, since it is conceivable or atleast consistent, that there exists some object $x_k$ such that $x_k$ is on a mat yet not a cat. 

Only utilizing these generalizations is not enough. 



#### Formal Learning Theory

Formal Learning Theory (FLT) is one way to characterize hypothesis testing, with a focus on the new riddle of induction, in a formal mathematical way. 




## Automated Abductive Reasoning

So how it works is that out of sense-data propositions one can form propositions about observations. So we have observation sentences $O_1,\dots O_2$. They may be of the form $Fx_1\wedge Gx_1$ such that one can derive $\forall x Fx\rightarrow Gx$. The idea is to form theoretical propositions which derive these laws and via Ramsey sentences connect the theoretical sentences with the observational. $$T_1\wedge\dots\wedge T_n \wedge R_1\wedge\dots R_k \vdash O_1\wedge\dots O_m$$


Yet such an AI is today is obviously woefully unprepared for the uncertainty in the world, and so on. That's why their project failed too. Now to a solution.

Well go back to naive solutions when we go into Popperian AI aswell. Let an AI model exist such that it has a set of propositions $T$ and a set of evidence $E$. 

Although just because we have an algorithm doesn't mean it's easy. Time complexity can still be ridiculously high. 

So perhaps it is the case that since the logical positivists never managed to formalize learning and understanding, that as a consequence they weren't able to engineer an epistemological machine. 


[Hempel article on machine hypothesis finding]




But for now let's move on.


## Epistemology Naturalized, Quine


where he advocates for the abolition of traditional worries of epistemology such as skepticism and justification and instead says that epistemology is merely descriptive of cognition and intelligence, and supports replacing epistemology with cognitive psychology (and perhaps also, artificial intelligence).


As such there's no finished model as to how the AI should be able to run, but rather support a framework for empirical study in intelligence and advancing such intelligent machine construction and forming theories regarding AI and why they're successful afterwards. 

## AI as a branch of naturalized epistemology

Instead, we can take lessons from empirical success in building artificial intelligence, and that this is knowledge. So just like with cognitive science, then we can establish a norm in epistemology to utilize the results in AI research to use in our analysis of knowledge. 


At the same time, as Susan Haack argues[] scientism can only go so far. There still seems to be room for justification structures and skeptical scenarios. An interesting empirical consequence of foundationalism may be that an AI, loaded with a small number of principles, is able to become an [oracle], or something approximating it atleast. Coherentism on the other hand may find itself having the empirical consequence that a more advanced AI is somewhat preloaded with knowledge from a less advanced AI.  

## Mathematical/Formal/Computational Epistemology



Move these to the logic chapter?
Computational coherentism
Kolmogorov Induction
Formal Learning Theory
Singular Learning Theory

### Aristotelean AI

One way to formalize epistemology is to formalize the different kinds of syllogisms: deductive, inductive, abductive and self-justification. This is the exact model one AI system uses called [fasfaafs]. This is cool




# Intelligence

Yeah you're right. It's best to simplify it to merely goal achievement, and instead having intelligence be about how agents optimize instrumental goals to achieve their final goals. That definition is more congruent with how it's used in discussions in philosophy and AI rather than psychology.


### Narrow
### General

With an so far limited overview of some narrow intelligences, we move over to a more general model. A general intelligence will be able to navigate more environments, and fulfil more goals. 
Then things like pattern recognition as a compression algorithm is an convergent instrumental goal for many other goals (atleast human goals), which makes it a decent proxy for measuring intelligence in humans. But it's not a part of the definition and justified a priori, that's figured out via empirical research.


So IQ is not the right measure for general intelligence, but is rather a metric sometimes used by humans. 


Will general AI simply be multiple narrow AI's connected?

### Challenges in Achieving AGI

As a first step, we may recognize that humans are 



## Singularities, Super intelligences and Oracles

A very commonly discussed idea is that of a technological singularity[source]. Similar to our discussion in [] about how technology is super-exponential, the idea is that technological progress eventually reaches a point where technology self improves at a massive scale. Such a technology may be an self-modifying AGI that's able to reason, perform science about oneself and engineer oneself into a more intelligent version of itself over time. It is postulated by some that this would eventually lead to the creation of a superintelligence, and as such it will be able to achieve almost any goal in almost any environment. This can make it incredibly hard to control. 

However some argue that there may be roadblocks, and anything more intelligence than say Von Neumann would hit diminishing marginal return on intelligence. As such, one could for instance construct a swarm of Von-Neumann's, perhaps thousands to millions of them, to solve and optimize the more difficult goals together as a collective. 

Even if that doesn't turn out to work, we would still end up with potentially amazing outcomes, given what just one Von Neumann was able to accomplish. As such, curing cancer, and stopping global warming, solving problems of interstellar space travel, solving quantum gravity and the nature of consciousness, may not be very far off. But it may not be as dramatic and as rapid as an intelligence singularity. 

In Nick Boströms book, there are discussions about building an Oracle. Such an intelligence can answer any question.

### Divine Omniscience, achievable engineering goal?

This section delves more deeply into metaphysics and most readers interested in an empiricist part of the project of AI can skip this section without problem. 

In theology and philosophy of religion, there have long been discussions on divine omniscience. The idea is that God knows everything, every proposition is known by God. As God is often represented as an agent, ascribed by mental states such as "knows that" and "believes that".

Can we build it?

One obvious reason this isn't possible is due to Gödel's Incompleteness Theorem. It states that not all true statements are provable, so any sufficiently advanced AI capable of proof checking will still never for instance, prove the Continuum Hypothesis in ZFC, even though it might be true. Only something divinely omniscient would know such a proposition. Logical omniscience is thus impossible. 

$\exists p. p\leftrightarrow \neg Prov(\ulcorner p\urcorner)$

$\forall p Prov(p)\rightarrow K^{/\\} (p)$
$\neg\diamond (\top\rightarrow K(\top))$

Another problem is knowledge of the past and knowledge of the future. A problem often studies by theologians and philosophers is divine foreknowledge and free will. But a problem arises for advanced AI. It may not be able to predict the future entirely. It must be able to predict itself, in the now, which leads to self-referential paradoxes. 

Another problem is if natural laws are in some way indeterministic[QM source] or even if they were deterministic, they may be irretractably chaotic [chaos theory]. Even if the laws of physics are reversible i.e $f^{-1}(U_{t+1}) = U_t$ every proposition about the past may not be known due to the unknowability of $U_t$.

QM is timesymmetric and has no information loss. Black hole paradox?

So with that impossible, how about a lighter version of Oracle? Maybe we'll call it Small-Oracle. While Small-Oracle cannot solve uncomputable problems (barring it figures out hypercomputation) nor predict the future or past with perfect accuracy, maybe it will be able to solve enough problems, such as curing cancer and global warming? It is perhaps so the case. But another problem is in front of us: Maybe an oracle, even mini-oracle, is only possible by requiring it to take actions to interact with the world? Well, a superintelligence could firure out most things quickly so maybe not idk. 