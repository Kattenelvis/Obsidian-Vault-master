

![[Pasted image 20230531111701.png]]


[Challenges to Metaphysical Realism > The Model-Theoretic Argument and the Completeness Theorem (Stanford Encyclopedia of Philosophy)](https://plato.stanford.edu/entries/realism-sem-challenge/model-theory-completeness.html)


xample 1.3.15 Let  = {p}, and let T = {p}. Let  = {p,q}, and let T  = {p}. Here we must think of T and T  as different theories, even though they consist of the same sentences – i.e., T = T  . One reason to think of these as different theories: T is complete, but T  is incomplete. Another reason to think of T and T  as distinct is that they have different deductive closures. For example, q ∨ ¬q is in the deductive closure of T  , but not of T . The point here turns out to be philosophically more important than one might think. Quine argued (correctly, we think) that choosing a theory is not just choosing axioms, but axioms in a particular language. Thus, one can’t tell what theory a person accepts merely by seeing a list of the sentences that she believes to be true.



Tim Button Philosophy and Model Theory

![[Pasted image 20240110125131.png]]


![[Pasted image 20240110125938.png]]

Hybrid of Tarskian semantics and Robinson semantics introduces new variables as needed

![[Pasted image 20240110132046.png]]


https://www.reddit.com/r/math/comments/74q8ne/whats_the_difference_between_an_interpretation/
# What's the difference between an interpretation and a model?

> An interpretation of a theory _T_ in a theory _S_ is a mapping _I_ of sentences in the language of _T_ to sentences in the language of _S_ so that for every φ ∈ _T_ we have _S_ proves _I_(φ). For example, if _T_ is Peano arithmetic and _S_ is ZFC then we get an interpretation of PA in ZFC by replacing every arithmetical sentence φ with the sentence in the language of set theory asserting that φ holds of ω with the standard ordinal addition, multiplication, and order. (Explicitly giving this interpretation is a straightforward but tedious exercise.) If there is an interpretation of _T_ in _S_ then we say that _S_ interprets _T_.

> On the other hand, models aren't about syntax at all. A model or structure is just a set with some relations or functions on it and maybe also some constants on it. For example, (**R**; +, ×, <, 0, 1) is a model, referring to the usual arithmetic operations on the reals. Given a model you want to ask what statements are true about it. Formally, this requires that the statements be written in an appropriate language and that we have an assignment between relations/functions/constants from the structure and appropriate symbols from the language. For example, we might have a language with a symbol _R_ for a binary relation, two symbols _A_ and _B_ for binary functions, and two symbols _X_ and _Y_ for constants. Then we can talk about what sentences are satisfied by (**R**; +, ×, <, 0, 1) where we assign + to _A_, × to _B_, < to _R_, 0 to _X_, and 1 to _Y_. (Of course, we could choose a different assignment and get different sentences are satisfied.) Formally, the definition of satisfaction is given recursively by Tarski's compositional axioms. (See e.g. [this SEP page](https://plato.stanford.edu/entries/tarski-truth/).)

> In practice, we often use the same symbols for both the relation/function/constant in the model and the corresponding symbol in the language, with this implicitly giving the assignment from relations/functions/constants to symbols. It's easier to say that (**R**; +, ×, <, 0, 1) satisfies 0 < 1 + 1 than it is to say that (**R**; +, ×, <, 0, 1) satisfies _R_(_X_,_A_(_Y_,_Y_)) under the above-explained assignment.

> To bring the two concepts together: if _S_ interprets _T_ then this means that given any model _M_ of _S_ we can use it to construct a model _N_ of _T_. This is done in exactly the way you'd expect it. Working out the details is a good exercise.





