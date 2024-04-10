
If FOL can express "standard set theory", and FOL is complete, does that mean standard set theory is complete? Perhaps not, since completeness is a product of the inference system instead of expressibility. ''

On Gödel: "Incompleteness in this sense concerns not the logic itself, but theories expressed in a formal language such as FOL." So I was right I guess?

But if FOL is complete, some theories expressed in FOL are incomplete, theories cannot prove their own completeness, can FOL imply that complete theories expressed in FOL are complete?

"ödel had assumed, for the theories to which his result applied, that the problem of recognizing the axioms was primitive recursive, which means that the corresponding (characteristic) function is computable in a particularly simple way (see Chapter 8). But certain intuitively computable functions were known not to be primitive recursive, so for maximum generality in the incompleteness theorems one would need a precise notion of computability"

"It soon became clear that all theories to which the incompleteness theorems apply are undecidable (i.e. the problem of recognizing their theorems is undecidable)."

FOL is undecidable

Tractability: decidable and algorithms with "reasonable" time and space complexity.

A set of theorems is semi-decidable in the sense that one can find an effective procedure for positive answers to "Is $\phi$ a theorem in $T$ ?"

Tarski undefinability theorem

Compactness theorem gives results regarding models in FOL and their properties.

Löwenheim Skolem theorem is implied by compactness theorem.


Fullständighet: Alla modeller som gör premisserna sanna implicerar att om en sats är då också sann kan deriveras. 

Sundhet: Alla modeller som gör premisserna sanna implicerar att om **och endast om** en sats är då också sann kan deriveras. 
Checking that a system is sound is usually easy: it is a matter of verifying that all the rules lead from true assumptions to true conclusions (in any interpretation).

Natural Deduction inference rules:

![[Pasted image 20230121191900.png]]

![[Pasted image 20230121191852.png]]

![[Pasted image 20230121191843.png]]

![[Pasted image 20230121191833.png]]
![[Pasted image 20230121191828.png]]

![[Pasted image 20230121191744.png]]

![[Pasted image 20230121191803.png]]


![[Pasted image 20230222103125.png]]


	And an undecidable problem can have a decidable sub-problem; for example, first-order logic with only unary predicate symbols (FOLmon) is decidable, and predicate logic where quantification is restricted to certain formats can be decidable.
	
Theorem 7.2.4 (First Incompleteness Theorem) Every consistent axiomatizable extension of PA is incomplete.