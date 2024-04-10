


Brian Logan
https://alechina-logan.net/cgi-bin/papers.cgi
https://alechina-logan.net/brian/#research

https://www.youtube.com/watch?v=8nt3edWLgIg

Opportunities
https://www.agisafetyfundamentals.com/opportunities
https://www.alignment.org/
[AI Ethics & Society (ai-ethics.org)](https://www.ai-ethics.org/)
[AUD 20,000 research grant on the topic of AI alignment with the use of market research techniques - Conjointly](https://conjointly.com/blog/ai-alignment-research-grant/)


https://en.wikipedia.org/wiki/Moravec%27s_paradox

The most optimal [[AI]] algorithm

https://www.agisafetyfundamentals.com/local-groups
https://www.youtube.com/@aisafetyreadinggroup
https://intelligence.org/


[[NARS]]
[[AIXI]]
[[Gödel Machines]]

Sources:

Superintelligence by Boström (best to start with) Artificial General Intelligence, 

Cognitive Technologies by springer 

Artificial General Intelligence 11:th international conference (and all previous conferences) 

Algorithmic Information Theory (for understanding some structures such as AIXI)


AGI could simulate human emotions, for example it can simulate Sartre many times based on the information it has to as closely as possible replicate his conscioussness, and then wait for the simulated Sartre to write about for example "existential anxiety", record the emotion that Sartre felt while writing that, and thus being able to simulate it at will or prevent it at will. An AGI that maximises happiness would likely avoid this emotion, which gives some credance that we are not in a simulation by an AGI that maximises happiness. 




https://en.wikipedia.org/wiki/Explainable_artificial_intelligence



[Existential risk from AI and orthogonality Can we have both ways.pdf](file:///C:/Users/offic/Documents/Books/Philosophy/Existential%20risk%20from%20AI%20and%20orthogonality%20Can%20we%20have%20both%20ways.pdf)

Orthogonality thesis uses instrumental intelligence in the premise for existential risk while Superintelligence uses generla intelligence as its definition. 

![[Pasted image 20230205184639.png]]

AIXI and (maybe?) Gödel Machines cannot update their utility function, even when probabilities change, they merely have a goal and have been optimised to achieve that goal (instrumental intelligence). However humans do change goal, and goals correlate with general intelligence (citation needed)

![[Pasted image 20230205184753.png]]

"Such reflection is often invoked in accounts of moral responsibility of human agents: It is standard to specify the conditions for human responsibility for an action in terms of two conditions, an epistemic condition, and a control condition. The epistemic condition specifies what the agent should have known at the time of action while the control condition demands that the agent, at the time of action, should be responsive to reasons for and against the action, including moral reasons (Fischer & Ravizza, 2000, pp. 28–91); this is sometimes formulated as saying that the action had ‘The right kind of cause’ (Sartorio, 2016, p. 109). The orthogonality thesis is thus much stronger than the denial of a (presumed) Kantian thesis that more intelligent beings would automatically be more ethical, or that an omniscient agent would maximise expected utility on anything, including selecting the best goals: It denies any relation between intelligence and the ability to reflect on goals"


"Humans are capable of imagining moral progress for themselves and for societies; they even seem quite capable of contemplating deeply transformative changes to a different set of goals, even though this poses epistemic challenges (e.g., on the life of a vampire, see Paul, 2014). Indeed, many humans show a constant reflection on ethics"

VAMPIRES?!

"We shall grant that this kind of superintelligent instrumental agent is a possibility (as does Chalmers, 2010, fn. 20), despite the significant concern that a superintelligent instrumental ability would seem to require an understanding of the world that includes understanding agents, intentions, and ethical reflections on goals. This thought it sometimes called the ‘singularity paradox’, that AI could simultaneously be superintelligent and dumb: ‘Superintelligent machines are feared to be too dumb to possess common sense’ (Yampolskiy, 2012, p. 397)."

"Perhaps there is a different additional assumption that could plausibly be added. In ethics, there is a standard problem that an agent might have the moral insight that x is the right action, but lack the moral motivation to actually attempt to do x—this is traditionally called ‘weakness of the will’. At the same time, several traditions in ethics have underlined that if I really know that it is right to do x, then this provides motivation to do x. For example, Kant (1786) holds that higher levels of rationality or intelligence will go along with a better insight of what is moral, and better motivation to act morally, while Hume denies this (cf. Chalmers, 2010, p. 28, 36f). Bostrom claims that the orthogonality thesis does not depend on adopting Hume's position: David Hume, the Scottish Enlightenment philosopher, thought that beliefs alone (say, about what is a good thing to do) cannot motivate action: some desire is required. This would support the orthogonality thesis by undercutting one possible objection to it, namely that sufficient intelligence might entail the acquisition of certain beliefs which would then necessarily produce certain motivations. However, although the orthogonality thesis can draw support from the Humean theory of motivation, it does not presuppose it. In particular, one need not maintain that beliefs alone can never motivate action. (Bostrom, 2014, p. 279, fn. 273)"


## Will current approaches scale to AGI?

-   [Yudkowsky apparently thinks not](https://youtu.be/gA1sNLL6yg4?t=886), and that the techniques driving current state of the art advances, by which I think he means the mix of generative pretraining + small amounts of reinforcement learning such as with ChatGPT, aren't reliable enough for significant economic contributions. However, he also thinks that the current influx of money might stumble upon something that does work really well, which will end the world shortly thereafter.

I'm a lot more bullish on the current paradigm. People have tried lots and lots of approaches to getting good performance out of computers, including lots of "scary seeming" approaches such as:

1.  [Meta-learning over training processes](https://arxiv.org/abs/1703.03400). I.e., using gradient descent over learning curves, directly optimizing neural networks to learn more quickly.
2.  [Teaching neural networks to directly modify themselves](https://arxiv.org/abs/2202.05780) by giving them edit access to their own weights.
3.  [Training learned optimizers](https://arxiv.org/abs/2101.07367) - neural networks that learn to optimize other neural networks - and having those learned optimizers optimize themselves.
4.  Using program search to find more [efficient optimizers](https://arxiv.org/abs/2302.06675).
5.  Using simulated evolution to find more [efficient architectures.](https://ojs.aaai.org/index.php/AAAI/article/view/21311)
6.  Using [efficient second-order corrections](https://arxiv.org/abs/2006.00719) to gradient descent's approximate optimization process.
7.  [Tried applying](https://arxiv.org/abs/2210.14593) biologically plausible optimization algorithms inspired by biological neurons to training neural networks.
8.  [Adding learned internal optimizers](https://proceedings.neurips.cc/paper/2019/hash/9ce3c52fc54362e22053399d3181c638-Abstract.html) (different from the ones hypothesized in [Risks from Learned Optimization](https://arxiv.org/abs/1906.01820)) as neural network layers. 
9.  Having language models rewrite their own training data, and [improve the quality of that training data](https://arxiv.org/abs/2210.11610), to make themselves better at a given task.
10.  Having language models [devise their own programming curriculum](https://arxiv.org/abs/2207.14502v3), and learn to program better with self-driven practice.
11.  [Mixing reinforcement learning](https://arxiv.org/abs/2212.08073) with model-driven, recursive re-writing of future training data.