vs FDT?


The debate between EDT and CDT is a debate between two ways of calculating expected utility, so let's go over expected utility first.

We define choices to be selecting between some set of outcomes, weighted by their probabilities. The distribution which gives the best kind of outcome weighted by probabilities is the one with the highest expected value. 

The equation for expected utility of an action is then

$EU(a)=\Sigma_{o\in O}^n P(o,a)U(o)$

Where $P$ represent a probability function with o and a as parameters (this will make the distinction between CDT and EDT) and the utility function U. 

$EU_{CDT}(A) = \Sigma_{i=0}^n P(\square(A\to O_i)) U(O_i)$
$EU_{EDT}(A) = \Sigma_{i=0}^n P(O_i|A) U(O_i)$

One way of telling how they differ is with Newcombs problem.
Imagine that you enter a room and someone predicts what you're going to do once you enter the room. This prediction is very reliable. Once you enter, two boxes are put in front of you, one is transparent with $1000 and another is opaque. The predictor says that it has put one million dollars if it predicted that you were only going to take the opaque box, but not if it predicted that you would take two boxes. Do you pick juts the opaque box or both boxes?

Here's how one would utilize those equations to calculate expected utility in the two scenarios:

Calculations here for EDT from wikipedia

![[2d744629b0c750bcb19b5e2fdd3071cff82b9483.svg]]

TODO: Add CDT

Worth noting that the predictor is not perfect, for this opens up questions about determinism and free will and some other related issues (wikipedia, william craig), so I will skip these for now. 

Another is the smoking lesion problem. Imagine that there is a gene that causes both lesions and smoking. You prefer smoking over not smoking, but strongly prefer no lesion over lesion. There is a correlation, but no causal connection, between smoking and having the lesion. According to EDT you shouldn't smoke since smoking gives you evidence that you have a lesion, but according to CDT you should smoke because smoking doesn't cause the lesion. CDT is believed to be correct here. 

Another one is the Twin Prisoners dilemma. You are in a standard PD against a clone of yourself. EDT would reason this: If you choose to cooperate, this gives you evidence that your opponent would cooperate, which is good for you. CDT would reason that you choosing to cooperate or not won't cause your twin to act cooperatively, so you're better of defecting. So the winner here is EDT. The act itself gives you evidence that agents, atleast one's similar to you in some relevant way, will also act in that way, and you are rationally incentivized to act based on what evidence your act gives you.

There are two ways one can argue using thought experiments in decision theory, as the following two arguments posit:

CDT --> Ought(Two-Boxing)
Not Ought(Two-Box)
Not CDT

CDT --> Ought(Two-Boxing)
CDT
Ought(Two-Boxing)

Basically, one persons modus ponens is another's modus tollens. 

And it gets worse, Egan argues that for every thought experiment for EDT one can build for CDT and vice versa in the following concotion: 

Insert that here. 

So instead of utilizing thought experiments we can argue for the positions using more fundamental positions. 

CDT is more intuitive, it's probably how we actually reason most of the time. What will my action cause? But this is not a great argument, just because we do something it doesn't imply we ought to do it. 

CDT can be considered but also more Vague. It's not clear what exactly a cause or counterfactual is. Here is were David Lewis's analysis of counterfactuals come in. Possible worlds and shifting counterfactual closeness of worlds something like that.

Take on a radically Humean approach: there is no causation, I'm trying to predict my field of sensations, so of course my actions is evidence for future sensation states:

Humean causality
If Humean causality than only EDT is true
EDT is true

So a benefit of EDT then is that it has less metaphysical baggage so to speak. The simplicity of EDT might be worthwhile to consider. 

But moving away from Causality, a benefit of CDT is that it always upholds so called dominance principle, i.e it always picks the option that is strictly better on all outcomes. Given that the million dollars have been placed, one-boxing gives one million but two-boxing gives 1001000. Given that the million dollars have not been placed, one-boxing gives 0 dollars but two-boxing gives 1000 dollars. So two-boxing dominates one-boxing. 




The Psychopath Button thought experiment goes as follows: An agent is placed in front of a button. By clicking that button, it will kill all psychopaths. The agent develops an intention to click that button, but also believes that anyone who develops an intention to click that button is a psychopath themselves. Hence it creates instability, now the agent no longer has an intention to click that button. You get stuck. It is perhaps similar to to unstable beliefs in epistemology. 

One article argues that the sure thing principle implies instability. The STP states that no preference should be changed given some event i.e A > B --> A|E > A|B


Boström meta-newcomb



Earlier I argued that the predictor wasn't perfect. Let's look at this. Craig and Time Travel. If sufficiently good simulations give consciousness, then one is more likely to be in a Newcomb simulation than outside, so one ought to one-box. Similar to time-travel where the predictor just goes forward in time, sees the option, then back and changes the prize-money allocation. This can lead to a Grandfather paradox.


