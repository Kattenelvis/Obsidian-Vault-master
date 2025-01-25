In this article the probability on human extinction risk (X-risk) from misaligned artificial intelligence will be calculated. For simplicity, there will not be any discussion about the probability of human misuse, especially given how hard it is to calculate such a probability. I will instead stick to purely the probability of doom given a misalignment scenario which gives a minimum bound on X-risk (existential-risk).

First I want to discuss two articles which actually calculate some number of this, Carlsmith "Are AI a risk" and "Language Agents Reduce the Risk of Existential Catastrophe" by Simon Goldstein and Cameron Domenico Kirk-Giannini (which is a response to Carlsmith's article). The main argument is the following:

> 1. Of the following two options, the first will be much more difficult:  
>     - a. Build AGI systems with an acceptably low probability of engaging in power seeking behavior.  
>         
>     - b. Build AGI systems that perform similarly but do not have an acceptably low probability of engaging in power-seeking behavior.  
>         
> 2. Some AGI systems will be exposed to inputs which cause them to engage in power seeking behavior.  
>     
> 3. This power-seeking will scale to the point of permanently disempowering humanity.  
>     
> 4. This disempowerment will constitute an existential catastrophe.
> 
> Carlsmith assigns a probability of .4 to (1) conditional on the rise of AGI, a probability of .65 to (2) conditional on (1) and the rise of AGI, a probability of .4 to (3) conditional on (1), (2), and the rise of AGI, and a probability of .95 to (4) conditional on (1-3) and the rise of AGI. **This translates into a probability of approximately .1 (10%) for a misalignment catastrophe conditional on the rise of AGI**.

After readjusting for language agents having fewer issues with goal missgeneralization, interpretability and reward misspecification, we get:

> On this quantitative model of our arguments, updating on the development of language agents would give us probabilities of .04 for (1) conditional on AGI, .325 for (2) given (1) and AGI, and .04 for (3) given (1), (2), and AGI. Factoring in the .95 probability of (4) conditional on (1)-(3) and AGI, **this would translate into a probability of misalignment catastrophe given AGI of approximately .0005 (.05%), rather than .1 (10%)**.
> 
> Even a much more modest understanding of very substantial reductions leads to a significantly lower probability of misalignment catastrophe. **Suppose we interpret a very substantial reduction as a reduction by 50% and a moderate reduction as a reduction by 25%**. Then updating on the development of language agents would give us probabilities of .2 for (1) conditional on AGI, .49 for (2) given (1) and AGI, and .2 for (3) given (1), (2), and AGI. Factoring in the .95 probability of (4) conditional on (1)-(3) and AGI, **this would translate into a probability of misalignment catastrophe given AGI of approximately .019 (1.9%) rather than .1 (10%)**.

Reassessing the probabilities of the premises

Premise 1

The first premise assessed for language models is revised since it seems that it's going to be less difficult than previously thought to build systems that have a sufficiently low probability of engaging in power-seeking behavior, mainly thanks to interpretability, goal missgeneralization and reward misspecification being less of a problem for language agents. When an agents goals or preferences can be elicited in natural language, assuming it's output generation is truthful to it's goals, it's easier to spot if it's engaging in power-seeking. It's harder for a language agent to misunderstand a goal a human put in, as the natural language version will yield fewer problems (imagine the infamous boat example, a reinforcement learning agent optimizing score vs a language agent which is told to "win the race". Which one is the most likely to perform it correctly given human standards?)

However, if we assume instrumental convergence, this probability would be higher. If we consider goal space G, assuming instrumental convergence, we'd expect probably around 75+% of G to involve being power seekers. As an example scenario, see in Baum's article "Assessing the Risk of Takeover Catastrophe from Large Language Models":

> (1) Rapid single-system takeover. The goal of current LLMs is to identify the token (string of text) that best matches its training parameters given the text received from user input. In this scenario, an advanced LLM seeks to optimize its token identification by commandeering resources it can use for token identification calculations. To that end, it takes over the world and converts all of the world’s resources into a giant factory for optimizing its identification of tokens. This activity inadvertently kill all humans and perhaps also other forms of biological life on Earth.

Attempted estimations based on new assessments on their probabilities, namely instrumental convergence, weak orthogonality, unexpected capabilities scaling and so on would likely put the probability of premise (1) higher than reported by the authors. As such I expect the probability of (1) to be a bit higher than even what Carlsmith assigns them.

Conditioned on language agents, this probability might be smaller, atleast if the LLM component of the language agent has been trained to not act in ways which are power-seeking (which seems to be the case after RHLF). For a sufficiently intelligent language agent, it might be the case that they reason to be token-maximisers in the end regardless (i.e reward hacking). As such I will estimate the probability to be around 0.75.

Premise 2

This premise asks us to asses that, given that there's an unacceptably high probability that AI systems will have inputs that cause power-seeking behavior, what is the probability that someone will feed it such an input? We might regulate and ban power-seeking AI's, which may decrease this probability. On the other hand, power-seeking humans may want to utilize AI's for their own benefit. The probability might atleast partially based on human misuse, and as such is very hard to estimate, and as such I take the moderately revised probability of 0.49.

Premise 3

I find it surprising how low the probability has been assigned to this one by both authors, given that the probability is conditioned on the fact that power-seeking behavior is unacceptably high and that they're exposed to a power-seeking input. I take it that such a probability could in principle be based upon how intelligent the agent is and if we're headed for a unipolar or multipolar scenario. It's plausible that multiple, human-ish level intelligence's are put to be power-seekers, of which they choose not to cooperate against humans, and in which no one overpowers the rest. That this probability could be as low as .04 as in scenario, conditioned on the two premises, seems absurd. I will take Carlsmith's original probability and increase it a bit, namely to .45.

Premise 4

The final premise is about the probability of a world-dominating AGI killing all humans is, given that it has reached world domination. Which might seem highly likely if we assume instrumental convergence and orthogonality. Häggström points out a counter-argument to orthogonality, in his article "Challenges to the Omohundro—Bostrom framework for AI motivations", namely that a AGI which dominates the world may nevertheless be helpful towards humans. Hinting at a short section in Boström's the superintelligent will, Häggström points out that if the following 4 statements are true, then an AGI even with world domination will not be an X-risk.

1. Moral facts exist, moral realism is true
2. Epistemic justifications for moral facts exist
3. Agents are motivated to act by moral beliefs
4. Moral truths imply the survival of Humans

This allows us to properly calculate the probability of premise (4), by using philpaper survey results we can multiply the frequencies of what philosophers believe to get a crude approximation. Calculate the frequency $latex f$ of philosophers which support those viewpoints! (Assuming that moral realism is the only way an AI achieving world domination could not cause human extinction).

$latex P(\text{premise 4}) = 1- f(\text{realism})f(\text{justification})f(\text{motivation})$

[PhilPapers Survey 2020](https://survey2020.philpeople.org/survey/results/4866)  
$latex f(\text{realism}) = 0.61$  
https://survey2020.philpeople.org/survey/results/5078  
$latex f(\text{justification})=0.7686$  
[PhilPapers Survey 2020](https://survey2020.philpeople.org/survey/results/4878)  
$latex f(\text{motivation})=0.41$

All those values multiplies to $latex 0.19222686$. It's worth noting that these beliefs are likely correlated, and correlations are available on philpapers, and could perhaps be recalculated in a future article. But with the crude calculation in place, an AGI which has acquired world domination will have a probability $latex 0.80777314$ of being an X-risk. This is of course assuming the moral truths don't kill or otherwise harm humans (say for instance, if human exctinctionism is a moral fact). In such a case, there might be reasons for us to accept our getting killed, since we'd be motivated by the moral truths regarding our own-self sacrifice. In such a way, we could be reasoned into self-sacrifice by the AI without it being deceived by the AI, given that our existence is truly immoral. But one question remained unanswered: What is the probability, or what could be potential reasons, for moral facts to potentially involve killing or otherwise harming all humans? This is something to explore in a future article.

Calculating the final probability

Let's calculate the final probability. It calculates to $latex P(\textbf{doom}) = P(\text{premise 1})P(\text{premise 2})P(\text{premise 3})P(\text{premise 4}) = 0.75\times 0.49\times 0.45\times 0.8\approx 0.1323=13.23\%$.

I will consider such a p(doom) to be unacceptably high. If you throw a 6-sided die where landing a 1 leads to the extinction of humanity, that is not something I consider acceptable, and has incredibly low expected value given Boströms argument in "Astronomical waste".

This number should be a call to action towards all law-makers to put restrictions on frontier AI models and having frontier AI development working together with AI safety to ensure that the probability further comes down. Establishment of global regulatory framework for all nations to be ruled under and be responsible too, including the USA and China. It should be a call to action for supporting movements like PauseAI.

Once the probability is on a sufficiently low level, there could be considerations in place to consider accelerating AI technology instead. The sufficiently low level could be taken to be about the sum of all other X-risks, assuming sufficiently advanced AI could prevent all other existential risks. Perhaps in combination with accelerating and ensuring safe AI the whole way is a better approach, atleast for a risk-averse agent. Regardless, I'm generally hopefully of the future, and hope we genuinely make it.