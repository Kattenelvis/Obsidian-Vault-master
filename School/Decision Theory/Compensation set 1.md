

1.1
![[Exercise 11 decsion tree.excalidraw]]


1.3

Consider the following decision table:

| Actions/Outcomes | 1   | 2   | 3   |
| ---------------- | --- | --- | --- |
| a                | 10  | 9   | 8   |
| b                | 9   | 8   | 7   |

Let's apply the optimism-pessimism rule for action a, with an optimism index $\alpha\in[0,1]$:

$10\alpha + 8(1-\alpha)$

Likewise for action b:

$9\alpha + 7(1-\alpha)$

Since $\alpha \geq 0$, both terms in the summation are non-negative, we get

$10\alpha \geq 9\alpha$ and $8(1-\alpha) >7(1-\alpha)$

Hence it follows that

$10\alpha + 8(1-\alpha)> 9\alpha + 7(1-\alpha)$

Hence the optimism-pessimism rule fails to exclude the dominated option in this case.

1.4 

a) 

Consider the following decision table:

| Act/Outcome | s1 (1/2) | s2 (1/2) |
| ----------- | -------- | -------- |
| **a1**      | 1        | 1        |
| **a2**      | 0        | 1.5      |

As we can see, the principle of insufficient reason is applied as all states have equal probability (in this case, since there are two states, the probability is set to 1/2).

If we calculate expected utilities of the actions we can see that

$EU(a_1)= 1/2 + 1/2 = 1 > 0.75 = 0 + 1.5/2 = EU(a_2)$

However if we apply following ordinal transformation of the decision table, then the expected utilities of the actions will swap:

| Act/Outcome | s1 (1/2) | s2 (1/2) |
| ----------- | -------- | -------- |
| **a1\***    | 1        | 1        |
| **a2\***    | 0        | 3        |

$EU(a_1^*)= 1/2 + 1/2 = 1 < 1.5 = 0 + 3/2 = EU(a_2^*)$

Hence, some ordinal transformations fail to preserve the act picked by hte principle of insufficient reason.