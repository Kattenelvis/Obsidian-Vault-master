

Ideas for a queer blog post:
Title: Queer Labels as Inductive Hypothesis

## Introduction

Labels are inductive hypothesis's. Up for change. We begin with a detail account of Popperian falsification, followed by a sketch on how we could expand it to a Bayesian approach. 

What are queer labels

# Induction

Reasoning from certain premises to an uncertain conclusion. 
$(P(c_1)\wedge P(c_2)\wedge\dots\wedge P(c_n))\rightarrow\forall x P(x)$

This indeed posits that any future $c_{n+1}$ that is found will also have 

## Popperian falsificationism

To simplify the mathematics for now we assume there's only two genders (👩|👨) and that someone is either non-attracted (😐) or attracted (🔥) (but this could in theory be generalized to $m$ genders, with $2^m$ sexualities as a consequence). Let $E_i$ be a set of stimulus events containing either a man or a woman.  Let the table below be a finite number of observations made by an heterosexual male.

|Event|E_1|E_2|E_3|E_4|$\dots$|E_n|
|-|-|-|-|-|-|-|
|Gender of stimulus|👩|👨|👩|👨|$\dots$|👩
|Phenomenology|🔥|😐|🔥|😐|$\dots$|🔥

One can then create an inductive inference from this set of events into a generalized hypothesis. Let $M$ mean man, $W$ mean woman, and $A$ mean attracted too. We can take the inductive inference to be the following [SEP page on Formal learning theory]:  $(M(a)\rightarrow\forall x (W(x)\rightarrow A(a,x)\wedge M(x)\rightarrow\neg A(a,x)))\wedge (W(a)\rightarrow \forall x (W(x)\rightarrow A(a,x)\wedge M(x)\rightarrow\neg A(a,x)))$
Simply: If $a$ is man, then $a$ is attracted to all women and no men. If $a$ is a woman, then $a$ is attracted to all men and no women. Since it gives us the truth conditions for whether or not $a$ is straight, we can take this to be the meaning of "$a$ is straight". This also roughly captures the usage of the term, though one can always create explicative definitions of it and analyze them individually. I don't wanna get into the descriptivism vs prescriptivism debate in the philosophy of language though. 

But of course, the occasional opposite sex stimulus does not provoke a fiery response, and the rare same-sex attraction under certain circumstances aswell, so one can instead use the generalized quantifier "most" instead of "for all" [See SEP page on generalized quantifiers] (note that the 👩 stimulus is no longer provoking 🔥response)

| Event                | E_1 | E_2 | E_3 | E_4 | $\dots$ | E_n |
| -------------------- | --- | --- | --- | --- | ------- | --- |
| Visual Sense-Data    | 👩  | 👨  | 👩  | 👨  | $\dots$ | 👩  |
| Emotional Sense-Data | 🔥  | 😐  | 🔥  | 😐  | $\dots$ | 😐  |

Which gives us the revised meaning of straight as
$(M(a)\rightarrow \textbf{most}(x) (W(x)\rightarrow A(a,x)\wedge M(x)\rightarrow\neg A(a,x)))\wedge (W(a)\rightarrow \textbf{most}(x) (W(x)\rightarrow A(a,x)\wedge M(x)\rightarrow\neg A(a,x)))$
Which gives us the roughly correct truth conditions for "a is straight".

We will now connect this with physicalism. The earlier pattern can now be redescribed using physical objects instead of mental objects, given research done on sexuality [insert neurophysiology of sexuality study here].

|Event|E_1|E_2|E_3|E_4|$\dots$|E_n|
|-|-|-|-|-|-|-|
|Stimulus Pattern|👩|👨|👩|👨|$\dots$|👩
|Cortex Response|🔥|😐|🔥|😐|$\dots$|🔥

With similar truth conditions as before, but with slightly different predicates (physical predicates instead of mental predicates), this gives us the same truth conditions, if identity theory of mind is true. 

