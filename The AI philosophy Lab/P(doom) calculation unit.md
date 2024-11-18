
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