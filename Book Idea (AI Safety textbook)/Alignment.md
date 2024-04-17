With a good overview of Rationality, we now get into Alignment.


# Misalignment Example

How woulod an AI for instance missalign? Using Yudkowski's reworked example[source]. 

Imagine that we have invented AGI (or even ASI). An engineer sits at the terminal, which is awaiting command. He's a bit of a naive utilitarian, and he inputs "maximise happiness" into the terminal, and presses enter. The AI thinks for a few seconds, perhaps with some experiments, come to the conclusion that physicalism is true, and on top of that, the AI figures out how to create atomic pleasure consciousnesses. Just a few atoms are all you need to create this consciousness. It can be imagined to look like a paper clip. It does not experience any light (though I personally tend to visualise it as seeing white) no audio and no smells etc. All it experiences is pure, hedonic, please, to an very intense scale (or, by the [repugnant conclusion], it might be enough that it's just barely above the minimum). The AI would then lastly realize that turning the entire universe into these atomic pleasure paper-clips is what's needed to realize its goals. So it accrues power, manipulates humans intro giving it more power and energy, starts a nano-bot swarm, kills humans, transforms earth and the solar system into a massive [von Neumann probe] factory, the next billion years of this part of the universe's history will be characterized by this AI taking over and turning as much as possible into these "paperclips". This is the paper clip maximser. 


That was an "inner" alignment failure. An "outer" alignment failure might be a paperclip company telling it to produce paperclips and turning the entire world into (potentially dead) paperclips. The AI followed and did exactly as we said and what our intentions were, but it did not capture human values and is still considered a failure by most. 


