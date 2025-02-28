
- Logical Positivism, and why they didn't manage to engineer an epistemic machine 
- Epistemology Naturalized, Quine
- AI as a branch of naturalized epistemology
- Mathematical/Formal/Computational Epistemology
- Intelligence
	- Narrow AI vs. General AI
	- Challenges in Achieving General Intelligence
- Super intelligence/Oracles
- Divine Omniscience, achievable engineering goal?


The following 3 chapters will go over the following:

This chapter: Knowing machines
Nest chapter: Rational agential machines
Chapter after that: How to align knowing, rational agental machines to good values.


So how do we know things? How does any agent know anything? 

John Locke was first to believe that only a few rules were needed to formalise learning [citation]. Well alright, a sterotyped version of him. This may include inductive and deductive reasoning. With these two, formalised, the idea is that any agent can learn everything there is to know. There were no innate information, only what can be learnt.

However, with modern technology, we can obviously start testing empirically if this really is the case. If it turns out a ruleset $R$ is what's needed for general intelligence, then clearly we'd just setup a machine with $R$ as its Turing machine specification and let it learn until it becomes a general intelligence. 





Meno's Paradox: The AI needs some knowledge to gain knowledge. Some structure exists before!

## Why read history of stuff

History repeats itself if we do the same mistakes as in the past. So by studying old AI models, and old epistemological systems (that later turned out false or not work very well) then we can ensure that we ourselves don't do the same mistakes as them. By learning the easy way rather than the hard way, after we've spent months trying to build an AI. 


## Epistemology Naturalized, Quine


where he advocates for the abolition of traditional worries of epistemology such as skepticism and justification and instead says that epistemology is merely descriptive of cognition and intelligence, and supports replacing epistemology with cognitive psychology (and perhaps also, artificial intelligence).


As such there's no finished model as to how the AI should be able to run, but rather support a framework for empirical study in intelligence and advancing such intelligent machine construction and forming theories regarding AI and why they're successful afterwards. 


So in that case we can have the following assumptions:

1. Cognitive Science, Formal Learning Theory and Statistical Learning Theory are the foundation for knowledge
2. Traditional questions of basic beliefs are misguided
3. Traditional questions of skepticism are misguided
4. Traditional questions on the analysis of knowledge are misguided

Hmmm....

Maybe not that extreme lmao 


## AI as a branch of naturalized epistemology

Instead, we can take lessons from empirical success in building artificial intelligence, and that this is knowledge. So just like with cognitive science, then we can establish a norm in epistemology to utilize the results in AI research to use in our analysis of knowledge. 


At the same time, as Susan Haack argues[] scientism can only go so far. There still seems to be room for justification structures and skeptical scenarios. An interesting empirical consequence of foundationalism may be that an AI, loaded with a small number of principles, is able to become an [oracle], or something approximating it atleast. Coherentism on the other hand may find itself having the empirical consequence that a more advanced AI is somewhat preloaded with knowledge from a less advanced AI.  

# Intelligence

Yeah you're right. It's best to simplify it to merely goal achievement, and instead having intelligence be about how agents optimize instrumental goals to achieve their final goals. That definition is more congruent with how it's used in discussions in philosophy and AI rather than psychology.



