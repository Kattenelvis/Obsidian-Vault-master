
In this article I explicate a phenomenalist ontology and mereology (POM) formalized in set theory which takes phenomenal consciousness as seriously as it deserves. Philosophy of mind sometimes lacks mathematical formalism. Often it is the general theories of neuroscience that involve such mathematical formalism, such as Integrated Information Theory and Global Workspace Theory (as the two competing scientific models of consciousness). 

The ontology is minimal, is fairly trivial and not particularly profound as it may seem (this goes for both sceptics and people who are prematurely praising this). There's a decent chance not everyone will be familiar with the concept of phenomenal experience as lay people have [no concept for it and has to be taught as a part of an education in philosophy]([Folk_Psychology_and_Phenomenal_Consciousness.pdf (pitt.edu)](https://philsci-archive.pitt.edu/5180/1/Folk_Psychology_and_Phenomenal_Consciousness.pdf)). They claim this is due to differences in how philosophers and lay people attributed "seeing red" between robots and humans. If you are not trained in philosophy and know what phenomenal consciousness is, one way to conceive of it is what it is like to be. It is the colors, the textures of touch, the sounds. It is not things, or ordinary objects such as a blue bottle of water, but rather the flat 2D screen of blue in some region of your visual field. Imagine putting on VR glasses, and taking a look at the pixels of there. It's not about acting as if red is there.

# Brief overview of formal phenomenology

I go more in depth about formal phenomenology here: [Formal Phenomenology]. But I will give a brief overview here.

Visual experience can be constructed in set-construction notation as the following:
$V=\{v:v\in[0, X]\times [0, Y] \times [0, B] \times [0, H] \times [0, S] \}$

This gives us points such as 
$\{4,4,0.5,0.3, 0.8\}$

This object is the point at position $(4,4)$, has a brightness of 50% and a hue of 0.3, which if we take a hue of 0 as red, then 0.3 would be some kind of orangy-yellow on the hue wheel with a strong saturation of 0.8. It is worth noting by [non linearities in visual space], the space may be more complicated (such as peripheral vision having larger pixels). It is up to perceptive psychological research, heterophenomenology etc. to figure out the ultimate nature of these set structures. But we assume a cartesian 2D grid for visual space at the moment for simplicity, it's not important for the argument. 

We can take all subsets i.e the powerset of visual space as a $P(V)$. We can take this to be an important set as each member could then fully describe an individual's visual experience (such as a human looking at a computer screen). $V$ just predicates over visual points or pixels (if visual space is continuous or discrete respectively, we will come back to this later). The Powerset of is all possible ways of combining different visual points into larger experiences (such as a pencil, a thought, a sunset). I am only aware of a subset of the power set that maximises predictability i.e I’m not aware of random subsets of the powerset, but there’s order to what I am aware of. 

We can now define an entire experiential space, including visual space V, auditory space A etc. with the powerset operation P as the following:

$E = \{P(V)\times\dots\times P(F) \}$

Which makes $E$ the space of all possible phenomenal experiences. We will call $E$ *experiential space*. 

We can then for instance take certain experiences out of it and index them, for instance, if I have a pet rabbit at some moment $t$, it's experience in that set could be marked as $E_🐰\in E$ . We mark "The" experience that's currently happening right now to YOU reading this as $E_@\in E$ where the "@" symbol is inspired by the "actual world" in possible worlds semantics. What $E_@$ refers to changes over time. As such we may index it at each timestep t as $E_{@,t}$. Most of $E$ is going to be something akin to "white noise" for all senses, only a tiny subset are structure the way human or animal experiences are structured. 

We can take the union of all concretely instantiated experiences in the 
universe at some timestep $t$ to be

$E_{U,t} = \{E_{1, t},\dots E_{N, t}\}$

For ease we define $E_{U,t}=U_t$ and we can say that this is the "phase point" of $E$ where we can take to be $E$ is the phase space as it changes over time. The latter "$U$" is chosen to stand for the universe. We will later see how one can model the phase space changes using psycho-physical laws. 

Solipsism can then be defined as
$E_@ = U_t$

Lastly, we take all consciousness over all time steps between $1$ and $T$ to be 
$U = \{U_1,\dots U_T\}$

# Continuity vs Discreteness

We now come back to the question whether experiential space is discrete or continuous. We can model some arbitrary member of experiential space in any of the three following ways: 

(1) $|A| = c$
(2) $|A| = \aleph_0$
(3) $|A| = \aleph_n$ for all n>0

While POM does not included any metaphysically substantive claims, and is agnostic towards all 3 theses, I will argue that thesis (1) is the most reasonable. ([A lot of similar systems to POM seem to take (2) or (3) for granted]) 

