I have for a long time been a utilitarian, and I still believe the theory has a lot of merits, especially considering some versions of utilitarianism such as leximin-rule utilitarianism with it's [wonderful properties of pareto efficiency and egalitarianism (Pigou-Dalton principle)](https://en.wikipedia.org/wiki/Egalitarian_rule#Properties). However, it turns out that the utility function is equivalent to a preference relation with 4 properties (by the [Von-Neuman Morgenstern theorem)](https://en.wikipedia.org/wiki/Von_Neumann%E2%80%93Morgenstern_utility_theorem), and that the properties necessary to form a utility function might not rationally be the case, in a way necessary to form an theory of rational or ethical choice with normative force. Specifically, it's the [intransitivity](https://plato.stanford.edu/entries/decision-theory-descriptive/#Tran) and [non-completeness of preference relations](https://plato.stanford.edu/entries/rationality-normative-nonutility/#ChalInco) that aren't the case, and completeness doesn't even seem to ought to be the case. With completeness no longer the case, the utility function will have multiple outputs such as happiness, knowledge e.t.c. Instead of monomaniacally maximizing say happiness, there is a plurality of values.

The first section of this article goes over a more detailed argument of the above. After that, a new, generalized theory of intransitive non-complete preference relations and how to generate one given set of values and optimize for it despite being unable to formulate it easily in a utility function. For intransitivity, we show how dynamic choice can be applied as one figures out that there is an intransitivity in one's preference relation. Finally, I go over that Boströms argument for minimizing existential risk still holds for almost all values, giving some direction to one's life despite plural values.

The main argument

## The theorem connecting preferences to utility functions

Definition: A preference between two objects, options, lotteries or state of affairs A and B tells you that you'd rather one over the other. So for instance, a preference relation R such that R(A,B) tells you that B is preferable to A (usually denoted with <, so A < B).

1. Transitivity of preferences. If A is preferred over B and B is preferred over C, then A is preferred over C (Premise)  
    
2. Completeness of preferences. Either A is preferred over B, B is preferred over A, or they are equally preferable. Two options are always comparable (Premise)  
    
3. A preference relation with properties 1-2 is a utility function, since one can map the preference relation to the structure of the "greater than" relation on the natural numbers.

## The unreasonableness of transitivity

4. Transitivity of preferences is unrealistic (Controversial empirical premise)  
    
5. A utility function for some agent is unrealistic (3, 4)

## The unreasonableness of completeness

6. If preferences are incommensurable*, then preferences cannot be complete (Premise)  
    
7. Preferences are probably incommensurable (Controversial empirical premise)  
    
8. Preferences are probably not complete (6, 7)  
    
9. A utility function for some agent is unrealistic (3,8)

## Conclusion of the argument

Utility functions don't work to model preferences of consequences or actions, and thus cannot be used in morality. Both 5 and 9 are on their own sufficient for such a conclusion.

*Definition: Preferences are incommensurable if they cannot be compared. For instance, choosing between happiness and knowledge. Maybe if A is happiness and B is knowledge, then they are incomparable. As a replacement I've been getting into moral uncertainty, which applies preference relations and probabilities on different normative theories themselves, and calculating which is strictly preferable. Transitivity and completeness might even work in this restricted context (they might work for other kinds of restricted contexts aswell, such as picking between say 2 preferences), so calculating and maximizing expected utility might work for moral uncertainty. But that's just speculation on my part.

## How to maximise a non-complete non-transitive preference relation

So what ought we to do if our preference relations are not able to form a utility function? Well, it's still possible to "climb the lattice" of a partial ordering of preferences.

For example, imagine 4 alternatives, and they are ranked as per the following picture, with the preference option at the top is preferred over everything.

![](https://thephilosophyaddict.files.wordpress.com/2023/11/image-4.png?w=356)

As can be seen, this allows for climbing the lattice even under incommensurable values. There might be no rational choice between the two middle choices, since they are not strictly preferable over eachother. An example of such a scenario is this:

Imagine you're trying to maximize happiness. You have different choices, and you pick the one you believe will give you more happiness than the others. However, imagine that you're instead maximizing multiple sometimes incompatible things. What if you value two different things, such as knowledge and happiness? Or friendship? Suddenly, you might have to offer up one of them in favor of the other, and so it's difficult to judge the different options. Is it preferable to learn an uncomfortable truth or to keep yourself in blissful ignorance? To what extend and in which situations? This is a difficult question and I don't believe it's obviously the case that one should only value happiness. It might be, but I'm unsure.

Now what about the lack of transitivity? [Due to the possibility of preference cycles under an intransitive preference relation](https://plato.stanford.edu/entries/dynamic-choice/#IntrPref), the image one might get is the following:

![](https://thephilosophyaddict.files.wordpress.com/2023/11/image-6.png?w=469)

Now combining both of them you might end up with two incommensurable preference cycles

![](https://thephilosophyaddict.files.wordpress.com/2023/11/image-7.png?w=1024)

If faced with such an option, first use your selection process for incommensurability, and then the one for non-transitivity.

So how could for instance, a selection for non-transitive preferences look like? One example is that one can then transform non-transitive sections into something transitive, where all three are equivalent, as soon as intransitivity is found.

![](https://thephilosophyaddict.files.wordpress.com/2023/12/image-1.png?w=1024)

A mathematical formalism for such a theory will not be given out in this blogpost (though likely in a future one), but it's certainly something for the future. For an, albeit complicated, already existing one, check out [Appendix M for dynamic epistemic logic in SEP](https://plato.stanford.edu/entries/dynamic-epistemic/appendix-M-preferences.html), it's fairly complicated combination of preference relations and multi-agent dynamic epistemic logic (up to public announcements and the S5 axiomatization of the knowledge modal operator). If you're inclined to logic then I recommend giving it a read. But it does not cover how an intransitive preference relation changes to a transitive one, as it assumes transitivity already.

## How to figure out which inconsumensurable values to have

Now how should the selection process for an incomplete preference relation be? This is a more complicated and difficult, so will require it's own section. First, we can list some common values as candidates for what that can look like.

First and foremost, there are many different kinds of [happiness](https://plato.stanford.edu/entries/happiness/), for example:

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

And the risk is that there is no rational procedure where well-being or list items 1-8 are considered "good values" and list items 9-12 are considered "bad values" to have. This is likely a question I will have to revisit in future blog posts. For now, during a period of suspending judgment, one can take [McAskill's theory of moral uncertainty](https://www.williammacaskill.com/info-moral-uncertainty) into account, where one can have a probability distribution where the values 1-8 has a higher probability of being true values than 9-12, such that one can act as if those are true and then update one's beliefs over time. I'm not advocating for moral radical relativism.

## Why we still ought to minimize existential risk and accelerate technological change

[In Boströms paper "Astronomical Waste",](https://nickbostrom.com/astronomical/waste) he argues that astronomically large amount of the universe is being wasted, primarily due to entropy. we are currently wasting the potential 10^47 valuable lives per century. Here I will give a short overview of the argument, pointing out the very important section on that the argument works even under plural values. It's worth noting that the argument may not work under non-infinite time-discount rate, but that is for a future blog post. Here is an overview of the argument

1. Under conservative assumptions, due to entropy and black holes, the local Virgo supercluster looses the potential of simulating upwards of 10^47 happy biological humans every century (a conservative estimate giving us an lower bound of future potential lives).  
    
2. Accelerating technological growth means less entropy, meaning that the faster we colonize the local Virgo supercluster, the fewer happy people we loose.  
    
3. We value almost anything commonly valued (From the paper: "For example, we can take a thicker conception of human welfare than commonly supposed by utilitarian's (whether of a hedonistic, experientialist, or desire-satisfactionist bent), such as a conception that locates value also in human flourishing, meaningful relationships, noble character, individual expression, aesthetic appreciation, and so forth.")  
    
4. the evaluation function is aggregative (does not count one person’s welfare for less just because there are many other persons in existence who also enjoy happy lives)  
    
5. The value function is not relativized to a particular point in time (no time-discounting)

We can conclude that we should accelerate technology However, as he points out later

6. Loosing human civilization would delay colonization of the Virgo supercluster by a tremendous amount of time.  
    
7. A single percentage point less existential risk is worth delaying colonization 10 million years

Therefore, we should minimize existential risk. though the argument is crude and informal (though that will be resolved in a future blog post) we can conclude with that **you ought to make sure your life is all about minimizing existential risk, that's the best way to further your most likely values.**

Thanks for reading, and comment if you have any feedback!