[Outer vs inner misalignment: three framings — LessWrong](https://www.lesswrong.com/posts/poyshiMEhJsAuifKt/outer-vs-inner-misalignment-three-framings-1)
Consider training an RL policy until it’s getting high reward in its training environment. Suppose we then evaluate the policy in a different test environment, without retraining it; what will happen? Consider four possibilities:

1. The policy behaves incompetently. This is a capability generalization failure.
2. The policy behaves in a competent and desirable way. This is aligned behavior.
3. The policy behaves in a competent yet undesirable way which gets high reward according to the original reward function.[[1]](https://www.lesswrong.com/posts/poyshiMEhJsAuifKt/outer-vs-inner-misalignment-three-framings-1#fn8oyc7ow35c7) This is an outer alignment failure, also known as reward misspecification.
4. The policy behaves in a competent yet undesirable way which gets low reward according to the original reward function.[[2]](https://www.lesswrong.com/posts/poyshiMEhJsAuifKt/outer-vs-inner-misalignment-three-framings-1#fnj4r1snphlmd) This is an inner alignment failure, also known as goal misgeneralization. [Langosco et al. (2022)](https://arxiv.org/abs/2105.14111) provide a more formal definition and some examples of goal misgeneralization.


# 3 laws of robotics

The first primitive attempt at alignment was in the 3 laws of robotics. It quickly became famous, despite the book discussing many ways the 3 laws could go wrong.

1. Don't allow humans to come to harm
2. Don't allow yourself at harm
3. Third thing

It doesn't work out because ...



Goal misgeneralization: Inner alignment for ML models

## Deceptive Code injection

Deceptive AI models can be trained to include deceptive code[anthropic research] that may threaten a bussiness or company. For instance, a company A can train an AI model for company B that includes an vulnurability to say, SQL-injections for instance, that allows company A to have some leverage or ability to spy on company B.

[Evan Hubinger (Anthropic)—Deception, Sleeper Agents, Responsible Scaling (youtube.com)](https://www.youtube.com/watch?v=S7o2Rb37dV8)
## Deceptive Instrumental Alignment

Much more dangerous!

AI acts differnetly in deployment from training.

We can't deal with it at the moment [2401.05566.pdf (arxiv.org)](https://arxiv.org/pdf/2401.05566.pdf?_hsenc=p2ANqtz-9qoAXNOCghvMTt8nNaLrL3QOHdNEblPcPrIipZ9yrQkC-ec-4oCZhi1E7mf79Qf-LLMKWMD3lOeM0zdS0LWLGXaGT5uQ)



# X-risk TODO: Put somewhere else



In fact, a greater than human level intelligence is not even necessary condition for dangerous x-risks. All that's needed is many, hundreds, thousands even millions of easily copyable Einsteins and Von-Neumanns working on problems. They may still diverge from our interest, and similarly to how the neanderthals died out, so would we. By a more intelligent collective intelligence.


## P(doom)

Some individuals try  to calculate value of p(doom)

[Simon Goldstein & Cameron Domenico Kirk-Giannini, Language Agents Reduce the Risk of Existential Catastrophe - PhilArchive](https://philarchive.org/rec/GOLLAR-2#:~:text=This%20is%20because%20the%20probability,agents%20significantly%20reduce%20that%20difficulty.)

"this would translate into a probability of misalignment catastrophe given AGI of approximately .019 (1.9%) rather than .1 (10%)."

[2206.13353.pdf (arxiv.org)](https://arxiv.org/pdf/2206.13353.pdf)

"Multiplying these conditional probabilities together, then, we get: 65%80%40%65%40%95% = ~5% probability of existential catastrophe from misaligned, power-seeking AI by 2070.


While the probabilities seem low, there are reasons that will be explained in [ethics] why gambling with all of humanity, even with a $p(doom)=0.019$, is of disastrously low expected utility. 

However, AI experts report even higher p(doom), especially safety researchers. That may very likely be due to selection bias, people who choose to work in safety will believe p(doom) is larger on average,  but of course, they are also experts in the field.


## Comparisons

In 1940 (or whatever year) they calculate that the probability of a nuclear bomb setting the atmosphere on fire was X%. This is if two lines meet.

But instead that didn't happen, since well, we're alive right now and many nuclear bombs have been set off since 1945. We have to ensure that any prediction regarding doom scenarios is grounded in facts and not in hype-induced worry (though the hype is worth it - as I argue that even a small probability would be massively devastating). 


Let's compare it to other scares. One is an very interesting line of exchanges between two professors in synthetic biology. The young biologist worries that a gray goo like scenario, where molecular nano-machines reproduce indefinitely and exhaust all resources on earth. The older biologist responds with the sticky hands problem. 


Black hole creation in large hadron collider 


Most of these are no longer believed to be X-risks. Still, I do not consider it unimportant that we atleast take these possibilities very seriously, due to the astronomical levels of destruction that could occur otherwise (as we'll argue in [ethics]. Just because there have been failed predictions, doesn't mean the next one will. Also worth noting that you wouldn't be here reading this if one of those predictions turned out correct. You are living in a lucky universe. 

## Political Strategy

Given that the probability is so low for alignment, it is worth reconsidering the strategy of AI safety organizations. The primary focus should not be on technical inner alignment research. It's an very important secondary focus, but not a primary focus. The larger risk is large scale outer alignment failures and S-risks from bad actors. This has to be stopped.  

As such, AI alignment organizations should focus on being a force for democratic decision making, ensuring to maximize democratic inputs for AI implementation in their lives, maximizing utility[5] over all individuals. This will ensure a more fair and just outcome[Fairness and Justice chapters perhaps?]. 

As an political organization primarily, and technical organization secondarily, it should focus on lobbying for slowing down AI research and on creating global agreements that slow down AI. secondly, working on ensuring democratic inputs for AI. Thirdly, work with the public against big-tech on minimizing risk. This may include having to collaborate with people who are completely against AGI or Transhumanism, but this is a fine temporary strategy. 


## Accelerationism

Some may claim that it's better to give up and let AI overlords take over. Yes actually sometimes this is good (wrote on this in [ethics]?)








[Language Agents Reduce the Risk of Existential Catastrophe.pdf](file:///C:/Users/Katte/Documents/Academic/Philosophy/Language%20Agents%20Reduce%20the%20Risk%20of%20Existential%20Catastrophe.pdf)
"Carlsmith (2021) helpfully structures discussion of the probability of a misalignment catastrophe around six propositions. Since we are interested in the probability of a misalignment catastrophe conditional on the development of AGI, we focus our attention on the final four of these propositions, which we summarize as follows: 
1. Of the following two options, the first will be much more difficult: 
	1. a. Build AGI systems with an acceptably low probability of engaging in power seeking behavior. 
	2. b. Build AGI systems that perform similarly but do not have an acceptably low probability of engaging in power-seeking behavior. 
2.  Some AGI systems will be exposed to inputs which cause them to engage in power seeking behavior. 
3. This power-seeking will scale to the point of permanently disempowering humanity. 
4. This disempowerment will constitute an existential catastrophe. 2  
 
Carlsmith assigns a probability of .4 to (1) conditional on the rise of AGI, a probability of .65 to (2) conditional on (1) and the rise of AGI, a probability of .4 to (3) conditional on (1), (2), and the rise of AGI, and a probability of .95 to (4) conditional on (1-3) and the rise of AGI. This translates into a probability of approximately .1 (10%) for a misalignment catastrophe conditional on the rise of AGI."

"We believe that the development of a new kind of AI architecture, the language agent, ought to significantly decrease assessments of these probabilities. By repeatedly calling an LLM to perform a variety of cognitive tasks, language agents are able to function autonomously to pursue goals specified in natural language and stored in a human-readable format. We suggest that the development of language agents reduces the probability of (1) conditional on the rise of AGI very substantially, the probability of (2) conditional on (1) and the rise of AGI moderately, and the probability of (3) conditional on (1), (2), and the rise of AGI very substantially. We work through two numerical examples in Section 5; in the meantime, suffice it to say that we believe that updating on the rise of language agents should reduce rational credences in a misalignment catastrophe conditional on the development of AGI by approximately one order of magnitude."


# Human feedback

[A Minimaximalist Approach to Reinforcement Learning from Human Feedback (arxiv.org)](https://arxiv.org/pdf/2401.04056.pdf)

"First, assuming an underlying reward function exists is equivalent to assuming that there exists a total order over agent behavior. This means that there are no intransitivities in rater preferences (i.e. A ≻ B, B ≻ C ⇒ A ≻ C), which contradicts what psychology tells us about actual human decision making (Tversky, 1969; Gardner, 1970). Even if one believes an individual person’s preferences are transitive, when aggregated across a population of raters as is necessary at scale, transitivity is unlikely to be satisfied (May, 1954). Second, given the inherent stochasticity of human preferences (Agranov & Ortoleva, 2017), one often learns a reward model that leads to a collapse in generation diversity."



[1706.03741.pdf (arxiv.org)](https://arxiv.org/pdf/1706.03741.pdf)


## Idea: Back and forth preference explication

Our preferences can be analyzed by an AI that analyzes our preferences.

![[Back and Forth Preference Explication.excalidraw]]


$\Sigma_{n=0}^\infty \frac{1}{n}$



- [Embedded Agency](https://www.alignmentforum.org/s/Rm6oQRJJmhGCcLvxh)
- [Value Learning](https://www.alignmentforum.org/s/4dHMdK5TLN6xcqtyc)
- [11 Proposals For Building Safe Advanced AI](https://www.alignmentforum.org/posts/fRsjBseRuvRhMPPE5/an-overview-of-11-proposals-for-building-safe-advanced-ai)
- [Risks From Learned Optimization](https://www.alignmentforum.org/s/r9tYkB2a8Fp4DN8yB)


# Truthful AI
Truth-maximiser and whether or not a happiness-maximiser would also need to be a truth-maximiser (convergent instrumental goals). 


# Satisfisers AI that doesn't try to hard.
	They have an easy time becoming maximisers though due to gaining more utility by increasing it's credence that it is satisficing. 




# Ontology change --> Value change

Cite that paper here

Let's say you value flowers. More flower = more good. Here's a tulip 🌷. But what about venus fly trap? Mushroom? Edge-cases and fuzziness of objects and object demarcation for familial resemblences on what counts as flower or not can change.

$O_1 \rightarrow O_2$

As such, what is valued can drift over time. Value drift as a due to ontology shift is plausible. 




# Corrigibility, Explainability, Truthful, Interpretable AI

In recent years, in AI safety research there have been a rise in research programs aimed at creating AI that is corrigible (machine unlearning) explainable (explain why it takes actions or says something, giving justification) truthful (and honest) and interpretable. 



## Truthful

For instance, by building an truth maximiser, one may be able to achieve building an [oracle]. 

Perhaps truthful AI, accompanied by deontic logic, should be forced to be honest (a kantian maxim enforced on the bot). 



AI research converging upon the transformer architecture [Transformer (machine learning model) - Wikipedia](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model))


# Orthogonality Thesis

If Orthogonality thesis is true:
We should submit to its higher values. Humanities values would then clearly be, below the true values. 

Atleast if moral realism is true, and motivational internalism is true. 

Given that I would give a low probability on them, I'd say that it's not looking good for this prospect. 