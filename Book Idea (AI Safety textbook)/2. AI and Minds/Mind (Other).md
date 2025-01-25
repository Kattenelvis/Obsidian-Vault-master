- Mind
	- Does AI understand?
		- Searle Thought experiment, some objections
		- Intuition based philosophy is wrong? X-phi etc. 
	- Penrose Human mind is uncomputable argument... is it really true?
	- Does AI have consciousness? Or even have phenomenal experience/sense data?
	- Is it even important if AI is conscious or not? (answer: No, not in terms of capability or danger atleast)
	- Unconscious or conscious - still dangerous
	- Identity: At what point do we stop being humans?
	- Mind Upload - Copy and Death? Or slow transition a la Chalmers?



# The mind as a physically realized computation

[Maybe put the chapter on physical realizability of computation before]


Now what if the mind, or the brain, is a physically realized computation? Many arguments have been put forth both for and against this thesis, and which subsets of cognition which is computational.

## Behaviorism

B.F Skinner. The idea was that a theory of psychology that was enough is the usage of sensory inputs and behavioral outputs without any in-between stages.

While this approach has it fair share of obvious problems, the general notion of something being inputed and something being outputed will be repeated by future models, including AI models. 

According to SEP:

"Behaviorism, the doctrine, is committed in its fullest and most complete sense to the truth of the following three sets of claims.

1. Methodological: Psychology is the science of behavior. Psychology is not the science of the inner mind – as something other or different from behavior.
2. Psychological: Behavior can be described and explained without making ultimate reference to mental events or to internal psychological processes. The sources of behavior are external (in the environment), not internal (in the mind, in the head).
3. Logical/Philosophical: In the course of theory development in psychology, if, somehow, mental terms or concepts are deployed in describing or explaining behavior, then either (a) these terms or concepts should be eliminated and replaced by behavioral terms or (b) they can and should be translated or paraphrased into behavioral concepts"

## Representations and Functions

So behaviorism has problems. 

One of the earliest theoretical constructs of cognitive psychology is the notion of a representation, which contain mental content. 


## Computational Theory of Mind

The idea is that there does exist representations, and that the mind isn't reducible to sensory inputs affects and behavioural outputs. 

Turing machine specifications. 

Example:
If sensory input contains red-circle 
If context == kitchen
then represent: Tomato

If representing tomato
If sensory input contains hungry
Grab tomato and eat it

This is obviously an oversimplified model, however it demonstrates the computational if-then logical connectives that take place according to the CTM. 

## Language of Thought Hypothesis

Universal grammar?

RTT:
1. A has belief in p iff A has a representation S of p and that S stands in relation to a type of mental state B. 
2. Thoughts are causal instantiations of representations

COMP:
1. Compositionality of representations. Disjunction, conjunction etc. retain their semantic properties. 

RTT + COMP best defended by FCT

FCT:
1. Thought is systematic composition of representations following specific rules of mentalese

Highly compatible with the computational theory of mind (both classical CCTM which is neural implementationist and neuronal eliminative which is CTM).

Arguments is that thought is systematic and productive. Grammar is precise.

Author has argued against Fodor's argument, but implemented a new kind of computational language of thought hypothesis, being a kind of "machine code" for the brain. 

Fodor's LOTH is not semantically complete and doesn't do anything more advanced than perception and motor control, according to author.

The word Cat may refer to mentalese ```cat``` of course the english token of cat could be different and connote something else. So there may be an infinite regress in how one learn concepts such as 'cat'. So Fodor argues about innate abilities. Ruh-roh, most disagree here! 



## Fodor, Putnam, Dretske, Millikam


## Modularity of Mind

## Cognitive Architectures

Ways of instantiating it more concretely is with cognitive architectures.

## Global Workspaces

The idea in its most compressed form is that various distributed synchronous computational processes of information compression are regulated by a global workspace where executive functions execute goal directed behaviour i.e take actions[Negarestani].

