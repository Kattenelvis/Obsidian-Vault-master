
[Gödel’s Incompleteness Theorems (Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/entries/goedel-incompleteness/)

1. There's a difference between **recursively enumerable** sets (i.e sets of natural numbers which have a procedure to list them all, for instance, a way to calculate a list of prime numbers) vs **decidable/recursive sets** (sets with a function that returns yes if some input number is in that set, not the case for prime's I believe?).
2. $\omega$-consistency, such that it is *not* the case for a formal system $F$ that a formula $A(x)$ is such that $F\vdash \neg A(n)$ for all n and $F\vdash \exists x A(x)$. This implies consistency. The assumption can be lightened to 1-consistency i.e this is the case for all $\Sigma_0^1$ sentences. ![[Pasted image 20240324212255.png]]
3. A formal system F has a strongly representable set S so long as there exists some formula $A(x)$ in the language of F such that
   1. $n\in S \implies F\vdash A(n)$
   2. $n\notin S \implies F\vdash \neg A(n)$
      And weakly representable if 
     $n\in S \leftrightarrow F\vdash A(n)$

"It is obvious how all these notions are generalized to many-place relations. "

"There are also related notions of representability for functions."

"As the incompleteness results in particular teach us, there are sets which are only weakly but not strongly representable"

"[**Warning:** Here the terminology in the literature varies a lot: “strongly represent” is sometimes called, e.g., “represent”, “numeralwise express”, “bi-numerate”, “define” or “strongly define”; “weakly represent” is in turn also expressed, e.g., by “represent”, “define”, “weakly define”, or “numerate”. One should be careful here and focus on the relevant definitions, and not let the words mislead.]"

**The Representability Theorem**  
In any consistent formal system which contains **Q**:

1. A set (or relation) is strongly representable if and only if it is recursive;
2. A set (or relation) is weakly representable if and only if it is recursively enumerable.

"This holds for all formalized systems which contain Robinson arithmetic **Q**, from Robinson arithmetic itself to the strongest axioms systems of set theory like **ZFC** and beyond (as long as they are (recursively) axiomatizable)."

" A set S� is _definable_ in the language of arithmetic if there is a formula A(x)�(�) in the language such that A(n––)�(�_) is true in the standard structure of natural numbers (the intended interpretation) if and only if n∈S.�∈�. There are many sets which can be defined in the language of arithmetic but not (even weakly) represented in any F�, such as the set of consistent formulas, the set of sentences unprovable in the system F�, or the set of Diophantine equations with no solutions (see below)."




Kinda related to the second:

1.  Self-containment: a formal system that can describe the entire world with a bijection from a set of propositions to the world does not require a meta level to describe the world per definition. Assume a non-absolute formal system that includes some infinite set theory with some infinite set. A non-absolute formal system will point to the same set being of different cardinality in different models. A formal system describing the world is self-contained, meaning that we have to add an axiom in the system for which model to be chosen in that system, which changes the system and requires a new model, leading to regression. (ändrad)




The red stone volume 2:

![[Pasted image 20240202225911.png]]






