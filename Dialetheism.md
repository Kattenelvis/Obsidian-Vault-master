
Law of non-contradiction: There does not exist statement $A$ such that $A\wedge\neg A$. 
Modally strong version: $\square\neg (A\wedge\neg A)$. 

![[Pasted image 20230726230255.png]]

\<Idea>
Argument for trivialism:
(1) True contradictions exist (Dialetheism)
(2) If a true contradiction exist, then all propositions are true (the explosion principle)
(3) All propositions are true (Modus Ponens, 1, 2)
<Idea/>

![[Pasted image 20230726230319.png]]

![[Pasted image 20230726230432.png]]

![[Pasted image 20230726230754.png]]
2 and 3 seem to be very similar though
![[Pasted image 20230726231308.png]]

![[Pasted image 20230726231406.png]]
They probably mean that the deflationary one is only semantical, unless I'm missunderstanding the correspondence view. 

![[Pasted image 20230726232844.png]]
"**dialetheism is itself a dialetheia**"

![[Pasted image 20230726233704.png]]
Belnap moment


"We find St. Pier Damiani getting close to dialetheism in the _De divina omnipotentia_, by blaming St. Girolamus for having claimed that God cannot overturn the past and twist what happened into something that didn’t happen. Since God lives an eternal present, denying Him power over the past equates to denying Him power over current and future events, which is blasphemous. So God must have the power of making what is done undone."
Idea: If Pierces law holds (all past events are necessary, $P_tp\rightarrow\square_t p$ at time $t$


Ambiguity, not actual contradiction:
![[Pasted image 20230727120316.png]]

## Paradoxes of Self-reference

"Probably the master argument used by modern dialetheists invokes the logical [paradoxes of self-reference](https://plato.stanford.edu/entries/self-reference/). It is customary to distinguish between two families of such paradoxes: semantic and set-theoretic. The former family typically involves such concepts as _truth_, _denotation_, _definability_, etc; the latter, such notions as _membership_, _cardinality_, etc. After Gödel’s and Tarski’s well known formal procedures to obtain non-contextual self-reference in formalized languages, it is difficult to draw a sharp line between the two families, among other things, because of the fact that Tarskian semantics is itself framed in set-theoretic terms. Nevertheless, the distinction is commonly accepted within the relevant literature."

"[Russell’s paradox](https://plato.stanford.edu/entries/russell-paradox/) is the most famous of the set-theoretic paradoxes; it arises when one considers the set of all non self-membered sets, the _Russell set_. [Cantor’s paradox](https://plato.stanford.edu/entries/settheory-early/) arises in connection with the universal set. The most famous of the semantic paradoxes is the [Liar paradox](https://plato.stanford.edu/entries/liar-paradox/). Although cases for the existence of dialetheias can be made from almost any paradox of self-reference, we will focus only on the Liar, given that it is the most easily understandable and its exposition requires no particular technicalities."

![[Pasted image 20230727131122.png]]
Idea: And also Yablo's Paradox

"Aattacking the paradoxes has been something of a _leitmotiv_ of modern logic. And one thing that appears to have come out of this is how resilient the paradoxes are: attempts to solve them often simply succeed in relocating the paradoxes elsewhere, as so called ‘strengthened’ forms of the arguments show."

"A radical solution, which never won big consensus but has been revitalised in recent times (Pleitz 2018), has it that there just cannot be meaningful self-rererential sentences. Various works (notably Martin 1967, van Fraassen 1968, Kripke 1975, Field 2008) have proposed to solve the Liar paradox by dismissing Bivalence, whereby some sentences are neither true nor false, and the Liar is one such truth value ‘gap’. Truth value gaps, and the inclusion of the Liar among them, are differently motivated in the various approaches. But the common core thought is the following: even though the Liar is a sentence such that, if it were true, it would be false, and _vice versa_, no explicit contradiction according to which it is both true and false need follow. We can avoid the contradiction by rejecting the idea that truth and falsity are the only two options for a sentence: the Liar is neither. For a comparative survey of the two kinds of approach, see Beall and Ripley 2018."

Idea: Self-referentiality is meaningless, meaningless iff truth value gap, the liar statement has a truth value gap, no contradiction follows from the liar statement being a truth value gap, crisis averted. 

"These approaches face difficulties with the so-called ‘strengthened’ Liars—sentences such as the following:"

"(3): (3) is not true."

"(4): (4) is false or neither true nor false."

## 🙀

\<idea>
What if one were to generalise liar-like statements?

They could look like this, where $p$ refers to itself, $T$ is the truth predicate, $F$ is falsity, $G$ is gap, $U$ is glut (more can be added):
$p\equiv_{def}Fp\vee\neg Gp$
which formalises (4)
This might not work though due to problems with truth-predicates, look into [[Tarski]] [[Semantic theory of truth]] [[Tarski's Paradox]]

<idea/>

"According to Priest the strengthened Liars show that a single feature of the semantic paradox underlies its different formulations. The totality of sentences is divided into two subsets: the true ones, and their ‘bona fide complement’—call it the _Rest_. Now the essence of the liar is “a particular twisted construction which forces a sentence, if it is in the bona fide truths, to be in the Rest (too); conversely, if it is in the Rest, it is in the bona fide truths” (Priest 1987, p. 23)."

This reminds me alot of the Nelson-Grayling paradox!

And adding more truth values doens't work as a consequence
""(5): (5) is false, or neither true nor false, or the fourth thing.""

"See Kirkham 1992, pp. 293–4. These strengthened liars are also called revenge liars, and the general phenomenon we have just witnessed has become known as _revenge_; see Beall 2007, e.g. the introduction, and Cook 2007, among other essays."

TODO: Figure out what this next section means
![[Pasted image 20230727154229.png]]


"Tarski, in short, identified the cause of the semantic paradoxes to be _semantic closure_—the fact that natural languages such as English satisfy the T-schema. Tarski took this to mean that there can be no consistent formalization of a semantically complete language, only a approximation thereof stratified into metalanguages. Dialetheists agree, but draw the conclusion in the other direction: the appropriate formalization of a language such as ours, because it is semantically closed and is not hierarchically stratified, will be inconsistent (Priest 1987, ch.1, Beall 2009, ch.1)."

"These two features—a claimed immunity to revenge/strengthened liars, and dispensing with the object-language/metalanguage distinction—are argued to give dialetheism about the paradoxes of self-reference some of its major appeal."

Idea: How would dialetheism solve Yablo's Paradox

### Set theoretic paradoxes

"In the larger family of paradoxes of self-reference beyond the semantic, dialetheism affords a treatment of the set-theoretic paradoxes. These paradoxes arise in set theories based on an unrestricted ‘comprehension schema’ for sets: for any condition or property, including paradoxical ones like non-self-membership, there exists a corresponding set. In particular, inconsistent sets like Russell’s are admitted; analogously to the Liar, the Russell set is and is not a member of itself. As with the truth schema, the set comprehension principle seems very natural and intuitive, and such contradictions do not give rise to triviality due to the paraconsistent logic underlying the formal theories. Though the issue is too technical to be addressed here, and more appropriately dealt with in the entries on [paraconsistent logic](https://plato.stanford.edu/entries/logic-paraconsistent/) and [inconsistent mathematics](https://plato.stanford.edu/entries/mathematics-inconsistent/), the reader can consult Routley 1979, Brady 1989, for inconsistent set theories, and Weber 2012. See also Mortensen 1995. For different approaches to dialetheic set theory, see Restall 1992 and Ripley 2015b."

"Since dialetheism appears to resolve both the semantic and set theoretic paradoxes at once and in the same sort of way (namely, accept the contradictory outcomes as true), this has been presented as another major strong point for dialetheism. Priest argues that the paradoxes share an underlying structure (which he calls the Inclosure Schema in Priest 2002). This is used in tandem with what Priest dubs the _principle of uniform solution_ (“same kind of paradox, same kind of solution”) to urge that, since all the set theoretic and semantic paradoxes are of a kind, then dialetheism presents a uniquely unified solution. For a detailed pursuit of a dialetheic response to the paradoxes in general, see Weber 2021."

Turns out this nice, uniform solution does not work because Curry's Paradox is different! 

"A point of dispute about the dialetheic approach to the paradoxes of self-reference concerns the [Curry paradox](https://plato.stanford.edu/entries/curry-paradox/). This is produced by a self-referential sentence claiming ‘If I am true, then ⊥’, where ⊥ is a constant (what logicians usually call the _falsum_) which is or entails something that is also dialetheically unacceptable, say ⊥= ‘Everything is true’, the incoherent trivialist claim. _Prima facie_, this does not involve negation, nor a falsity predicate. However, many logicians think that Curry’s paradox is very similar to the Liar, and therefore by the principle of uniform solution that it should be handled in the same way. A dialetheist, though, cannot simply accept that the Curry sentence is both true and false, because if it is true then ⊥ follows. Dialetheists need a different treatment of Curry."
![[Pasted image 20230727174817.png]]

Other reasons to accept dialetheism:
"(1) _Transition states_: when I exit the room, I am inside the room at one time, and outside of it at another. Given the continuity of motion, there must be a precise instant in time, call it t�, at which I leave the room. Am I inside the room or outside at time t�? Four answers are available: (a) I am inside; (b) I am outside; (c) I am both; and (d) I am neither. There is a strong intuition that (a) and (b) are ruled out by symmetry considerations: choosing either would be completely arbitrary. (This intuition is not at all unique to dialetheists: see the article on [boundaries](https://plato.stanford.edu/entries/boundary/) in general.) As for (d): if I am neither inside not outside the room, then I am not inside and not-not inside; therefore, I am either inside and not inside (option (c)), or not inside and not-not inside (which follows from option (d)); in both cases, a dialetheic situation. Or so it has been argued. For a description of inconsistent boundaries using formal mereology, see Weber and Cotnoir 2015."

"(2) Some of _Zeno’s paradoxes_ concerning a particular—though, perhaps, the most basic—kind of transition, that is, _local motion_: a moving arrow is both where it is, and where it is not. In any given instant, argues Zeno, it cannot move to where it is, since it is already there, and it cannot move to somewhere else, because there isn’t time for it to get there. The orthodox way out of the paradoxical situation, as formulated, e.g., by Russell 1903, has it that motion is the mere occupation of different places at different times. But one could argue that this is denial of the phenomenon itself, that is, of the actuality of motion: Russell’s solution entails that motion is not an _intrinsic_ state of the (allegedly) moving thing, for, at each instant, the arrow is not moving at all. Can a going-somewhere be composed by an (even continuum-sized) infinity of going-nowheres? An alternative, dialetheic account of motion, which takes at face value the aforementioned Hegelian idea that “Something moves, not because at one moment it is here and another there, but because at one and the same moment it is here and not here, because in this ‘here’, it at once is and is not”, is exposed in Priest 1987, Ch. 12."


## Objections

Argument by explosion


Argument by Exclusion:
"A version of the argument from exclusion against dialetheism found, for instance, in McTaggart 1922 (see Berto 2006, 2012) is as follows. A sentence is meaningful only if it rules something out. But if the LNC fails, A� does not rule out ¬A¬�, or, _a fortiori_, anything else. Hence meaningful language presupposes the LNC."



Argument by Negation:
Classical negation: $\neg A$ is true iff $A$ is not true
The Dialetheist response is that it begs the question, and instead define negation to be:
$\neg A$ is true iff $A$ is false and $\neg A$ is false iff $A$ is true

"A variant on the anti-dialetheic argument from negation comes from a Quinean conception of logical vocabulary. It goes as follows. Even granting that there is an operator, say, ∗∗, which behaves as dialetheists claim (namely, such that in particular in some cases A� is true together with ∗A)∗�), it is still perfectly possible to _define_ a negation with all the properties of classical negation; in particular, the property of being explosive. And since classical negation is the standard operator in logic, it is misleading to translate anything non-classical as ‘not’: such a translation risks simply calling ‘negation’ something different. A change in logical vocabulary is a “change of subject”, as the Quinean slogan goes. A version of this objection to dialetheism is due to Slater (1995); see also Restall 1993."

"There are many different and well-worked out logical theories of negation (minimal negation, intuitionistic negation, De Morgan negation, etc.). Insofar as each one of them characterizes its own theoretical object, there is no rivalry between logics."


The problem of the criterion of truth still affects dialetheists as much as non-dialetheists. 