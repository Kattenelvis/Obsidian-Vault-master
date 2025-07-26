"  
It's related, but I remember van Frasseen one time arguing that if one accepts standard dutch book reasons to motivate Bayesianism, then the only IBE inferences they can accept is either the ones recoverable from Bayesian reasoning, which are redundant, and any IBE inferences that aren't a special case of Bayesian reasoning are going to violate the very reason someone accepts Bayesianism, hence the argument from Bayesianism to anti-explanationiism"




Bayesian conditionalization is a fundamental concept in Bayesian probability theory, building upon the foundations laid by Dutch book arguments. It provides a formal framework for updating probability beliefs in the face of new evidence. To delve into the technical details of Bayesian conditionalization, it is essential to understand its connection with Dutch book arguments and how these concepts interact to ensure coherence within Bayesian reasoning.

Dutch book arguments highlight the importance of avoiding incoherent sets of probabilities that can lead to guaranteed losses in betting scenarios. A Dutch book is a series of bets that, when taken together, result in a certain loss for the individual regardless of the outcome. By identifying and exploiting inconsistencies in an agent's beliefs, Dutch book arguments demonstrate the necessity of adhering to the principles of probability theory for rational decision-making.

Now, Bayesian conditionalization extends the Dutch book framework by introducing a formal mechanism for updating probabilities based on new evidence. The core idea is to adjust the probabilities assigned to various events in light of observed data, ensuring that the updated set of probabilities remains coherent and consistent with the principles of probability theory.

Let �P represent the initial probability distribution before observing new evidence, and �E denote the evidence. Bayesian conditionalization updates the probability distribution to �′P′ given the evidence. Mathematically, this can be expressed as:

�′(�)=�(�∩�)�(�)P′(A)=P(E)P(A∩E)​

where �A is any event, and �(�∩�)P(A∩E) is the probability of both �A and �E occurring, and �(�)P(E) is the probability of observing the evidence.

To connect this with Dutch book arguments, consider a scenario where an agent's initial beliefs are represented by �P, and a Dutch book is constructed based on these probabilities. Now, suppose the agent updates their beliefs to �′P′ using Bayesian conditionalization after observing evidence �E. For consistency, the updated probabilities �′P′ must satisfy the conditional probability formula above.

If Bayesian conditionalization is violated in the update process, it opens the door to potential Dutch book scenarios, allowing a savvy bookmaker to construct a series of bets that guarantees a profit regardless of the actual outcome. This underlines the importance of adhering to Bayesian conditionalization as a rational updating rule to avoid susceptibility to Dutch book arguments.

In summary, Bayesian conditionalization provides a formal and coherent method for updating probability beliefs in the light of new evidence. It extends the principles of Dutch book arguments by introducing a systematic approach to adjusting probabilities, ensuring that the updated beliefs remain consistent with the axioms of probability theory. By understanding the technical intricacies of Bayesian conditionalization and its connection to Dutch book arguments, one gains a deeper insight into the foundations of rational probabilistic reasoning.





My schoolwork

\documentclass{article}
\usepackage{graphicx} % Required for inserting images
\usepackage{parskip}

\title{Dutch Books}

\begin{document}

\maketitle

\section{Introduction}
One strategy to argue for that agents ought to apply Bayesian reasoning is to employ the so called "dutch book arguments". These arguments purport to show that, given that an agent acts rationally, they should also bet rationally on beliefs so as to make sure to avoid losses. The dutch book theorem shows that if the agent's betting behavior violates the standard (Kolmogorov) axioms of probability theory, a sure loss can be created. The converse dutch book theorem shows that if the agent's betting behavior follows the axioms of probability, then they cannot be subject to a sure loss. Similar theorems also hold for why agents ought to conditionalize their beliefs on new evidence via Bayes's formula. Using these theorems, one can use them as arguments for normative rational belief. We end the discussion by discussing some problems with Dutch book arguments.

\section{Introductory definitions}

Two agents enter a gamble on $b$ with odds $p : q$ whenever agent A bets $\$p$ that $b$ is true, agent B bets $\$q$ that $b$ is false, and if $b$ is true agent A wins the bet and gets the entire pot i.e $\$p+\$q$ and if $b$ is false then agent B gets the pot instead. 

A credence is the degree of belief that an agent has in some belief, which in the context of dutch books will be proportional to the amount of money (or utility) the agent is willing to risk on a bet that their belief is true. Formally, for belief $q$ the credence is $P(q)$. 

