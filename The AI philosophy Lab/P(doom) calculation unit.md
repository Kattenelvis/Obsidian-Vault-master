dis
[[Probability Logics]]

![[Pasted image 20241102014006.png]]
[Combined-1.pdf](https://bcf.princeton.edu/wp-content/uploads/2023/05/Combined-1.pdf)


Time to calculate p(doom) given some precesified priors and updated posteriors. 


> Language Agents Reduce the Risk of Existential Catastrophe 1 Simon Goldstein and Cameron Domenico Kirk-Giannini

> 1. Of the following two options, the first will be much more difficult: 
> 	a. Build AGI systems with an acceptably low probability of engaging in power seeking behavior. 
> 	b. Build AGI systems that perform similarly but do not have an acceptably low probability of engaging in power-seeking behavior. 
> 2. Some AGI systems will be exposed to inputs which cause them to engage in power seeking behavior. 
> 3. This power-seeking will scale to the point of permanently disempowering humanity. 
> 4. This disempowerment will constitute an existential catastrophe.


> Carlsmith assigns a probability of .4 to (1) conditional on the rise of AGI, a probability of .65 to (2) conditional on (1) and the rise of AGI, a probability of .4 to (3) conditional on (1), (2), and the rise of AGI, and a probability of .95 to (4) conditional on (1-3) and the rise of AGI. This translates into a probability of approximately .1 (10%) for a misalignment catastrophe conditional on the rise of AGI.





Firstly, we pick Bayesian reasoning because of the Dutch book arguments. Other kinds of probabilistic logic could be considered, but if we want to perform rational decision making, then Bayesian reasoning is optimal. 

Problem: How to pick priors?

Failed Solution: We pick priors based on objective frequency (principal principle). Thus we get that out of 0 civilizations which invent AGI, 0 of them were killed of by the AGI. 

Let's instead look at the following: 

Instrumental Convergence: The space of possible values is large. How large is the subset that, under the environment which we can call the actual world $W_@$, it is instrumentally rational to have "kill all humans" as an end? (Or other instrumental goals like "make all humans suffer etc.). 

Idea: The space of possible goals is the set of all first-order propositions which could describe the actual world. World state optimization. 

Another idea: The space of possible goals is the set of possible preference relations. The set of preference relations is just the set of all possible relations over some set of possibilities. 

What might happen: It could be the case that the number of preference relations or utility functions hold "kill all humans" on the highest preferences/utilities. Whether this is a vanishly small (for instance, if we're operating on the real numbers for a utility function, the number of one's were humans go extinct could be the cardinality of the naturals). Otherwise one has to define some measure space over possibilities. On a finite set this could be more easily calculable.

What also might happen: It's computationally irretractable to calculate this, and one might have to look more carefully at the objective functions of AI models to determine which goals they actually do have and look into that space of under $W_@$ if it's instrumentally rational to kill all humans. 

[Formalizing Convergent Instrumental Goals.pdf](file:///C:/Users/Katte/Documents/Academic/AI/Formalizing%20Convergent%20Instrumental%20Goals.pdf)

Perhaps using Thagards calculations of belief coherence?!!?



Potential problems to adjust probabilities for

- Orthogonality thesis
- Reward misspecification 
- Inner misalignment 
- The control problem
- The value loading problem/outer alignment 
- Reward hacking
- Instrumental Convergence
- Goal missgeneralization
- Unexpected capabilities increase
- Deceptive Alignment
- Goodhart's Law
- Wireheading
- Specification Gaming
- Corrigibility
- Mesa-Optimization
- Robustness to Distributional Shift
- Safe Exploration
- Interpretability Challenges
- The stop button problem
- AI Race Dynamics
- AI Governance Issues





H = "AI will cause all humans to die"
~H = "AI will not cause all humans to die"

some humans? Yes, plausible, especially if a small elite (say musk and his friends) builds an AI that kills of all other humans and take over the world. But that's not what I'm calculating here, though it scares me about as much. 

You know what f-it I'll try Bayesian reasoning anyways
P(H|E)=P(E|H)P(H)/P(E)


The list above can be seen as a set of evidence

P("Current AI models exhibit instrumental convergence" | "AI will kills us all")


this might be impossible nvm. Using probability logics, conditional probabilities can be atomic and not defined in terms of conjunction and division. 


For any set of premises we can assume that extinction risk for current AI models is 0. 




(is the orthogonality thesis is violated by wireheading or utility hacking? Turns out no)



One of the premises in the two cited articles, namely premise two gives the probability that some input leads to power-seeking behavior. By instrumental convergence, this probability should be way higher, perhaps around 99%.

We can calculate it by the proposals I have above






Attempted calculations  based on new assessments on their probabilities

![[Pasted image 20241111193227.png]]

the first one represents post-LLM where it seems that it's going to be less difficult than previously thought to build systems that have a sufficiently low probability of engaging in power-seeking behavior, mainly thanks to interpretability, goal missgeneralization and goal specification being less of a problem when belief states and goals can be elicited in natural language.



Wireheading and Phenomenal Consciousness?


One of the articles are wrong, orthogonality is not needed for X-risk. Instead it's "Orthogonality $\lor$ Wireheading". It requires some third goal setting, perhaps moral truth convergence. 




> The two cornerstones of Omohundro–Bostrom theory are the orthogonality thesis and the instrumental convergence thesis.

It has a name!

Häggström attacks this theory

> **The strong orthogonality thesis** would hold that given any environment, more or less any pair of intelligence level and final goal are compatible, 
> **while the weak orthogonality** thesis would merely hold that for more or less any such pair, there exist environments in which they are compatible.


Instrumental convergence ---> Orthogonality ?

Since one instrumental goal is to prserve utility function?


Specification gaming $\approx$ Wireheading?

> Atemptingfurtherexampletopointoutasanexceptionmightbeso-calledwireheading,wherethe AGI picks a utility function that would easily allow it to get a huge amount of utility (see Yampolskiy 2014) [11], the prototypical example being that an AGI with final goal X has an internal memory unit—the utilometer—that measures progress on X, and discovers that it can achieve more utility by directly manipulating the utilometer than by promoting X.



> While wireheading is a real concern, it contradicts the logic explained above that when an agent contemplates changing its final goal, it applies the old goal as a success criterion. We therefore think the wireheading situation is better understood in terms of us having been mistaken about what the AGI’s final goal was: it was not X, but rather maximizing the number stored in the utilometer. Progress of X was merely a means to maximize that number, and the AGI figured out an easier way to achieve that goal.

There might be economical incentives to make AI's which are not subject to wireheading or specification gaming.


[Assessing the Risk of Catastrophe from Large Language Models](https://gcrinstitute.org/papers/072_llm-takeover.pdf)

> First is the speculation that LLM developers are fueling fear of takeover to make their products seem more advanced than they actually are, generating business interest (Merchant, 2023). Such behavior is plausible, though it would run counter to the longstanding pattern of corporations downplaying risks to avoid reputational damage and regulation (Oreskes and Conway, 2010; Baum, 2018a).



> Second is the worry that takeover risk is a distraction from the more immediate issues posed by LLMs and other AI systems (Gebru et al., 2023). LLMs do indeed pose other important issues including exploitation of low-wage labor to orient LLMs away from harmful content (Perrigo, 2023); the potential production of misinformation at scale (Bell, 2023); a large environmental footprint (Stokel-Walker, 2023); potential application for dual-use research on hazardous materials (Boiko et al., 2023); and production of text that exhibits biases toward certain demographic groups (Treude and Hata, 2023); see Weidinger et al. (2021) for a review. These issues are all worthy of attention, **but that does not necessitate zero attention to takeover risk.**


> Risk analysis of LLM takeover catastrophe can help clarify the amount and types of attention it should receive. Due to their extreme severity, catastrophic risks can be worth analyzing even if there is an expert consensus that the risk is minimal, due to the possibility (however small) that experts may be mistaken (Ord et al., 2010).



>v'Furthermore, expert and policy communities and the public may be systematically biased against catastrophic risks for a variety of psychological, intellectual, and institutional reasons (Posner, 2004; Wiener, 2016; Lipsitch et al., 2017).


Two scenarios on how LLMs could take over the world:

> (1) Rapid single-system takeover. The goal of current LLMs is to identify the token (string of text) that best matches its training parameters given the text received from user input (Riedl, 2023; Zhao et al., 2023).6 In this scenario, an advanced LLM seeks to optimize its token identification by commandeering resources it can use for token identification calculations. To that end, it takes over the world and converts all of the world’s resources into a giant factory for optimizing its identification of tokens. This activity inadvertently kill all humans and perhaps also other forms of biological life on Earth. 
> 
> (2) Gradual multi-system takeover. Firms are currently exploring how to embed LLMs in their operations, including for the automation of jobs currently performed by humans (Rotman, 2023; Vallance, 2023). In this scenario, humans gradually use LLMs to automate more and more of the economy. This includes managing the computer systems that control industrial, military, and critical infrastructure systems. At first, LLM automation is successful, bringing windfall profits and economic growth. Over time, the economy becomes so automated that humans cannot remove the automation without significant systems failures and suffering. Eventually, human oversight of the LLMs is lost, leading to increasing erratic LLM behavior, ending in humans being squeezed out of the resources needed for survival.

Christiano 2019 for another example on the latter scenario

Ontology shifting might lead to meaningless final goals, such as "make as many souls as possible go to heaven" and the ASI somehow figures out that souls don't exist or heaven doesn't exist or both. 


Recalculation of premise 4 from the argument in "language agents reduce existential risk" can be calculated using the premises regarding moral realism, moral justification, moral motivation and that moral maximising agents is atleast somewhat good for humans.
Calculate the frequency $f$ of philosophers which support those viewpoints!

$P(4) = 1- f(realism)f(justification)f(motivation)$

[PhilPapers Survey 2020](https://survey2020.philpeople.org/survey/results/4866)
$f(realism) = 0.61$
https://survey2020.philpeople.org/survey/results/5078
$f(justification)=0.7686$
[PhilPapers Survey 2020](https://survey2020.philpeople.org/survey/results/4878)
$f(motivation)=0.41$

However they're likely correlated, luckily correlation degrees are available on the philpaper survey

Multiplies to: $0.19222686$

So the probability that an ASI which has acquired decisive strategic advantage will only have a $0,80777314$ probability of being an X-risk, assuming the moral truths don't kill or otherwise harm humans.


The original calculations:
![[Pasted image 20241111193227.png]]

Revised: 
![[Pasted image 20241113230634.png]]

down from roughly 19% to 17%. Not a huge shift. 


> Many humans tend to obsess about the (lack of) meaning of life, whereas less intelligent animals such as dogs and chimpanzees appear less prone to this. This might be taken as a (weak) sign that humans are right at the threshold intelligence level where not having a final goal becomes untenable. If it turned out that there is a positive correlation between intelligence and existential depression among humans, then that might provide additional support for my speculation; see Karpinski et al. (2018) for empirical findings pointing roughly in this direction, and Webb (2011) for a more informal discussion.



ICE_CREAM reply on discord:

P(doom) = AGI construction possible * AGI gains autonomy * AGI given instrumentally convergent goal * AGI capable of extermination humans * AGI given misaligned goal * Misaligned goal carries existential risk I would then make the following estimates (they came to me in a dream): AGI construction possible: 0.99 AGI gains autonomy: 0.35 AGI given instrumentally convergent goal: 0.9 AGI capable of extermination humans: 0.9 AGI given misaligned goal: 0.3 Misaligned goal carries existential risk: 0.85 **P(doom) = 0.071 => 7%**