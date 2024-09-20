### Philosophical Foundations
Statistical methods (Bayesian vs Frequentist), Statistical models. Probability (objective vs subjective, frequency vs epistemic), fiducial, evidential probability, likelihoodism.
Methodological holism vs Methodological individualism
Syntactic vs Semantic Structures of theories
Social Ontology
Theory-ladeness and Value-ladeness
Population ethics (repugnant conclusion)

### Methodology
Multi-Agent Modelling (Mensa, Python)
Complex Systems Theory, Complexity Science. Chaos Theory, Self-organization Theory

### Psychology
Formal Learning Theory, Statistical Learning Theory (not good to model humans as Bayesian updaters?)
Moral Psychology 
Experimental Philosophy
Evolutionary Psychology
Cognitive architecture
Cognitive Psychology
Descriptive Decision Theory, Evidential Decision theory, Causal decision theory, Von-Neumann Morgenstern axioms and expected utility maximization, risk-averseness/risk-taking, Allais' Paradox, Ellsberg Paradox. Higher up positions are more rational, higher pressures. 
Ergodicity Economics (Ensamble average = time average) more rimligt med time average. Some decision theoretic paradoxes solved by ergodicity economics. 
Social Psychology

### Sociology
Sociophysics
Game theoretic contractarianism
Critical Juncture Theory
(Socio-)Cultural Evolution
Macrosociology
Formal Pragmatics [Formal pragmatics_final.pdf (blutner.de)](https://www.blutner.de/Documents/Formal%20pragmatics_final.pdf)
Sociolinguistics

### Economics
Thermonomics
Econphysics (Kinda cringe because it's often just used to predict stock markets) but also for wealth inequality. 
Ecological Economics (Cringe: Environmental Economics)
Welfare economics (Including Ramsey's intergenerational)
Formal social procedures/algorithms (cake-cutting theorem)
Game Theory (Iterative) (Problem of the commons)
Neoclassical Economics (coubb-doglas)
Post-Keynesian economics
Neo-Keynesian synthesis
Keynesian economics

### Pol Sci
Voting Methods
Policy Space (Linear Algebra)
Social Choice Theory (Arrow's Theorem, Gibbard's Theorem)
Jury Theorem's
Segregation multi-agent model
Selectorate Theory (Logic of political survival)

### Others
Category Theoretic social science (nvm just use theorems because Curry-Howard-Lambek). Maybe do it still though lol it's cool.
Meta-science
Cliodynamics, Cliometrics Historical covering-law explanations of history.
Analytical Marxism, Marxism as iterative coalition games (class analysis?)
International Relations Theory



Sectors:
Banks
Homes
Workplaces
Government
Environment
The Sun(?)

Arrows between sectors (money flow, also perhaps energy/matter flow?):
Loan
Interest
Savings
Salary
Purchase
Tax
Grants/Welfare


Smells like....category theory??? More like differential equations but I wanna sound cool


Are some of these theories merely a priori, or are all making predictions that can be tested? I'm thinking especially for voting theory, social choice theory, social procedures.


What are the fundamental axioms of these theories? Can they be formalized logically, can we proove contradictions between them? Can neoclassical economics and marxist economics be formalised and their conjunction can be shown to derive a contradiction? Is that important? Is there a functor between the category of marxism and the category of neoclassical?


Preferences assumptions on completeness and transitivieness. 
VNM-axioms add two more: irrelevance of third options and a fourth one


# Philosophical foundations
## Frequentist vs Bayesian Statistics

Important assumptions on the non-a priori fields: Induction, Probability and Statistics. Usual assumptions in most fields seem to assume that there is no sceptical solution to the problem of indcution, frequentist probability and statistics. T-tests, Chai squared and p-values are important. 

Most social science assumes Frequentist statistics.

[Philosophy of Statistics (Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/Entries/statistics/#ClaStaResCri)
"It should be emphasized that Bayesian statistics is not the sole user of an epistemic notion of probability. Indeed, a frequentists understanding of probabilities assigned to statistical hypotheses seems nonsensical. But it is perfectly possible to read the probabilities of events, or elements in sample space, as epistemic, quite independently of the statistical method that is being used. As further explained in the next section, several philosophical developments of **classical statistics employ epistemic probability, most notably fiducial probability (Fisher 1955 and 1956; see also Seidenfeld 1992 and Zabell 1992), likelihoodism (Hacking 1965, Edwards 1972, Royall 1997), and evidential probability (Kyburg 1961**), or connect the procedures of classical statistics to inference and support in some other way. In all these developments, probabilities and functions over sample space are read epistemically, i.e., as expressions of the strength of evidence, the degree of support, or similar."

Minor perspectives:
Fiducial Calculus, a kind of classical statistics with an epistemic view of probability 

[Akaike information criterion - Wikipedia](https://en.wikipedia.org/wiki/Akaike_information_criterion)

## Methodological Indivudalism vs Holism
Methodological holism: Explanans and Explanandum are macro-social variables. For example: We can explain increased loan taking with that there has been a decrease in interest rates. 

Methodological individualism: If the Explanans is a macro-social variable, then the Explanandum has to be a micro-social variable or psychological variable. For example: We can explain increased loan taking with that individual preferences/EU calculations for loans has increased. This may in turn be explained by decreased interest rate, which can in turn be explained by what individuals are doing (say the self-interest of central banks). 


### Microfoundations
Strong connections with Microfoundations
Företag $F_i$, aggregeting $F=\{F_1,\dots F_n\}$

Gives you macroeconomics with enough aggregation
In the Limit $n\rightarrow \infty$
Mass-simulation

No, more like statistical mechanics. Not computationally tractable. 

More neoclassical. Some leftist economists criticize this, abandoning microeconomics ENTIRELY(?). 

Steeve Keen
Axel Leijonhufvud (sociological analysis of neo-classicals, they are unscientific according to him).



## Syntactic Vs Semantic structure of scientific theories

Positivistic social science emphasise the idea of formal axioms (the syntactic view on the structure of scientific theories), while in the post-positivistic era, science emphasise the semantic view of scientific theories of models


"Writ large, social sciences appear to seek improved scientific legitimacy by copying the century-old linear deterministic modeling of classical physics—with economics in the lead ([2](https://www.pnas.org/doi/full/10.1073/pnas.092079799#core-b2))—at the same time natural sciences strongly rooted in linear determinism are trending toward nonlinear computational formalisms ([1](https://www.pnas.org/doi/full/10.1073/pnas.092079799#core-b1), [3](https://www.pnas.org/doi/full/10.1073/pnas.092079799#core-b3)). The postmodernist perspective takes note of the **heterogeneous-agent ontology of social phenomena**, calling for abandoning classical normal science epistemology and its **assumptions of homogeneous agent behavior, linear determinism, and equilibrium**."


"Social scientists need to thank postmodernists for their constant reminder about the reality of heterogeneous social agent behavior, but they need to stop listening to postmodernists at this point and instead study the epistemology of “new” normal science."

HAhahaha couldn't agree more


"Finally, social scientists need to take note of the other nonpostmodernist postpositivisms that give legitimacy: _scientific realism_, _evolutionary epistemology_, and the model-centered science of the _Semantic Conception_"

Is a return to positivism possible? I have argued this before in my blogpost on it


"Third, Campbell ([16](https://www.pnas.org/doi/full/10.1073/pnas.092079799#core-b16)) combines scientific realism with semantic relativism. Nola ([9](https://www.pnas.org/doi/full/10.1073/pnas.092079799#core-b9)) separates relativism into three kinds:

1. Ontologically nihilistic. “Ontological relativism is the view that what exists, whether it be ordinary objects, facts, the entities postulated in science, etc., exists only relative to some relativizer, whether that be a person, a theory or whatever” ([9](https://www.pnas.org/doi/full/10.1073/pnas.092079799#core-b9)).

2. Epistemologically nihilistic. Epistemological relativisms may allege that what is known or believed is relativized to individuals, cultures, or frameworks; what is perceived is relative to some incommensurable paradigm; and that there is no general theory of scientific method, form of inquiry, rules of reasoning or evidence that has privileged status. Instead they are variable with respect to times, persons, cultures, and frameworks.

3. Semantically weak. Semantic relativism holds that truth and falsity are “… relativizable to a host of items from individuals to cultures and frameworks. What is relativized is variously sentences, statements, judgments or beliefs” ([9](https://www.pnas.org/doi/full/10.1073/pnas.092079799#core-b9))."


"
1. A scientific realist postpositivist epistemology that maintains the goal of objectivity in science without excluding metaphysical terms.

2. A selectionist evolutionary epistemology governing the winnowing out of less probable theories, terms, and beliefs in the search for increased verisimilitude may do so without the danger of systematically replacing metaphysical terms with operational terms.

3. A postrelativist epistemology that incorporates the dynamics of science without abandoning the goal of objectivity.

4. An objectivist selectionist evolutionary epistemology that includes as part of its path toward increased verisimilitude the inclusion of, but also the winnowing out of the more fallible, individual interpretations and social constructions of the meanings of theory terms comprising theories purporting to explain an objective external reality."


The syntactic view:

"The advantage of this view is that there seems to be a common platform to science and a rigor of analytical results. This conception eventually died for three reasons: 

1.  axiomatic formalization and correspondence rules proved untenable and were abandoned;
2. newer 20th century sciences did not appear to have any common axiomatic roots and were not easily amenable to the closed-system approach of Newtonian mechanics.
3. parallel to the demise of the Received View, the Semantic Conception of theories developed as an alternative approach for attaching meaning to syntax."


Surely 2 is false? I have seen books that axiomatize modern physics at the minimum. 



## Different views on the philosophy of history

Positivistic (Comte, Hempel)

Teleological (Hegel)

Constructivist (Oakshot)

Post-Modernist. Power-Structures (Foucault)


My current view is positivistic. 


## Positivism Vs Interpretevism (in general?)

Last section goes over it within history to some extent. But it seems to be more general then that. 


## Free will vs Determinism, is social science fundamentall different from physical science?

Does this matter? If free will exists, and it's the acausal account that leads the world into genuinely indeterministic outcomes i.e from $W_1$ there exists $W_2$ and $W_2^*$ where an uncaused event $e$ in $W_1$ selects either world. Causality can be imagined as a directed graph from events to other events, changing the world state over time. Can be formalized in branching time temporal logic. 

Teleological causes?
[Methodological dualism - Wikipedia](https://en.wikipedia.org/wiki/Methodological_dualism)


## Social ontology


[Social Ontology (Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/entries/social-ontology/)








# A new way of doing social science?

So it seems a common view in most of the fields laid at the start is:
1. Frequentist Statistics
2. Methodological Holism(?)
3. Semantic Structure 

Can I do it with the complete opposite?
1. Bayesian Statistics
2. Methodological Individualism
3. Syntactic structure



There are also assumptions of rationality (NVM), not sure what to do with those. Assumptions on how to divide different sectors of the economy. Ecological economics adds the assumption of the environment as an extra sector. Thermonomics talk about more than money flow in the economy, also includes matter and energy. 

Sectors:
Banks
Homes
Workplaces
Government
Environment (Earth)
The Sun

Arrows between sectors (money flow, also perhaps energy/matter flow?):
Loan
Interest
Savings
Salary
Purchase
Tax
Grants/Welfare

![[The Economy.excalidraw]]




Different Economical Models:
- [IS–LM](https://en.wikipedia.org/wiki/IS%E2%80%93LM_model "IS–LM model")
- [AD–AS](https://en.wikipedia.org/wiki/AD%E2%80%93AS_model "AD–AS model")
- [Keynesian cross](https://en.wikipedia.org/wiki/Keynesian_cross "Keynesian cross")
- [Multiplier](https://en.wikipedia.org/wiki/Multiplier_(economics) "Multiplier (economics)")
- [Accelerator](https://en.wikipedia.org/wiki/Accelerator_effect "Accelerator effect")
- [Phillips curve](https://en.wikipedia.org/wiki/Phillips_curve "Phillips curve")
- [Arrow–Debreu](https://en.wikipedia.org/wiki/Arrow%E2%80%93Debreu_model)
- [Ramsey–Cass–Koopmans](https://en.wikipedia.org/wiki/Ramsey%E2%80%93Cass%E2%80%93Koopmans_model "Ramsey–Cass–Koopmans model")
- [Overlapping generations](https://en.wikipedia.org/wiki/Overlapping_generations_model "Overlapping generations model")
- [General equilibrium](https://en.wikipedia.org/wiki/General_equilibrium_theory "General equilibrium theory")
- [DSGE](https://en.wikipedia.org/wiki/Dynamic_stochastic_general_equilibrium "Dynamic stochastic general equilibrium")
- [Endogenous growth](https://en.wikipedia.org/wiki/Endogenous_growth_theory "Endogenous growth theory")
- [Mundell–Fleming](https://en.wikipedia.org/wiki/Mundell%E2%80%93Fleming_model "Mundell–Fleming model")
- [Overshooting](https://en.wikipedia.org/wiki/Overshooting_model "Overshooting model")
- [NAIRU](https://en.wikipedia.org/wiki/NAIRU "NAIRU")
- [Dynamic stochastic general equilibrium - Wikipedia](https://en.wikipedia.org/wiki/Dynamic_stochastic_general_equilibrium)




## Uncertain
- [Matching theory](https://en.wikipedia.org/wiki/Matching_theory_(economics) "Matching theory (economics)")

## Keynesian
- [Harrod–Domar](https://en.wikipedia.org/wiki/Harrod%E2%80%93Domar_model "Harrod–Domar model") (Direct competition with Solow-Swan)
- [Keynesian cross - Wikipedia](https://en.wikipedia.org/wiki/Keynesian_cross)


Post-Keynesian
- [The Oxford Handbook of Post-Keynesian Economics, Volume 1: Theory and Origins | Oxford Academic (oup.com)](https://academic.oup.com/edited-volume/38636)
Marc Lavoie (also fäktare)

## Neoclassical
- [Solow–Swan](https://en.wikipedia.org/wiki/Solow%E2%80%93Swan_model "Solow–Swan model") (Direct competition with Harrod-Domar) (Later lead to [Ramsey–Cass–Koopmans model](https://en.wikipedia.org/wiki/Ramsey%E2%80%93Cass%E2%80%93Koopmans_model))
- [Ramsey–Cass–Koopmans model](https://en.wikipedia.org/wiki/Ramsey%E2%80%93Cass%E2%80%93Koopmans_model)

## Austrian
[Austrian economics without extreme apriorism: construing the fundamental axiom of praxeology as analytic - PMC (nih.gov)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8550560/) 
Central Axiom: Man acts
Auxilliary axioms: Disutility of labor

## Marxist
Okishio theorem ([Nobuo Okishio - Wikipedia](https://en.wikipedia.org/wiki/Nobuo_Okishio#Fundamental_Marxian_theorem))
![[Pasted image 20240708181313.png]]




[Reasoning About Power in Games (Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/entries/logic-power-games/#AnalPowe) 
Sadly this article does not account for extensive form games, which I think is the heart of marxist analysis of class/power. Try to find papers which include that. 

## Modeling historical materialism game-theoretically

Marxist materialism as extended form coalition games with dynamics where the results over time impact coalitions in dynamic ways.

Individuals form self-interested coalitions to engage in game-theoretic payout situations to maximize their own utility function/preference relation.

At each timestep, they "vote" (impact) on how to change the world in some way. This changes the world-state at each time.

This in turn changes the members of the group, changes the number of members, changes their utility function



In Roemer's book on exploitation between 2 coalitions:
TODO: Add what I wrote in discord

## Modeling history with mathematical dynamics (cliodynamics)

[Cliodynamics - Wikipedia](https://en.wikipedia.org/wiki/Cliodynamics)
![[Pasted image 20240701141106.png]]



# Macrosociology

[s41599-023-01862-0.pdf (nature.com)](https://www.nature.com/articles/s41599-023-01862-0.pdf)


# The prospects of ancestor simulations

There may be impossible barriers towards figuring out this shit. So let's just run a simulation instead. 

Problems with initial conditions: Either you somehow figure out what the initial conditions where at some $t$, or run the laws backwards towards t. 

I think the second one sounds more reasonable, but any kind of approximation will lead to entropy increasing in that world, which is what we see in ours, so we might not be living in one. This is fine, that's not the point of this article anyways, but it might give some credence against Boströms argument. 



# Social Games


"The theory of social games: outline of a general theory for the social sciences"


I will try to answer the following criticism: 
"Creating a general social theory with games-for-fun as a starting point has been criticized, however, with scholars arguing that, unlike a game (for example, a game of chess between friends), the rules of social life are often complex, ambivalent, and open to different interpretations by different actors; that the actors may not con sciously know these rules and sometimes only discover them while playing the game; and that there may be substantial disagreement on the rules, which may be contested and changed by powerful players (Bourdieu, 1980; Garfinkel, 1967; Giddens, 1984; Rawls, 1955). Furthermore, critics have argued that, unlike games-for-fun, situa tions in social life are extremely complex; actors have to react to cues that belong to various, and sometimes conflicting, frames and contexts; and that a game does not have this complexity (Goffman, 1974). Finally, it has been argued that, unlike in games-for-fun, actors in social life are not in a make-believe world of a game, but in the real world. Thus, they cannot just stop the game, take “time out”, or ignore the consequences of their actions (Maynard, 1991)."



Rule's in games can be extremely complex and only discovered while playing. I forgot the name of it but there's a sci-fi game with extremely complex rules. D&D is another example of rules that are shifty and "open to interpretation" (whatever that means). 

We're always in a make-believe world. 

Sub-games and meta-games. Hierarchy of games. Me choosing to engage in rock-papers-scissors can be a sub-game in selecting say options for who joins which team in some sport.

There's no highest-level meta game, there's a bunch of games that connect in complicated ways. 


List of games including social one's, will fit together later:
- Rock Paper Scissors
- Monopoly
- Yahtzee
- Russian Roulette 
- Computer Games (many such cases)
- Sports

Social games:
- Security
- Emergency Services
- Markets
- Academia


Language is a central piece to use for moves in social games. Language may or may not be meaningful in their use within social games. They might not be, if they are meaningful for other reasons than their use then that might give an explanation for why they're used. 

"A theory of social games must necessarily make at least six assumptions about the individuals who play such games. I call this actor model “homo ludens” (for a comparable set of assumptions see Fligstein and McAdam, 2011)."


- First, homo ludens speaks and understands a language. Games are language-based, and, without language, the actor could not play a social game (Searle, 1995). 
  
- Second, homo ludens has basic human needs, such as the need for food, water, clothing, sleep, shelter, security, the sense of belonging, and social worth. 
  
- Third, homo ludens recognizes social games in her surroundings and can adopt and internalize their goals, understand their representations, and follow their rules, as well as also being able to a certain extent to explain them causally and to predict their outcomes. Much of the waking time of a homo ludens consists in scanning the world for clues of various games. 
  
- Fourth, homo ludens makes different games and their goals the center of her action, and uses them to fulfill her basic needs and motives. She does so by identifying her personal goals with the game goals. Thus, homo ludens seeks to gain social worth through being in a group of friends, to earn money through being employed in an organization, and to reach her place of work through driving through traffic. 
  
- Fifth, homo ludens creates a sense of “who she is”, of her own “identity”,by monitoring and judging her relative performance in the game and by identifying with a game that she or others are playing. She may also create identity by identifying with the leaders of some of the games that she plays. 
  
- Finally, homo ludens will try to satisfy her needs as much as possible by expending as little energy/input on a game as possible. She will try to balance her engagement in dif ferent games to maximize the satisfaction of her overall needs. This is not to say that homo ludens always calculates in a perfectly rational way. Rather, it is assumed that homo ludens tries overall to “play the games well”.



- Players
- Resources
- Actions/moves
- Goals
- Rules
- Objects
- Representations/Signs
- Space and Time. 
  Idea: players must agree on a geometry beforehand, implicitly euclidean in almost all social games.  
- Outcomes
- Context



State changes. Branching time temporal logic? Causal logic? Spatial logic? So many ways to formalize this! Payout matricies, game theory.


# Game Theory

[(Analytical Methods for Social Research) Nolan McCarty, Adam Meirowitz - Political Game Theory_ An Introduction-Cambridge University Press (2007).pdf](file:///C:/Users/offic/Downloads/(Analytical%20Methods%20for%20Social%20Research)%20Nolan%20McCarty,%20Adam%20Meirowitz%20-%20Political%20Game%20Theory_%20An%20Introduction-Cambridge%20University%20Press%20(2007).pdf)
[Hobbes's State of Nature: A Modern Bayesian Game-Theoretic Analysis | Journal of the American Philosophical Association | Cambridge Core](https://www.cambridge.org/core/journals/journal-of-the-american-philosophical-association/article/hobbess-state-of-nature-a-modern-bayesian-gametheoretic-analysis/A5369CCA6E040E5381FBBD6A603003B7)






# Putting it all together




