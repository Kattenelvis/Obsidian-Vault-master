[Lucas-Penrose Argument about Gödel’s Theorem | Internet Encyclopedia of Philosophy (utm.edu)](https://iep.utm.edu/lp-argue/)

The main idea is that a formal system F which is transformed into a Turing Machine which runs F, where F is a w-consistent formal system which contains peano arithmetic, can by Gödel's first incompleteness theorem never prove their own Gödel sentence G, yet a human mind can "understand" G to be true. 

The main counter-argument brought forth by Benacceraff is that human minds are implemented by something much more complicated than Peano arithmetic, and that we can not proove nor see the truth of our own Gödel sentence. This mirrors Daniel Dennetts criticism that humans don't just go around doing Peano arithmetic and nothing else. The Gödel sentences describing a human mind is too complicated for  said human mind to know. So we end up with a disjunction, either we are non-computational, or we don't know our own Gödel sentence. 

Another counter-argument is Putnam's (a philosopher who is a big proponent of the computuational theory of mind) which uses Gödels second incompleteness theorem. Since we cannot prove humans minds implement w-consistent formal systems from itself, then we cannot know whether or not the human mind is computable. Here it is from his article:

"(1) Gödel's First Incompleteness Theorem only applies to consistent formal systems. 
(2) Gödel's Second Incompleteness Theorem establishes that one cannot establish the consistency of a formal system from within the system itself, so 
(3) If we are TMs, we can never establish our own consistency (and cannot, therefore, confidently apply Gödel's First Theorem to ourselves)." (citation)





From the bachelors essay


\subsubsection{Gödel's disjunction and the Lucas-Penrose Argument}
A technical argument sometimes brought up is Gödel's disjunction and the related but more controversial Lucas-Penrose argument. The idea is that Gödel's first Incompleteness Theorem implies that human minds are beyond "Turing machines". A Turing Machine is a formal idealization of computational systems. In Turing's formulation of it, a Turing machine is an infintely long tape of discrete slots where each slot can take on a symbol from some alphabet. There's a device which can read the slots, where based on the rules of the device, the device's internal state, and the number it scans, it might rewrite the symbol, change its state and move either left or right or stay put. Perhaps the human mind can be described by such a formal idealization. What's especially important to note for this section, is that any formal system $F$ can be trivially run on a Turing Machine. 

Gödel's first incompleteness theorem states that for consistent formal systems that capture arithmetic, there exists statements which are true but unprovable. Formally, for a Gödel sentence $G$, Gödelization of $G$ as $\lceil G\rceil$, the provability predicate $Prov$ and formal system $F$: \cite{raatikainen2020goedel}

$$F\vdash G\leftrightarrow \neg Prov(\lceil G\rceil)$$

Gödel thought that his theorem implies the following disjunction: either the human mind exceeds computation or that there are absolutely unsolvable Diophantine equations. This has become known as Gödel's disjunction, and is generally accepted. However this is merely a disjunction, and only demonstrates that the human mind exceeds computation only if there are no absolutely unsolvable diophantine equations, which is controversial.

A stronger argument was put forth by Lucas \citep{originalLucas} and later defended by Penrose, though remains highly controversial. The argument goes as follows: a formal system $F$, for which Gödels incompleteness theorem's apply, is transformed into a Turing Machine which runs $F$. By Gödels first incompleteness theorem the Turing machine could never prove its own Gödel sentence $G$, yet a human mind can "understand" $G$ to be true (We "see" the The Gödel sentence as true since it is not provable). \cite{megill-lp}

One major counter-argument brought forth by Benacerraf is that human minds are implemented by very complicated formal theories, and that we can not prove nor see the truth of our own Gödel sentence. The Gödel sentence of our own minds is unreachable from ourselves. This mirrors Dennetts criticism that humans don't just go around doing first order arithmetic, the simplest formal theory where Gödels incompleteness theorems apply, and nothing else. The Gödel sentences describing a human mind is too complicated for  said human mind to know. So we end up with a disjunction, either we are non-computational, or we don't know our own Gödel sentence. \cite{megill-lp}

Another counter-argument is Putnam's, where Putnam considers the argument to be a logical error, since it can be shown false by considering Gödel's second incompleteness theorem. The kinds of systems where Gödel's incompleteness theorem apply have to be consistent. By Gödel's second incompleteness theorem, one cannot prove that a system is consistent from within itself. Thus it follows that one cannot prove that humans minds implement consistent formal systems from itself, then we cannot know whether or not the human mind is computable. Putnam sets up the argument as follows \citep{paraconsistent}: 

\begin{enumerate}
    \item Gödel's First Incompleteness Theorem only applies to consistent formal systems. 
    \item Gödel's Second Incompleteness Theorem establishes that one cannot establish the consistency of a formal system from within the system itself
    \item If we are Turing Machines, we can never establish our own consistency (and cannot, therefore, confidently apply Gödel's First Incompleteness Theorem to ourselves).
\end{enumerate}

Putnam's argument is generally considered decisive in the literature, and people like Penrose can be considered very heterodox for remaining in defense of the argument. So few are convinced by Lucas's argument.