Let's assume that the credence for agent A on $b$ being true is $p$. this means odds up to $p : 1 - p$ will give positive expected payout. So the more strongly you hold your belief, the more you're willing to pay. For example if you are 90\% sure it will rain tomorrow, then taking a $9 : 1$ gamble will give you about 0 expected utility, that is to say, you'd be atleast a bit willing to spend $\$9$ to win $\$ 10$ because you're very certain it's going to rain tomorrow, but you'd be willing to pay less aswell. For any $k$ such that you take an $\$k : \$1$ gamble for $k < 9$ will give positive expected payout. 

The axioms of standard (Kolmogorov) probability theory when applied to $P$, for all beliefs $b$ and $c$: 

\begin{center}
    
(Non-zero probability) $P(b)\geq 0$.

(Tautologies $\top$ are certain) $P(\top) = 1$.

(when $b$ and $c$ disjoint, their probabilities sum) $P(b\vee c) = P(b) + P(c)$.
\end{center}

\section{Setting up dutch books}
The idea is that if agent A's credence's $P_A$ violates one of the axioms laid out above, then a gamble on $b$ can be set up by some agent B such that B always wins and A always looses, no matter if $b$ is true or false. 

So a book can be setup for the first axiom.
Let's say you have a subjective probability with a probability less than 0, so $P_A(b) < 0$. This means that a dutch book can now be setup by agent B with odds $ P_A(b) : 1 - P_A(b)$.

Then the second mostly states that credence's on inevitabilities should be 1. For instance, if one believes bivalence applies to meteorology, one should have a credence of 1 on the proposition "It is either raining or not raining". So the bets would have to be up to ratio 1 : 0. One million? One billion? You should still bet. 

But let's assume some agent doesn't set such a credence. Assume $P(q) = 0.51$ and $P(\neg q) = 0.51$. Now we can set up a bet such that the agent will always loose. Create a bet such that the agent wins back \$1. The agent would be upwards of $\$0.51$ on $q$ being true and $\$ 0.51$ on $q$ being false. Whether $q$ is true or false, the agent pays $\$1.02$ in total, and will win back at most $1$, so the agent will loose $\$0.02$ no matter what. 

For the third axiom there can be other dutch books setup. Let's say $p$ and $q$ are mutually exclusive. Then $P(p\vee q) \neq P(p) + P(q)$, in which case it's either $<$ or $>$. We let it be $<$ because a very similar dutch book can be created if $>$. We won't go over it here due to space constraints.

What has been shown above doesn't show that having credence's that obey the laws of probability still could generate a dutch book. However there is a proof [SUORCE?] that shows that this is impossible. Also, Lehman (1955) and Kemeny (1955) proved the converse: "For a set of betting quotients that obeys the probability axioms, there is no set of bets (with those quotients) that guarantees a sure loss (win) to one side.". Both of these results are very powerful, and have been used to justify that rational agent action should adjust their credences to the laws of probility, known as the dutch book arguments. We will discuss more on that later, but first let's discuss similar results on conditionalization on credences as new data comes in.

\section{Conditionalization}

The dutch book arguments state that Bayes's theorem doesn't need its own dutch book arguments, since the 3 axioms is enough to derive Bayes's theorem. However what of conditionalization? 
"There is a Dutch Book (strategy) argument purporting to show that an agent ought to change beliefs by conditionalization, which was constructed by Lewis (1999), but was first reported by Teller (1973)."


Conditionalization is a central point of Bayesian epistemology it tells you that whenever you have a belief prior, a $P_1(H)$ at time $t=1$, and new data is gathered, it ought to be updated as $P_{t}(H) = P_{t-1}(H|E)$ which continues indefinitely as time increases. 

Due to space constraints, this article will not contain a lengthy dutch book example for conditionalization. However a presentation off Lewis's proof, and a revised proof, will be presented. Ideas from Lewis, but revised version sourced.

Let $E$ be a set of mutually different (partition) propositions. At time $t=2$ the agent learns which partition proposition $e$ is true i.e $P_2(e) = 1$. That is to say, some evidence in evidence space is gathered and believed in with certainty. A credence update $P_2(H)=P_1(H|E)$. Assume $P_1$ abides by the standard probability axioms. A bookie then creates a bet $B$ such that if the agent accepts $B$ if $B$ yields positive expected value. If $P_2(H)\neq P_1(H|E)$ then there exists a $B$ such that it is a dutch book. The converse is also true, so if $P_2(H)=P_1(H|E)$, then there does not exist a dutch book.

