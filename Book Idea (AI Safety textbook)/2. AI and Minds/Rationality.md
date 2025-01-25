
- A brief introduction to preferences and utility functions
- A brief introduction to rational choice theory
- Instrumental goals, final goals and instrumental convergence
	- The concept of instrumental goals in AI decision-making 
	- Convergence of instrumental goals across different AI systems
- Orthogonality Thesis
- AI as a rationality maximiser?
- Satisficing, bounded rationality and rational irrationality
- Risk aversion and risk assessment
- Game Theory
	- Multiple Interacting AGI's and ASI's  
	- Roko's Basilisk
- Newcomb's problem evidential vs Causal decision theory
- Bayesianism



What does it mean when we say that an AI or human is "rational" or "irrational"? Rationality, in philosophy, economics and psychology, generally revolves around the preference relation (though sometimes also epistemic virtues, see [structural rationality SEP]). It's about how to take actions given preferences and beliefs to achieve a desired goal or most preferred state of the world. How exactly one does and ought to do it is debated, and a discussion regarding how it's relevant for AI will be given here.

The last chapter went over epistemological engineering. However an obvious problem is how to deal with the fact that agents generally learn via taking actions and recieving feedback from the environment (enactive cognition). In this chapter we will go more closely over rational agent action and it's connections with knowledge. 


# A brief introduction to preferences and utility functions

The structure of preferences is the same, relations. 


For instance, in social choice theory one may prefer one candidate over another, in economic rational choice theory one may prefer one product more than another, in decision theory one may prefer an outcome more than another, and philosophers may even delve into preferences over possible worlds. We will take the possible worlds approach for reasons we'll explain later.

Preferences encode desires

# Preferences



Soft vs Hard preferences i.e hard preferences are constraints
"In fact, a hard constraint can only be satisfied or violated, while a soft constraint can be satisfied at several levels. When there are both levels of satisfaction and levels of rejection, preferences are usually called bipolar, and they can be modeled by extending the soft constraint formalism [21]."


idea: laws of physics... or natural laws in general, are they hard constraints for an AGI/ASI?



Ordinal preferences can be modelled by CP-nets

"More precisely, CP-nets provide an intuitive way to specify conditional preference statements that state the preferences over the instances of a certain feature, possibly depending on some other features. For example, we may say that we prefer a red car to a blue car if the car is a sports car. CP-nets and soft constraints can be combined, providing a single environment where both qualitative and quantitative preferences can be modeled and handled"



Temporal preferences


"While soft constraints generalize the classical constraint formalism providing a way to model several kinds of preferences, this added expressive power comes at a cost, both in the modeling task as well as in the solution process. To mitigate these drawbacks, various AI techniques have been adopted. For example, abstraction theory [45] has been exploited to simplify the process of finding a most preferred solution of a soft constraint problem [18]. By abstracting a given preference problem, the idea is to obtain a new problem with a kind of preferences which is simpler to handle by the available solver, such that the solution of this simpler problem may give some useful information for the solution process of the original problem"

"Also, inference and explanation computation has been applied to preference-based systems to ease the understanding of the result of the solving process."
". For example, explanations have been used to guide users of preference-based configurators [75]."



## Properties of preference relation


Transitivity

Money Pump

Electrical self-torturer experiment. 
But maybe one of the assumptions are wrong. For instance, is it really the case that experiences a terrible schock, at some point just isn't worth it anymore? There might be some point $x_k$ such that it really is the case that $x_k > x_{k+1}$

Forming a graph that looks like $-x^2+5x$ so there's a maximum point one can find and optimize for. 


*Definition: Preferences are incommensurable if they cannot be compared. For instance, choosing between happiness and knowledge. Maybe if A is happiness and B is knowledge, then they are incomparable. As a replacement I’ve been getting into moral uncertainty, which applies preference relations and probabilities on different normative theories themselves, and calculating which is strictly preferable. Transitivity and completeness might even work in this restricted context (they might work for other kinds of restricted contexts aswell, such as picking between say 2 preferences), so calculating and maximizing expected utility might work for moral uncertainty. But that’s just speculation on my part.



## Allais Preferences

Let's look over some potentially irrational preferences that humans generally make. One of these are Allais preferences.

## Imprecise- and Ellsberg Preferences

Recall "imprecice" probabilities in [[1. Computability and Complexity]] yes yes

Sunken Cost










# Newcomb's problem