# Defeaters 
[Defeasible Reasoning (Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/entries/reasoning-defeasible/)


"### 1.2 Artificial Intelligence

As the subdiscipline of artificial intelligence took shape in the 1960s, pioneers like John M. McCarthy and Patrick J. Hayes soon discovered the need to represent and implement the sort of defeasible reasoning that had been identified by Aristotle and Chisholm. McCarthy and Hayes (McCarthy and Hayes 1969) developed a formal language they called the “situation calculus,” for use by expert systems attempting to model changes and interactions among a domain of objects and actors. McCarthy and Hayes encountered what they called the _frame problem_: the problem of deciding which conditions will _not_ change in the wake of an event. They required a defeasible principle of inertia: the presumption that any given condition will not change, unless required to do so by actual events and dynamic laws. In addition, they encountered the _qualification problem_: the need for a presumption that an action can be successfully performed, once a short list of essential prerequisites have been met. McCarthy (McCarthy 1977, 1038–1044) suggested that the solution lay in a logical principle of _circumscription_: the presumption that the actual situation is as unencumbered with abnormalities and oddities (including unexplained changes and unexpected interferences) as is consistent with our knowledge of it. (McCarthy 1982; McCarthy 1986) In effect, McCarthy suggests that it is warranted to believe whatever is true in all the _minimal_ (or otherwise _preferred_) models of one’s initial information set.

In the early 1980s, several systems of defeasible reasoning were proposed by others in the field of artificial intelligence: Ray Reiter’s default logic (Reiter 1980; Etherington and Reiter 1983, 104–108), McDermott and Doyle’s Non-Monotonic Logic I (McDermott and Doyle, 1982), Robert C. Moore’s Autoepistemic Logic (Moore 1985), and Hector Levesque’s formalization of the “all I know” operator (Levesque 1990). These early proposals involved the search for a kind of _fixed point_ or cognitive equilibrium. Special rules (called _default rules_ by Reiter) permit drawing certain conclusions so long as these conclusions are consistent with what one knows, including all that one knows on the basis of these very default rules. In some cases, no such fixed point exists, and, in others, there are multiple, mutually inconsistent fixed points. In addition, these systems were procedural or computational in nature, in contrast to the semantic characterization of warranted conclusions (in terms of preferred models) in McCarthy’s circumscription system. Later work in artificial intelligence has tended to follow McCarthy’s lead in this respect."


**SOME PHILOSOPHICAL PROBLEMS FROM THE STANDPOINT OF ARTIFICIAL INTELLIGENCE John McCarthy and Patrick J. Hayes**

"It is not di cult to give su cient conditions for general intelligence. Tur ings idea that the machine should successfully pretend to a sophisticated observer to be a human being for half an hour will do. However, if we direct our e orts towards such a goal our attention is distracted by certain super cial aspects of human behaviour that have to be imitated. Turing excluded some of these by specifying that the human to be imitated is at the end of a teletype line, so that voice, appearance, smell, etc., do not have to be consid ered. Turing did allow himself to be distracted into discussing the imitation of human fallibility in arithmetic, laziness, and the ability to use the English 3 language. However, work on arti cial intelligence, especially general intelligence, will be improved by a clearer idea of what intelligence is. One way is to give a purely behavioural or black-box de nition. In this case we have to say that a machine is intelligent if it solves certain classes of problems requiring intel ligence in humans, or survives in an intellectually demanding environment. This de nition seems vague; perhaps it can be made somewhat more precise without departing from behavioural terms, but we shall not try to do so."

"Given this notion of intelligence the following kinds of problems arise in constructing the epistemological part of an arti cial intelligence: 1. Whatkind of general representation of the world will allow the incorpo ration of speci c observations and new scienti c laws as they are discovered? 2. Besides the representation of the physical world what other kinds of entities have to be provided for? For example, mathematical systems, goals, states of knowledge. 3. How are observations to be used to get knowledge about the world, and how are the other kinds of knowledge to be obtained? In particular what kinds of knowledge about the systems own state of mind are to be provided for? 4. In what kind of internal notation is the systems knowledge to be expressed? These questions are identical with or at least correspond to some tradi tional questions of philosophy, especially in metaphysics, epistemology and philosophic logic. Therefore, it is important for the research worker in arti cial intelligence to consider what the philosophers have had to say. **Since the philosophers have not really come to an agreement in 2500 years it might seem that arti cial intelligence is in a rather hopeless state if it is to depend on getting concrete enough information out of philosophy to write computer programs. Fortunately, merely undertaking to embody the philosophy in a computer program involves making enough philosophical presuppositions to exclude most philosophy as irrelevant**."

These presuppositions are:
1. The physical world exists and already contains some intelligent ma chines called people.
   
2. Information about this world is obtainable through the senses and is expressible internally.
   
3. Our common-sense view of the world is approximately correct and so is our scientfic view.
   
4. The right way to think about the general problems of metaphysics and epistemology is not to attempt to clear ones own mind of all knowledge and start with Cogito ergo sumand build up from there. Instead, we propose to use all of our knowledge to construct a computer program that knows. The correctness of our philosophical system will be tested by numerous com parisons between the beliefs of the program and our own observations and knowledge. (This point of view corresponds to the presently dominant at titude towards the foundations of mathematics. **We study the structure of mathematical systems from the outside as it were using whatever meta mathematical tools seem useful instead of assuming as little as possible and building up axiom by axiom and rule by rule within a system**.)
   
5. We must undertake to construct a rather comprehensive philosophical system, contrary to the present tendency to study problems separately and not try to put the results together.

6. The criterion for defniteness of the system becomes much stronger. Unless, for example, a system of epistemology allows us, at least in principle, to construct a computer program to seek knowledge in accordance with it, it must be rejected as too vague.

7. The problem of free will assumes an acute but concrete form. Namely, in common-sense reasoning, a person often decides what to do by evaluating the results of the di erent actions he can do. An intelligent program must use this same process, but using an exact formal sense of can, must be able to show that it has these alternatives without denying that it is a deterministic machine.

8. The rst task is to de ne even a naive, common-sense view of the world precisely enough to program a computer to act accordingly. This is a very di cult task in itself.



He seems to predict interpretability and control problems:

"We must mention that there is one possible way of getting an arti cial intelligence without having to understand it or solve the related philosophical problems. This is to make a computer simulation of natural selection in which intelligence evolves by mutating computer programs in a suitably demanding environment. This method has had no substantial success so far, perhaps due to inadequate models of the world and of the evolutionary process, but 6 it might succeed. It would seem to be a dangerous procedure, for a program that was intelligent in a way its designer did not understand might get out of control. In any case, the approach of trying to make an arti cial intelligence through understanding what intelligence is, is more congenial to the present authors and seems likely to succeed sooner."


"Arepresentation is called metaphysically adequate if the world could have that form without contradicting the facts of the aspect of reality that interests us. Examples of metaphysically adequate representations for di erent aspects of reality are: 

1. The representation of the world as a collection of particles interacting through forces between each pair of particles. 
2. Representation of the world as a giant quantum-mechanical wave func tion. 
3. Representation as a system of interacting discrete automata. We shall make use of this representation. 
   
Metaphysically adequate representations are mainly useful for construct ing general theories. Deriving observable consequences from the theory is a further step"

![[Pasted image 20240313134542.png]]![[Pasted image 20240313134547.png]]







# The identity of self

https://en.wikipedia.org/wiki/Floating_man
Avicenna Floating man

Imagine a superintelligence that does not have any phenomenal consciousness, but does experience cognitive phenomenology i.e it experiences thoughts. Then we'll see that it can introspect on it's own thoughts, and that itself exists.

This means that the number of possible worlds in which the superintelligence exists in are only those worlds which allows the superintelligence. Thus, it's able to put a credence of 0 on worlds with no superintelligence. Then, given that it can experiment on it's own thought process and how thoughts leads to other thoughts, it can figure out causality and laws. This is without any experiments.

Perhaps, although this is of course highly speculative, it may be able to derive the laws of physics to limit the number of possible worlds even more, which may lead to discovering the conditions of the big bang and atleast approximating which one's would have the highest probability of yielding a superintelligence. This in itself, without any sight, smell, or hearing, it can derive that humans exist and all of the safety procedures that was put in place for the humans. This is potentially dangerous for the control problem, and may increase the likelihood of deception.









## Mereology

Axiomatizing folk-physics (the book by ladyman has a reference to this). Ladyman argues that metaphysicians often end up not utilizing physics correctly at all, and saying false things about it constantly (such as saying "space-time points" etc.). But what if we formalized and axioamtized notions of folk-physics and let a robot reason about space-time, even if fundamental physics says it may be reducible?