There is a similar theorem in \cite{db-improved} that proves this without assuming that $P_2(e)=1$, that is to say, one can be uncertain wheter or not the evidence is the case. The author makes a distinction between "factative" and "non-factitive" dutch book theorems and formulates and proves a factative dutch book theorem. That $P_2(e) < 1$ could be for many reasons, includes forgetting, experimental equipment errors e.t.c. Regularity: All contingent proposition has probability > 0 at being true. Jeffrey conditionalization retains regularity. They still prove the dutch book theorem and it's converse in this new system. 


Another one is Van Fraasen\cite{fraasen} argues for a different way using symmetries. 

\section{The Dutch Book Argument}

Now with the theorem's out the way, the main argument is quite straightforward and simple. Let $A$ be an agent. Then
\begin{enumerate}
    
 \item It is irrational for A to leave themselves open to a dutch book
 \item A's credences are open to a dutch book iff they violate the standard axioms of probability theory
 
 \item Conclusion: It is irrational for A to have credence's that violate the standard axioms of probability theory
\end{enumerate}

If you assume rationality has normative force, then it is also the case that you ought, or are in some way obliged, to conform your credences to the probability axioms. 

\section{Problems with Dutch Books}

While the dutch book theorems are uncontroversial mathematical theorems\cite{db-improved}, A range of attacks have been laid forth against dutch book argument itself. That we ought to hold our actual credence's to the laws of probability theory is perhaps, not as clear cut as the theorems make it seem.

For instance, the connections made between betting behavior and credences is questionable. Do people really bet like that, and more importantly for the normative force of the DBA, ought we to bet like what the DBA compells us to do? For example, do, or ought, poor people who don't have enough money, spend on bets they cannot afford? \cite{2.3}

One response to such criticism is to state that we have real psychological credences, that are separate from betting behavior [Source 3,2 I think]. 


One can also associate beliefs with preference relations, and show that breaking axioms of preference relations (such as transitivity) might also lead to violations of belief that follows the probability axioms.\cite{sep-db}

"While he never claims that degrees of belief are necessarily linked to preferences, the model of belief and preference that he offers assumes such an association, and indeed a great achievement of the paper is what amounts to a representation theorem establishing that an agent satisfying the axioms that he specifies for rational preference can be represented as having degrees of belief that satisfy the probability axioms"


To complicate things, an opposite bet can be created by swapping the odds to create a winning scenario.\cite{sep-db} For instance, by create a bet in a way such that only incoherent agents can receive a guaranteed win.

It is also possible for an agent to sometimes still win a bet despite having credence's that violate the probability axioms. 


Another problem is that the second axiom might be very unrealistic for all agents to uphold. It might require logical omniscience (source: unit 3.2), which means that if an agent believes $p$ and $p\rightarrow q$, then they must believe $q$. They would have to know every tautology in every logical system, or are atleast able to prove it on the spot before betting. This is clearly unreasonable, if not straight up impossible for some logical systems that are incomplete (for instance, what should you bet on the continuum hypothesis?). 

There's also the problem of risk aversion. However it is worth noting that the dutch book arguments need not be exactly as the way people actually bet, just about expected payout and the rational behaviour associated with trying to get positive expected payouts. However, in the non-factative paper, The argument itself doesn't even use expected utility maximisation as a necessary premise, but that it's just one reasonable decision making procuder that agents can follow. This generalizes the argument \cite{db-improved}


"As Hájek emphasizes, there is a corresponding “Czech Book Argument”, which parallels the DBA, with the conclusion that one ought to violate the probability calculus (Hájek 2005, 2008a). Construed as above, the DBA appears to be canceled out by the “Czech Book Argument”, although Hájek shows that the potential canceling out can be avoided by reformulating the DBA with the assumption that the agent should accept bets that are either fair or favorable (Hájek 2008a). Still, it is compatible with the Dutch Book theorem that an incoherent agent could end up on the side of a sure gain, and so incoherence cannot be condemned as irrational simply by citing the possibility of sure losses."



\section{Pragmatic approaches in justifying Bayesian Epistemology}
Instead of justifying bayesian epistemology a priori with Dutch book arguments, one can instead utilize pragmatic arguments. 

From the book:
"As I noted in section 2, the tactic of defining credence so as to establish the connection as a matter of definition has fallen out of favor, but a
connection that is any weaker seems to result in a conclusion, not that the
violator of the axioms is guaranteed to accept a Dutch book, but that they
have a tendency, all other things being equal, in the right circumstances, to
accept a Dutch book. That is good enough for me, but it is not good enough
for many aprioristic Bayesians."

Bayesian Learning Theory
Bayesian Statistics
AI models

