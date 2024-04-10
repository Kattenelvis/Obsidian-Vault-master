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

# Does AI have consciousness? Or even have phenomenal experience/sense data?


## Phenomenal Consciousness



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

## Copy and Death? 

Uploading yourself to the PC, is a copy


## Or slow transition a la Chalmers?

But what if you did it like the Ship of Theseus? The idea here is to slowly replace the biological neurons with the brain with something digital. Some kind of slow, gradual shift from something biological to something technological. 

This idea seems to be the more risk-averse approach, as it assumes fewer number of philosophical assumptions regarding identity continuity and mental combination. So it's the more risk-free option, without too much of a cost (especially compared to the benefits of mind uploading) and the one I would advocate for.

## Metaphysics of consciousness?


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

Identity 

Type identity

Token identity

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

$\neg M\vee \exists p K^*(p)$


It turns out that the philosophical implications of this (though, following benacceraff 1967, requires in addition to the incompleteness theorems additional philosophical premises) can be quite vast. Particularly in the philosophy of mathematics (such as whether or not logicism has been defeated, it's atleast on shakier grounds) aswell as implications regarding platonism and mechanism (the view that the mind is computational). 

### Lucas's Argument

The poor old Turing machine can't calculate it, but we can "see" it as true. True? No cap fr?


"Benacerraf's criticism: the Lucas argument ignores the fact that there is a limit to the descriptive complexity of proofs that a person can understand. There may be a formal system F that captures my reasoning. But its Godel sentence may be too complicated for me to understand, much less verify."

### Penrose's New and Improved Argument 
As presented in Chalmers (19XX), it's like this

(1) 






