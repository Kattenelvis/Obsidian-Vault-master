

> Homotopy type theory also brings new ideas into the very foundation of mathematics. On
the one hand, there is Voevodsky’s subtle and beautiful univalence axiom. The univalence ax-
iom implies, in particular, that isomorphic structures can be identified, a principle that mathe-
maticians have been happily using on workdays, despite its incompatibility with the “official”
doctrines of conventional foundations. On the other hand, we have higher inductive types, which
provide direct, logical descriptions of some of the basic spaces and constructions of homotopy
theory: spheres, cylinders, truncations, localizations, etc. Both ideas are impossible to capture
directly in classical set-theoretic foundations, but when combined in homotopy type theory, they
permit an entirely new kind of “logic of homotopy types”.

> This suggests a new conception of foundations of mathematics, with intrinsic homotopical
content, an “invariant” conception of the objects of mathematics — and convenient machine
implementations, which can serve as a practical aid to the working mathematician. This is the
Univalent Foundations program. The present book is intended as a first systematic exposition of
the basics of univalent foundations, and a collection of examples of this new style of reasoning
— but without requiring the reader to know or learn any formal logic, or to use any computer
proof assistant.





Types are not weird sets, they are spaces
And guess what homotopy theory deals with! Mappings between spaces!


![[Pasted image 20250720124639.png]]
Question: In the case where f and g are mappings from the real number line to the torus, would this make the real number line and the torus "isomorphic up to homotopy"? What about mappings from the torus to the 3-sphere?



![[Pasted image 20250720124951.png]]


"No topological notions such as open subsets, only homotopical principles like paths and mappings between paths"

So I guess neighborhoods, cauchy sequences and so on also aren't there?



![[Pasted image 20250720130506.png]]"For instance, interpreting types
as sheaves helps explain the intuitionistic nature of type-theoretic logic, while interpreting them
as partial equivalence relations or “domains” helps explain its computational aspects. "

Hmmm

"The key new idea of the homotopy interpretation is that the logical notion of identity a = b of
two objects a, b : A of the same type A can be understood as the existence of a path p : a ; b from point a to point b in the space A"




![[Pasted image 20250720132407.png]]

![[Pasted image 20250720133215.png]]



![[Pasted image 20250720133720.png]]