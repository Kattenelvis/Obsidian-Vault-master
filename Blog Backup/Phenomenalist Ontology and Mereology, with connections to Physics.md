In this article a phenomenalist ontology and mereology (POM) formalized in set theory is developed, which takes regions of phenomenal experience as subsets of experience. I believe that philosophy of mind as it currently stands often lacks mathematical formalism. General theories of neuroscience tend to involve mathematical formalism, for instance Integrated Information Theory and Global Workspace Theory (as the two competing scientific models of consciousness). I will extend the theory developed in [Formal Phenomenology](https://thephilosophyaddict.wordpress.com/2023/11/25/formal-phenomenology/), but enhanced with new features such as experience as points in phase space, natural laws on how experience changes over time, and a deeper exploration of mind space and its connection to physics utilizing a very basic movement model and harmonic oscillator.

The ontology is minimal, fairly trivial and not particularly profound as it seems (this goes for both sceptics and people who are prematurely praising this). There's a decent chance not everyone will be familiar with the concept of phenomenal experience as lay people might not have a [concept for it and has to be taught as a part of an education in philosophy](http://Folk_Psychology_and_Phenomenal_Consciousness.pdf (pitt.edu). Differences in how philosophers and lay people attributed "seeing red" between robots and humans is purported as evidence for that claim. If you are not trained in philosophy and don't know what phenomenal experience is, one way to conceive of it is what it is like to be. It is the colors, the textures of touch, the sounds. It is not things, or ordinary objects such as a blue bottle of water, but rather the flat 2D screen of blue in some region of your visual field. Imagine putting on VR glasses, and taking a look at the pixels of there. It's not about acting as if red is there.

# Brief overview of formal phenomenology

I go more in depth about formal phenomenology in my previous blog post [Formal Phenomenology](https://thephilosophyaddict.wordpress.com/2023/11/25/formal-phenomenology/). But I will give a brief overview here.

Visual experience can be constructed in set-construction notation as the following:  
$latex V=\{v:v\in[0, X]\times [0, Y] \times [0, B] \times [0, H] \times [0, S] \}$

This gives us points such as  
$latex \{4,4,0.5,0.3, 0.8\}$

This object is the point at position $latex (4,4)$, has a brightness of 50% and a hue of 0.3, which if we take a hue of 0 as red, then 0.3 would be some kind of orangy-yellow on the hue wheel with a strong saturation of 0.8. It is worth noting that according to [The geometries of visual space](https://www.routledge.com/The-Geometries-of-Visual-Space/Wagner/p/book/9780805852530), visual space is likely more complicated (such as peripheral vision having larger pixels). It is up to perceptive psychological research, heterophenomenology etc. to figure out the ultimate nature of the structure of the experiential sets. But we assume a cartesian 2D grid for visual space at the moment for simplicity, it's not important for the argument.

We can take all subsets, i.e the powerset of visual space as a $latex P(V)$. $latex V$ just predicates over visual points or pixels (the question on whether visual space is continuous or discrete respectively, we come back to later). The powerset is all possible ways of combining different visual points into larger experiences (such as a pencil, a thought, a sunset). We can take this to be an important set as each member could then fully describe an individual's visual experience (such as a human looking at a computer screen) but also every other possible visual experience.

We can now define an entire experiential space, including visual space V, auditory space A etc. with the powerset operation P as the following:

$latex E = {P(V)\times\dots\times P(F) }$

$latex E$ is thus the space of all possible phenomenal experiences. We will call $latex E$ _experiential space_.

Each element of $latex e\in E$ can be intuitively thought of as an experience at a moment in time. As an example, If I have a pet rabbit at some moment $latex t$, its experience in that set could be marked as $latex E_{rabbit}\in E$ . We mark "The" experience that's currently happening right now to YOU reading this as $latex E_@\in E$ where the "$latex @$" symbol is inspired by the "actual world" in possible worlds semantics. What $latex E_@$ refers to changes over time. As such we may index it at each timestep t $latex E_{@,t}$. As a final note on $latex E$, Most of it is going to be something akin to "white noise" for all senses, only a tiny subset are structure the way human or animal experiences are structured.

# Continuity vs Discreteness

We now come back to the question on modelling experiential space as discrete or continuous. We can model some arbitrary member of experiential space in any of the three following ways, where $latex |.|$ is the cardinality operator (which is sort-of like the size of set):

(1) $latex |A| = c$ for some constant $latex c$  
(2) $latex |A| = \aleph_0$  
(3) $latex |A| = \aleph_n$ for all n>0

While POM does not included any metaphysically substantive claims, and is agnostic towards all 3 theses, I will argue that thesis (1) is the most reasonable, although theories similar to similar POM such as [Smith's Husserl inspired formal ontology](https://philpapers.org/archive/SMITBT.pdf) and other [topological versions](https://psycnet.apa.org/record/2019-17364-004) assume (2) or (3).

The first argument is due to the Löwenheim-Skolem's theorem and the related Skolem's paradox. The theorem (when you combine its upward and downward version) states that for any formal theory $latex \Gamma$ of propositions, if there exists a model with cardinality $latex \aleph_n$, there will exist models of other cardinalities. If we take $latex \Gamma = POM$ we would have multiple models, multiple different $latex E$'s. This does not lead to a contradiction, but may be otherwise undesirable. By the [push-through construction](https://www.amazon.com/Philosophy-Model-Theory-Tim-Button/dp/0198790406), this is still the case for finite models, but you atleast end up with one identical cardinality for all models (and one can simply adopt structural realism here).

The second argument are two empirical arguments. For humans, phenomenal experience cannot be continuous, due to the finite processing power of perceptive organs and the brain, which is believed to be in some way strongly correlated with phenomenal experience. There have been individuals who have [gotten head-trauma and end up seeing the world discretized](https://www.washingtonpost.com/national/health-science/a-man-became-a-math-wiz-after-suffering-brain-injuries-researchers-think-they-know-why/2014/05/12/88c4738e-d613-11e3-95d3-3bcd77cd4e11_story.html). It might be that the seeming continuity of phenomenal experience is an illusion by the brain.

An example of how (1) can play out in the discreteness of phenomenal points:  
Take hue for example, from $latex [0,H]$ (including the topological property that it is a circle and $latex 0=H$.). It must then be the case $latex H\in\mathbb{N}$. As such there's only an finite number of possible experiences of hue's. Take us humans $latex M\subset E$ for instance, they could experience more hue's than we currently do with future technology, but at some point there's no more. It is generally believed that we can experience about 1 million colors, though [some disagree](https://www.davidpapineau.co.uk/uploads/1/8/5/5/18551740/can_we_really_see_a_million_colours.pdf).

We can then model mereology using [Finitist Set Theory](https://content.iospress.com/articles/applied-ontology/ao196). Some axiomatizations of finitist set theory are complete and decidable. Decidability means that an algorithm can be constructed where one can input any formula and it outputs whether it’s true or false. And they are complete, so all formulas are derivable through a finite number of steps. We thus have for instance, that a red region in visual space is a subset of say, a rainbow. We discover that even in most (all?) human experiences $latex \{E_{h1}\dots E_{hn}\}$ there will be sets and subsets, constructed from the so called ur-elements. It will thus be interesting if one could demonstrate if one can prove all statements about experiential space, so long as it's discrete and finite.

# Points of experiential space as points in phase space

Experience change over time. A sunset turns to night, a taste of food start to occur as it enters the tongue, a happy moment becomes boring etc. Let's construct functions which map experiences to experience. So let's establish some timestep $latex t$ and some member of experiential space to be the totality of experience at that timepoint.

$latex E_{U,t} = \{E_{1, t},\dots E_{N, t}\}$

We define $latex U_t=_{df}E_{U,t}$ and we call this the "phase point" of the phase space $latex E$. The letter "$latex U$" is chosen to stand for the universe.

Solipsism can then be defined as  
$latex E_@ = U_t$

Lastly, we take all experience over all time steps between $latex 1$ and $latex T$ to be  
$latex U = \{U_1,\dots U_T\}$

Definition: Let $latex T :E \rightarrow E$ be a function that inputs experience sets and outputs experience sets. As an example we get $latex T(U_1) = U_2$ between two time points for a discrete updating process. For continuous processes we may establish $latex T : \mathbb{R}\rightarrow E$ such that one inputs time and gets the experience at that time, for instance $latex T(\sqrt{2})$ gives you the phenomenal experience at time square root of two. We will be continuing with discrete time steps.

Let's now discuss 3 different restrictions that $latex T$ can take on. Firstly, we can take note of a single visual pixel in visual space, $latex v\in V$, which we want to model as having a color change. Let $latex E_0=\{\{blue,1\},\{red,2\}\}\in E$ be an experience that contains a visual field with one blue pixel to the left and one red pixel to the right with nothing else. Then define $latex T(\{blue, x\}) = \{red, x\}$ and $latex T(\{red, x\}) = \{blue, x\}$. The following derivation is thus:

$latex T(E_0)=T(\{\{blue,1\},\{red,2\}\})$  
$latex =\{T(\{blue,1\}), T(\{red,2\})\}$  
$latex =\{\{red,1\}, \{blue,2\}\}$  
$latex =E_1$

To vizualise this, the experience will go from something roughtly like this

![](https://thephilosophyaddict.wordpress.com/wp-content/uploads/2024/08/image.png?w=362)

To this

![](https://thephilosophyaddict.wordpress.com/wp-content/uploads/2024/08/image-1.png?w=355)

The experience swapped the red to the left and blue to the right. As can easily be seen, this process will go back and forth indefinitely. With this basic example in mind, imagine if something like this was applied to an experience with human-level complexity. In general, the time function defined above has the following property:  
$latex T(E_t) = T(\bigcup_{n\in E_t} r)=\bigcup_{n\in E_t} T(r)=E_{t+1}$

The second definition of time to go over is one where the time-function updates the entire experience at once. $latex T(E_t) = E_{t+1}$

We then define a set of experiences that makes up some universe $latex U$ at time $latex t$.

$latex T(U_t) = T(\bigcup_{E_{i,t}\in U_t} {E_{i,t}})=\bigcup_{E_{i,t}\in U_t} T({E_{i,t}})=U_{t+1}$

Our third time-function restriction is as such  
$latex T(U_t) =U_{t+1}$

The totality of experience is all updated at once. If solipsism is true, then the second definition is identical to the third.

It's worth noting that POM does not make any substantive metaphysical claims about which version of $latex T$ is the true one (or which set of $latex T$ generate the same experience as has occurred in the actual world, especially if one takes a Humean approach of natural laws).

Another thing worth mentioning is that these functions can act as cellular automata, and open up the question for their ability to perform computations, which brings MPO into the realm of being compatible with functionalism and the computational theory of mind, as a formalism for the input layer.

# Isomorphism to Physics

The philosophical debate between in the metaphysics of mind, primarily between idealism, dualism and physicalism, aswell as the hard problem of consciousness within physicalist theories, can be clarified with the help of POM. In this section we are interested in if there exists an isomorphism (structure preserving one-to-one mapping) between phenomenal states and physical states. I will show that for certain physical systems, particularly one-dimensional movement and harmonic oscillators, one can construct an experiential state and time-function such that there's an isomorphism between the phenomenal experience and the physical system.

Let's take a very basic system as a start. Imagine a space with one spatial dimension $latex \mathbb{N}$ and two boxes at some location $latex x,y\in\mathbb{N}$, such as in the example illustration below where where $latex x = 4$ and $latex y = 18$ . The distance between the two boxes is described by $latex |x-y|$. Let $latex t\in [0,\infty)\subset\mathbb{N}$ be the time of the system. Let $latex v_y=1$ be the velocity of box $latex y$ and $latex v_x=0$ be the velocity for $latex x$. The system can be visualized as the figure below:

t = 0 ---[ ]-------------[ ]--------

t = 1 ---[ ]----------------[ ]-----

t = 2 ---[ ]-----------------[ ]-----

Let us now find a point in experiential space and a time-function that is isomorphic with this system. Now the two box system is one dimensional, but we only need two pixels in the visual space, since there is enough information to for an isomorphism to the physical system. We thus get the following systems:

Physical system:  
$latex S = \{dx/dt, |x-y|, t, dy/dt\}$

Experiential system:  
$latex E_S = \{h_1, b_1, h_2, b_2\}$

The way to visualize $latex E_S$ is to consider two pixels where the one on the right changes hue over time but whose brightness is the same, and the one on the left has constant hue with a slowly increasing brightness as the distance between x and y increases. As a final note, it's fine for us to arbitrarily change the experiential system as we want since what I'm trying to show is that there exists an experiential system for every physical system, so I can construct it however I want.

[Harmonic oscillators](https://www.feynmanlectures.caltech.edu/I_21.html) are infamous in physics for their prevalence, so a phenomenal model of them should allow us to seriously scale up the theory to more advanced systems. One can for instance, imagine a pixel of light change over time into a darker shade and into a lighter shade, based on the equation $latex F=-kx$ where F is the force, k is the spring constant, and $latex x$ the position.

Another, highly speculative connection with the second law of thermodynamics is the following. As established earlier, the subset of experiential space that consists of white noise is vastly more common then that of the average structure of human experience (or structured experiences in general). We may expect experiences to statistically move towards white noise. I am however unsure if and how this connects to the requirement that systems that undergo entropy have to be isolated systems. Feel free to dismiss this as nonsense.

# Implications for Philosophy

POM is a formal theory which can accommodate many metaphysical substantive claims, such as solipsism, continuity or discreteness of phenomenal experience, and mental laws. The clarity that can arise from clear, concise mathematical formalisms of philosophical problems is not to be underestimated. As such, I hope POM, or similar theories to it, can be established within the philosophy of mind to clarify debates.

POM can be used to asses the nature of mind-upload and teletransportation, as it can allow for a precise formulation over the process, which allows philosophers to asses the possibility of survival.

Empiricism epistemology can now be properly formalized. One example of such may be Carnapian foundationalist empiricism found in the Aufbau, and its partial revival with the Canberra plan. The project of sense-data as foundational beliefs as they justify empirical generalizations and in turn justify higher-level theories.

Possible worlds semantics can be infused with POM, as each possible world can hold some experiential state at any one time. Can also be combined with various temporal or causal logics and counter-factuals as to how experience would change, given some action. In a more extreme case regarding David Lewis' modal realism, the view that all possible worlds exists, then it seems to follow that every member of $latex E$ also exists.

When it comes to psychedelics, which takes us to some point in experiential space $latex E_{psychedelics}\subset E$ very far away from typical human experiences, we could try to establish more on how the mathematics of such experiences work, as has [been explored previously](https://www.youtube.com/watch?v=loCBvaj4eSg&t=1s). Mindfulness meditation is about focusing on one's entire experiential space at the moment.

# Undermined by the private language argument?

One objection is that experiences as we have defined them are not a part of a public language whose correctness conditions can determine the meaning of the sentences. This threatens the meaningfulness of sentences made utilizing $latex E$.

There are multiple ways of avoiding this objection. The first is to abandon the use theory of meaning, and the better one is to establish that correctness conditions can be done by self-imposing correctness conditions (one's own thought can be multiple agents at different times). The third is to state that experience is actually non-private, and that all it's all publicly accessible in some way.

I personally propose that a better theory of meaning is that based on thinker intentions under a functionalist/computationalist theory of mind, particularly input states for the Turing machine that models the mind. I will not defend this view in this article, but it is very much compatible with the view laid out above.