A realistic scenario is elections. Me voting gives evidence people like me would vote. But my vote won't cause changes, so the opportunity cost is not worth it. This can be extended to many every-day decisions.

From the book on Newcombs problem:

"(c) The choice between vice and virtue in the context of Calvinist pre-
destination. 8
(d) Macroeconomic policy choice in the context of rational expectations 9
(but see the chapter by Bermúdez in this volume).
6 For instance: in the UK since 1832, there have been five elections for Parliamentary representatives,
out of approximately 30,000 such, in which the margin of victory has been zero or in single
figures. This gives a frequency of about 0.05% of cases in which the margin of victory was in
single figures.
7 For evidence that they (i) think this and (ii) do so reasonably, see Ahmed 2014a section 4.6.
8 Resnik 1987: 111; Ahmed 2014a: 9ff.; for historical details, see Weber 1992; Tawney 1998.
9 Frydman, O’ Driscoll and Schotter 1982.
Introduction 5The choice whether to engage in some mildly unpleasant activity that is
symptomatic of cardiac health. 10
(f ) The choice whether to smoke, when present smoking indicates future
smoking. 11
(g) Bets about experiments involving non-causal quantum correlations. 12
(h) Choices in the Libet experiment, where experimenters can predict the
agent’s decision before she becomes consciously aware of it. 13
(i) Bets about the prior state of the world in the context of determinism.14
(j) Decisions made by autonomous vehicles in an environment containing
many similar agents. 15
(k) Prisoners’ Dilemma (from game theory) also realizes Newcomb’s Prob-
lem, if each prisoner is confident enough that both reason alike16 (but see
the chapter by Bermúdez in this volume)."


Acausal trade, Hyperrationality



Yudkowski, TDT and FDT?





Or Determinism


QBism

Calvinism, or, in a deterministic universe, what you do gives you evidence. 


Pascal's wager and Roko's Basilisk



If we have $n$ choices with 2 options each, then there are $2^n$ decision theories?

And with say $n_2$ choices with 2 options, $n_3$ choices with 3 options etc we get a total of 

$2^n_2 3^n_3...k^n_k$

$\Pi_2^k i^n_i$

No this doesn't work because of an article which posits that anything but CDT or EDT leads to contradictions? Not sure though. 




FDT implies murdering people??? Something to do with Roko's Basilisk


An example: International politics. Imagine USA and China on an agreement. Realist interpretation. One uses CDT and the other EDT. The one using EDT and the other predicts? International politics newcomb. 



Newcomb prisoners dilemma



> Imagine an agent that is going to face first Newcomb’s problem, and then the smoking lesion problem. Imagine measuring them in terms of utility achieved, by which we mean measuring them by how much utility we expect them to attain, on average, if they face the dilemma repeatedly. The sort of agent that we’d expect to do best, measured in terms of utility achieved, is the sort who one-boxes in Newcomb’s problem, and smokes in the smoking lesion problem. But Gibbard and Harper (1978) have argued that rational agents can’t consistently both one-box and smoke: they must either two-box and smoke, or one-box and refrain—options corresponding to CDT and EDT, respectively. 



Uniqueness of philsoophical thought: Having thought P, one has evidence that some think P, hence decreasing the subjective probability that P is a unique thought. 



The twin prisoners dilemma
The newcomb predictor has a mini-twin in his head that one is acting against.
By FDT, one ought to cooperate when playing against a twin. 





Everyday example?

I can choose or not choose to be nice at some small cost to myself.

Does EDT advice me to be nice since it gives me evidence that other nice people will be nice to me? CDT will say that my choice will not affect how nice others are, so I should not be nice (in this one-shot case with no other negative effects)

Purchase food to a poor person or not
Outcome 99% it's just a poor person, 1% it's a social experiment and you win $10000

$EU_{CDT}(a) = U(o) P(a \square\to o)$
$EU_{EDT}(a) = U(o) P(o|a)$


$EU_{CDT}(b) = -9.90  + 100$
Same for EDT tbh

Hmmm.......

Buying food for poor people gives evidence others act like you do, dropping the probability?
Actually let's calculate EDT

EDT involves Bayesian updating where one's own action is an evidence update step.

$P(o_1|a) = P(a|o_1)P(o_1)/P(a)$



$EU_{EDT}(a) = 0.99 P(o_1|a) + 0.01P(o_2|a)$
$= 0.99 P(o_1|a) + 0.01P(o_2|a)$





P(onemillion|onebox) = P(onebox|onemillion)P(onemillion)/P(onebox)


P(onebox) is the prediction, let's say 0.99

P(onebox|onemillion) = 0.99
P(onemillion) using the principal principle, given the predictors previous perfect score, we can put it at 0.99 aswell

So total: 0.99

But for CDT

P(onebox []-> onemillion) = 0








Quantum mechanics: Retrocausality CDT and problems with EPR correlations and EDT




