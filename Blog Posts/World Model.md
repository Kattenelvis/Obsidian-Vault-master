Since empirical objects are unknowable beyond their direct sense-perception, we form a world-model which is:

An ontology $O=\{x_1,\dots ,x_n\}$ which is a set of empirical objects.
A set of empirical n-ary predicates (relations and predicates between objects) $\{F_1, F_2,\dots F_m\}$.
A set of logical symbols $\{\wedge, \vee, \leftrightarrow,\rightarrow\}$.

And a recursively defined propositional structure in intuitinistic type theory.
$F_i(x_1,\dots x_k) : proposition$  (for k-ary predicate $F_i$)
$p\wedge q : proposition$
$p\vee q : proposition$
$p\leftrightarrow q : proposition$
$p\rightarrow q : proposition$

Which then defines the set of all propositions $P$.

LEM is denied (for what reasons?)

This is a First order intuitionistic logic (I belive it's complete and consistent, try to find a source)

Uncertianty: Each object of type proposition have a confidence level attached to it which is a number between 0 and 1. 

Let $C:P\rightarrow [0,1]$ be a function from propositions to one's confidence level on a proposition.

If $p$ and $q$ are independent propositions (they don't share any predicates or objects) then
$C(p\wedge q)=C(p)C(q)$
$C(p\vee q)=min(C(p), C(q))$


Now let's say $q$ and $p$ are dependent. Then we reason (following NARS architecture):

Deduction (RELEVANCE LOGIC?)
Induction
Abduction
Confidence Updating

-   [3.2 Computational Philosophy of Science](https://plato.stanford.edu/entries/computational-philosophy/#CompPhilScie)
    -   [3.2.1 Network models of scientific theory](https://plato.stanford.edu/entries/computational-philosophy/#NetwModeScieTheo)
    -   [3.2.2 Network models of scientific communication](https://plato.stanford.edu/entries/computational-philosophy/#NetwModeScieComm)
    -   [3.2.3 Division of labor, diversity, and exploration](https://plato.stanford.edu/entries/computational-philosophy/#DiviLaboDiveExpl)


Scientific theory


Example: Newtonian mechanics

Inconsumerability of paradigms
Duhem Quine thesis

Example: Special Relativity


Encode a scientific theory into intuitionistic first order logic/FST and then demonstrate weak emergence i.e the existence of emperical objects and predicates of a higher theory. One example would be demonstrating the existence of chemical bonds from a formalised theory of quantum mechanics.

The syntactic view of scientific theories revival: Make them weaker than Peano Arithmetic.

Goal: Demonstrate that this is false:
"As was correctly pointed out by van Fraassen, Suppes, and others, scientists themselves don’t demand first-order axiomatizations of these theories – and so it would do violence to those theories to try to encode them in first-order logic. Thus, the demise of the syntactic view allowed philosophers to freely draw upon the resources of set-theoretic structures, such as topological spaces, Riemannian manifolds, Hilbert spaces, C∗-algebras, etc."

Does the Löwenheim-Skølem theorem apply to logical systems weaker than PA?
"By the 1970s, scientific realism was firmly entrenched as the dominant view in philosophy of science. Most the main players in the field – Boyd, Churchland, Kitcher, Lewis, Salmon, Sellars, etc. – had taken up the realist cause. Then, with a radical aboutface, Putnam again took up the tools of mathematical logic, this time to argue for the incoherence of realism. In his famous “model-theoretic argument,” Putnam argued that logical semantics – in particular, the Löwenheim-Skølem theorem – implies that any consistent theory is true. In effect, then, Putnam proposed a return to a more liberal account of theoretical equivalence, indeed, something even more liberal than the logical positivists’ notion of empirical equivalence. Indeed, in the most plausible interpretation of Putnam’s conclusion, it entails that any two consistent theories are equivalent to each other."


1.  Let $T$ be a consistent theory without objective truth. THE WORLD can be broken into infinitely many pieces. The theory has only infinite models. The completeness theorem implies that $T$ has a model of every infinite cardinality. Pick a model $M$ of the same cardinality as THE WORLD. Map the individuals of $M$ one-to-one into the pieces of THE WORLD, and use the mapping to define relations of $M$ directly in THE WORLD. The result is a satisfaction relation SAT - a 'correspondence' between the terms of [the language] $L$ and sets of pieces of THE WORLD such that theory $T$, comes out true true of THE WORLD provided we just interpret 'true' as TRUE(SAT). So whatever becomes of the claim that $T$ might be false? (Putnam 1978, pp. 125-126)
    
2.  _[_23:19_]_
    
    bara om du någonsin behöver en sammanfattning
    
3.  _[_23:19_]_
    
    Hilary Putnam model theoretic argument
    
4.  _[_23:19_]_
    
    Indeterminancy of reference: there are multiple ways to make a theory $T$ true.



Potentially Relevant Papers:

NARS in that AGI book

TOWARDS A PHILOSOPHY OF CHEMISTRY JOACHIM SCHUMMER

The Logic of Observation and Belief Revision in Scientifc Communities Hanna Sofe van Lee Sonja Smets

The Logics of Discovery in Popper’s Evolutionary Epistemology Mehul Shah

Logical Tools for Human Thinking: Jaakko Hintikka (1929–2015) Ilkka Niiniluot

The logic in philosophy of science




Field on Tarski's Truth 1972
![[Pasted image 20230114154317.png]]
![[Pasted image 20230114154350.png]]
It is convenient to introduce the expression 'primitively denotes' as follows: every name primitively denotes what it denotes; every predicate and every function symbol primitively denotes what it applies to or is fulfilled by; and no complex expression primitively denotes anything

Definition of $s_k$ 
![[Pasted image 20230118155103.png]]

< Idea >
Using Tarski's truth definition and have the primitive symbols denote concept of sensory perception. Correspondence with perception gives true statements. 

Primitive terms (the empiricist viewpoint) found in [[Semantics]]. Do I want to justify the empiricist theory of primitive terms? Or leave it as a premmiss?

Correspondance to sense-experience or phenomenology (the distinction being?). Are the primitive terms microphenomenal or macrophenomenal? How are they abstracted? Barkley?!

Avoiding gestalt primitive terms. Shapes and melodies are not primitive terms, but are made up of microvisual and microauditory phenomenal points.  

Now fields view on Tarski's truth definition. 
Each variable $x_k$ in the language has a referent $s_k$ that is an phenomenal primitive. 

1. 
2. 
'red' denotes$_s$ the experience of redness
'loud' denotes$_s$ the experience of loudness
3. $\left\ulcorner f_k(e) \right\urcorner$ denotes$_s$ phenomenal object $a$ iff 
	1. There is an object $b$ that $e$ denotes and 
	2. '$f_k$' is fulfilled by (a,b).
	   Where $e$ ranges over the expressions in $L$

1. $\left\ulcorner p_k(e) \right\urcorner$ is true iff 
	1. There is an phenomenal object $a$ that corresponds to $e$ and
	2. $p_k$ applies to $a$
2. Recursive clauses...

Even "me" or "I" is non-primitive since what I consider to be me is a subset of perception.

We must now specify the character of the phenomenal objects and how multiple microphenomenal objects form complex expression for macrophenomenal and gestalt objects, including mathematical objects which justify an empiricist view of mathematical objects. 

Complex expressions expressible in FOL:
"There is an experience 'red$_{44}$' at location $x,y$ in the visual phenomenal field" Can generalize coordinates if the visual system is not a simple cartesian grid. "There is an experience 'red$_{44}$' at location $r_1, r_2,\dots r_n$ for some coordinate system $r_i\in R$ in the visual phenomenal field".

"I experience pitch$_{35}$ at decibel$_{74}$ in the auditory phenomenal field".

Because it's first order logic we cannot predicate over sets, so if each visual microphenomena would be modelled as, for example $\{red_{44}, x, y\}$ then we would be predicating over sets rather than objects. Problems of phenomenal indexicals. 

[Visual space - Wikipedia](https://en.wikipedia.org/wiki/Visual_space)
CALL IT VISUAL SPACE NOT VISUAL FIELD

Williams says this: "Epistemic foundationalism does not really offer external constraints on our beliefs" is this uuhh, important?


Takedown of the difference between "objective" and "subjective" truth.

Objective and subjective truth as subject independent and dependent respectively.

Subjective: "There is experience pitch$_{35}$ at decibel$_{74}$ in the auditory phenomenal field".

Objective: "Subject $S_i$ is experiencing pitch$_{35}$ at decibel$_{74}$ in the auditory phenomenal field".

Theorem: There exists a translation from all subjective truths to objective truths.

This distinction might not be valid if objective and subjective truth is defined to be truth about the external world. This I will not discuss in this article. 


Complex definitions and gestalt objects

Cup $=_{df}$ Sight experience of cup $\wedge$ Tough experience of cup 

Properties derived from similarities in complex objects. Belief formation about complex objects. Causality between complex objects. Theories about complex objects. Coherence between theores, theory ladeness. Bracketing. 

Scientific realism or anti-realism

Belief revision of a complex sentence. 
Falsifying a belief: $P(S|E_i)>P(S|E_{i+1})$
Verifying a belief: $P(S|E_i)<P(S|E_{i+1})$

The newly added evidence in the larger set $E_{i+1}$ can increase or decrease the probability of a complex sentence S. 
What about Quinean global support? Other theoretical sentences can be a part of $E_{i+1}$!

This is why Bayesian > Inferentialism!!! A case for changing science!

Orthogonality thesis/Hume's guillitotine: Why science is not value-driven. A global act axiom is needed to justify any act, sentances with the word "should" in it.
Example of modus ponens with ethical axiom:
(1) You should take actions that maximise happiness
(2) Eating x chochlate bars will maximise happiness
(3) You should eat chocholate

Formalised:

$\forall x. max_x(H(x)) \rightarrow O(x)$
For obligatory modal operator $O$ and happiness function $H$ and action x. 

$max_x(H(x) = H(a)) \rightarrow O(a)$
Therefore
$O(a)$

Collective science? Takes place in sociology? 
A combined subject increases the number of sense-data, observation sentences, complex sentences and number of models and theories. It's only a sped up and there are no emergent collective structures. Institutional problems (for academia or corporate science) can affect the accuracy, negatively, for epistemic virtues on larger scale. 

Formalisation of phenomenal space and the space of all minds. Subsets and classes of phenomenal space, capable of different types of cognition, intelligences, consciousness and self-consciousness. 

Mind space of an electron
{spinup, momentum, energy level} isomorphic with {red, 1hz 1db sound, 1 point of popcorn smell}
As an example. 


Time dependence, finite state, Hoffmans evolutionary perspective, e.t.c will be discussed in future blog post. 


< /idea >

  
Let $f_1$ be an $n$-ary function $f_1(x_1, \cdots, x_n)$, and $f_i$ be a $(n+1-i)$-ary function and $f_i(x_1, \cdots, x_{n+1-i}) = f_{i+1}(x_1, \cdots, x_{n-i})$, then it follows that $f_1$ can be rewritten as $f_1(f_2(f_3(\cdots f_{n-2}(x_1, x_2) \cdots), x_{n-1}), x_n)$. This is given that all of this is within the language, then every $n$-ary function can be broken down into a finite composition of binary operations on the set \cite{Sierpinski}. Bevisar Sierpinskis påstående

Putnams arrgument:

Permutationer mellan modeller. Om en mängd axiom/språk har 5 null-ary predikat (konstanter) och ett axiom som säger "Det existerar endast en sann predikat" så har den 5 modeller. En för varje sann konstant. 

En teori är kategorisk om den bara har en modell upp till isomorfism.


Principle of Computational equivalence: Two finite automata with same tapelength and memory can express the same language.
Som konsekvens kan man beskriva samma system på flera sätt, som t.ex Pressburger aritmetik och FST samt Bayesiansk updatering/fuzzy updatering e.t.c. 

Men FST och bayesiansk updatering har varit lättast val då det kan mappas fill fenomenologi.