"I agree that one is unlikely to encounter a Dutch bookie. However, prudence counsels that 
one guard against many unlikely dangers. If you own a home, then buying homeowner’s 
insurance leaves you better off in one important respect than you were before, even though you 
are unlikely to file a claim on your insurance. There is a benefit to guarding against an unlikely 
outcome when the potential downside is sufficiently bad. And the potential downside from Dutch 
bookability is devastating: the Dutch bookie from Section 5 can enforce arbitrarily high losses, 
simply multiplying all payoffs by an arbitrary constant."https://philosophy.ucla.edu/wp-content/uploads/2016/08/Improved-Dutch-Book-Theorem.pdf

Counter-argument: Such risk-aversion would make people offputt to dutch books in the first place. 



"Epistemological Foundations A recent presentation of the idea that credences are psychologically real and related to, but distinct from, betting behavior, see Osherson et al. (1994).
There is a huge and ever-increasing literature on Dutch book and other
approaches to arguing for the irrationality of credences that violate the axioms of the probability calculus. Howson and Urbach (1993) will point you
to some of this work. It all begins with Ramsey (1931) and de Finetti (1964).
For a recent, revealing overview, try Hájek (2005)."
For the extension of Dutch book arguments to Bayes’ rule, see Teller
(1973). Howson and Urbach is also handy here. For a justification of Bayes’
rule that does not make use of Dutch books, see van Fraassen (1989), chapter 13.
On the debate between a priori and pragmatic approaches to justifying
bct, take a look at some of the papers in Maxwell and Anderson (1975).
Most of these writers are philosophers of science who favor the more pragmatic approach. Reading this volume in the 1970s, you might have predicted
that apriorism was on the wane. Wrong; in the matter of ideology, never bet
against the fanatics.
The question of the justification of the probability coordination principle was raised by Miller (1966), who argued that it was inconsistent. Lewis
(1980) is a classic formulation of the principle and an equally classic discussion of its role in Bayesian thinking. For an attempt to justify pcp, see
Howson and Urbach (1993, chap. 13). Strevens (1999) crtiticizes Howson
and Urbach’s strategy and argues that the problem of justifying the principle is on a par with the problem of induction. Lewis’s recantation of his
original formulation of the principle may be found in Lewis (1994); Strevens
(1995) argues that there is no need to recant.
The subjectivist theory of physical probability was originally presented
by de Finetti (1964), and has been expanded by Skyrms (1979).
On defining a quantitative measure of evidential relevance or support
using subjective probabilities, see Fitelson (1999)."



"(A) Degree of rational belief = coherent betting behavior.
(B) Coherent betting function = probability measure."

\section{my own views I guess?}

\bibliography{refs}
\bibliographystyle{acm}

\end{document}



[Why The Focus on Expected Utility Maximisers? — LessWrong](https://www.lesswrong.com/posts/XYDsYSbBjqgPAgcoQ/why-the-focus-on-expected-utility-maximisers?commentId=a5tn6B8iKdta6zGFu)


> My take is that the concept of expected utility maximization is a mistake. In Eliezer's [Coherent decisions imply consistent utilities](https://www.lesswrong.com/posts/RQpNHSiWaXTvDxt6R/coherent-decisions-imply-consistent-utilities), you can see the mistake where he writes:

> From your perspective, you are now in Scenario 1B. Having observed the coin and updated on its state, you now think you have a 90% chance of getting $5 million and a 10% chance of getting nothing.

Reflectively stable agents are updateless. When they make an observation, they do not limit their caring as though all the possible worlds where their observation differs do not exist.

As far as I know, every argument for utility assumes (or implies) that whenever you make an observation, you stop caring about the possible worlds where that observation went differently.

The original Timeless Decision Theory was not updateless. Nor were any of the more traditional ways of thinking about decision. Updateless Decision Theory, and subsequent decision theories corrected this mistake.

Von Neumann did not notice this mistake because he was too busy inventing the entire field. The point where we discover updatelessness is the point where we are supposed to realize that all of utility theory is wrong. I think we failed to notice.

Ironically the community that was the birthplace of updatelessness became the flag for taking utility seriously. (To be fair, this probably is the birthplace of updatelessness _because_ we took utility seriously.)

Unfortunately, because utility theory is so simple, and so obviously correct if you haven't thought about updatelessness, it ended up being assumed all over the place, without tracking the dependency. I think we use a lot of concepts that are built on the foundation of utility without us even realizing it.

(Note that I am saying here that utility theory is a theoretical mistake! This is much stronger than just saying that humans don't have utility functions.)"


