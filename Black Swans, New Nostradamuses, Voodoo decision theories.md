[black swans, new nostradamuses voodoo decision theories.pdf](file:///C:/Users/Katte/Documents/Academic/Philosophy/black%20swans,%20new%20nostradamuses%20voodoo%20decision%20theories.pdf)


Short Essay 800-1000 words


Severe uncertianty, yet using an OR model without uncertianty!??



Section 
2. Severe uncertainty: Brief discussions on ‘‘Black Swans’’ and ‘‘New Nostradamuses’’, and a formulation of a simple model of severe uncertainty. Section 
3. Decision model: Formulation of a simple model for decision problems subject to severe uncertainty. Section 
4. Voodoo decision theory: A discussion on Voodoo decision theory and its apparent ‘‘advantage’’ over conventional scientific theories. Section 
5. Robustness against severe uncertainty: An overview of Wald’s Maximin model, the conservatism of worst-case analysis, and a terse introduction to robust optimization. Section 
6. Local robustness: Formulation of a radius of stability model, discussions on its invariance property, and the reason why it is unsuitable for the treatment of severe uncertainty. Section 
7. Case study: the campaign. Some points about my experience over the past 7 years in attempting to contain the spread of Voodoo decision making in Australia. Section 
8. Conclusions: an OR perspective.




Operations research involves the study of optimal decision making in dynamical systems. In cases of severe uncertainty, traditional approaches of applying decision theory may not be reliable anymore. The idea of severe uncertainty is that the uncertainty space $U$ might be enormous, even unbounded. The amount of possibilities makes estimating the true value $u^*\in U$ very difficult. Examples of such uncertainty spaces includes the climate of the future, or the economic system.

A black swan event is an event such that it is highly or totally unpredictable (it's somewhere in uncertainty space, who knows where), where it's impact is massive, and is amenable to explanation so it appears predictable in retrospect. Examples of where black swan events might occur is the global financial sector.  

While some scholars take black swan events as making it impossible to utilize mathematical tools for prediction, Sniedovich takes it that on the other side of the spectrum some scholars don't care about severe uncertainty. He takes political scientist and supposed superpredictor Bueno de Mesquita as an example. 

To ground this debate, let's formalize the notion of severe uncertainty. Let $U$ be a space of possible outcomes (say, a set of possible worlds or subsets of $\mathbb{R}^n$). We take $u^*\in U$ to be the "true" state of the world, the actual world or outcome. We take $\tilde{u}\in U$ as a point estimate of $u^*$. The assumption of severe uncertainty states that we do not know the probability $P(u^*)$, $\tilde{u}$ is probably very wrong, and $U$ can be a very large set devoid of a known probability measure. 

How exactly would one take an optimal action, or do decision theory, over $U$? If we have a value function $f(d,u)$ which maps decision $d$ and state $u$ to some number which describes how good the outcome is, we can try to find the $d$ which maximizes the value given our point estimate $\tilde{u}$. i.e $max_d f(d,\tilde{u})$. However given that we don't even have the slightest clue as to what $\tilde{u}$ could be, we should take actions which are robust against severe uncertainty. Specifically in a way where we're not very bad off by some decision. 

Sniedovich criticized some scholars for ignoring vast uncertainty, calling it "Voodoo decision theory". The idea is to not assume severe uncertainty and to take actions as if one had a good idea over the probability of one's estimate over a smaller region of possible outcomes. But worse then that, it also purports to avoid typical scientific scrutiny, and that evidence over that one's estimate is subject to severe uncertainty are rejected. 

The author argues that some kinds of Voodoo decision theory, namely info-gap theory, is simply an application of the kind of minimax solution. We take it that the best decision is the one with the least bad worst outcome as compared to the worst outcome of other decisions. This allows for robustness against bad outcomes, no matter what $u$ is. To formalize the notion a bit more, we can imagine a constraint $C$ of the values that the value function must be within. We can try to find the action which maximizes the number of states $u$ which upholds $C$. We can't expect there to be a decision such that it ensures that all points of $U$ upholds $C$. A purported downside of such an approach is that it can be highly conservative, and one is performing very expensive solutions to outcomes that might not actually have a chance to happen. 

One can go for local optimization. Any decision which ensures that $C$ is upheld for some point $u^*$ might have points close to $u^*$ such that they no longer uphold $C$. In the case of vast uncertainty, this would be potentially quite dangerous, since we don't know whether $u^*$ is close to $u$ or not. As such, we can measure the radius of uncertainty around $u^*$, and perhaps try to optimize the decision based on the radius of this n-dimensional sphere instead (assuming $U$ is $\mathbb{R}^n$). Of course, under vast uncertainty, where almost any guess is wrong, this kind of local optimization isn't reliable. By the invariance theorem, it doesn't take into account anything outside of the radius of the sphere.

This is all voodoo decision theory, according to Sniedovish. Some scholars make the mistake of considering the model to include a known probability measure of which one can optimize around in some radius, this however is impossible. 

My own assessment is that the author is atleast partially wrong. I do think that under a lot of instances were OR is applied, it is not the case that vast uncertainty is the case. Take the climate as an example. That the global temperature will be 2 degrees higher compared to 2000 levels by 2060 is more likely than global temperatures being 20 degrees higher by tomorrow. There still is some resemblance of a probability measure, and we can try to optimize for the situations around which might be say, average of the likely scenarios, say between 1-5 degrees of warming so 3 degrees as the average point, and optimize around that. This allows for robustness around a most likely point, while not being overly conservative or expensive.

This can also be applied to potential future of artificial general intelligence. Some argue that conditioned on the rise of AGI, human society might be transformed in a large number of ways. It will likely be a very vast outcome space, much larger than the outcome space for climate, while having less evidence over its projected outcomes. It can be all from utopian abundance to suffering risks. If we optimize given an average point, and ensure robustness around that point, we can for instance, invest in AI safety and not allowing rampant unsafe use of AI models. All while not being so expensive and overbearing so as to prevent the utopian potential of AI agents. 







Chapter 2

> In his best-selling book The Black Swan: The Impact of the Highly Improbable, Nassim Taleb (2007) contends that true uncertainty is manifested in what he calls Black Swans. He defines a Black Swan as a highly improbable event with three characteristics: 

> It is totally unpredictable. 
	Its impact is massive. 
	It is amenable to explanation, after the fact, so that in retrospect it appears predictable, not random.



> Taleb maintains that Black Swans have major impacts on the lives of individuals and the evolution of organizations; indeed, they shape the very course of history. However, because of their distinctive characteristics (as ‘‘rare events’’), they are outside the purview of formal mathematical treatment. His criticism of methods and models that are the staple fare of the OR curriculum (e.g. classic portfolio analysis) has no doubt infuriated many OR specialists.


Not outside of chaos theory, running massive parallell simulations?

But also yeah, this reminds me of what someone once said about the 2008 financial crash. Models underestimated rare events

We can minimize the impact of "bad" black swan events.

> 1. What is fragile should break early while it is still small. Nothing should ever become too big to fail. 
> 2. No socialization of losses and privatization of gains. 
> 3. People who were driving a school bus blindfolded (and crashed it) should never be given a new bus. 
> 4. Do not let someone making an ‘‘incentive’’ bonus manage a nuclear plant– or your financial risks. 
> 5. Counterbalance complexity with simplicity. 
> 6. Do not give children sticks of dynamite, even if they come with a warning. 
> 7. Only Ponzi schemes should depend on confidence. Governments should never need to ‘‘restore confidence.’’ 
> 8. Do not give an addict more drugs if he has withdrawal pains. 
> 9. Citizens should not depend on financial assets or fallible ‘‘expert’’ advice for their retirement. 
> 10. Make an omelette with the broken eggs. 
> 
> The full version can be found at the web site2 of Taleb’s (2005) book Fooled by Randomness.So the question is: can OR offer tools capable of coping with Black Swans?


So vague


![[Pasted image 20250122220526.png]]


1. Pick a wild guess of the true value of the parameter of interest. 
2. Ignore the severity of the uncertainty, the vastness of the uncertainty space, and the poor quality of the wild guess. 
3. Conduct an analysis in the immediate neighborhood of this wild guess to seek a decision that is robust in this neighborhood.




Formalization

We have a uncertianty space U

Uncertianty space contains points u

One proposed way to optimize is to take the action that maximizes the worst outcome
![[Pasted image 20250124153639.png]]


> This means that tracking down a policy that is driven by the worst-case concept, where the worst-case analysis is conducted over a vast uncertainty space, can yield highly conservative– hence costly– solutions. This characteristic has, over the years, gained the Maximin paradigm the reputation (or notoriety) of being excessively conservative



Example of a case where the optimization is on an subset of n-dimensional real space. 

$c(d,u)\in C$


![[Pasted image 20250124155521.png]]


![[Pasted image 20250124155716.png]]

So on a sphere, a subsphere A would be smaller.

![[Pasted image 20250124155749.png]]

Not sure why this is clear. Depends on the outcomes and how preferable they are, no?