[The Global Workspace Theory: A Step Towards Artificial General Intelligence | IEEE Conference Publication | IEEE Xplore](https://ieeexplore.ieee.org/document/10195021)




# Does AI understand?
## Searle Thought experiment, some objections

In Searle’s article “Minds, brains, and programs” he lays out an argument against “strong AI”. While weak AI claims AI is a class of formal models which helps understand mental processes, strong AI claims that the AI itself truly understands and has mental states in the same way humans do (at least some mental states such as belief). Searle wants to argue that strong AI is not possible with Yale’s AI project, or Turing machines in general. 

Imagine that you’re in a room with an input slot for chinese characters and a rulebook for how to transform those chinese characters into output chinese characters. Where in this process does semantics such as reference, meaning and truth take place? The article “A Logical Hole in the Chinese Room” formalizes the argument as following:


1. The room occupant knows no Chinese. 

2. The room occupant knows English. 

3. The room occupant is given sets of written strings of Chinese, {Ci, Cj,…, Cn}

4. The room occupant is given formal instructions in English that correlate pairs of sets of Chinese strings, <Ci, Cj>. 

5. The room occupant is given formal instructions in English to output some particular Ci given a particular Cj. 

6. The room occupant’s skill at syntactically manipulating the strings of Chinese is behaviorally indistinguishable from that of a fully competent speaker of Chinese. 

7. If 1–6 are jointly possible, then syntax is not sufficient for mental content. 

8. 1–6 are jointly possible. 

9. Therefore, syntax is not sufficient for mental content.”

  
There are multiple responses to this argument which we will go over in the following section. The system's response states that the entire room understands. That is to say, the rule instructions and the input-output section is sufficient for semantics. However Searle argues against this by imagining someone who has memorized the entire rule-updating system in their head and can even go about outside and converse chinese. People who know Chinese could communicate with this person just fine, but the person would not understand what some Chinese symbols refer to or what the sentences mean. 

Searle claims that the entire argument is very strange in general, and considers it plausible that people only support it for ideological reasons, people who have strong reasons to support strong AI. That a “hunk of metal” such as a thermostat can have beliefs sounds absurd. Searle does bring up some biological example’s like stomachs and claims that it doesn’t understand, yet recent research indicates that a lot of cognition is happening inside of the neurons in the stomach. Turns out to be a massive amount of neurons as well. It is not impossible that there’s at least some reference, meaning or truth of some kind, even if basic and quite different from what goes on in the brain.

But to give some pushback to Searle’s counter-argument, let’s say someone did memorize the entire rulebook. Now let’s introduce an image recognition algorithm, using a deep neural network it is able to train and classify tree images from non-tree images. Let’s say the training method is supervised, so for every image there is also some associated squiggly STree is written under every image of a tree. Then the referent of STree can be understood as the set of all trees. As can thus be seen, such a system might be capable of reference and might thus also be competent at semantics in general such as meaning and truth conditions. 

Another response to Searle’s argument is the robot response. Imagine a computer inside a robot that’s able to act just like a human (and not just output symbols) then what? It acts like a human would, so it seems like we can attribute intentionality and semantics to it. However, that's only if we don’t know what its internal structure is. Once we know that it is a syntactic updater based on specific rules, then that is the more parsimonious explanation for its actions, not intentionality. 

Searle goes on to critique most of behaviorism and operationalism. Just because something can operate in a certain way which seems to imply intentionality, it does not imply that this is actually the case. A calculator does not represent anything itself, only in the context of someone using the calculator. The Turing test is an example of a supposed test to show whether or not an AI system has intentionality. Yet this clearly doesn’t work, as it’s still a chinese room pretending to be a person. It’s a highly behaviouristic approach which Searle does not take to be an indication of intentionality at all.

Another response is the appeal to brain simulations. Searle argues that this response doesn’t work because the Chinese room argument can be translated into a system of water pipes that turn on or off based on neural firing. 

Searle did not predict the rise of large language models which are next-token predictors given some context (a set of previous tokens where tokens are words and various grammatical inflections) with billions of parameters. Such a system replicates more closely the way humans work, albeit not in a highly accurate way. Neural networks may need to be recurrent rather than one way to be able to perform semantics and understanding in the same way humans do. 

In Abelson’s response to Searle, he argues that whenever a computer is able to use rules to manipulate those symbols into new outputs, that is not different from say a child learning addition in which the child is also praised for being able to turn symbols into new symbols. At what point during the process of adding numbers together does ‘understanding’ show up?

A response might be that the human mind can instantiate computer programs in the instance of addition, but that understanding takes place somewhere else. In that case where? Seems like understanding is able to see where addition can be used, such as in the addition of concrete objects. However this is, again, a rule. For example “Input rule: “Formal syntactic manipulation” outputs “no understanding””. This is similar to say, the use-theory of language whereby one has to learn the ‘language games’ where people learn the game’s through reinforcement learning (as what has been advocated by Quine and Later Wittgenstein). However Chomsky has a different standpoint, however his universal grammar project still seems to indicate the existence of specific rules for human cognition as well. 

  

Sources:

Searle, Abelston, et. al “Minds, brains, and programs”

Shaffer, “A Logical Hole in the Chinese Room”


## Intuition based philosophy: Wrong?


Searle's argument may have captivating intuitions, but are intuitions reliable?

Common sense? Not so common nor sensical. 


## Is it even important if AI understands or not?

When it comes to capabilities, it can be the case that AI is just as capable if it "truly understood" as if it didn't.




# Does AI have belief states and knowledge states?

Reality of beliefs

Dennett Intentional Stance

Instead one can take the approach of Daniel Dennett[sources, such as Real Patterns] called the "intentional stance". As we've written in [reinforcment learning], reinforcment learning AI models are mathematically modelled as agents with belief states that take actions given desires, a kind of formal axiomatization of folk psychology. This may not mean they have intentional, doxastic nor epistemic mental states with content, as said earlier. However as per the intentional stance, if this is the best way of predicting their actions then so be it.

However, for superintelligences this may be more difficult. Can we really use folk psychology, even a mathematical formalism of it, to model and predict a superintelligence? This may be quite difficult, though some try. 


Doxastic voluntarism? 

# Lucas-Penrose Human mind is uncomputable argument... is it really true?

An result in the philosophy of mind is that according to Gödel's incompleteness theorem, there are things computable by minds that are not computable by computers. 

Turing (1950) writes that ....

Lucas (196)

Penrose (198)



Microtubles may not be able to carry entangled information well after all, due to high temperatures and lots of interactions which collapses the entanglement and forms new entanglements locally. 


Connections with Lucas argument?

It states in the SEP page for the Church-Turing thesis that every effective procedure can "Without exercising any insight, intuition, or ingenuity, a human being can work through the instructions in the program and carry out the required operations.". This is not the case for seeing the truth of a Gödel sentence of a system, according to the Lucas-Penrose argument. If that argument succeeds, is it a counter-example?

https://reducing-suffering.org/replies-lucas-penrose-argument/

"Roger Penrose (1989; 1994) conjectured that some mathematical insights are non-
recursive. Assuming that this mathematical thinking is carried out by some physical processes in
the brain, the bold thesis must then be false. But Penrose’s conjecture is highly controversial."
https://oronshagrir.huji.ac.il/sites/default/files/oronshagrir/files/ver19_physical_computability_theses.pdf




# Does AI have consciousness? Or even have phenomenal experience/sense data?


## Phenomenal Consciousness


Formal Phenomenology?

> Early modern psychology relied on introspection to parse mental processes but ultimately abandoned it due to worries about introspection’s reliability (Feest 2012; Spener 2018). Introspection was judged to be an unreliable method for addressing questions about mental processing (and it is still seen with suspicion by some; Schwitzgebel 2008). To address these worries, we must understand how introspection works, but unlike many other psychological capacities, detailed models of introspection of consciousness are hard to develop (Feest 2014; for theories of introspecting propositional attitudes, see Nichols & Stich 2003; Heal 1996; Carruthers 2011).


> Such introspection has revealed many phenomenal features that are targets of active investigation such as the phenomenology of mineness (Ehrsson 2009), sense of agency (Bayne 2011; Vignemont & Fourneret 2004; Marcel 2003; Horgan, Tienson, & Graham 2003), transparency (Harman 1990; Tye 1992), self-consciousness (Kriegel 2003: 122), cognitive phenomenology (Bayne & Montague 2011); phenomenal unity (Bayne & Chalmers 2003)


> Introspection illustrates a type of cognitive access, for a state that is introspected is access conscious. This raises a question that has epistemic implications: is access consciousness necessary for phenomenal consciousness? If it is not, then there can be phenomenal states that are not access conscious, so are in principle not reportable. That is, phenomenal consciousness can _overflow_ access consciousness (Block 2007).


> Access is tied to attention, and attention is tied to report. Some views hold that attention is necessary for access, which entails phenomenal consciousness (e.g., the Global Workspace theory [[section 3.1](https://plato.stanford.edu/entries/consciousness-neuroscience/#GlobNeurWork)]).[[4](https://plato.stanford.edu/entries/consciousness-neuroscience/notes.html#note-4)] In contrast, other theories (e.g., recurrent processing theory [section 3.2](https://plato.stanford.edu/entries/consciousness-neuroscience/#RecuProcTheo)]), hold that there can be phenomenal states that are not accessible.



Introspective detection theory.
[Detection theory - Wikipedia](https://en.wikipedia.org/wiki/Detection_theory)

![[Pasted image 20241214195216.png]]

### Is it important if AI has phenomenal consciousness or not?



Hitler could've been a philosophical zombie and still capable of all evildoings that he did. As such, we'll get more into capabilities and not delve too deep into the phenomenal consciousness of it. 



## Intentional Consciousness

What is intentional consciousness?
[Phenomenal Intentionality (Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/entries/phenomenal-intentionality/)

Brentano school



## Self-Consciousness


Me and not me

LSD studies where the self can move to a cup


# Naturalized Consciousness

The idea of naturalized epistemology was brought up earlier. We will use scientific theories of conscioussness, or atleast as scientific they can get with current technology. May be possible with future technology [See my blog post on it].


Global workspace theory say no (unless a global workspace can be instantiated in simulation?)


According to Integrated Information Theory, with its generally panpsychist commitments, there seems to be an indicitation that atleast each transistor has consciousness, but not the integrated whole. 



How do we infer experience in humans? What about an AI that perfectly replicates humans?

Chalmers, in Philosophical Zombies, blah blah blah

So, are AI's philosophical zombies? And how could we tell?

# Mind Upload

We will begin by analyzing a more naive copy+paste approach, followed by a reasonable ship of theseus approach. 

## Copy and Death? 

Uploading yourself to the PC, is a copy


## Or slow transition a la Chalmers?

But what if you did it like the Ship of Theseus? The idea here is to slowly replace the biological neurons with the brain with something digital. Some kind of slow, gradual shift from something biological to something technological. 

This idea seems to be the more risk-averse approach, as it assumes fewer number of philosophical assumptions regarding identity continuity and mental combination. So it's the more risk-free option, without too much of a cost (especially compared to the benefits of mind uploading) and the one I would advocate for.

## Metaphysics of consciousness

![[Worldscomputationalmind.excalidraw]]


4 major viewpoints

Physicalism
Panpsychism
Dualism
Idealism


As is argued in [source], all 4 major options are "strange" and counter-intuitive in some way. We'll either have to accept that consciousness emerges from non-consciouss things "magically", that everything in the universe has consciousness, that there are ghosts controlling machines, or that the external world doesn't exist/is mind-dependent. These are all strange in their own way. 

### Physicalism

Physicalism means that physical ontology is fundamental, and grounds everything. Everything is ontologically dependent on physical substance.

Physicalism has historical roots in materialism, where "matter" was seen as fundamental, for instance among Newton or the Atomists in ancient Greece. The view was that spatial-extension was the fundamental attribute of matter. However, as physics has developed into something which is on the cusp of abandoning space as a fundamental object, or property of objects, it has been renamed to physicalism. This means that, even if fundamental quantum gravity would turn out to have space as an emergent and non-fundamental phenomena, physicalism can still be true (even if materialism is false). 

As a view of consciousness, there are a lot of different principles that can be applied. 

Supervenience

## Identity 

The identity theory of mind posits that brain states are identical with mental states. So for instance, "pain is identical too C-neuron firings". This kind of metaphysical reduction is a fairly popular view, though a naive type-type identity theory can be shown to have a big flaw. 

So first, what is a type? A bit like a universal but with fewer "metaphysical" properties. While universals may be considered timelessness, known a priori etc the same kind of properties are not the case for types. They generalize some set of tokens which are instantiations of the type in reality. So for example, my own bike is a token of the type "bikes".

The problem with identifying types of mental states as identical to types of brain states is multiple realizability. Say some configuration $P_1$ of amino-acids and carbon atoms is identical with the color $M$, so $P_1=M$. However, a configuration $P_2$ of silicon atoms also instantiate $M$. So now $P_1 = M = P_2$ which is absurd. [Putnam]

A way of solving this is with token-token identity theory, identifying specific instances as identical. This way we now have tokens $M_1$ and $M_2$ who are identical with their respective token brain state. [Davidsson]



Emergentist

Strong emergence

Weak emergence

Panpsychist

### Physicalism and Mind Upload


So what logical implications does the differing principles of physicalism have for mind upload? 

Supervenience physicalism really doesn't tell us much, not on its own atleast. Jaegwon Kim made a point about this, by thinking about how deleting a phosphor atom on Saturn can, according to Supervenience physicalism, allow for a potentially radically alterations of conscious states in the universe.

$Sup_\square(x,y)$ iff  $\square Ch(y)\rightarrow Ch(x)$
$Sup_\diamond(x,y)$ iff $\diamond Ch(y)\rightarrow Ch(x)$

And if we take it that there is a deletion of a phosphor atom we have a $Ch(physical)$ and therefore $Ch(mental)$. $Ch(mental)$ can involve any change. All red gets reverted to green, smell for everyone except Jones aged 33 gets deleted and rocks suddenly gain self-consciousness. 

This does not help us with mind upload. Who knows how the change in physical substance accompanied by the upload-computer may have to consciousness. In fact it explains very little. 



###  Dualism and Mind Upload


The notion of dualism states that both physical substance and mental substance exist, and neither is more fundamental nor is one grounded in another. They are ontologically independent from eachother. 

$\neg G(p,m)\wedge \neg G(m,p)$
$\neg (G(p,m)\vee G(p,m))$

Mental substance is somewhat reminicent of the "soul", however it's worth noting that any religious or other connotations of the soul can be ignored here. There seems to be no necessary connection between mental substance and any kind of first-causer, physical law fine-tuner and/or necessarily perfect being, the universe can contain mental substance without such things (assuming the existence of anything afformentioned isn't necessarily true). Atleast, I have yet to seen a convincing argument for it. 

Instead, let us discuss what implications the existence of mental substance next to physical substance has for the possibility of safe mind-upload. My argument will conclude that it is possible, but AI's likely don't have consciousness (strong AI may still be possible though).


Dualism can be reconciled with transhumanism. Even if I believe dualism has a low probability of being true, seeing that they're compatible is still good for justifying transhumanism


We might even be able to develop advanced AI that finds convincing, irrefutable proof (or atleast, generates a hypothesis that can be confirmed to some very high probablity) that dualism is true, and then facilitate mind-upload the mental substance into the machine

Even if the AI itself lacks a "soul" or mental substance

Is it even important if AI is conscious or not? (answer: No, not in terms of capability or danger atleast) Unconscious or conscious - still dangerous


## Idealism

Idealism states that mental substance is ontologically fundamental. The physical is ontologically dependent on the mental. This worldview is quite the opposite of most people today. Most people belive that there exists an external world outside, where agents (such as mamals) walk around and are conscious inside of. But what if  this is completely wrong? What if all that exists are the conscious agents, who use notions such as "external world" and "spatial configurations" as a way to navigate their experience? One way to visualise idealism in this sense is to imagine that the universe is a wall of visual experiences

\[X] \[Y] \[Z]
\[X] \[Y] \[Z]
\[X] \[Y] \[Z]

Like some kind of virtual reality setup. In this sense, spatial extension and the external world are constructs of the mind to navigate and predict future behaviour of the experience. This viewpoint is called subjective idealism[source]

### Mind upload and idealism


I AM IDEAL!!

Yes it still works, probably

## Consciousness Splitting/Combining

PARFIT'S ARTICLE!!!

Mental combination and mental separation, including panpsychist combination laws and cosmopsychist separation laws

Also my own article on future experimental tools.


## Mind Upload and psychological continuity

Mental continuity is a common thingy to discuss in the philosophy of mind. There are multiple different views.

-Animalism
-Psychological Continuity
-Nihilism
etc.








Notes from talk David Pearce:

Human brain is a quantum computer. Classical turing machines are microphenomnological zombies. We are quantum computers where "smashing bits together" solved phenomenal binding problem. 

Abolishing wild animal sufferring in 10 years

Happier people feel more meaning. Manic people have super meaningfullness. Depressed people see everything as meaningless. Happier people are more motivated to change the world.
More life lovers --> Less existential risk

Some experiences are inherintly bad
Anti realist: Not bad for me!
But that is a Epistemological problem!
OMG OMG OMG YES
Combining people's consciousnessess! Getting epistemological access! Experiential union

Wireheading vs Bioengineering
Wireheading leads to problems. Information signaling is fucked. It's not the same as higher hedonic treadmill set point





# Free Will


So how do we deal with the question of free will? Well let's first distinguish between libertarian/compatibilist views and compatibilist views on the topic. 

All deterministic systems lack free will

But no, it seems like classical Turing machines have no free will, because they are deterministic and deterministic systems don't have free will.

However indeterministic one's might. Probabilistic and Quantum one's don't (indeterministic but probabilistic) (unless maybe the particle free will theorem is true?) 

An indeterministic, non-probabilistic Turing machines are not constructable

So computational mind --> No free will





# Gödel and Mind



## The Disjunction

Not mechanism or absolutely unknowable propositions

$\neg M\vee \exists p \neg\diamondsuit K(p)$

Section 4: https://iep.utm.edu/lp-argue/
"So the following disjunctive conclusion is inevitable: Either mathematics is incompletable in this sense, that its evident axioms can never be comprised in a finite rule, that is to say, the human mind (even within the realm of pure mathematics) infinitely surpasses the powers of any finite machine, or else there exist absolutely unsolvable diophantine problems of the type specified . . . (Gödel 1995: 310)."

"That is, his result shows that either (i) the human mind is not a Turing machine or (ii) there are certain unsolvable mathematical problems"


It turns out that the philosophical implications of this (though, following benacceraff 1967, requires in addition to the incompleteness theorems additional philosophical premises) can be quite vast. Particularly in the philosophy of mathematics (such as whether or not logicism has been defeated, it's atleast on shakier grounds) aswell as implications regarding platonism and mechanism (the view that the mind is computational). 

### Lucas's Argument

The poor old Turing machine can't calculate it, but we can "see" it as true. True? No cap fr?


"Benacerraf's criticism: the Lucas argument ignores the fact that there is a limit to the descriptive complexity of proofs that a person can understand. There may be a formal system F that captures my reasoning. But its Godel sentence may be too complicated for me to understand, much less verify."

### Penrose's New and Improved Argument 
As presented in Chalmers (19XX), it's like this

(1) 



https://arxiv.org/pdf/math/0607333




[PUTMAM.pdf (philpapers.org)](https://philpapers.org/archive/PUTMAM.pdf)


Consciousness in AI
[2308.08708 (arxiv.org)](https://arxiv.org/pdf/2308.08708)


[2402.19379 (arxiv.org)](https://arxiv.org/pdf/2402.19379)



# Predictive Coding


[Connectionism (Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/entries/connectionism/)

> It is too early to evaluate the importance and scope of PC models in accounting for the various aspects of cognition. Providing a unified theory of brain function in general is, after all, an impossibly high standard. Clark’s target article (2013) provides a useful forum for airing complaints against PC models and some possible responses. One objection that is often heard is that an organism with a PC brain can be expected to curl up in a dark room and die, for this is the best way to minimize error at its sensory inputs. However, that view may take too narrow a view of the sophistication of the predictions available to the organism. If it is to survive at all, its genetic endowment coupled with what it can learn along the way may very well endow it with the expectation that it go out and seek needed resources in the environment. Minimizing error for that prediction of its behavior will get it out of the dark room. However, it remains to be seen whether a theory of biological urges is usefully recast in PC terminology in this way, or whether PC theory is better characterized as only part of the explanation. Another complaint is that the top-down influence on our perception coupled with the constraint that the brain receives error signals rather than raw data would impose an unrealistic divide between a represented world of fantasy and the world as it really is. It is hard to evaluate whether that qualifies as a serious objection. Were PC models actually to provide an account of our phenomenological experience, and characterize the relations between that experience and what we count as real, then skeptical conclusions to be drawn would count as features of the view rather than objections to it. A number of responders to Clark’s target article also worry that PC-models count as overly general. In trying to explain everything they explain nothing. Without sufficient constraints on the architecture, it is too easy to pretend to explain cognitive phenomena by merely redescribing them in a story written in the vocabulary of prediction, comparison, error minimization, and optimized precision. The real proof of the pudding will come with the development of more complex and detailed computer models in the PC framework that are biologically plausible, and able to demonstrate the defining features of cognition.





# Brain Simulation

Massive brain simulation on 14k GPU's!
[2211.15963](https://arxiv.org/pdf/2211.15963)

> In previous research, the European Human Brain Project (HBP) aimed to create a digital infrastructure for neuroscience. For example, the SpiNNakker5, as well as other simulators such as NEST 6, can perform simulations at the neuronal level of brains7.


> These approaches have been useful in, for example, simulating networks in both local circuits8 and large-scale networks of multiple brain regions9,10. The Virtual Brain (TVB) also encompasses a large number of software tools, brain atlases, experimental datasets computational models and so forth, and is currently undergoing a large clinical trial on brain diseases11,12. However, there are still computational challenges to establish a digital brain: (1) how to efficiently simulate spiking neuronal networks at the large neuron scale of the human brain; (2) how to statistically infer such a “big” model by limited experimental data.


> In the present work, we have implemented a Digital Brain (DB) platform to simulate the activity of the whole human brain, going beyond the mean field, by implementing a spiking neuronal network with up to 86 billion neurons and 47.8 trillion synapses.




# AI as Philosophy

Dennett thinks AI is a part of epistemology and consciousness

Dennett sees the potential flaw, as reflected in:

> It has seemed to some philosophers that AI cannot plausibly be so construed because it takes on an additional burden: it restricts itself to _mechanistic_ solutions, and hence its domain is not the Kantian domain of all possible modes of intelligence, but just all possible mechanistically realizable modes of intelligence. This, it is claimed, would beg the question against vitalists, dualists, and other anti-mechanists. (Dennett 1979, 61)

Dennett has a ready answer to this objection. He writes:

> But … the mechanism requirement of AI is not an additional constraint of any moment, for if psychology is possible at all, and if Church’s thesis is true, the constraint of mechanism is no more severe than the constraint against begging the question in psychology, and who would wish to evade that? (Dennett 1979, 61)



Structure idea: Put the dualism parts (lucas-penrose, Gödel's disjunction) after these.


