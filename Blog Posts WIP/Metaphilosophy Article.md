I would like to say in addition that philosophy is best done in a precise way which analyzes phenomenal consciousness and builds up all concepts with phenomenal concepts as its foundation which is also first philosophy, some kind of Empiricist Foundationalism.
# Propositional Derivational Systems

In its highest generality, philosophy, science and mathematics is about arguments from premises to conclusions. This includes observation sentences. Philosophy, science, mathematics and other similar studies will be named "propositional derivative systems" to indicate their foundation in formal logic. They are similar to Carnaps' linguistic frameworks [Empiricism, Semantics, and Ontology](https://www.ditext.com/carnap/carnap.html).

To formalize this notion we fix a logic $S$ for some language $L$ for which to formalize some argument in. The structure of $L$ can remain vague for now. It can be the languages for propositional logic, a first order logic, second order, modal logic etc. $S$ can also remain vague, whether (under a propositional language) classical, intuitionistic, paraconsistent etc. or however it deals with quantifiers, identity, inference rules, deductive system etc. This allows us to not accidentally include hidden assumptions made in applying formal systems to theories., such as for instance, non-Meinongian quantification in standard first order logic (which could in principle be remedied by adding an existence predicate [Nonexistent Objects (Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/entries/nonexistent-objects/#ConcNoneObje)). 

In general, it will include formulas built up inductively from atomic formulas and grammatical rules, aswell as a set of inference rules. Some theory $T$ in $S$ holds the non-logical axioms of which an argument is formalized as. $T$ would then contain for instance, the axioms of $ZFC$ which are the premises of the conclusions in classical mathematics, $T$ may contain the postulates of quantum mechanics and definitions of observables which allows one to derive observation sentences describing the experiments, $T$ can be Reichenbach's axiomatic formalization of special relativity, $T$ may be the list of axioms in integrated information theory, $T$ can be Spinoza's axioms or $T$ can just be a small simple argument, for instance the cosmological argument or the no miracles argument. 

We also get the logical closure of $T$ as $C(T)$ which include all derivations of $T$ given the inference rules in $S$ that $T$ is in. If $T$ is the empty set, then $C(T)$ will just be the tautologies of the system.

We get a definition (where $=_{df}$ stands for "identical by definition) of philosophy as the set of all such theories:

$Philosophy=_{df} \{T_1,\dots T_n\}$.

In the case of the set being larger than finite $n$, we can have some arbitrary indexing set $I$, for instance if there's some one-to-one mapping from some infinite cardinal to possible theories in all languages and systems:

$Philosophy=_{df} \{T_i\}_{i\in I}$

Carnap distinguishes the analytic and synthetic in a way which is not critiqued by Quine's dogmas. Whenever we have a fixed system in some language, we can take it that the tautologies are the analytic statements and anything derived from an axiom in some theory $T$ is synthetic. 

Notably, by these definitions, mathematics is synthetic. Note that it might seem like we're assuming some kind of Logicism, or perhaps [Hilbert's thesis], the idea that mathematics is reducible to ZFC. But no, all of mathematics don't have to reduce to a single PDS. 

We may distinguish philosophy from other propositional derivational systems such as science and mathematics in that it generally lacks observation statements while also containing synthetic propositions. 

Note also that for scientific theories, this is not to be taken as a restriction on scientific methodology. Fully formalized science is compatible with even Feyarabendian approaches to method restrictions (i.e the empty restriction) so long as theories are formalized. It might then seem to assume the syntactic structure of scientific theories, though with the right ZFC axioms in conjunction with the scientific theory we could easily accommodate the semantic view aswell, and all modern mathematics. Sometimes axiomatizations may require $S=$ second order logic or higher. Natural language is not special, the pragmatic account of scientific theories can likely also be accommodated. 

There is no genuine division between the PDSs that are considered parts of "science", "mathematics" and "philosophy". The content may differ, but they make more of a familiar resemblance then a strict separation. Perhaps we could define mathematical PDSs as those not containing observation sentences, however since observation sentences are simply formal sentences, they are not genuinely different.  

Example for a philosophy themed PDS:

Descartes:

$T=\{ \diamondsuit\neg \exists x Hand(x), \diamondsuit\neg \exists x Hand(x)\to \neg K(\exists x Hand(x)) \}$

$\{\neg K(\exists x Hand(x))\}\in C(T)$ (By modus Ponens)

Another theory in the same language and formal system (which in this case is a Moorean shift):

$T'=\{ K(\exists x Hand(x)), \diamondsuit\neg \exists x Hand(x)\to \neg K(\exists x Hand(x)) \}$

$\{\neg \diamondsuit\neg \exists x Hand(x))\}\in C(T)$ (By modus tollens)

One could apply something like [Sneed's project], We can define a natural history of certain propositional derivational systems as the adding or negating propositions in $T$. A full exploration of how this can be applied will not be covered here. 

Just how many notions this can PDS's fall under? Literature may also fall under it, though as an induction schema as we translate the piece of literature into a theory $T$. Art in general too, as we can simply formalize the experience of the art into formal phenomenology. Application areas are likely limited, though could be used to find inconsistencies in worldbuilding (however for sufficiently long novels this becomes untenable due to the exponential time complexity of derivational algorithms that check every consequence, not to mention possible incompleteness if the novel can derive sufficient arithmetic). It's worth noting that this may not be useful, even if it possible to do. But for my project it suffices that it's in principle possible, not whether it's useful for applications. 

PDS may be applicable to a kind of formalized Hermeneutics, where over time a finished formalism is done:
Adding propositions $T' = T\cup \{p\}$ 
Removing contradictions: $T' = T / \{p\} \cup \{\neg p\}$
Etc.

It's worth noting that I'm not doing a rational reconstruction, or faithful reconstruction, of what mathematicians, scientists or philosophers actually do, for it is unimportant and those without proper foundations should be pointed out as having none. This is not sociology. I do not think that it's important that there just so happen to be humans who just so happen to be mathematicians, philosophers or scientists who just so happen to do things which also contradicts the philosophy presented in this article. Regarding anthropocentric reasoning, it might not have been humans doing philosophy. Humans are just a mere contingency, a tiny speck in the space of possible minds. 

Some may wonder if there is there an explanation for why natural language is used in philosophy at all? NP-hardness makes searching the space of possibly philosophies extremely time consuming, and has to be efficient by algorithms searching through that space in P-time, which humans seem to be decent at? There's obviously a combinatorial explosion of possible philosophies, and diminishing the search space is efficient and useful. There is an assumption that philosophy is to be done in natural language. I will call this the NL-assumption. I will contend that the NL-assumption is false. 

We can define positivism as the view that all propositional derivation systems are mathematical or scientific, with no extra categories. But how could philosophy differ if it does? As Machery says:

> For much of the history of philosophy, philosophers could not have imagined their philosophizing as separate from not only mathematics, but also the empirical sciences.

- Machery Philosophy within its proper bounds

This analysis of concepts could be what philosophy differs from science and mathematics. Conceptual analysis is done withing T's which would include intuition statements (which would probably be similar to observation statements in science). There may be no special conceptual analysis that makes Philosophy a distinct propositional derivational system. 
# Concepts

Conceptual analysis is a possible hypothesis on what makes philosophy different from other PDS. How can we characterize concepts, and is it actually different from science?

**Conceptual analysis**: Conceptual analysis breaks down **concepts** into (perhaps multiple) other **concepts**. Examples include knowledge as justified true belief, free will as the ability to do otherwise, or supervenience as no x change without y change. As part of a formal theory we may for instance include:

$Kp \leftrightarrow (Jp\wedge Bp\wedge p)$
$Willed(x)\rightarrow\diamondsuit Willed(\neg x)$
etc.

The idea is to find the necessary and sufficient conditions for a concept to apply, the idea is then to find counter-examples until one has a concept which covers all instances and leaves no counter-examples. This is known as the **Method of cases**: **Concepts** are applied to **thought experiments**, or **cases**, of which **intuitions** are elicited and informs a revision of **concepts**. According to some defenders of the method of cases. this works because we are competent speakers of the language the concept is in. 

Williamsons formalization of conceptual analysis applying method of cases applying alethic modal logic in the following way for the knowledge concept, with the possibility of Gettier cases:

$\square (Kp \leftrightarrow JBTp)$
$\diamondsuit (\neg Kp\wedge JBTp)$

The problematic intuition of the case in the possible world where the JBT is not K, i.e Gettier worlds. As such, the PDS generated from both statement at once must be contradictory. One can give up one of the statements, according to the method of cases, one always gives up the general rule. But there is an alternative.

**Reflective Equilibrium**: Iterated applications of method of cases eventually yield reflective equilibrium where the general concept definitions apply to all cases. Instead of just going by intuitions, we can sometimes reject intuitions, if they're for instance, not strong enough. The long term goal according to some is to achieve a  Equilibrium, whereby one has applied conceptual analysis many times, thought through many thought experiments until all universal laws match all intuition on all cases. [[Method of Cases and Reflective Equilibrium]]

## Experimental philosophy

The idea is to test intuitions on lay people. Are horribly dependent on irrational factors such as someone's sex, ethnicity or age. 

Expertise defense states that there exists some special skill and/or talent philosophers have which has allowed them more fine-tuned intuitions which are actually true, just like fine-calibrating a scientific instrument to get the best scientific data. 

Turns out most lay-people intuitions still apply to experts [Source]. Expert philosophers are bad at modal reasoning, if anything, mathematicians are the modal experts [Source]. Extrovert lay people are just as more likely to believe in free will than introverts as is the case for professional philosophers. 

## Conceptual Engineering, Method of Cases 2.0 and Familiar Resemblance

I think the earlier mentioned methods is "flawed", even though it is perfectly compatible as a PDS. Instead I will defend explicative definitions given our goals, in our theories $T$.

On a side-note, and potentially a fairly controversial one, is my view of gender. At some moments if asked what a gender is, or what a woman is or what a man is, I would try to find the optimal definition given some utilitarian calculus, which would at a minimum include transwomen as women and transmen as men as affirming their gender identity optimizes happiness related factors such as decreased suicide risk, depression symptoms and anxiety symptoms in transgender individuals. But an argument I received back was that this is a fallacy, namely the moralistic fallacy. However, it is clear to me now that since gender is a constructed concept, we can construct them however we like, including optimizing the state of the world given some decision theoretic or moral system. We can do the same for race and mental illnesses. 

One could explicate all concepts to be reducible to sense-experience, or as long descriptions of sense data, as this serves our goal of being robust against skeptical problems. 

I also think that typically, the main reason there's disagreement is philosophy is because different agents hold slightly different unclarified folk-concepts. It's typically when concepts are clarified, observation sentences based on those concepts are derived and checked or falsified, as they are in the sciences, that agreement is reached. The conceptual constructions are standardized between individuals. I think the same does happen in philosophy a lot more often than people give credit for.

# Skeptical problems and Phenomenalism

Philosophy differs in its focus on skeptical problems. Scientific and mathematical theories might in principle include assumptions about knowledge, or atleast some kind of constructed concept that's similar to knowledge. Is this what separate philosophical PDS from other PDS? 

We haven't constructed the concept "knowledge" yet. To figure out optimal conceptual constructions, it's worth setting a goal first. The goal I posit here is to build robustness against skepticism. Our goal is not to match our intuitive folk concept of "Knowledge" nor is it about some kind of reflective equilibrium. The goal will be about clarity with regards to the limits of knowledge that phenomenal experience can possible give us. I believe it is uncontroversial that what I argue will be the best approach for that goal. I will by no means make an exhaustive account of all skeptical problems in this article, but I will give an idea for how a general project with Carnapian concepts could handle skepticism. Carnap himself, atleast during his phenomenalist era in the Aufbau, preferred the phenomenalist approach for how it deals with skepticism. 

The cartesian demon problem, which posits that we could possible be fooled by an evil demon into having experiences and belief formations, presupposes modal knowledge of possibilities. Let $p$ be a true proposition about the actual world.

$K_{you}\diamondsuit (p \land Fool(demon, you, \neg p))$

Keep in mind, so does the "common sense" i.e "the possibility of the existence of the external world basically as our folk theories posit it is" too. 

$K_{you}\diamondsuit (p\land K_{you}p)$

This is a kind of local skepticism against modal epistemology as Van Inwagen's critique of modal epistemology in that there could be hidden contradictions and results from experimental philosophy which shows that philosophers are bad at modality [source]. But it also leads to a kind of global skepticism, as it would seem there is a lack of knowledge states over distinguishing possible worlds. As the most common type of semantic for epistemic logic is about distinguishability of possible worlds, we will take that to be the Knowledge concept.

There is a way to save distinguishability: we can state that worlds are distinguishable given different phenomenal experiences. I know that I am experiencing the concept I construct as "Blue" given my color experiences. Since I cannot assume the possibility of external worlds, or a community of speakers, or public objects, or surfaces painted blue, or light rays, or preceptory systems in the brain, or anything else as such, I cannot take any of them for granted. It is a true foundation in phenomenal experience. Even if we hold beliefs that change the experience, via some kind of myth-of-the-given situation, or the rabbitduck case etc., there's still an experience. I take the approach that the problem of beginning [source] can be solved this way. 

We can start specifying a rudimentary formal structure for phenomenal experience, such as regions R in visual space V. We can specify visual pixels, containing x-y locations, brightness, hue and saturation values, and put then into a vision set of all possible visual pixels. $V=\{\{x,y,h,b,s\} : x,y,h,b,s\in\mathbb{N}\}$, subsets of which form visual spaces, of which one member is one's experience. For a more detailed description on this, including auditory and other systems, check out [earlier posts].

Memories and change in experiences promote a set of experiences over time $E_1,...E_n$ and as a new one is inputted, more possible worlds are distinguished. For example, if I have the experience of red to the left and yellow to the right as the only two visual points, with no other modality on (no sound, no smell etc.). While it is distinguishable from worlds where I for instance see blue on the left, it is indistinguishable from worlds in which my experience at the next time step is yellow on the left vs ones that are pink on the left and so on. We can create a whole updating possible world semantics for possible minds. This is a formal project that I'm just outlining here but might do in the future.

A more general such semantics which has already been developed is dynamic semantics. Dynamics semantics does this on general possible worlds. This is preferable, given that we might want to model hypothesizes of things which are not phenomenal experience existing independently of phenomenal experience. As such, the set of indistinguishable worlds has become huge, and this is the same as underdetermination of hypothesizes. Experiences and memories of experiences can always be accommodated by a very large number of possible worlds, such as the [pea soup hypothesis] which is an infinite number of indistinguishable possible worlds. Imagine that at any radius $r$, everything outside of that is just pea soup which just so happen to look like the external world. One can see that any set of experiences and memories of experiences holds this entire set of worlds as indistinguishable. We accept this result, and take no steps to remove it or resolve it with ad-hoc values like "simplicity" or similar options. 

However, from a decision theoretic standpoint, it can be good to establish a probability distribution over possible worlds, even if they are technically indistinguishable. Any rational individual must hold their credence's up to the laws of probability theory, lest be subject to [dutch books], which are guaranteed loosing bets. This includes the diachronic Dutch books, which state that rational agents updates their beliefs using Bayes's formula. One good weighing of one's priors might be based on simplicity, such as minimized ontology of the hypothesis, for instance as adding one more existing thing decreases the probability of being correct. AIXI works on the basis that its prior probabilities are distributed over the one's with minimum Kolmogorov complexity, i.e the shortest computer program that can compute all the facts about that world (but that only works for computable possible worlds).  

Given our construction of knowledge as distinguishability of worlds, justification is difficult to asses. As such this view doesn't get subject to any kind of Angrippan trilemma. The problem of the criterion too, as there's no need to "justify" the conceptual construction of knowledge this way, in any kind of substantive metaphysical universal "knowledge". But rather just as a means to the end of respecting external world skepticism.
## The case for phenomenal intentionality via cognitive phenomenology

To pursue the goal of constructing a PDS which admits to the goal of robustness against skepticism, we will advocate to include an account of [Phenomenal Intentionality (Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/entries/phenomenal-intentionality/) that is phenomenal and narrow. Some PDS's might benefit from both, which is where 2D semantics come in. We could establish such, but for the goal of robustness against skepticism, it is better to pick 

Since we've already discussed that intuitions and method of cases doesn't work, we can exclude arguments such as twin earth or Gödel-Schmitt cases immediately. We can still use them as intuition pumps, and explain narrow content. In the twin earth thought experiment, twin earth has something like water, but is a posteriori identical to XYZ instead of water. We presume that H2O $\neq$ XYZ. The narrow, phenomenal content of water is the color of water, the way it sounds, feels and so on. The idea is that Twin Earth Water is by narrow, phenomenal content identical to Earth Water, but it's "intuitively false" that they would have identical content. I reject the intuition. 

An argument for a particular kind of narrow content, namely phenomenal content, is to use cognitive phenomenology. 

The three main views are the following [varieties of consciousness]: 

Primitivism: Cognitive phenomenology is just another kind of experience, just like vision, sight, etc. and cannot be reduced to other types of experiences nor eliminated as linguistic confusion.

Reductionism: Cognitive phenomenology can be reduced to other experiences, such as vision and audio. 

Eliminativism: Cognitive Phenomenology doesn't exist, and is merely linguistic confusion to use it that way.

I will argue for reductionism. We begin by taking a look at how primitivism could be modelled with formal phenomenology. We take it that the set of experiential points $E = \{V, A, T,...\}$ for visual space $V$ auditory space $A$ and thought space $T$. I will argue that empirically, $T$ is most likely reducible to $V$ and $A$. The main argument will be appeal to mental images and inner thoughts.  people with aphantasia have predisposition to write it down, hence an experience. As such we make the following conjecture:

There exists $a\subset A$ and $v\subset V$, such that $T=\{a,v\}$

The thought of a green patch and envisioning green patch are not different, it has been a long standing conceptual confusion that they're different. 

As Strawson puts it:
> To deny this [cognitive phenomenology], one must hold that the total lifelong character of our lived experience—everything that life is to us experientially—consists entirely of bare or pure sensation or feeling of one kind or another. It must, for example, be false to say that anguish at someone’s death includes _conscious comprehending believing entertaining_ of the proposition that he is dead. (Strawson 2011a: 295, italics in original)

Kriegel writes:

> For my part, I am persuaded of the existence of cognitive experience […] most vividly by something like everyday experiential overwhelm: it simply seems that my inner life is much more interesting to me than it would be if my conscious experience consisted merely in perceptual experiences. (Kriegel 2011a: 50)

An objection may be the "Ah-Hah!" Experience that some have reported[source]. However I think that is more or less the same, but perhaps with some sense of pleasure. As such we introduce pleasure space $P$ and argue for the following conjecture:

There exists $a\subset A$, $v\subset V$ and $p\subset P$ , such that $Ahhah! = \{v,a,p\}$

The important part of the argument from cognitive phenomenology is that it might imply that mental content is nothing above and beyond their phenomenal content (inner voices, mental imagery). We can engineer the concept of mental content so as to exclude the many-to-one mappings and instead posit a one-to-one mapping, or even identity relation, between phenomenal content and mental content. 

$T_1 = M_1, T_2=M_2, ..., T_n=M_n$

We can now go back to intuitions from our previous discussion, now that we can formalize what they are. 

Something very many people are wrong about, especially rationalists, is what thoughts are. So much confusion has arisen from the belief that thoughts are different from other experiences. This can also be applied to a priori justification, as is done here [SEP article section etc]. A "thought" is just an inner voice or mental imagery and just another perception, there's no big difference between it. An "inner" voice is just as much of a phenomenal experience as an "outer" voice, as said earlier. As such the distinction between a priori justification and a posteriori justification disappears, leaving only a posteriori justification. Since no proposition is justified a priori, then no proposition is justified synthetic a priori, and since rationalism is defined here as the existence of a proposition that is justified synthetic a priori, then rationalism is false. We assume that rationalism being false implies empiricism is true, hence empiricism is true. 

It has also been purported to have different justificatory power, but by the phenomenal egalitarian principle, it would not be the case. They may be different justificatory for different theories but that's it. There are reasons to believe that there's no true aphantasiac, they usually just lack one or the other. Why rely on the phenomenal experience of "intuition" rather than the phenomenal experiences of "regions of blue"? 

We will come further with philosophy if we recognize thought as indistinct from sight and hearing. 

## Innateness of Concepts, conceptual reduction

In the quest of robustness against skepticism I will propose a project of reducing all concepts to a small set of concepts about phenomenal consciousness. Other concepts may exist, but we're not interested in them. As Carnap states:

"In the case of many words, specifically in the case of the overwhelming majority of scientific words, it is possible to specify their meaning by reduction to other words ("constitution," definition). E.g., "'arthropodes' are animals with segmented bodies and jointed legs." .... In this way every word of the language is reduced to other words and finally to the words which occur in the so-called "observation sentences" or "protocol sentences."

Or John Locke
> I think I need not go any farther in the Analysis of that complex Idea, we call a Lye: What I have said is enough to shew, that it is made up of simple Ideas: And it could not but be an offensive tediousness to my Reader, to trouble him with a more minute enumeration of every particular simple Idea, that goes into this complex one; which, from what has been said, he cannot but be able to make out to himself.

Carnap suspected that all such concepts might be reducible all the way to a similarity relation $R$ between some sense data $s_1$ and $s_2$. For instance, a rectangle at coordinates $[x_1,x_2]$,$[y_1,y_2]$ with the same color at time $t$ and at time $t+1$ would count as similar to eachother. The reduction also included logical concepts as primitives, such as the typical propositional logic connectives $\neg,\lor,\land,\to$. In the most extreme case we might even propose a reduction of logical concepts? A sense data for instance: Either region A is blue or it is not the case that region A is blue. By forbidding the empty mind, we can always ensure that such an region A exists. In finitist set theory, which [I model phenomenal experience] in, there is no empty set, so it holds there.

While such an extreme kind of reduction might not be possible for all concepts ever, we're interested in what concepts can be built up from such basic fundament.  (though I'd have a hard time seeing how anything could not be reduced to experience). 

Example of conceptual reduction:

Time in the GIF of changing blue to red and back

CHANGE = MEMORY OF X CURRENTLY Y

MEMORY is an imaginative process [source], and hence experiential. Mental image of blue, or atleast some semantic information, about past state of the pixel. 

One example in one paper was LIE into 4 other concepts find it and try to do it on the other 4

> Unfortunately, it is all but obvious how to complete the analysis, breaking the concept down into simple, sensory components. As several authors have observed (Armstrong et. al. 1983 [chapter 10], Fodor 1981), it isn't even clear that definitions such as the one suggested by Locke bring us any closer to the level of sensory concepts than the concept under analysis. Are the concepts SPEAKER, AFFIRMATION, NEGATION, or STANDING FOR really any closer to the sensory level than the concept LIE?

Play a game with people: Ask them to give you a concept and see if you can reduce it. Let's play the game with the concept LIE!
$$Sp(a)\leftrightarrow \diamondsuit\exists p Ut(a,p)$$Where $Ut$ is the "Utters" predicate. Utterance is perception of sound in a certain way, which reduces to sounds and thoughts and we've shown how thoughts are reducible to audio and sounds. 

While we could play the game of attempting to find the definition for it which eventually reduces down to phenomenal experience, we can instead focus on building them bottom-up. This may mean we leave out some everyday concepts and that the new concepts don't align up with folk concepts. We won't necessary get anywhere otherwise, for people's folk concepts differs, hence the reduction to experience (not to mention the possibility of inverse qualia, meaning that descriptions of experience could differ in ways that cannot be properly explicated by individual experiences). For instance, in the reduction of speaker in my example above, someone you reading this may have alternative intuitions over whether this is the case, and perhaps come up with some "counter-intuition" to it. I argue that this is fine, you have $Sp_2(a)$, a different speaker concept which can be reduced to concepts about phenomenal experience like the rest. 

**If you come up with any concept you think can't be reduced, comment it below and I'll try to reduce it the best I can.**

Note that what I've said above is not about how we learn concepts psychologically. A being capable of developing concepts and rational reasoning may need to be bootstrapped with some concepts to develop new one, some critical mass of concepts needed for human-level concept understand and concept making. We could take Fodor's view to be the case that there are innate concepts, in the sense of "biological bootstrapping". But we can simply build up the concepts from the ground up, after we've learnt about phenomenal experience. We may need Neurath's boat to float, but we can always build a new smaller one from scratch on the side. Chomsky and Fodor can be right in that we may still be bootrapped as cognitive agents with certain concepts to which learn more concepts. But afterwards we can reduce them all to experiences anyways. Including logical concepts.

As an objection to the view, some say science must involve public objects. I will argue that "public objects" in a way robust against skepticism doesn't work, we have to adopt methodological solipsism the way Carnap did. One can experience $E$, form the belief that $E$ applies to concept "Human pointing at a dial which reads 23.4" and conclude that "public object" is somehow reducible to this. But I'm positing that the idea it has to be external is wrong. The best hypothesis is that two human-like consciousnesses $E_1\in E$ and $E_2\in E$, have some subset $O_1\subset E_1$ and $O_2\subset E_2$. 

The possibility of semi-public objects are worth considering. Imagine for instance, three people of which one is colorblind looking at a 3 that the color blind person cannot see. Sometimes paranormal stuff where only some people see them can be considered semi-public, but that might be for other reasons. 

# Ontological Commitment and metametaphysics

Concepts will be constructed grounded in sense-data, just as in Carnap's aufbau. This will make the theory robust against external world skepticism, and makes sure that the account holds no metaphysical commitments other than the existence of phenomenal experience. 

But how should we characterize ontological commitment? Can theories $T$ as part of PDS's may include any quantification realm, but don't commit to existence of its domain or ontology of objects?

If we're talking about the subset of PDS's that are in the language of first order logic (and others with quantification over objects in some way), the models hold the objects. But any $T$ will be satisfied by an arbitrary set of models using for instance the push-through construction [source]. We can always swap around the objects, constants and so on and keeping the theory satisfied with appropriate changes to predicates etc. Finding some arbitrary subset of "intended" models is arbitrary. Instead proposing a kind of structuralism, where the structures are what's important. Structuralism can thus work for both scientific, mathematical and philosophical PDS's. 

Quine argued against such a view. Quinean commitments on reality as it is, leads to arguments about the existence of mountains. Mereological argument:

$T=\{$Mountains are composites, No composites exist$\}$

So a consequence of this theory in a system which allows modus ponens yields "There are no mountains". 

"To be is to be a value of a quantifier"

I will hence forth reject that any $T$ has privileged access to reality and is the true nature of it. I adopt a Carnapian view that existence just follows trivially from a theory. Let's say we formalize geology axiomatically as $G$ in some formal system. It's likely a consequence of $G$ that mountains exist. Geologists may not use $G$ though, as it may turn out a better theory for their goals is $G'$ which doesn't have that implication

Speculative metaphysics from premises is thus an epistemically inferior way of characterizing philosophy as a PDS, though I can see it plausibly work for that. I really work towards a more critical, guided by the limit of phenomenal experience, in a way some may perhaps could consider (neo)-Kantian metaphysics. 

With a Carnapian view then, I don't have to accept my PDS as the ultimate truth or anything like that. As such, I make no metaphysical commitments (atleast, I don't think I do). 

We can also look into scientific reductionism, such as Hempel-Schaffer reduction. If we have a scientific theory $T_b$ and a scientific theory $T_t$, we can say that if $T_b\vdash T_t$  then $T_b$ reduces $T_t$. The idea of such a reduction is that the theorems of $T_t$ is derivable using the inference rules in $\vdash$ from the bottom theory $T_b$. Keeping in mind the need for all theories to derive observation sentences to be confirmable or disconfirmable. Eventually one could form a long chain of theories with a bottom one, of which the ontology of the most fundamental theory $T_{fund}$ can be the ontology one commits to (for instance, the strings in string theory). This possibility assumes quite a few things of course, such as that theories are reducible this way and not "emergent" (emergence with the definition of supervenience without reduction) aswell as mereological nihilism. 
# Language

Meta level on the way this entire article has been written in a language with what seems to be assumptions. I have been making assumptions regarding the formalizability of philosophy. I will hereby state that there are two broad claims:

1. The Formal Language claim
2. Natural language assumption.

These can both be in turn have different versions such as possibilism i.e philosophy can in principle be formalized, or normative claim that it ought to be formalized and even a necessity claim that philosophy necessarily involves formalism (and that what is commonly called philosophy done before formal logic is not philosophy, or only a proto philosophy). I will argue for the necessity claim. 

Here's a great quote from Kriegel:
> let it suffice to say that Rudolf Carnap’s Der logische Aufbau der Welt is like a breath of fresh air and that it is a paradigm case example of what philosophy should be like in the future. Indeed, this is my prediction: 80 years from now no philosopher will get away with doing philosophy without logical and mathematical means; it would be like doing modern theoretical physics without mathematics. There will be no trivial arguments, no hidden assumptions, no talking at cross purposes. Philosophy will be done in the way in which this young German does it, for it is the only way in which philosophy will make progress. I hear you say But there is no progress in philosophy—if only Carnap’s book had come out 80 years earlier…'

With the rise of Ideal language philosophy and Ordinary Language philosophy, no more substantive claims. Substantive/Naturalized philosophy can make comeback. Philosophy is more than no substantial claims. Ideal language vs Ordinary article here, all of philosophy would then be analytic. As such I think of a combination of ideal and substantive philosophy, and a rejection of ordinary language. 

A potential problem with talking about phenomenal experiences is that it may fall under the private language argument. I will argue that the argument not just fails to establish languages used for theories which are robust to skepticism, but also that public languages are the actually incoherent pseudo-languages which are at best supervenient on private languages. 

Chomsky's idea is a distinction of I-language and E-language. The I-language is the intentional, internal or private language, E-languages is the extentional, external or public language. 

Skeptical worries of the robustly skeptical theory T being inconsistent can be solved in two ways: Either we prove the consistency within the system, we accept paraconsistency. We could also simply accept that an inconsistency is possible, which is what most mathematicians have done with ZFC.

![[Frame 4.png]]


We can almost certainty say natural language is inconsistent. We can prove the consistency of formal systems with sufficient arithmetic only from stronger systems which retain sufficient arithmetic. What remains are a set of small languages which can define their own truth predicate and prove their own consistency, such as Pressburger Arithmetic.  

To truly stave it off, then, we may have to look into formalizing our philosophical system within a system which cannot express sufficient arithmetic, which can be done in many ways.

A possible objection is that a philosophical theory $T$ would include some kind of metaphysics, some kind of description of the world. Hence cannot predict that there would exist systems such as Peano Arithmetic. However Max Tegmark argues against this view:

> "Even a world corresponding to a Gödel-complete mathematical structure could in could in principle contain observers capable of thinking about Gödel-incomplete mathematics, just as [finite-state digital computers](https://en.wikipedia.org/wiki/Turing_machine "Turing machine") can prove certain theorems about Gödel-incomplete formal systems like [Peano arithmetic](https://en.wikipedia.org/wiki/Peano_arithmetic "Peano arithmetic")."

We may thus very well be able to formulate a philosophical PDS such that it lacks the arithmetic needed for those theorems to apply, thus allowing it to only talk about itself without any meta-philosophy. Thus, all that I have said is largely redundant, which in some way reminds me of the ending of Tractatus where you climb the ladder just to kick it down.

PDS's can thus be completely self-contained, without reference to the larger project. Those languages can be built up from the inside, without a meta language. 

But don't I risk trivializing the view if anything falls under it? Am I not just saying "Philosophy, science and math are all done within a language?". Yes, that is what I'm saying, and languages are formalizable. 

The holy grail would be a theory that implies all observation sentences and that can express and prove it's own consistency and completeness. 
# Conclusion
I may have failed to construct certain concepts that I still end up using such as "rational", "me" etc. but I don't have time to write an entire book on every concept and may go on to expand that later. We can simply take it that whenever I'm using an undefined concept, imagine it's constructed in such a way that it makes sense to consider its properties that I give it. 



# Sources

[[Metaphilosophy Constructive Article]]

["Criticizing philosophy is philosophy" is a bad objection to criticism of philosophy (lanceindependent.com)](https://www.lanceindependent.com/p/criticizing-philosophy-is-philosophy)

[Intuition (Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/entries/intuition/)
[Experimental Philosophy (Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/entries/experimental-philosophy/)
[https://plato.stanford.edu/entries/experimental-moral/](https://plato.stanford.edu/search/r?entry=/entries/experimental-moral/&page=1&total_hits=597&pagesize=10&archive=None&rank=1&query=Experimental)
[https://plato.stanford.edu/entries/thought-experiment/](https://plato.stanford.edu/search/r?entry=/entries/thought-experiment/&page=1&total_hits=2145&pagesize=10&archive=None&rank=0&query=Thought%20Experiments)
https://plato.stanford.edu/entries/progress/





# Others






## Common sense Philosophy

Radically relative
Experimental philosophy

(Is PC even comon sense or smth else?)
Phenomenal Conservatism: With the unreliance of intuitions, there's no reason so support our initial beliefs until defeaters show up or anything like that

I think it clicked: Every appearance is justificatory in some way. I have to agree with this. They are all observation sentences. There's no need to privilege different appearances. 

We could be radically wrong
Reid, who supported Common Sense philosophy does also take it that we *could* be radically wrong (fallibilism).


Moore and why the hand shifting argument doesn't work


# Naturalizations

Consciousness Research and AI research is the best bet we have. 

A real case against the rationality of working on most issues in philosophy: AI may be able to do it for us in the future

Science is like philosophy anyways, but with observation sentences as premises. 

IIT vs GWT as the two competing models of consciousness.

But let's not take it too far.


Naturalizations are sometimes eliminative about folk psychological states

Circularity without it?
Yet kinda bad and can be eliminated? Not sure tbh... Ask Youv




# Philosophical progress

Not quite true. But lack of it in some fields is cause for concern? Ehhh I guess lack of progress is only a concern whenever there is no finished consensus view that finishes in the establishment of something.

Add that article here

LLM's for progress?


With our formalisation we can now posit some progress. It's about the addition of systems $T$.  

Yet another object-level debate that's trivial after we've applied conceptual engineering and empirical evidence. There are multiple different notions of progress [source] We find that progress in the sense of adding more texts and publishing more papers that it's uncontroversial. By other metric it's also uncontroversial whether there's progress or not. 



# No meta-philosophy

Only really philosophy of philosophy. It's just a set of object level debates of which is typically conceived to have a lot of importance for many other branches, which is already the case within many branches. As a consequence one cannot be "anti-philosophy" without making atleast one philosophical proposition or argument. 

If philosophy is "valuable" is just an object level proposition that follows trivially from a theory of value or decision theory $T$. 

We thus get philosophical knowledge. Knowing a system $T$. Follows trivially from epistemological theories $T$ what counts as knowledge or not, just like philosophical value.

Likewise, debates about methodologies in for instance, analytic philosophy, continental philosophy and pragmatic philosophy all turn out to be some set of mostly object-level debates. 

Analytic Philosophy $\approx$ {Conceptual Analysis, Method of Cases, Reflective Equilibrium, Conceptual Engineering, Formal Logic, Naturalizations, Experimental Philosophy, ILP, OLP, Phenomenal Conservatism, ...}

Continental Philosophy $\approx$ {Hermeneutics, Dialectics, Material Conditions analysis, Phenomenology, Critical Theory, Deconstruction, ...}

(Neo-)Pragmatic Philosophy $\approx$ {Ironism, Quietism, Fideism, Analyzing Language Games, OLP, ...}

Scholastic Philosophy $\approx$ {Natural Theology, Negative Theology, Revelation, ...}


But the sets are vague, and nothing says debates about the sets are any good to have, as contrary to the methods themselves. While I do think Formal Logic as a method in philosophy is overwhelmingly powerful and good, where I see no reason to support Natural Language based philosophy instead. However for all other methodologies, I am unsure about it (though I suspect many of the pragmatic and continental one's as very bad in some regards). So while I will consider myself analytical for now, I do not think methodology debates on grand-scales such as between analytic, continental and pragmatic are any good. 









# Old epistemology stuff might reuse


With empiricist foundationalism or empiricist foundherentism, there is no knowledge which is based on intuitions, but only in lists of sense-data

Phenomenal Justificatory Egalitarianism: Inspired by Phenomenal Conservativism, it states that we have no reason to take some regions of phenomenal experience as constituting special justification. This includes cognitive phenomenology. 


The issue is the myth of the given, which is remedied with a foundherentist system, developed by Haack and mathematically formalized by Thagard. There is a coherence relation between theoretical propositions, formalized in logical systems (all of which is definitional and explicative, no intuitions are ever used for any of the inference rules)

There are two kinds of justification, S-justification and C-justification, depending on if sense data is justifying a theory or if theories are justifying sense-data. But foundherentism takes a special privileged role to sense data (though tbh I think she doesn't use the term 'sense data' so this might be a mischaracterization) because sense data is what upholds something which would otherwise be fully Coherentism, and thus the typical problems of Coherentism which includes that a coherent set of propositions could just be fictional.

Coherence function on a set of propositions and coherence relations, aswell as 5 optimization algorithms that try to maximize which propositions to put in a set to maximize coherence. Including a formalism of Haacks work









Putnam is  wrong. We have predictive world models of VR games. It can be the same in the world. A tree having properties $P_1,...P_n$ can be true in a virtual world just as well, with the added property of $P_{n+1}=$ "is digital". The causal theory of knowledge is weird anyways, and not what we're constructing anyways. 





Conlangs demonstrate that natural languages are not all they're painted to be, and we'd be so much freer if we used a larger range of possible languages. 



Philosophy is a highly technical branch of STEM. I condemn the rest as semi-philosophy, or semi-formal philosophy. 



Someone [who?] has argued that the English mereologists use is not quite English. I will argue for the Formal Language assumption FL-assumption as true. 





Memory skepticism: If we are FSTs we cannot generate the syntax we want in the Chomsky Hierarchy.



We can formulate probabilistic arguments for Boltzmann brains and the Simulation Hypothesis. However I will argue that this doesn't quite work. Both aforementioned assumes an upper world with the same laws as the experiential one. 

It might be likely that I'm reliving my life as a simulation before. Even with a small probability that I'd do it, the amount of times would still be staggering given the amount of time I can live in the post-singularity.  