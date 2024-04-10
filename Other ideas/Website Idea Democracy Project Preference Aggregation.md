

## General idea
4 different sections: An interactive teaching section, a blog/education section (were I write about say, social choice theory e.t.c), a page were people can vote and send links to friends e.t.c to vote on decisions, and a playground for different people to play around with. 



## Blog/Education section
Pretty basic, won't write much about this section
Just putting politics related blog posts there aswell. Link the rest of my stuff

## Voting page

Sendable links to friends for voting


## Social Choice Playground

Multi-agent model

There will be a world state

Each agent will have a belief state and a preference relation. 

Votings will commence and the aggregated system in place will change the world state. 

Different voting procedures to explore (score voting, star voting, approval, range, majority, condorcet, unanimity, 2-runoff, cardinal, quadratic, cumulative, schulze, kemeny-young, ranked pairs (Tideman), ...)

Turning on or off different assumption on individual agents (such as transitivity, completeness, IIA, Archimedean Property) and such. 

Information on impossible states of affairs due to impossibility theorems (arrows, gibbard-satterthwaite, liberal paradox)


Testing on what happends in different scenarios.
Test: If only one voter exists, given that their preferences do not have an intransitive loop at the height of their preference relation, should converge to their top preference. Otherwise it should loop in the intransitive loop (the agent will never be happy, poor guy). I.e a 1-person democracy degenerates into a "dictatorship".


Preference relationship "editor", where one can create a poset preference relation and give some set of the population that preference relationship. 

## Interactive Teaching
Use tools above to teach people on different decision methods in a pedagogical way, like that game theory game I need to find again. 

## Technical stuff

Saves into local storage, but you can create an account to save for longer period of time

Django Backend (so I can learn django) but it would be cool to use some kind of frontend that wasn't svelte just to learn something new. Something like Elexir?



| Design problem: | Our implementation: |
| ---- | ---- |
| Voting method (and betting method). | Score voting where scores approximate probabilities. |
| How ties are handled if there is supposed to be a single winner. | The winner is randomized among the tied proposals. |
| How to decide when there can only be one winner and when <br>there can be many. | This is left to a group to decide by a poll, which by default should have a single winner. |
| How to divide basic types of subject areas. | Delegation areas, prediction areas and implementation areas are the same. |
| How to define subject areas. | Hyper tag self regulating subject tags. |
| Time-separated phases, simultaneous phases, mixed phases can be chosen. | Time-separated phases. |
| Phases, their order and permissions. | Which phases we have and their order, as well as which role does what during each phase has been described previously, see figure 2. |
| Meta-delegation. | Meta-delegation is allowed per default. |
| ‘Optimal’ aggregation of prediction bets. We want the convergence speed to be as fast as possible. | Taking the weighted average of optimal predictor bets weighted by prediction scores (per proposal). <br><br>  <br><br>We have not discussed what is optimal considering the convergence speed, there is other work considering this that is outside of the main scope of this article (Goodin & Spiekermann, 2018). |
| Prediction score function. | Brier score function. |
| Initial prediction scores. | It is possible to import or estimate prediction scores before using PLD, using correlations with for example PhDs in some subject area where they get a starting boost compared to someone without previous merit. This, however, is something that organizations should be very careful with, because a study on such a correlation needs to be about the predictions that end up in the subject area and really cover it to a large extent. |
| Removal of items. | Not allowed (note that bets are not items, they can be changed during the betting phase but not after it). |
| The regulation of which predictions are within the area. | Self-regulated by competing expert predictors, and a penalty if predictors do not bet on predictions that pass:  <br><br>1. The number of bets on the proposal, weighted by prediction scores, passes a threshold value number 1.<br>    <br>2. At least two different bets on the proposals, made by predictors with prediction scores over some threshold value number 2, passes a threshold value number 3 in difference. |
| Alignment score function. | This is left open, but some similarity between voters and delegates, either by how the voter stated voting history or by their stated goals, and then compared to how the delegate has voted will probably be used. Some AI solution that is trained seems to fit in well here. |
| Parameter values. | We have left this open. This includes values of quorums, the prediction bet phase thresholds, the penalty value, the discrete interval used for score voting and times of the phases etc. |