The first argument is due to Skolem's paradox and the related Putnam's paradox. Propositions about POM in cases of infinities will also have models whose ontology has higher cardinals, leading to multiple models. The solution is to only allow a finite number of items. The rest of this article will not run on this assumption, but may mention it. 

The second argument is an empirical argument, based on our current understanding of perceptive psychology. It seems like, for humans atleast, phenomenal experience cannot be continuous, due to the finite processing power of perceptive organs and the brain. If we take heterophenomenology to be empirical, there have been individuals who have [gotten head-trauma and end up seeing the world discretized]. It is likely that the continuity of phenomenal experience is an illusion by the brain. 

An example of how (1) can play out in the discreteness of phenomenal points:
Take hue for example, from $[0,H]$ (including the topological property that it is a circle and $0=H$.). It must then be the case $H\in\mathbb{N}$. As such there's only an finite number of possible experiences of hue's. Take us humans $M\subset E$ for instance, they could experience more hue's than we currently do with future technology, but at some point there's no more. We currently experience roughly 12 million colors [source].

# Idealist Mereology

There are many ways we could model the mereology. As this is a minimal model, we will be using [ontological modelling in finitist set theory]. Finitist set theories (there are several ones that include different set theoretic axioms) are complete and decidable. Decidability means an algorithm is constructible, where one can input a formula and it outputs whether it’s true or false. And they are complete, so all formulas are derivable through a finite number of steps. As we argued for (1) earlier, this turns out to be fully compatible with that view. 

We can as thus form the ur-elements as say, visual pixels in visual space, and then have subsets and chains of subsets within visual space. So if I see a blue region, then there is a subset of that blue region which is also blue. The blue region may be a subset above it, and so on. Let k be the singleton set for a single pixel of perception (like one pixel red or one frequency of audio or the strength of some type of aroma e.t.c) 

Gunky phenomenal consciousness
Junky phenomenal consciousness

# Change Over time

Empirically we can tell that experience is not static, but changes. We may say that it changes ‘over time’. Time in this context is defined as a mapping from experiences to the changed one at a later point in time. 

Definition: Let $T :E \rightarrow E$ be a function that inputs experience sets and outputs experience sets. As an example we get $T(U_1) = U_2$ between two time points for a discrete updating process. For continuous processes we may establish $T : \mathbb{R}\rightarrow E$ such that one inputs time and gets the experience at that time, for instance $T(\sqrt{2})$ gives you the phenomenal experience at time square root of two. We will be continuing with discrete time steps.

We can take note of a single microphenomenal point on the visual field, take $v\in V$. We can then see that the color changes. We can model it using such a function. Example:

Let $E_0=\{\{blue,1\},\{red,2\}\}$ be an experience that contains a visual field with one blue pixel to the left and one red pixel to the right and nothing else. Then we define $T(\{blue, x\}) = \{red, x\}$ and $T(\{red, x\}) = \{blue, x\}$. Using our definition of time above we get:

$$T(E_0)=T(\{\{blue,1\},\{red,2\}\})$$
$$=\{T(\{blue,1\}), T(\{red,2\})\}$$
$$=\{\{red,1\}, \{blue,2\}\}$$
$$=E_1$$

Which tells us that the subject is now experiencing the red to the left and blue to the right. As can easily be seen, this process will continue indefinitely. With this basic example in mind, imagine if something like this was applied to an experience with human-level complexity. In general, the time function defined above has the following property: 
 $$T(E_t) = T(\bigcup_{n\in E_t} r)=\bigcup_{n\in E_t} T(r)=E_{t+1}$$

The second definition of time. And that is if the function updates one's entire experience at once.
$$T(E_t) = E_{t+1}$$
This one takes one’s entire experience and processes it at once. This one is always going to be true as long as solipsism is true. Why? Recall , this implies the following:
$$E_t\subset U$$ 
This means that we’ve basically copied the previous time definition but scaled it up.  
 
$$T(U_t) = T(\bigcup_{E_{i,t}\in U_t} \{E_{i,t}\})=\bigcup_{E_{i,t}\in U_t} T(\{E_{i,t}\})=U_{t+1}$$

And the last one
$$T(U_t) =U_{t+1}$$

The totality of experience is all updated at once. If solipsism is true, then 2 is identical to 3.

Again, it's worth noting that POM does not make any substantive metaphysical claims about which version of $T$ is the true one (or which set of $T$ generate the same experience as has occurred in the actual world, especially if one takes a Humean approach of natural laws).

Another thing worth mentioning is that these functions can act as cellular automata, and open up the question for their ability to perform computations, which brings MPOM into the realm of being compatible with functionalism and the computational theory of mind, as a formalism for the input layer. 

# Isomorphism to Physics

