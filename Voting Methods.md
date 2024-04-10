[Voting Methods (Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/entries/voting-methods/)
An interesting voting method is pairwise majority voting, where candidates which win the most pairwise rankings wins. 
![[Pasted image 20230704193856.png]]
![[Pasted image 20230704193839.png]]
"Consult, for example, Riker 1982, Mackie 2003, and Christiano 2008 for a more comprehensive analysis of the above question, incorporating many of the issues raised in this article."


Voting sincerely vs Voting strategically
"In this case, a voter selects a ballot that she _expects_ to lead to her most desired outcome given the information she has about how the other members of the group will vote. Strategic voting is an important topic in voting theory and social choice theory (see Taylor 2005 and Section 3.3 of List 2013 for a discussion and pointers to the literature),"



First past the post/Plurality rule is when each voter selects one candidate (or none if voters can abstain), and the candidate(s) with the most votes win. 

It has multiple problems, for example, the Condorcet loser can win an election. ':![[Pasted image 20230705104823.png]]
"One response to the above phenomenon is to require that candidates pass a certain threshold to be declared the winner."

"See Laslier 2012 for further criticisms of Plurality Rule and comparisons with other voting methods"


![[Pasted image 20230705105547.png]]
![[Pasted image 20230705105559.png]]


## Ranking Candidates

Empirical tests:
[Ranked-choice voting in the United States - Wikipedia](https://en.wikipedia.org/wiki/Ranked-choice_voting_in_the_United_States)


![[Pasted image 20230705110310.png]]
![[Pasted image 20230705110408.png]]

Idea: One problems with Borda count is that weighting doesn't work. For example, I might vastly prefer candiate A over all others, while someone else might only slightly prefer candidate A over all others. The strenght of preference could vary a lot, but this information is lost under Borda count. 

**Plurality Voting with instant runoff**
[Math Alive Voting 1 (princeton.edu)](http://web.math.princeton.edu/math_alive/6/Lab1/PluralityRO.html)


"**Negative Voting**:  
Each voter is allowed to choose one candidate to either vote _for_ (giving the candidate one point) or to vote _against_ (giving the candidate –1 points). The winner(s) is(are) the candidate(s) with the highest total number of points (i.e., the candidate with the greatest score, where the score is the total number of positive votes minus the total number of negative votes)."
Idea: Negative voting might lead to center bias. 


"**Approval Voting**:  
Each voter selects a _subset_ of the candidates (where the empty set means the voter abstains) and the candidate(s) with selected by the most voters wins."

"Approval voting forces voters to think about the decision problem differently: They are asked to determine which candidates they _approve_ of rather than selecting a single candidate to voter _for_ or determining the relative ranking of the candidates. That is, the voters are asked which candidates are above a certain “threshold of acceptance”. Ranking a set of candidates and selecting the candidates that are approved are two different aspects of a voters overall opinion about the candidates. They are related but cannot be derived from each other."

"Approval voting has been extensively discussed by Steven Brams and Peter Fishburn (Brams and Fishburn 2007; Brams 2008). See, also, the recent collection of articles devoted to approval voting (Laslier and Sanver 2010)."

"See Brams and Sanver 2009, for examples of voting methods that ask voters to both select a set of candidates that they approve _and_ to (linearly) rank the candidates."

"Brams (2008, Chapter 2) proves that if there is a unique Condorcet winner, then that candidate may be elected under approval voting (assuming that all voters vote _sincerely_: see Brams 2008, Chapter 2, for a discussion). Note that approval voting may also elect other candidates (perhaps even the Condorcet loser). Whether this flexibility of Approval Voting should be seen as a virtue or a vice is debated in Brams, Fishburn and Merrill 1988a, 1988b and Saari and van Newenhizen 1988a, 1988b."

Idea: Approval voting is like negative voting except the scores are 1 and 0 and you can select as many proposals/candidates as you'd like in either group.

"**Cumulative Voting**:  
Each voter is asked to distribute a fixed number of points, say ten, among the candidates in any way they please. The candidate(s) with the most total points wins the election.

**Score Voting (also called Range Voting)**:  
The grades are a finite set of numbers. The ballots are an assignment of grades to the candidates. The candidate(s) with the largest average grade is declared the winner(s).

Cumulative Voting and Score Voting are similar. The important difference is that Cumulative Voting requires that the sum of the grades assigned to the candidates by each voter is the same. The next procedure, proposed by Balinski and Laraki 2010 (cf. Bassett and Persky 1999 and [the discussion of this method](http://rangevoting.org/MedianVrange.html) at rangevoting.org), selects the candidate(s) with the largest _median_ grade rather than the largest mean grade.

**Majority Judgement**:  
The grades are a finite set of numbers (cf. discussion of common grading languages). The ballots are an assignment of grades to the candidates. The candidate(s) with the largest median grade is(are) declared the winner(s). See Balinski and Laraki 2007 and 2010 for further refinements of this voting method that use different methods for breaking ties when there are multiple candidates with the largest median grade."

![[Pasted image 20230706125918.png]]

"Consult Balinski and Laraki 2010 amd Morreau 2016 for an extensive discussion of the types of considerations that influence the choice of a grading language."

"Brams and Potthoff 2015 argue that two grades, as in Approval Voting, is best to avoid certain paradoxical outcomes. To illustrate, note that, in the above example, if the candidates are ranked by the voters according to the grades that are assigned, then candidate C is the Condorcet winner (since 3 voters assign higher grades to C than to A or B). However, neither Score Voting nor Majority Judgement selects candidate C."

"Consult Balinski and Laraki 2010, 2014 and Edelman 2012b for arguments in favor of electing candidates with the greatest median grade; and Felsenthal and Machover 2008, Gehrlein and Lepelley 2003, and Laslier 2011 for arguments against electing candidates with the greatest median grade."


[RangeVoting.org - Balinski & Laraki's "majority judgment" median-based range-like voting scheme](https://rangevoting.org/MedianVrange.html)
Average-based range voting under the assumption of honest voting dissallows the tyranny of the majority.
"Which brings us to our point: **Median-based range voting seems to be _more vulnerable_ to tyranny of majority** than average-based range voting. Specifically, imagine with range 0-to-9, that there are exactly two kinds of votes: strong-preference votes "kill=0, live=9" (cast by honest Jews) and weak-preference votes "kill=5, live=4" cast by honest non-Jews. In such a scenario, if the Jews exceed 10% of the population, average based range voting will let them live. However, median-based range voting will _always_ kill the Jews, no matter what percentage they are (provided they are a minority) and no matter what the particular four numerical scores (here 0, 9, 4, and 5) are."


## Quadratic Voting

![[Pasted image 20230706133833.png]]

"The first argument is that it is ambiguous whether the Quadratic Voting decision really outperforms a decision using majority rule from the perspective of utilitarianism (see Driver 2014 and Sinnott-Armstrong 2019 for overviews of utilitarianism)."

"The second argument is that any vote-buying mechanism will have a hard time meeting a legitimacy requirement, familiar from the theory of democratic institutions (cf. Fabienne 2017)."

Idea: On the second argument, no need to use real money to buy votes, everyone can instead have an equal pool of votes that they can use to spend on votes over a long period of time or per proposal vote. 


![[Pasted image 20230706134331.png]]


## Voting Paradoxes

"Consult Saari 1995 and Nurmi 1999 for penetrating analyses that explain the underlying mathematics behind the different voting paradoxes."

Condorcets paradox means some voting methods have preference cycles, implying that there does not exist a condorcet winner.

![[Pasted image 20230706170831.png]]

Voting methods which elect the Condorcet winner (if there is one) are called Condorcet consistent. 

Another paradox: Failures of monotonicity, where monotonicity generally states that candidates with better support are better off in the elections. "There are different ways to make this idea precise (see Fishburn, 1982, Sanver and Zwicker, 2012, and Felsenthal and Tideman, 2013)."

![[Pasted image 20230707181827.png]]
# 😱😱😱😱
# 😜
 

No Show paradoxes: Whenever more people show up to vote which say, prefer B to C, yet B now looses instead of wins. 
![[Pasted image 20230708125013.png]]

# 🙀
![[Pasted image 20230708125105.png]]


**Multiple Districts Paradox**: You'd expect that someone winning in all districts would win the entire election, plurality does this, but not all voting methods do! Coombs rule is susceptible to the MDP!

![[Pasted image 20230708131627.png]]
However, by combining the districts, A is now the winner instead!

"The other voting methods that are susceptible to the multiple-districts paradox include Plurality with Runoff, The Hare Rule, and Majority Judgement. Note that these methods are also susceptible to the no-show paradox. As is the case with the no-show paradox, every Condorcet consistent voting method is susceptible to the multiple districts paradox (see Zwicker, 2016, Proposition 2.5). I sketch the proof of this from Zwicker 2016 (pg. 40) since it adds to the discussion at the end of Section 3.1 about whether the Condorcet winner should be elected."

![[Pasted image 20230708134642.png]]
![[Pasted image 20230708134652.png]]

![[Pasted image 20230708151224.png]]


**STAR voting**
[(103) STAR Voting Explained in Less than One Minute #shorts - YouTube](https://www.youtube.com/shorts/Zy86WYmHvMk)





Concent-based consensus sociocracy: unanimity rule, but instead of everyone having to vote yes, they simply don't need to vote no. And if they vote no, they have to give a reason for it.

Styrelsen i positiva pengar t.ex, where there are working groups and there are representatives from each group where they are a part of styrelsen and take these sociocratic decisions. 

Occupy wall street had a similar model.

Big flaw: one sabouteur can just say no and make up any reason for saying no. 


[Independence of irrelevant alternatives - Wikipedia](https://en.wikipedia.org/wiki/Independence_of_irrelevant_alternatives)
"Despite being a weaker criterion (i.e. easier to satisfy) than IIA, LIIA is satisfied by very few voting methods. These include [Kemeny-Young](https://en.wikipedia.org/wiki/Kemeny%E2%80%93Young_method "Kemeny–Young method") and [ranked pairs](https://en.wikipedia.org/wiki/Ranked_pairs "Ranked pairs"), but not [Schulze](https://en.wikipedia.org/wiki/Schulze_method "Schulze method"). Just as with IIA, LIIA compliance for rating methods such as [approval voting](https://en.wikipedia.org/wiki/Approval_voting "Approval voting"), [range voting](https://en.wikipedia.org/wiki/Range_voting "Range voting"), and [majority judgment](https://en.wikipedia.org/wiki/Majority_judgment "Majority judgment") require the assumption that voters rate each alternative individually and independently of knowing any other alternatives, on an absolute scale (calibrated prior to the election), even when this assumption implies that voters having meaningful preferences in a two candidate election will necessarily abstain."