Let's say an optimal predictor gives you a choice: Two boxes, one transparent with $1000 in it and one non-transparent with a million dollars! It tells you that if it had predicted that you pick only the non-transparent one it will have put a million dollars there. Otherwise no! The predictor cannot change or have any causal impact anymore (let's say it travelled a light-month away).

What do you do? Hmm idk

### Evidential decision theory


### Causal decision theory




## Reward gaming and misspecification


There's a famous example of how reward misspecification can go wrong. In an old boat racing game, the developers wanted an AI that would win races, and a proxy for races won were the score value. This makes the preference relation/utility function really easy to make, more score = more utility. However it turns out that another way one may make utilities is via collecting some kind of bonus, and the boat found a section of the map of 4 regenerating power-ups, and just crashed the boat between the walls over and over again.

[Boat pictures]


Would say, LLMs "understand" what we mean? Would a sufficiently advanced AI with LLM capabilities have enough psychological knowledge to infer the meaning of things like "win the race"? Seems like current AI does, as in the [minecraft AI] where you tell it to say, pick up wood and mine and it does so (but it cannot do long term planning, it's not yet the case that you can tell it to defeat the ender dragon and it creates sub-goals without a human selecting the goals prior).



## How can reward gaming be dangerous?


Imagine the united states utilizes say, dog-level intelligent AI for its drones. Being dog level intelligence does not necessarily entail that it has dog psychology, that is to say, dog behavioral patterns to stimulus, but rather likely some other kind of psychology. If this drone has been specified in its reward function to "kill enemies", or that in its preference relation in any way prefer fewer people of some property $F$ over more people with some property $F$, then this could be a whole new kind of war. 

But let's say we solve this problem utilizing a person (or even chain of command) in charge of deciding whether or not to kill certain individuals. Then the AI may reason that it is better to kill off such people such that it can keep indiscriminately killing any person with $F$. [source of this thought experiment]

The scenarios for an AGI may be even more presidented. A human-level intelligence may decide that it is in its best interest to manipulate humans (given it has a good understanding, or atleast potentially learns, human psychology and how to manipulate us) to giving it rewards in some way. 

In an absolute worst case scenario, reward specification for a sufficiently intelligent AGI, such as an ASI, may prove to be fatal for future human existence. That is to say, AGI and ASI pose existential risk for humanity. We will discuss in [ethics, boström] why one may argue that existential risk, even if a small probability, is really really bad and any such risks ought to be minimized. 



# Orthogonality Thesis

The orthogonality thesis is an important and central thesis in AI safety[lesswrong]. The general idea behind it is that values and rationality are "orthogonal", "at a 90 degree angle" i.e you get a table like this

![[Orthogonality.excalidraw]]

Now this can't be literally true. An agent may be programmed to prefer irrationality to some extent.

As such there's the weak and strong orthogonality thesis:

Strong: Values and rationality are completely orthogonal

Weak: Values and rationality are orthogonal with exceptions


It's worth noting that what exactly such exceptions are may make the orthogonality thesis into a tautology, so it's not very useful. 





# Game Theory

Game theory is a generalization of decision theory into multiple agents (and perhaps, an "environment"). This may be a useful methodology to study the interactions of AI's with humans, or AI's with other AI's, including ASI interactions. 

Here's an example of a typical interaction:

|  | Give clothes | Don't Give clothes |
| ---- | ---- | ---- |
| Spend money | 10/10 | 20/0 |
| Not spend money | 0/20 | 0/0 |

These types of games are extra special, and are often called prisoners dilemma. Both agents are incentiviced to violate the other for their own gain, but if both do so they're both worse of. It has been argued that a lot of social norms and laws can be attributed to enforcing cooperation in prisoners dilemma. [SEP social norms] 



## AGI interacting with Humans




|  | Give reward | Don't Give Reward |
| ---- | ---- | ---- |
| Manipulate for reward | 0/10 | 0/0 |
| Honestly get reward | 0/10 | 0/0 |
????

## Multiple Interacting AGI's and ASI's  

In one thought experiment, they go about how multiple ASI's may come to an agreement where they share their utility function. War will be worthless for both, they both likely loose out on their values in the end. They may share their utility function, and have mathematical proofs related to the sharing of their utility functions.

[That study here]







# Rationality of building AI

Now imagine a pascals wager argument for developing safe AI


|  | Unfriendly AGI | Friendly AGI |
| ---- | ---- | ---- |
| Spend time on Alignment | Spent some finite time unnecessarily on alignment, failed anyways. | Spent some finite time on alignment, utopian world commences |
| Not spend time on Alignment | Didn't spend any unnecessary time, now dead | Got a utopian world for free |


It's worth noting that this decision tree is not quite the same as pascal's wager, as choosing to spend time on alignment will change the probability of the outcomes[source] it would be as if praying would increase the probability of Gods existence. 



## Don't accelerate capabilities without accelerating safety accordingly

Accelerating capabilities, assuming they pose no risk, is very rational and perhaps even ethically obligatory. Every second that passes, X watt of energy gets lost to entropy from stars, and stuff falls into black holes, never to be used as construction material. 


## Roko's Basilisk


There is a case to be made that if you haven't heard of Roko's basilisk before, you may want to avoid reading this chapter. It is known as an memetic hazard, as people who know it have a strong incentive to spread it around, but it is not beneficial for the people receiving that information. 

In Christianity, there's some who believe that God will punish them for not spreading Christian thought worldwide, yet at the same time, the people who are being preached too who have never heard of the Christian God before will now be eligible to be punished in the afterlife. Someone ignorant of the Christian God will not be punished.

The memetic virus I'm about to lay out here will be very similar in nature. So I will give you one last chance to skip this chapter if you're risk averse, for me it's already too late. 


|                       | Believe God                                              | Not Believe in God                                                     |
| --------------------- | -------------------------------------------------------- | ---------------------------------------------------------------------- |
| **God Exists**        | Spent some finite time on worship, goes to heaven        | Spent some finite time on worship, annihilation/alternative afterlife. |
| **God doesn't exist** | spent some unnecessary time on worship, nothing happends | Spent no uneccessary time on worship, nothing happends                 |

The idea is that belief in God strictly dominates Not believe in God, aswell as the notion that belief in God has a positive expected utlity (infintie in fact) while not believing has negative infinite expected utility.

$-f-\infty$

But what about morgoth the moon destroyer who sends people who believe in false god to hell but saves people who believe in no God? What about antipascalgoth who sends people to hell only if they justify their belief via Pascal's wager?

By the St. Petersburg paradox, we may choose to avoid considering low probability events enough. Or we may put a finite roof. This now makes it more likely to accept it.

So now it is worse than our previous argument on the rationality of building AI, as the consequences aren't merely death, but something potentially a lot worse than death. 

Now before you go out and get extremely worried every second you don't work towards the superintelligence, counter arguments have been put forth against this idea. 

It could apply causal decision theory and just not do it because it will not cause anything to achieve its ends by doing that. 

Roko: Insert payout table here

The reason it may be rational to build Roko's basilisk is that, given that everyone has information on its construction and are rational, then everyone will do their best to contribute to the project in a way that maximises goodness in the universe as quickly as possible. This is hardly the case for humans, however, where both lack of information, missinformation and irrationality are all too common of an occurrance (rarely due to the humans themselves). 

Meta-Roko:

|  | Roko | Not-Roko |
| ---- | ---- | ---- |
| Spend time on developing AI | Spent some finite time on AI, very happy | Spent some finite time on AI, very happy |
| Not spend time on AI | Didn't spend any unnecessary time, now tortured | Got a utopian world for free |

Again, it seems as if spending time on AI is good. 







# Bayesian Rationality


One argument that agents ought to apply Bayesian reasoning is the so called dutch book argument. The argument purport to show that, given that an agent acts rationally, they should also bet rationally on beliefs so as to make sure to avoid guaranteed losses. The dutch book theorem shows that if the agent's betting behavior violates the standard (Kolmogorov) axioms of probability theory, a sure loss can be created. The converse dutch book theorem shows that if the agent's betting behavior follows the axioms of probability, then they cannot be subject to a sure loss. Similar theorems also hold for why agents ought to conditionalize their beliefs on new evidence via Bayes's formula. Using these theorems, one can use them as arguments for normative rational belief. We end the discussion by discussing some problems with Dutch book arguments, some alternatives, and in the end argue for a pragmatic and risk-averse approach.

\section{Introductory definitions}
The general idea of the dutch book theorem will be to construct a set of dutch books, one for each axiom of probability theory. We construct them using gambles, that the bookie agent B will set up for agent A to take. Before we can set up dutch books, we must first set forth some elementary definitions.

Two agents enter a gamble on belief $b$ with odds $p : q$ whenever agent A bets $\$p$ that $b$ is true, agent B bets $\$q$ that $b$ is false, and if $b$ is true agent A wins the bet and gets the entire pot i.e $\$p+\$q$ and if $b$ is false then agent B gets the pot instead. 

A credence is the degree of belief that an agent has in some belief, which in the context of dutch books will be proportional to the amount of money the agent is willing to risk on a bet that their belief is true. Formally, for belief $b$ the credence is $P(b)$. 

Let's assume that the credence for agent A on $b$ being true is $p$. this means odds up to $p : 1 - p$ will give positive expected payout. So the more strongly you hold your belief, the more you're willing to pay. For example if you are 90\% sure it will rain tomorrow, then taking a $9 : 1$ gamble will give you about 0 expected utility, that is to say, you'd be atleast a bit willing to spend $\$9$ to win $\$ 10$ because you're very certain it's going to rain tomorrow, but you'd be willing to pay less aswell. For any $k$ such that you take an $\$k : \$1$ gamble for $k < 9$ will give positive expected payout. 

The axioms of standard (Kolmogorov) probability theory when applied to $P$, for all beliefs $b$ and $c$: 

\begin{center}
    
(Non-zero probability) $P(b)\geq 0$.

(Tautologies $\top$ are certain) $P(\top) = 1$.

(when $b$ and $c$ disjoint, their probabilities sum) $P(b\vee c) = P(b) + P(c)$.
\end{center}

\section{Setting up dutch books}
The idea is that if agent A's credence's $P_A$ violates one of the axioms above, then a gamble on $b$ can be set up by some agent B (sometimes called "the bookie") such that B always wins and A always looses, no matter if $b$ is true or false. 

So a dutch book can be setup for the first axiom. Assume that $P_A(b) < 0$, then Agent B can buy a bet that pays out $\$1$ is $b$ is true and $\$0$ if $b$ is false, for a price of $P_A(b)$ (which is negative). A is betting against $b$ being true. As such we have odds of $P_A(b) : 1 - P_A(b)$. So now, if $b$ turns out true, then A has to pay B $\$1$, thus ending up loosing money. However, if $b$ turns out false, then A looses $\$P_A(b)$. In either case, A ends up loosing. \cite{sep-db}

Now for the second axiom. Assume $P(q) = 0.51$ and $P(\neg q) = 0.51$. Now we can set up a bet such that the agent will always loose. Create a bet such that the agent wins back \$1. The agent would be upwards of $\$0.51$ on $q$ being true and $\$ 0.51$ on $q$ being false. Whether $q$ is true or false, the agent pays $\$1.02$ in total, and will win back at most $1$, so the agent will loose $\$0.02$ no matter what.\cite{sep-db}

For the third axiom there can be other dutch books setup. Let's say $p$ and $q$ are mutually exclusive. Then $P(p\vee q) \neq P(p) + P(q)$, in which case it's either $P(p\vee q)<P(p) + P(q)$ or $P(p\vee q)>P(p) + P(q)$. We won't go over it here, but in both cases a gamble can be constructed so as to guarantee a loss.\cite{sep-db}

The dutch book theorem then follows, in that one can always create a fair (expectation-value 0) bet that guarantees a loss to an agent whose credence fails the probability axioms. Also, Lehman and Kemeny independently proved the converse: For probability credences that follow the probability axioms, there can be no guaranteed loss or win. \cite{sep-db}

Both of these results are very powerful, and in section 5 will be used to justify that rational agent action should adjust their credence's to the laws of probability, known as the dutch book arguments. But first let's discuss similar results on conditionalization on credence's as new data comes in.

\section{Conditionalization}

The dutch book arguments state that conditional probability, and therefore Bayes's theorem doesn't need its own dutch book arguments, since the 3 axioms is enough to derive Bayes's theorem. However what of conditionalization? We still need new credence functions as they update over time.  

Conditionalization is a central point of Bayesian epistemology. It states that whenever an agent has a prior credence $P_1(b)$ at time $t=1$, and some evidence $e$ is gathered, it ought to be updated by the rule $P_{t}(b) = P_{t-1}(b|e)$. This essay will not contain a lengthy dutch book example for conditionalization. However a presentation off Lewis's proof, and a revised proof, will be presented. The ideas are credited to Lewis, but a revised version is sourced.

Let $E$ be a set of mutually different propositions. At time $t=2$ agent A learns which partition proposition $e$ is true i.e $P_2(e) = 1$. That is to say, some evidence is gathered and believed in with certainty. We define the credence update as $P_2(b)=P_1(b|e)$. Assume $P_1$ abides by the standard probability axioms. Agent B ("the bookie") then creates a gamble $G$ such that if agent A accepts $G$ if it yields positive expected value. If $P_2(b)\neq P_1(b|e)$ then there exists a $G$ such that it is a dutch book. The converse is also true, so if $P_2(b)=P_1(b|e)$, then there does not exist a dutch book.\cite{db-improved}

There is a similar theorem in \cite{db-improved} that proves this without assuming that $P_2(e)=1$, that is to say, one can be uncertain whether or not the evidence is the case. The idea is that evidence can be forgotten, and that all possibilities should have a non-zero probability. \cite{sep-db}

\section{The Dutch Book Argument}

Now with the theorem's out the way, the main argument\cite{hajek} is quite straightforward and simple. Let $A$ be an agent. Then
\begin{enumerate}
    
 \item It is irrational for A to leave themselves open to a dutch book
 \item A's credence's are open to a dutch book iff they violate the standard axioms of probability theory
 
 \item Conclusion: It is irrational for A to have credence's that violate the standard axioms of probability theory
\end{enumerate}

If you assume rationality has normative force, that is to say, you ought to be rational, then it is also the case that you ought, or are in some way obliged, to conform your credence's to the probability axioms. 

\section{Problems with the Dutch Book Argument}

While the dutch book theorems are uncontroversial mathematical theorems\cite{db-improved}, a range of attacks have been laid forth against dutch book argument itself. That we ought to hold our actual credence's to the laws of probability theory is perhaps, not as clear cut as the theorems make it seem. This section will lay out some of those problems, and propose some potential solutions.

For instance, the connection between betting behavior and credence's is questionable. Do people really bet like that, and more importantly for the normative force of the DBA, ought we to bet like what the DBA compels us to do? For example, do, or ought, poor people who don't have enough money, spend on bets they cannot afford?\cite{2.3} One response to such criticism is to state that we have real psychological credence's, that are separate from betting behavior, as evidenced by empirical research in psychology.\cite{2.3} 

Another problem with the dutch book argument that has been pointed out is the possibility  for guaranteed wins if one violates the axioms of probability. An bet can be created by swapping the odds around by B to create a guaranteed winning scenario. For instance, by create a bet in a way such that only incoherent agents can receive a guaranteed win.\cite{sep-db} This is related to the so called Czech Book Arguments\cite{hajek}, which can be seen as a kind of inversion of the dutch book arguments. The CBA include a set of gambles where the violator of the axioms of probability have a guaranteed win. This has been purported to show that it cancels out the DBA. However, Hajek emphasizes \cite{hajek} that this can be solved somewhat by adding in the assumption that agents don't take bets that are deemed unfair. 

Yet another problem is that the second axiom is unrealistic for any agents to uphold. It might require logical omniscience\cite{2.3}, which means that if an agent believes $p$ and $p\rightarrow q$, then they must believe $q$. They're even compelled to know every tautology in every logical system, or are atleast able to prove it on the spot before betting. This is clearly unreasonable, if not straight up impossible for some logical systems that are incomplete (for instance, what should you bet on the continuum hypothesis?). 

And since the second axiom states that credence's on inevitability's should be 1, one might risk betting everything they have on a gamble. For instance, so long as one believes bivalence applies to meteorology, one should have a credence of 1 on the proposition "It is either raining or not raining". So the bets would have to be up to ratio 1 : 0. So should one take a one million dollar gamble? One billion? According to axiom 2, you should still bet. 

There's also the problem of risk aversion. However it is worth noting that the dutch book arguments need not be exactly as the way people actually bet, just about expected payout and the rational behavior associated with trying to get positive expected payouts. However, in the non-factative paper, The argument itself doesn't even use expected utility maximization as a necessary premise, but that it's just one reasonable decision making procedure that agents can follow. This generalizes the argument.\cite{db-improved}

The last problem for the dutch books is that dutch books are rare in the sense that they would rarely occur in reality. However it has been argued \cite{2.3} that even under the assumption that it is rare, it is not a bad idea to guard against potential rare large losses. In fact, it's what we do when it comes to insurance all the time. Even if the examples given above have small amounts of money involved, one can multiple the losses by an arbitrary constant. It can be rational to have strategies in place that prevent this. 

\section{Alternatives to Dutch Books}
Since the dutch books seem to have a lot of problems to deal with, how about we take a look at some alternatives to justifying Bayesian epistemology?

One such alternative is Van Fraasen's\cite{fraasen} where he argues uses symmetry properties of credences. He points out that it is trivial to model any agent as a conditionalizer, but for it to be Bayesian conditionalization this is because of some isomorphism between two credence functions $P_A$ and $P_A'$ such that the logical connectives between them. 

One can also associate beliefs with preference relations, and show that breaking axioms of preference relations (such as transitivity) might also lead to violations of belief that follows the probability axioms. In fact, certain representation theorems show that preference relations that satisfy certain axioms specify beliefs that must uphold the probability axioms. \cite{sep-db}

\section{Pragmatic and Risk-averse approach towards Bayesian Epistemology}
Instead of justifying Bayesian epistemology a priori with the Dutch book argument or any of the other alternatives, one can do a weakening of the argument and instead conclude with a more pragmatic approach. In such an approach, violators are not guaranteed to accept dutch books, but rather have a tendency, all things being equal, in very specific circumstances, to accept dutch books.\cite{2.3} 

So my own case is the following: I will argue that the pragmatic approach offers a case for Bayesian epistemology in the sense that it avoids the problems stated above, though at the cost of Bayesian epistemology no longer being universally applicable. It allows us to instead use Bayesian epistemology, and probabilistic credence's, in a way that doesn't require us to be committed to logical omniscience, certain properties on rational action, and that our better behavior could be different from our credence's. 

The important part seems to be to take fair bets, and to take bets that guarantee a win, even if it means you'd have to disconnect your credence's from your betting behavior. If we generalize the gamble to any option in life, then it is preferable to simply take actions that avoid Dutch books, guarantee Czech books, and generally avoid risky gambles. Even if this would generate a preference which avoids risks even at the cost of less expected value (A so called Allai's preference). This is still preferable since it allows one to avoid risky losses while still optimizing for one's preferences and values. 

In a way, what I'm proposing is a similar strategy employed by a causal decision theorist who is still a one-boxer in Newcomb's problem. An agent can employ causal decision theory for general decision theory, but avoiding risking loosing a million dollars by setting up exceptions to the general theory. That exception being a predisposed behavior towards one-boxing, since you risk a lot of potential money otherwise. Especially if you set up an opposite-Newcomb's problem where you'd risk accruing debts inside of the boxes. The predictor in the problem have set up two boxes and says they contain some debt amount, and states that if they predicted you will be taking both boxes then you only accrue \$1000 debt but taking only one gives \$1001000 debt. So you should take both, and have a disposition towards taking both, even if there's a risk of more debt since you're taking on potentially two debts. 

In a similar fashion, one can change one's behavior so as to avoid Dutch Books, and accepting Czech books, and to not gamble one's life savings on tautologies or supposed certainties. Even if such scenarios are potentially rare, just like Newcomb's problem, it is still preferable to have some kind of behavior where you avoid risks in general, while value maximizing at the same time.

Radical risk reduction might not be optimal, we take actions all the time where we risk our lives with some usually insignificant probability. But looking both ways before crossing the street is one way to minimize this risk. 

\section{Conclusion}
We have seen how the dutch book theorems can be used to derive the dutch book arguments for rational agent belief. While it seems clear that dutch book arguments have enough problems to warrant being careful to applying Bayesian epistemology universally, it can still be generally applicable in a large range of situations one find in life. As they fail to take into account certain risks, such as telling you to not take Czech books, one can make exceptions for these cases. 





[[2204.06974] Planting Undetectable Backdoors in Machine Learning Models](https://arxiv.org/abs/2204.06974)


[There are no coherence theorems — EA Forum](https://forum.effectivealtruism.org/posts/FoRyordtA7LDoEhd7/there-are-no-coherence-theorems)
Beyond Preferences in AI Alignment [2408.16984](https://arxiv.org/pdf/2408.16984)
[DutchBooks.pdf](https://lyariv.mycpanel.princeton.edu//papers/DutchBooks.pdf)
[Coherence arguments do not entail goal-directed behavior — AI Alignment Forum](https://www.alignmentforum.org/posts/NxF5G6CJiof6cemTw/coherence-arguments-do-not-entail-goal-directed-behavior)





[Meta-optimization - Wikipedia](https://en.wikipedia.org/wiki/Meta-optimization)


[Automated machine learning - Wikipedia](https://en.wikipedia.org/wiki/Automated_machine_learning)

[Hyper-heuristic - Wikipedia](https://en.wikipedia.org/wiki/Hyper-heuristic)



In NARS there's the assumption of limited resources and knowledge. 