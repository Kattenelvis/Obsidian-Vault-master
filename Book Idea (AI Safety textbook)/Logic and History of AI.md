

- Logic and History of AI
	- Good old AI paradigm
		- Narrow: Word2Vec, Mini-world agents
		- Cyc, databases, formal ontology
		- General: Gödel machines, AIXI
	- Why didn't it work?
		- Frame Problem (HAI?)
		- Modal Fusion systems have to high time-complexity
	- Current AI models
		- Statistical Learning
		- Neural Networks and Backpropagation 
		- Reinforcement Learning
		- Transformer architecture
		- Generative Adversarial Networks, Diffusion models, LLMs
	- Frontiers
		- Corrigible, Explainable, Truthful, Interpretable and Aligned AI
		- Resurrection for GOAI? Neural logic





z
## Representation AI

Let's say you want to represent the external world. Representations stores properties about objects, such that for all object $x$ with $\{P_1x,\dots P_nx\}$ aswell as relational properties with other objects $\{R_1(x_1,\dots x_n),\dots R_m(x_{k},\dots x_w)\}$. 

Example of such ontology may be "The cat is on the mat" or $OnMat(Cat, Mat)$ and that the AI is merely preloaded with this kind of "common sense" knowledge of the world. 


But this leads to the frame problem. Given any problem, there's likely many objects involved, and as such is very slow in being able to bring up the relevant properties and relations. 

We can fix this!





Mereology

Axiomatizing folk-physics (the book by ladyman has a reference to this). Ladyman argues that metaphysicians often end up not utilizing physics correctly at all, and saying false things about it constantly (such as saying "space-time points" etc.). But what if we formalized and axioamtized notions of folk-physics and let a robot reason about space-time, even if fundamental physics says it may be reducible?



# General Seed AI systems

## AIXI
![[Pasted image 20240204125552.png]]

Insert the slide from my phil of science professor with the lecture on events and laws which compress the information.

[Artificial Intelligence > The AIXI Architecture (Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/entries/artificial-intelligence/aixi.html)

uncomputable bro. If weh ad access to hypercomputation, it seems like we could run an AIXI until it figures out an optimal solution for maximising utility. So while we have argued that [hypercomputation is likely not nomonologically possible], if anyone ever finds closed timelike curves, stay on the lookout for anyone trying to implement an AIXI model into it. 



## Gödel Machine

Somewhat self-referential kekw.

## Modal Fusion Systems
So for instance in modal logic one can simply state that $Kp$ to mean that "it is known that $p$". This can be amended in multi-agent epistemic logic with things like $K_1p\wedge \neg K_2p$ in which case agent 1 knows p but agent 2 doesn't know p. 

With fusion logics, one can state the typical JBT definition of knowledge by fusing it with doxastic and justification logic. [Fusion systems]

$$Kp \leftrightarrow (Bp\wedge Jp \wedge p)$$
If we merely a priori reason about what justifies belief, we could simply build an AI that way? This is not entirely possible, because what makes something justificatory is more of an empirical question than something that can be reasoned from armchair philosophy. 





## Neural Networks


Activation level RHLF

Multi layered

Deep Neural Networks



## Reinforcement Learning

Pavlov famously ... dogs bell

Well we have the same thing now with AI. This kind of agent model takes action, receives feedback/reward from the environment based on those actions, and revises one's action strategy accordingly

Mathematically speaking:
$A={R, A}$
environment state-action pairs
utility goes brrr


A simple model is the multi-armed bandit
(insert that here)


Woaw!




# Corrigibility, Explainability, Truthful, Interpretable AI

In recent years, in AI safety research there have been a rise in research programs aimed at creating AI that is corrigible (machine unlearning) explainable (explain why it takes actions or says something, giving justification) truthful (and honest) and interpretable. 



## Truthful

For instance, by building an truth maximiser, one may be able to achieve building an [oracle]. 

Perhaps truthful AI, accompanied by deontic logic, should be forced to be honest (a kantian maxim enforced on the bot). 



AI research converging upon the transformer architecture [Transformer (machine learning model) - Wikipedia](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model))