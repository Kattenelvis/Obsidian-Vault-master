
[The Problem of Induction (Stanford Encyclopedia of Philosophy/Spring 2023 Edition)](https://plato.stanford.edu/archives/spr2023/entries/induction-problem/)

My own idea of Hume's argument:
1. Cause and effect has to be either justified a priori or a posteriori.
2. A proposition $p$ justified a priori implies it's a necessary truth
3. Propositions regarding cause and effect are contingent.
4. Therefore propositions regarding cause and effect must be justified a posteriori.
5. e.t.c


SEP's version:
"P1.

There are only two kinds of arguments: demonstrative and probable (Hume’s fork).

P2.

Inference _I_ presupposes the Uniformity Principle (UP).

_1st horn:_

P3.

A demonstrative argument establishes a conclusion whose negation is a contradiction.

P4.

The negation of the UP is not a contradiction.

C1.

There is no demonstrative argument for the UP (by P3 and P4).

_2nd horn:_

P5.

Any probable argument for UP presupposes UP.

P6.

An argument for a principle may not presuppose the same principle (Non-circularity).

C2.

There is no probable argument for the UP (by P5 and P6).

_Consequences:_

C3.

There is no argument for the UP (by P1, C1 and C2).

P7.

If there is no argument for the UP, there is no chain of reasoning from the premises to the conclusion of any inference that presupposes the UP.

C4.

There is no chain of reasoning from the premises to the conclusion of inference _I_ (by P2, C3 and P7).

P8.

If there is no chain of reasoning from the premises to the conclusion of inference _I_, the inference is not justified.

C5.

Inference _I_ is not justified (by C4 and P8)."


"There have been different interpretations of what Hume means by “demonstrative” and “probable” arguments. Sometimes “demonstrative” is equated with “deductive”, and probable with “inductive” (e.g., Salmon 1966). Then the first horn of Hume’s dilemma would eliminate the possibility of a deductive argument, and the second would eliminate the possibility of an inductive argument. "

"Premise [P3](https://plato.stanford.edu/archives/spr2023/entries/induction-problem/#P3) could be modified to say that a demonstrative (deductive) argument establishes a conclusion that cannot be false if the premises are true. But then it becomes possible that the supposition that the future resembles the past, which is not a necessary proposition, could be established by a deductive argument from some premises, though not from _a priori_ premises (in contradiction to conclusion [C1](https://plato.stanford.edu/archives/spr2023/entries/induction-problem/#C1))."



## Second horn

"Most arguments of form _X_ that rely on UP have succeeded in the past.

Therefore, most arguments of form _X_ that rely on UP succeed.

But this argument itself depends on the UP, which is the very supposition which we were trying to justify."

"Suppose we adopt the rule _R_ which says that when it is observed that most Fs are Gs, we should infer that most Fs are Gs. Then inference _X_ relies on rule _R_. We want to show that rule _R_ is reliable. We could appeal to the fact that _R_ worked in the past, and so, by an inductive argument, it will also work in the future. Call this argument _S_*:

Most inferences following rule _R_ have been successful

Therefore, most inferences following _R_ are successful.

Since this argument itself uses rule _R_, using it to establish that _R_ is reliable is rule-circular."


"Some authors have then argued that although premise-circularity is vicious, rule-circularity is not (Cleve 1984; Papineau 1992). One reason for thinking rule-circularity is not vicious would be if it is not necessary to know or even justifiably believe that rule _R_ is reliable in order to move to a justified conclusion using the rule. This is a claim made by externalists about justification (Cleve 1984). They say that as long as _R_ is _in fact_ reliable, one can form a justified belief in the conclusion of an argument relying on _R_, as long as one has justified belief in the premises.

If one is not persuaded by the externalist claim, one might attempt to argue that rule circularity is benign in a different fashion. For example, the requirement that a rule be shown to be reliable without any rule-circularity might appear unreasonable when the rule is of a very fundamental nature. As Lange puts it:

> It might be suggested that although a circular argument is ordinarily unable to justify its conclusion, a circular argument is acceptable in the case of justifying a fundamental form of reasoning. After all, there is nowhere more basic to turn, so all that we can reasonably demand of a fundamental form of reasoning is that it endorse itself. (Lange 2011: 56)

Proponents of this point of view point out that even deductive inference cannot be justified deductively. Consider Lewis Carroll’s dialogue between Achilles and the Tortoise (Carroll 1895). Achilles is arguing with a Tortoise who refuses to perform _modus ponens_. The Tortoise accepts the premise that _p_, and the premise that _p_ implies _q_ but he will not accept _q_. How can Achilles convince him? He manages to persuade him to accept another premise, namely “if _p_ and _p_ implies _q_, then _q_”. But the Tortoise is still not prepared to infer to _q_. Achilles goes on adding more premises of the same kind, but to no avail. It appears then that _modus ponens_ cannot be justified to someone who is not already prepared to use that rule.

It might seem odd if premise circularity were vicious, and rule circularity were not, given that there appears to be an easy interchange between rules and premises. After all, a rule can always, as in the Lewis Carroll story, be added as a premise to the argument. But what the Carroll story also appears to indicate is that there is indeed a fundamental difference between being prepared to accept a premise stating a rule (the Tortoise is happy to do this), and being prepared to use that rule (this is what the Tortoise refuses to do)."

Holy shit so 
$(p\wedge (p\rightarrow q))\rightarrow q$
The tortious would claim it's circular to accept $q$ since it requires the modus ponens inference rule!!!
[[Metalogic]]

There is however a problem brewing around the corner. 
"After all, less sane inference rules such as counterinduction can support themselves in a similar fashion. The counterinductive rule is CI:

Most observed As are Bs.

Therefore, it is not the case that most As are Bs.

Consider then the following argument CI*:

Most CI arguments have been unsuccessful

Therefore, it is not the case that most CI arguments are unsuccessful, i.e., many CI arguments are successful.

This argument therefore establishes the reliability of CI in a rule-circular fashion (see Salmon 1963)."

Idea: So long as law of double negation is true/the inference rule is used. 


#### No rules!

[(174) Induction Without Rules - YouTube](https://www.youtube.com/watch?v=DY0-tRu0ms0&ab_channel=KaneB)

But there is a second way to argue against Hume's second horn, that is by postulating that induction doesn't have a general rule so to speak.

"It is possible to go even further in an attempt to dismantle the Humean circularity. Maybe inductive inferences do not even have a rule in common. What if every inductive inference is essentially unique? This can be seen as rejecting Hume’s premise [P5](https://plato.stanford.edu/archives/spr2023/entries/induction-problem/#P5). Okasha, for example, argues that Hume’s circularity problem can be evaded if there are “no rules” behind induction (Okasha 2005a,b). Norton puts forward the similar idea that all inductive inferences are material, and have nothing formal in common (Norton 2003, 2010, 2021)."

"One moral that could be taken from Goodman\['s problem of induction\] is that there is not one general Uniformity Principle that all probable arguments rely upon (Sober 1988; Norton 2003; Okasha 2001, 2005a,b, Jackson 2019). Rather each inductive inference presupposes some more specific empirical presupposition. A particular inductive inference depends on some specific way in which the future resembles the past. It can then be justified by another inductive inference which depends on some quite different empirical claim. This will in turn need to be justified—by yet another inductive inference. The nature of Hume’s problem in the second horn is thus transformed. There is no circularity. Rather there is a regress of inductive justifications, each relying on their own empirical presuppositions (Sober 1988; Norton 2003; Okasha 2001, 2005a,b)."

"One way to put this point is to say that Hume’s argument rests on a quantifier shift fallacy (Sober 1988; Okasha 2005a). Hume says that there exists a general presupposition for all inductive inferences, whereas he should have said that for each inductive inference, there is some presupposition. Different inductive inferences then rest on different empirical presuppositions, and the problem of circularity is evaded."

"What will then be the consequence of supposing that Hume’s problem should indeed have been a regress, rather than a circularity? Here different opinions are possible. On the one hand, one might think that a regress still leads to a skeptical conclusion (Schurz and Thorn 2020). So although the exact form in which Hume stated his problem was not correct, the conclusion is not substantially different (Sober 1988). Another possibility is that the transformation mitigates or even removes the skeptical problem. For example, Norton argues that the upshot is a dissolution of the problem of induction, since the regress of justifications benignly terminates (Norton 2003). And Okasha more mildly suggests that even if the regress is infinite, “Perhaps infinite regresses are less bad than vicious circles after all” (Okasha 2005b: 253)."

"Any dissolution of Hume’s circularity does not depend only on arguing that the UP should be replaced by empirical presuppositions which are specific to each inductive inference. It is also necessary to establish that inductive inferences share no common rules—otherwise there will still be at least some rule-circularity. Okasha suggests that the Bayesian model of belief-updating is an illustration how induction can be characterized in a rule-free way, but this is problematic, since in this model all inductive inferences still share the common rule of Bayesian conditionalisation. Norton’s material theory of induction postulates a rule-free characterization of induction, but it is not clear whether it really can avoid any role for general rules (Achinstein 2010, Kelly 2010, Worrall 2010)."


From the SEP page on inductive logic section 1 there's even more arguments in favour of this. Basic enumerative induction doesn't quite work for all instances. For example, Newtonian mechanics is not a basic enumerative induction but rather a theory where observational consequences are derived logically and then tested for. This can be considered as abduction. [[Abduction]] [[Structures of scientific theories]].






Response to Discord DM

"1. I don't understand how that the non-sceptic would change their opinion upon novel observations is connected with the justification of induction. I hope to have some time very soon such that I can read the SEP.
    
2. _[_21:14_]_
    
    Furthermore, why does it matter that the hypothesis space is a topological space? And what does it mean for a space to be topological?
    
3. _[_21:15_]_
    
    Maybe we should discuss this some time in the future when we call again"







Tags [[Formal Learning Theory]] [[Induction]]