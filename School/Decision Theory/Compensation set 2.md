

1

a)

If the summer is rainy and she doesn't buy a pass, then she has to pay $30\cdot 100 =3000$ SEK. If the summer is sunny and she doesn't buy a pass, then she has to pay $6\cdot 100=600$ SEK. A season pass costs $1500$ SEK

Expected cost for not purchasing:
$3000\cdot 0.4 + 600\cdot 0.6= 1560$

Expected cost for purchasing:
$1500$

Hence the expected cost of purchasing is lower, and assuming Sjöström is an expected utility maximizer, she ought to buy the season pass.


b)

We now have revised costs conditioned on Sjöström buying the weather forecast, given that she picks the cheaper option:

Rainy summer cost: 1600
Sunny summer cost: 700

Thus the expected utility conditioned on Sjöström buying the weather forecast is:

$700\cdot 0.4 + 1600\cdot 0.6=1240$

Which is less than $1500$, and so again assuming she is an EU maximizer, she ought to buy the forecast.

c)

![[Decision Tree.excalidraw|1500]]


d)

We revise the previous decision tree by introducing appropriate conditional probabilities. Let's zoom in on the revised left side of the decision tree:

![[Decision Tree 2.excalidraw|1500]]

Using this image we can see that buying a forecast gets an expected loss of 
$0.4\cdot 0.6\cdot 700 + 0.4 \cdot 0.2 \cdot 1600 + 0.6 \cdot 0.2 \cdot 3100 + 0.6 \cdot 0.8 \cdot 1600 = 1492$
Which is just lower than buying a pass, making it slightly more valuable. Given that Sjöström is an EU maximizer, she ought to buy the partially reliable forecast. 

3

a)

Consider the following income distributions:
![[Egalitarian 2|1500]]

If we let $\succ$ stand for the "is more egalitarian than" relation, it is obvious that $A\succ B$. 

The Von-Neumann axiom of independence states the following: Let $p$ be some probability, then $A\succ B \leftrightarrow (1-p)A+pC\succ (1-p)B+pC$ 

However, by introducing $C$ as seen in the image above with $p=0.5$, we can tell that $A$ is no longer the most egalitarian while $B$ becomes more egalitarian. That is to say, $0.5B+0.5C\succ0.5A+0.5C$ or more cleanly $B+C\succ A+C$. But this then contradicts the fact that we postulated $A\succ B$.

This demonstrates that using the independence axiom to characterize "more egalitarian than" relation doesn't work.


b)

One axiom that could potentially characterize a "more egalitarian than" relation is that there is a smaller difference between the least well off and the most well off. That is to say, if $Y_A,Z_A,Y_B,Z_B$are income levels where $Y_i$ is maximum income and $Z_i$ is minimum income, for distributions $A$ and $B$ respectively, then $A\succ B \leftrightarrow (Y_A - Z_A < Y_B - Z_B)$.

If we take the distribution in the image in 3a above, we can see that the preference relation $A\succ B$ upholds since $(Y_A - Z_A < Y_B - Z_B) \equiv 0<1$ (we can take that the difference $Y_B-Z_B$ is one step and can thus be characterized as 1). 