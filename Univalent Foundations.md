

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




![[Pasted image 20250804215123.png]]

![[Pasted image 20250804215226.png]]


![[Pasted image 20250804215525.png]]


![[Pasted image 20250804215632.png]]


![[Pasted image 20250804220400.png]]


![[Pasted image 20250804222854.png]]
1 is like $\top$


![[Pasted image 20250804223150.png]]



![[Pasted image 20250804224558.png]]


![[Pasted image 20250804231647.png]]

![[Pasted image 20250804232242.png]]




# Homotopy Type Theory

Systematic, Semi-formal

![[Pasted image 20250811214501.png]]

![[Pasted image 20250811215443.png]]
![[Pasted image 20250811215536.png]]
![[Pasted image 20250811215943.png]]



![[Pasted image 20250811220151.png]]


![[Pasted image 20250811220547.png]]

![[Pasted image 20250811221752.png]]


![[Pasted image 20250811222800.png]]
![[Pasted image 20250811223209.png]]




![[Pasted image 20250811224012.png]]Not just a point but moves in space
Up to homotopy equivalence


![[Pasted image 20250811225240.png]]

