# Lecture 1
Stockholm AGI Lab
Digital Futures
Robert Johansson


AGI-23 Annual AGI conference
![[Pasted image 20241205132135.png]]


Functional learning psychology, not Cognitive learning psychology

Cybernetics


Ben Görtzel




![[Pasted image 20241205141413.png]]
![[Pasted image 20241205141525.png]]
![[Pasted image 20241205141620.png]]
![[Pasted image 20241205141711.png]]


![[Pasted image 20241205142636.png]]


![[Pasted image 20241205142846.png]]

![[Pasted image 20241205143055.png]]

![[Pasted image 20241205151239.png]]

![[Pasted image 20241205152625.png]]


OpenNARS:

Git Clone it
./build.sh
./NAR shell | python3 colorize.py
G! :|:

![[Pasted image 20241205154902.png]]

Learning!



My question 1:
We discussed this course with a logic professor and he was a bit worried about the name "non-axiomatic" logic, as in a sense all logics can be non-axiomatic if you only have a semantics without axiomatizing it. It's also the case that some logics are non-axiomatizable where he gave second order logic as an example. You seem to try in footnote 2 to answer this but he doesn't really understand what you mean with "deriving the inference rules from axioms" as that is generally not possible. 

Answer:

Term logic.
Instead of typical axioms to conclusion, it requires combining two terms into something else.






My question 2: 
How would I go about if I wanted to participate in the Stockholm AGI lab. For bachelor, masters or PhD thesis' or even as independent researcher.




My question at swecog answered better here:

NARS is not pre-trained, so the alignment problem might be more problematic. But it might be required for human level AGI. 
RHLF it using some kind of "education" (not really RHLF since it's not a LLM but something similar). Bias is different, no longer about training data but the kind of school.



Anandi is writing a book on AGI from the perspective on philosophy!!!!!
HUGE!!!!!!!
OMG!!!


# Lecture 2


Learning psychology


Ontogenetic adaptation. 
Ontogonetic: Throughout a lifetime. Not pre-trained or phylogenetic adaption.


Learning as changes in behavior due to regularities in the environment.

Behavior Changes: 

Regularities: Repeat events. Law-like behaviour. Beahavior and consequences.

Causality.


Independent and dependent variables in an experimental setting. What we can change and the effects respectively. We can look at how there's changes in behaviour between being and environment.

![[Pasted image 20241206092017.png]]




![[Pasted image 20241206093129.png]]

![[Pasted image 20241206093411.png]]
![[Pasted image 20241206093618.png]]


![[Pasted image 20241206093747.png]]
![[Pasted image 20241206094104.png]]

The "when" does learning occur is important for the functional perspective. 
Idea: The "how" question is more cognitive?


![[Pasted image 20241206101036.png]]
### Complex learning 1


🟥
🟥🟩?
Red is correct answer.

🟩
🟥🟩
Green is correct answer.


Then generalize to new situation
⭐
⬜⭐
Yellow star will generally be picked

Transfer learning

![[Pasted image 20241206102524.png]]


### Complex learning 2 

![[Pasted image 20241206102746.png]]


### Complex learning 3

Picking largest objects
![[Pasted image 20241206103051.png]]

New stimulus and  pick the largest one

![[Pasted image 20241206103108.png]]


Q: The environment’s role here is stored as memory of multiple experience then, right?

A: It's a cognitive hypothesis which explains the functional work. 


![[Pasted image 20241206104120.png]]


Swapping is not found in any non-human animal!!!

B1

A1   A2

Taught A1 as the right answer

Given such a training, humans will in the following scenario pick B1

A1

B1    B2

However animals don't! That's probably why he said it was the key to general intelligence.


Meta-regularity:

![[Pasted image 20241206110515.png]]

Children as young as 16 months old cannot do the bottom line only, but can do the bottom line if it has been trained on the upper line.

Relational Frame Theory
About Arbitrarily applicable relational responding. Learning arbitrary relations. 

The symmetry is more abstract. 


![[Pasted image 20241206112053.png]]
![[Pasted image 20241206112234.png]]



Behavioural psychology  critique by noam chomsky. 
1. The generativity of language. How could that be explained by beahavioural psychology? (poverty of stimulus argument, argument from productivity of language).
2. Symbolisms of language how can reference of object and the idea be explained (symbol grounding problem).




# Lecture 3

## Readings before

Wang 2013:
"In NARS, a “concept” is a data structure with a unique ID called a “term”. At the interface between the system and its environment, a concept may directly correspond to a sensation obtained from a sensorimotor channel, a character received from a language channel, and so on. From them, compound terms are constructed to represent the patterns found in experience. Though it is fine to consider each term as a symbol representing a concept, a concept itself is not a symbol representing an external object or event. This is a fundamental difference between NARS and the traditional “symbolic AI” (Newell and Simon, 1976; McCarthy, 1989)."

> Since a conceptual relation is usually an abstraction of experience, it may agree with different segments of the system’s experience to different extents, that is, a statement may have both positive and negative evidence. Consequently, whether the statement is “true” becomes a matter of degree. Though multi-valued logic is not novel, what makes NARS dif ferent from various probabilistic logics (Nilsson, 1986) and fuzzy logics (Zadeh, 1983) is that its truth-value is obtained by checking the statement against the system’s ever-expending experience, rather than a static description of the domain, as in model-theoretic semantics (Barwise and Etchemendy, 1989).

> In summary, NARS segments and abstracts its experience into concepts related by a few forms of substitutability. As the meaning of concepts and the truth-value of conceptual relations are defined according to the system’s own experience, NARS is fundamentally different from both the symbolic approaches and the connectionist ones in knowledge rep resentation, and does not suffer from the “symbol grounding problem” in its original sense (Harnad, 1990), as its concepts do not become meaningful by being “grounded” in outside objects or their sensations, even though the meaning of abstract concepts can get richer with relations to sensorimotor activities that directly interacting with the environment.

## The Lecture

![[Pasted image 20241210131734.png]]



NARS 9 layers?

Layer 1:
![[Pasted image 20241210132022.png]]

[OpenNARS for Applications: Shell](http://91.203.212.130/ONA/GUI.html)

\*concepts

"Juice" <-> juice


![[Pasted image 20241210133816.png]]


NARS layer 4
![[Pasted image 20241210133859.png]]

One can then derive opposite between juice bottle and coffee, and then derive that coffee is bad, assuming it has learnt that good is the opposite of bad

![[Pasted image 20241210134112.png]]


![[Pasted image 20241210134525.png]]

![[Pasted image 20241210134700.png]]



# Lecture 4

Rat conditional learning, explore vs exploit inside the cage. Gets water if turning clockwise and light off, and if turning counter-clockwise and light on.


Only layer 7 and 8, the basis of operant conditioning.
Top of the hierarchy.

But you can do it bottom up aswell.

![[Pasted image 20241211131457.png]]

any learning situation can be described for NARS

"Light_on. :|:"    is a Status update
"G!" is some goal

![[Pasted image 20241211131933.png]]

Different scenario:

![[Pasted image 20241211132433.png]]

"G. :|: {0.0 0.9}" means  G happened with 0 frequency.

What you wanted did not happen. The AI did not know what would happen if light is off. 

cw clockwise
acw anti-clockwise
^ means the AI can execute it.



![[Pasted image 20241211132732.png]]
Revision after doing it twice. Confidence goes up. 

Temporal inductions. Learn from experience over time. Basic unit of NARS is event in time. Learn from experience, derive something from that.



![[Pasted image 20241211133034.png]]



![[Pasted image 20241211133622.png]]
Stimulus-response conditioning


![[Pasted image 20241211142005.png]]

NARS does not need a goal to learn, unlike reinforcement learning

Triangle tests, kittens? And NARS

Symbol matching tests

![[Pasted image 20241211144203.png]]



Open Sesame design psychological experiments with human beings. Or NARS! As a participant. Ok huge.


Typesetting:

![[Pasted image 20241211152537.png]]

left * green is of combined typed location \* color

![[Pasted image 20241211152602.png]]


![[Pasted image 20241211154018.png]]


# Lecture 5



![[Pasted image 20241213092401.png]]

![[Pasted image 20241213092506.png]]


Intelligence has more to do with general purpose cognition and being able to reason in novel conditions. Under resource and time constraints.

Find programs that find the best explanations of observations. 

Catastrophic forgetting. With fixed memory, data might be overwritten. 

![[Pasted image 20241213093158.png]]


![[Pasted image 20241213093321.png]]

Domain independence it can learn about many concepts.

rich expressing power in terms of logic. Implications, conjunctions etc. 

Predictive coding

![[Pasted image 20241213101313.png]]

![[Pasted image 20241213101850.png]]

![[Pasted image 20241213102211.png]]


Formalizing human knowledge into fol in an earlier project.
Didn't quite work because of universally quantified statements are often false. So you add exceptions. "All ravens are black except instance 1,2,...n" (say, albino ravens) which is not good for resource constrained agents. 


Term logic based deduction, induction, abduction and revision

![[Pasted image 20241213103243.png]]


![[Pasted image 20241213103827.png]]



![[Pasted image 20241213104144.png]]

![[Pasted image 20241213111202.png]]


Question:Does instrumental convergence apply to NARS. That is to say, when subgoaling there is a small set of sub-goals which end up useful for a large set of goals?


Answer: Revision of goals

Want to achieve 
![[Pasted image 20241213112617.png]]

if also w accumilitates evidence. 

Reinfocrmcent learning: Model-free and model-based reinforcment learning.

Model-free: Utility function maximization. Doesn't know much about states other than reward?
Model-based: Modeling state transition and inferences. Encodes states. 



# Lecture 6


![[Pasted image 20241217130842.png]]





![[Pasted image 20241217134027.png]]
Temporal reasoning, temporal induction (found in operant condition aswell)

vs Abstraction, variable introduction



Functional equivalence + implications Stage 5. Moderated learning.

Multiple standard (i.e non-meta) regularities involved at the same time.

![[Pasted image 20241217144542.png]]

Substitutable events


![[Pasted image 20241217151240.png]]

$R_i$ means pressing button $i$, perhaps at some location.

![[Pasted image 20241217151431.png]]
![[Pasted image 20241217151500.png]]


http://91.203.212.130/AniNAL/demo.html




# Lecture 7 

Arbitrarily Applicable Relational Responding
Relational Frame Theory

![[Pasted image 20241218131125.png]]


Imitation game. Turing argues that "can machine think" is hard/indeterminate to answer without a definition of "think". So he skips it and changes the question.

We can go back with defining what thinking is with the help of relational frame theory.


Murray Sidman Reading and auditory-visual equivalences. A menatlly handicapped boy who couldn't read.

![[Pasted image 20241218132639.png]]
He knew A-B-D but was trained to do A-C

He got to know things he wasn't explicitly trained in. Could point between the word "cat" and pictures of cat. 


![[Pasted image 20241218132816.png]]

Upheval in cog sci: People thought it was only through operant condition that someone learnt. Common behaviourist L and cognitivist W.


Transitivity and reflexivity. Sameness.

![[Pasted image 20241218133448.png]]


![[Pasted image 20241218133907.png]]


The key part of intelligence: Being able to derive many relations from a few.

From
A > B
B > C

You can derive
A > C
B < A
C < A
B < C

![[Pasted image 20241218140253.png]]

![[Pasted image 20241218140527.png]]



Equivalence relations

![[Pasted image 20241218141505.png]]

![[Pasted image 20241218141650.png]]

![[Pasted image 20241218141717.png]]

Measuring skin-conductance under fear response when trained under a greater-schock relation between A, B, C.

![[Pasted image 20241218142227.png]]

![[Pasted image 20241218142443.png]]

![[Pasted image 20241218142624.png]]

![[Pasted image 20241218142933.png]]

![[Pasted image 20241218143128.png]]

![[Pasted image 20241218151229.png]]

![[Pasted image 20241218151955.png]]

![[Pasted image 20241218152325.png]]

![[Pasted image 20241218152916.png]]




# Lecture 9 Ethics


Bias

Deep Learning requires labeled data, typically have an over-representation of some groups over others.

"The meaning of symbols is based on its experience" Heck yeah.


Responsibility gaps when training NARS systems. Independence of AI agents. 


Make many simulations of depression!?


![[Pasted image 20250114104926.png]]

![[Pasted image 20250114105406.png]]