The philosophical debate between in the metaphysics of mind, primarily between idealism, dualism and physicalism, can be clarified with the help of POM. In this section we are interested in if there exists an isomorphism (structure preserving one-to-one mapping) between phenomenal states and physical states. I will show that for certain physical systems, particularly one-dimensional movement and harmonic oscillators, one can construct an experiential state and time-function such that there's an isomorphism between the phenomenal experience and the physical system. 

Let's take a very basic system as a start. Imagine a space with one spatial dimension $\mathbb{N}$ and two boxes at a singular location $x,y\in\mathbb{N}$. The Euclidean distance between these two boxes is described as $|x-y|$. Let $t\in [0,\infty)\subset\mathbb{N}$ be the time of the system. Let $v_y=-1$ be the velocity of box $y$ and $v_x=0$ be the velocity for $x$. The system can be visualized as the figure below.

t = 0   ---\[ \]-------------\[ \]--------

t = 1   ---\[ \]----------------\[ \]-----

Let us now find a point in experiential space and a time-function that is isomorphic with this system. Now since the two box system is one dimensional, it will have a zero-dimensional visual field, so each object may only need one single visual point

$e_x =  F  = \{ h_x, b_x\}$
$e_y =  F  = \{  h_y, b_y\}$

The system is entirely describable by four variables: The distance $|x-y|$ between the boxes and velocity $v_y$ for y (given an reference frame set to x, we assume no acceleration). So the physical system is entirely describable by the following variables:

Physical system:
$S = \{|x-y|, dx/dt, t \}$

Experiential system:
$E = \{h_x, b_x, b_y\}$

With $h_y$ removed since it's not possible to make an isomorphism with it. Recall that it's fine for us to arbitrarily change the ideal system as we want since what I'm trying to proove is that ther exists an ideal system for every physical system, so I can construct it however I want. 

Harmonic oscillators are infamous in physics for their prevalence, so a phenomenal model of them should allow us to seriously scale up the theory to more advanced systems. One can for instance, imagine a pixel of light change over time into a darker shade and into a lighter shade, based on the equation $F=-kx$ where F is the force, k is the spring constant, and x the position. 
https://www.feynmanlectures.caltech.edu/I_21.html

Another, highly speculative connection with the second law of thermodynamics is the following. As established earlier, the subset of experiential space that consists of white noise is vastly more common then that of the average structure of human experience (or structured experiences in general). We may expect experiences to statistically move towards white noise. I am however unsure if and how this connects to the requirement that systems that undergo entropy have to be isolated systems. Feel free to dismiss what I just said as nonsense. 

# Implications for Philosophy

POM is a formal theory which can accommodate many metaphysical substantive claims, such as solipsism, continuity or discreteness of phenomenal experience, and mental laws. The clarity that formalising such notions can achieve has a lot a of potential.  

POM can be used to asses the nature of mind-upload and teletransportation, as it can allow for a precise formulation over the process, which allows philosophers to asses the possibility of survival.

Empiricism epistemology can now be properly formalized. One example of such may be Carnapian foundationalist empiricism. The project of sense-data as foundational beliefs as they justify empirical generalizations and in turn justify higher-level theories, can perhaps be formalized in exactly this way. 

POM can be used to formalize Ramsey Sentences. A Ramsey sentence of a theory $T$ describes 

Problem: Our best theories posit external world/physical world F
"Solutions": Dualism, add on physical theory. How does E and F interact?
Panpsychism: Combination problem
Cosmopsychism: Separation problem
E = F i.e physicalism: Hard Problem

Physicalism could work like this:
Isomorphisms to physics (atleast harmonic oscillators)

Psychadelics and Qualia Research Institute, computing qualia

For Modal Realism, the view that all possible worlds exists, then it seems to follow that every member of $E$ also exists. 

Mindfulness
# Undermined by the private language argument?

And just to be clear, this makes the assumption that either the private language argument is false, or that the private language argument is true and experience is non-private.  

External world may have almost consensus, and sense data has almost no support, but there may be good reasons to question it. 


I will be using [Howard Robinson]'s formalization [book name: perception] of the private language argument  

*"1 The meaning of a word is given by the rule which governs its use.* 

*2 A rule must be such that there is a difference between following it correctly and not following it correctly.* 

*3 If a word purports to name a logically private object then there is no difference between following the corresponding rule correctly and not following it correctly. Therefore (from (2) and (3))* 

*4 If a word purports to name a logically private object it does not follow a genuine rule. Therefore (from (1) and (4))* 

*5 If a word purports to name a logically private object then it lacks meaning."*


There are multiple ways of avoiding this objection. The first is to abandon the use theory of meaning, and the better one is to establish that correctness conditions can be done by self-imposing correctness conditions (one's own thought can be multiple agents at different times)

I personally propose that a better theory of meaning is that based on thinker intentions under a functionalist/computationalist theory of mind, particularly input states for the Turing machine that models the mind. I will not defend this view in this article, but it is very much compatible with the view laid out above. 