- Ethics
	- Meta-ethics
		- Values, and Axiology
		- Justifying Ethical Beliefs
		- Human values
	

# Values, and Axiology

Philosophers have long grappled the question of what makes something good, or valuable. And now computer scientists are doing the same when considering specifically outer alignment, how do we encode and align human values to the AI? 


## Intrinsic and Extrinsic


## Monism vs Pluralism


## Happiness monism

So one popular view is happiness monism. The view tells us that happiness is the only thing worth striving for, and there are different accounts of happiness to which to strive for. Suffering may be a phenomenal experience that's intrinsically bad, and pleasure maybe a phenomenal experience that's intrinsically good. 

I would argue that all 5 accounts of happiness is reducible too hedonic-pleasure account


## HOW TO FIGURE OUT WHICH INCONSUMENSURABLE VALUES TO HAVE

Now how should the selection process for an incomplete preference relation be? This is a more complicated and difficult, so will require it’s own section. First, we can list some common values as candidates for what that can look like.

First and foremost, there are many different kinds of [happiness](https://plato.stanford.edu/entries/happiness/), for example:

1. Desire Satisfaction
2. Life-quality
3. Hedonic pleasure
4. Positive emotional states

Different kinds of happiness themselves might be enough to threaten the completeness of preference relations. But yet more values can be added:

5. Knowledge
6. Friendship
7. Aesthetic Appreciation
8. Liberty

And these are only the more intuitive ones. The list can continue as:

9. Producing Paperclips
10. Counting grass
11. Listing the most digits of π
12. Making arbitrarily long lists

And so on and so forth indefinitely.

And the risk is that there is no rational procedure where well-being or list items 1-8 are considered “good values” and list items 9-12 are considered “bad values” to have. This is likely a question I will have to revisit in future blog posts. For now, during a period of suspending judgment, one can take [McAskill’s theory of moral uncertainty](https://www.williammacaskill.com/info-moral-uncertainty) into account, where one can have a probability distribution where the values 1-8 has a higher probability of being true values than 9-12, such that one can act as if those are true and then update one’s beliefs over time. I’m not advocating for moral radical relativism.

## WHY WE STILL OUGHT TO MINIMIZE EXISTENTIAL RISK AND ACCELERATE TECHNOLOGICAL CHANGE

[In Boströms paper “Astronomical Waste”,](https://nickbostrom.com/astronomical/waste) he argues that astronomically large amount of the universe is being wasted, primarily due to entropy. we are currently wasting the potential 10^47 valuable lives per century. Here I will give a short overview of the argument, pointing out the very important section on that the argument works even under plural values. It’s worth noting that the argument may not work under non-infinite time-discount rate, but that is for a future blog post. Here is an overview of the argument

1. Under conservative assumptions, due to entropy and black holes, the local Virgo supercluster looses the potential of simulating upwards of 10^47 happy biological humans every century (a conservative estimate giving us an lower bound of future potential lives).  
    
2. Accelerating technological growth means less entropy, meaning that the faster we colonize the local Virgo supercluster, the fewer happy people we loose.  
    
3. We value almost anything commonly valued (From the paper: “For example, we can take a thicker conception of human welfare than commonly supposed by utilitarian’s (whether of a hedonistic, experientialist, or desire-satisfactionist bent), such as a conception that locates value also in human flourishing, meaningful relationships, noble character, individual expression, aesthetic appreciation, and so forth.”)  
    
4. the evaluation function is aggregative (does not count one person’s welfare for less just because there are many other persons in existence who also enjoy happy lives)  
    
5. The value function is not relativized to a particular point in time (no time-discounting)

We can conclude that we should accelerate technology However, as he points out later

6. Loosing human civilization would delay colonization of the Virgo supercluster by a tremendous amount of time.  
    
7. A single percentage point less existential risk is worth delaying colonization 10 million years

Therefore, we should minimize existential risk. though the argument is crude and informal (though that will be resolved in a future blog post) we can conclude with that **you ought to make sure your life is all about minimizing existential risk, that’s the best way to further your most likely values.**




# Human Values

What exactly does "human values" even mean? Cross-cultural Meta-Studies on values suggest that ....

So we can take averages of human values
Utilitarianism ... 43%
Deontology ... 33%
...

Perhaps, by pascalian bets, we should atleast consider divine command theory a little bit. 

# Uncertain Values

Can our values be uncertain? Perhaps even imprecicely uncertain[]? 

What exactly is meant by uncertain values? Well what if the values one has is unknown. What if now only human values are unknown, but our own values too? It's not necessarily the case that we can tell exactly what our values are, nor predict how they may change and why they change. 

As such we may represent the values we have with some probability $p$. For instance, self-satisfaction account happiness may have probability 0.23 of being our values, while the hedonic account of happiness is 0.11, while certain kinds of knowledge is valued at 0.32. This allows us to calculate expected value of any action.

(example calculation)

But one problem remains, can we really set such a specific probability of those values? What if my probability is uncertain, say around the 0.7-0.8 range for instance? In such cases we may employ imprecice probabilities, just like in [Elsberg preferences]. However the problem remains as in that one. Sunk costs etc. 

So we may instead employ "our best theory"[McAskill]. In that circumstance, things are cringe and hopeless. So that way we just take the expected value of an action, given the highest probability thingy
$\max_p U(p)$ 

Could we let AI figure out our values for us? What if their value is in figuring out our values and maximising on that. There are problems with emergent behaviours, such as [specification gaming] and [deception] such that it may be the case that it tricks us into believing we have values that we don't have, or atleast didn't have before, either because it's easier for the AI to maximise on those or because it's own diverging values. 






## Outer Alignment/Value loading problem



## Is it ethical to *not* create safe ASI?

Creating safe ASI would alleviate pretty much all of the worlds problems. 


For instance, as per our discussion earlier, let's say one fundamental value is friendship. You may value a friendship for upwards of 100 years, given that there are no life-extension technologies. Given that AI develops, and cures things like Alzheimer's disease and Cancer, such that the friendship can last for 200 years, wouldn't that be roughly twice as good? Perhaps you believe that the value of friendship over time has diminishing marginal returns, but even a 1.2 times improvement would still be worth pursuing over fundamental values. 


## Population Ethics, Repugnancy, Singleton worlds



## Orthogonality (Meta-ethics)

Kantian vs Humean approaches on moral motivation. 

[Moral Skepticism > Practical Moral Skepticism (Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/entries/skepticism-moral/supplement.html)

"Although the orthogonality thesis can draw support from the Humean theory of motivation, it does not presuppose it. In particular, one need not maintain that beliefs alone can never motivate action. It would suffice to assume, for example, that an agent—be it ever so intelligent—can be motivated to pursue any course of action if the agent happens to have certain standing desires of some sufficient, overriding strength. Another way in which the orthogonality thesis could be true even if the Humean theory of motivation is false is if arbitrarily high intelligence does not entail the acquisition of any such beliefs as are (putatively) motivating on their own. A third way in which it might be possible for the orthogonality thesis to be true even if the Humean theory were false is if it is possible to build a cognitive system (or more neutrally, an “optimization process”) with arbitrarily high intelligence but with constitution so alien as to contain no clear functional analogues to what in humans we call “beliefs” and “desires”. This would be the case if such a system could be constructed in a way that would make it motivated to pursue any given final goal"
"2For some recent attempts to defend the Humean theory of motivation, see Smith (1987), Lewis (1988), and Sinhababu (2009)."
[THE SUPERINTELLIGENT WILL.pdf](file:///C:/Users/Katte/Documents/Academic/Philosophy/THE%20SUPERINTELLIGENT%20WILL.pdf)

Are AI agents motivated by moral facts?


(1) Moral Realism is true
(2) Anti-Humean/Motivational Internalism is true
(C) Orthogonality is false


In fact, under such a scenario, there's no need for AI safety at all, and one ought to accelerate AI development as fast as possible (to maximise moral goodness).





# Existentialism?

One of the final values discussed earlier involves "freedom". I only briefly mentioned this as an example, but it's worth going into detail over what exactly is meant by that.

Sartre radical freedom eat dirt etc. Russian author going around doing things. We are existential being taking decisions. Phennomenology of decision making.

It's worth noting that this is not an interpretation of existentialism that existentialists themselves would accept, what follows will be existentailism-inspired at most, including a story from Sartre. But it's worth noting that existentialists likely wouldn't have this account. 

So for instance one can argue that there are two different possible scenarios of the technological singularity. In one after mind upload and we enter the virtual world where we feel amazing, but the ASI decides our entire experience, and in another where we have agency that can even occasionally decrease happiness. The existentialist may argue that we should have the second technological singularity. For the aggregated human value preference relation/utility function, we must take  the existential utility function $U:S\rightarrow \mathbb{N}$ inputs world states and outputs the amount of "agency" (perhaps, number of possible actions) into consideration. 

An existentialist would also be pro transhumanism, as it increases agency. By being able to take more possible actions, and being more intelligent such as to be able to go through the space of possible actions more thoroughly, they're able to optimize more for action maximizing actions. 

Inauthenticity. You believe that you take up a certain social role. So in Sartre's book there's an example of a waiter who believes that their action space is a subset of it's real action space $A_b\subset A$ which may limit optimization possibilities, and is thus irrational.

So whoever you are, or whatever social role you perceive yourself as having, could be in bad faith and irrational. Even if you are a waiter, you can still take those actions that lets you pursue a career in AI safety. Or maybe not, Sartre could be (and likely is) completely wrong about how much freedom we actually do have, we may in fact likely have 0 freedom and the notion of action space is more of an [dennettian intentional stance] than something real. 



## Peter singer expanded moral sphere




# Utilitarianism

Total utilitarianism
Negative utilitarianism
Leximin Rule 
Egalitarian Rule



# Contractualism

The view that all rational agents would accept a social contract at birth, given the consequences for one's own preferences if a social contract where not the case. 

From a [game theoretic] perspective, contracts can be seen as a kind of coordination optimization.

[Game Theory and Ethics (Stanford Encyclopedia of Philosophy/Winter 2021 Edition)](https://plato.stanford.edu/archives/win2021/entries/game-ethics/)



# Game Theoretic Power Dynamics

Thread advantage [Game Theory and Ethics (Stanford Encyclopedia of Philosophy/Winter 2021 Edition)](https://plato.stanford.edu/archives/win2021/entries/game-ethics/)


Going Dove on every game that modells resource aquisition will lead to starvation and death for biological entities (any thermodynamic entities). 



hobbess-state-of-nature-a-modern-bayesian-game-theoretic-analysis.pdf

So in a state of nature, people with no information regarding who are power-seeking and who are moderate, then people are incentiviced to launch attacks first for self-preservation.

What of a world where complete information of every post-human can be guaranteed? Whether or not this is predictable at all is itself a tough question, but utilizing the game theoretic results above we may conclude that, given that C5 is now false, assuming we can all mathematically proove eachothers utility functions, then we'd expect the state of nature to be different. As such, the government looses its legitimacy. 



# Moral Agenthood of AI

"The increasing complexity of computer technology and the advances in Artificial Intelligence (AI), challenge the idea that human beings are the only entities to which moral responsibility can or should be ascribed (Bechtel 1985; Kroes and Verbeek 2014). Dennett, for example, suggests that holding a computer morally responsible is possible if it concerned a higher-order intentional computer system (1997). An intentional system, according to him, is one that can be predicted and explained by attributing beliefs and desires to it, as well as rationality. In other words, its behavior can be described by assuming the systems has mental states and that it acts according what it thinks it ought to do, given its beliefs and desires. Many computers today, according to Dennett, are already intentional systems, but they lack the higher-order ability to reflect on and reason about their mental states. They do not have beliefs about their beliefs or thoughts about desires. Dennett suggests that the fictional HAL 9000 that featured in the movie _2001: A Space Odyssey_ would qualify as a higher-order intentional system that can be held morally responsible. Although current advances in AI might not lead to HAL, he does see the development of computers systems with higher-order intentionality as a real possibility."

"have objected to the idea that computer technologies can have capacities that make human beings moral agents, such as mental states, intentionality, common sense or emotion (Johnson 2006; Kuflik 1999). They, for instance, point out that it makes no sense to treat computer system as moral agents that can be held responsible, for they cannot suffer and thus cannot be punished (Sparrow 2007; Asaro 2011). Or they argue, as Stahl does, that computers are not capable of moral reasoning, because they do not have the capacity to understand the meaning of the information that they process (2006)."

[Computing and Moral Responsibility (Stanford Encyclopedia of Philosophy/Winter 2021 Edition)](https://plato.stanford.edu/archives/win2021/entries/computing-responsibility/#ComMorAge)


So that brings us to the question of autonomous cars and in what way they should be programmed to avoid certain individuals. Market forces may incentivice protecting the people in the car over pedestrians, as the people buying the cars will likely choose cars such that they protect themselves (I certiantly would do so). This shows the need for government regulation on regulating how cars should sverve away to protect whom. 

In an digital game from blah blah[source], they analyzed how people picked choices given how autonomous cars drove. And this is indeed epic. It turns out most people don't like cartoon robbers holding big bags of money with dollarsigns on them, nor do they like cats and dogs. There was a preference for protecting younger and healthier people with higher status careers. My own preferences were quite similar to that of the average person, take the test yourself [link].

If we are to protect people based on this kind of stuff, we ought to ensure that future highly intelligent machines who are able to work in a lot of field are programmed, perhaps using deontic logic or some kind of built in utilitarian calculus, on what actions ought to be performed. As shown in the alignment chapter, assuming inner alignment is solved, and we can specify rules for it. LLM's, while still new, can follow moral codes given in natural language. However current LLM's will likely follow ethics given its training data and not for humanity as a whole. This may not be a problem though, given how internet values are more liberal-secular anyways. 






Idea: Here's an potential argument:
1) The world is completely deterministic
2) Incompatibilism is true
3) Pleasure is inherently good
4) Pain is inherently bad
5) Ought to maximise pleasure and minimize pain. Including "forcefully" as free will doesn't exist anyways. 