So falsification forms an impartial ordering of sexualities where the "possible falsification" relation between hypothesises determines how those hypothesises may develop. 

Here is the case for $n=2$ genders
![[2 gender case.excalidraw]]
This makes bisexual the most stable, and unfalsifiable since we've ran out of other hypothesises. Asexual being the least stable, as a single counter-example could ruin everything.


## New problem of induction
Goodmans new problem of induction. 

When we have a hypothesis that uses some up to the current moment gathered evidence, we may find ourselves not being so pogchamp. This is because the evidence we have can justify different hypothesises about the future. 

(Cylinder image here from formal learning theory)

You can have the hypothesis say "Gay", because you only have evidence of boy-attraction pairs. However, "Bisexual at time t" is also justified by the evidence for all t greater than current time moment. 

## Bayesian Probabilism

But this is not entirely correct, introduce probabilities and Bayesian updating. 

One reason most of popperian falsificationism may be wrong is the possibility of [fluid sexuality]. If that is true, then being called bisexual may produce very skewed predictions that are not always correct. As such,we can change it to probabilities!

Again, for the gender $n=2$ special case we get:

$P(Hetero)$
$P(Homo)$
$P(Bi)$
$P(Ace)$



As such one could use base-rates to determine one's prior probability (in philosophy, this is called the [principal principle]). Being autistic and asexual puts a vastly greater probability in being aromantic for instance. 


# Problem of other minds

We cannot escape the possibility of solipsism[source], but assuming other minds do exist, how can we have justified belief in what is is like to be something else? And what is it like for average human experiences?

We don't want to end up in a situation where we're using these labels based on sense-data and they turn out to be completely meaningless or radically indeterminate in some way!

## Simulation theory vs theory theory. 



This is really only a problem if we're not behaviorists. 

Can we simulate other sexualities? Can we create a mental-simulation model which allows us to atleast partially feel what it is like to have a certain sexuality?


## Wittgensteinian beetle in a box.

Imagines us to have a beetle in a box. People talk about how their beetle is like. But they are private, they can be radically different, only you can see it. As Wittgenstein says, some boxes may be empty!

So in such a sense, all kinds of attractions, as an experience and not as a set of behaviors, might be impossible by the use-theory of meaning to be meaningful. 



## Heterophenomenology

The queer community and psychologists have done a generally good job at heterophenomenology. For instance, the 2-factor model that distinguishes romantic from sexual attraction. But more distinctions have been made, such as aesthetic attraction and sensual attraction. With these terms, we may be able to figure out how it is like to be another person, atleast by simulating/theorizing about it. 



# Appendix: Many sexualities for n genders

Here's how to generalize it to $m$ genders and get $2^m$ sexualities.

$1$ gender, $2^1=2$ sexualities:
Asexual
Homosexual

$2$ genders, $2^2=4$ sexualities:
Asexual
Homosexual
Hetereosexual
Bisexual

$3$ genders, $2^3=8$ sexualities:
Asexual

3 types of hetero/homosexual:
Attracted to gender 1
Attracted to gender 2
Attracted to gender 3

3 types of bisexuality:
Attracted to gender 1 and 2
Attracted to gender 1 and 3
Attracted to gender 2 and 3

Pansexuality (all genders)

$4$ genders, $2^4=16$ sexualities:

Asexual

4 types of hetero/homosexual

6 types of bisexuality
Attracted to gender 1 and 2
Attracted to gender 1 and 3
Attracted to gender 1 and 4
Attracted to gender 2 and 3
Attracted to gender 2 and 4
Attracted to gender 3 and 4

types of trisexuality
Attracted to gender 1 and 2 and 3
Attracted to gender 1 and 2 and 4
Attracted to gender 2 and 3 and 4

Pansexual



# Other random ideas
Science and statistics, trauma, happiness

Gender identity, "AGP" and "HSTS"
The ethics of it: No, you are not just a fetish and don't let transphobes say that it's just that. Not perverted. Here's what AGP and HSTS is about. AAP. 





