https://plato.stanford.edu/entries/voting-methods/
https://www.radicalxchange.org/concepts/plural-voting/
https://plato.stanford.edu/entries/dynamic-choice/
https://plato.stanford.edu/archives/win2021/entries/social-procedures/
https://plato.stanford.edu/archives/win2021/entries/arrows-theorem/
https://plato.stanford.edu/archives/win2021/entries/jury-theorems/
https://plato.stanford.edu/entries/social-choice/



$f(<v_1, \dots v_n>)$ for $n$ voters. Decision procedure is defined extensionally, not intensionaly (i.e no rule, just a mapping from inputs to outpust). $v_i$ can vote either 1, -1 or abstain 0. 

Aggregation rules sum up votes, sum up weighted votes.

A dictator $v_i$ in an aggregation system if $f(<v_1, \dots v_n>)=v_i$ .



"The Rae-Taylor theorem then states that if each individual has an equal prior probability of preferring each of the two alternatives, majority rule maximizes each individual’s expected utility (see, e.g., Mueller 2003)."

![[Pasted image 20230629202446.png]]

Arrow's theorems states that not all five of the following principles can hold in any preference aggregation function F over a domain of preference relations $<R_1,\dots,R_n$ for n individuals:

![[Pasted image 20230630212001.png]]

(And also the number of proposals are strictly over 2)

This then applies to a large range of possible cases
![[Pasted image 20230630213303.png]]


The liberal paradox is really interesting, it states that weak pareto efficiency, minimal liberalism and two other conditions cannot be the case at once. 
![[Pasted image 20230630221547.png]]

![[Pasted image 20230630221608.png]]

"As shown by Condorcet’s paradox, this may produce an empty choice set. By contrast, plurality rule and the Borda count induce social choice rules that always produce non-empty choice sets."
![[Pasted image 20230702104604.png]]

![[Pasted image 20230702104816.png]]
![[Pasted image 20230702104845.png]]
"Moulin (1980) has shown that when the domain of the social choice rule is restricted to single-peaked preference profiles, pairwise majority voting and other so-called ‘median voting’ schemes can satisfy the rest of the conditions of the Gibbard-Satterthwaite theorem. Similarly, when collective decisions are restricted to binary choices alone, which amounts to dropping the range constraint, majority voting satisfies the rest of the conditions. Other possible escape routes from the theorem open up if resoluteness is dropped. In the limiting case in which all alternatives are always chosen, the other conditions are vacuously satisfied."

"The requirement of strategy-proofness has been challenged too. One line of argument is that, even when there exist strategic incentives in the technical sense of the Gibbard-Satterthwaite theorem, individuals will not necessarily act on them. They would require _detailed information_ about others’ preferences and _enough computational power_ to figure out what the optimal strategically modified preferences would be. Neither requirement is generally met. Bartholdi, Tovey, and Trick (1989) showed that, due to computational complexity, some social choice rules are resistant to strategic manipulation: it may be an NP-hard problem for a voter to determine how to vote strategically. In this vein, Harrison and McDaniel (2008) provide experimental evidence suggesting that the ‘Kemeny rule’, an extension of pairwise majority voting designed to avoid Condorcet cycles, is ‘behaviourally incentive-compatible’: i.e., strategic manipulation is computationally hard."

Idea: Even if they were NP-hard to do perfectly, there could exist P-hard approximations which people may use.

  
"Dowding and van Hees (2008) have argued that not all forms of strategic voting are normatively problematic. They distinguish between ‘sincere’ and ‘insincere’ forms of manipulation and argue that only the latter but not the former are normatively troublesome. Sincere manipulation occurs when a voter (i) votes for a compromise alternative whose chances of winning are thereby increased and (ii) genuinely prefers that compromise alternative to the alternative that would otherwise win. For example, in the 2000 US presidential election, supporters of Ralph Nader (a third-party candidate with little chance of winning) who voted for Al Gore to increase his chances of beating George W. Bush engaged in sincere manipulation in the sense of (i) and (ii). Plurality rule is susceptible to sincere manipulation, but not vulnerable to insincere manipulation."

Section 4 discusses alternative ways of enriching the theory of social choice to not merely be a preference ordering of states of affairs, which allows one to avoid the forementioned impossibility theorems such as Arrows theorem. 

It also discusses different ways of constructing welfare functions $W_1,\dots W_n$ for $n$ in individuals which maps from state of affairs to the real numbers which determine the welfare of that individual under those state of affairs. 

Some of these allow for inter and intra personal comparisson of utilities, so sometimes only squishing/stretching and moving is allowed i.e $W^* = \alpha W_i(p) + \beta$. Which doesn't allow for interpersonal comparrison. This comparissing is important because of the following:
![[Pasted image 20230703085923.png]]

"Once we introduce interpersonal comparisons of welfare levels or units, or zero comparisons, there exist possible SWFLs satisfying the analogues of Arrow’s conditions as well as stronger desiderata. In a welfare-aggregation context, Arrow’s impossibility can therefore be traced to a lack of interpersonal comparability (for detailed analyses, see Sen 1977 and Roberts 1980)."

Turns out certain ways of intra and inter-personal comparisson of welfare function there does exist a social welfare function that upholds all of the criterions in Arrow's theorem! Not only that, but even stronger criterions aswell!

ONC, CNC does not have any SWFL's
OLC, CUC, and ONC+0 does have SWFL's

![[Pasted image 20230703093404.png]]
Rawls indifference principle! Which satisfies not just the weak, but also the strong pareto principle.

![[Pasted image 20230703101458.png]]





Future discussion with online (some people call her discount katten lmao kinda mean tbh)

In your example, there were three possible states of affairs 
$x = \text{a,b,c,d watches movie A}$
$y = \text{a,b,c,d watches movie B}$
$z =$ a,b watches movie A while c,d watches movie B

In which case z is weakly preferred by all agents, x is weakly prefered by a and b while y is weakly prefered by c and d. This means that by majority voting, z is selected. Not only that, but it also the pareto efficient outcome (maximises everyone's utility with no other possibility increasing utility for anyone).

However, not all aggregation rule are pareto efficient, and will require, indeed, "coercion", to achieve optimal outcome as many people as possible. 


Idea: Connections with [[Ramsey intergenerational welfare economics]] where the preference relation is about possible consumption patterns. Look more into the book on welfare economics by springer.  