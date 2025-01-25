Consciousness research is still in its infancy. Questions on the metaphysics of consciousness, i.e. the debate between physicalism, dualism, idealism etc. is however very old and doesn't seem to be close to being finished yet. It's likely the case that some research methods are currently unavailable with current technology that would allow for empirical consequences of different theories on the metaphysics of consciousness. In this article I propose an idea on potential future experimental methods and machines which might be invented in the future to test many predictions from scientific theories of phenomenal consciousness utilizing different metaphysical views of consciousness. Tools that allows us to combine, separate, and test smaller reduced sections of phenomenal consciousness, such as a tool that can create a fully-red experience for the researcher, who can then introspect as say, a blue region in the center is created by scientists. It's unlikely the case that current humans will be able to achieve this technology, and that it's likely going to be some post-humans who can change their structure with ease, or AI.

In this article I will use the word "consciousness" to mean phenomenal consciousness, that is to say, some kind of experience of vision, audio, smell e.t.c as seen in [formal phenomenology](https://thephilosophyaddict.wordpress.com/2023/11/25/formal-phenomenology/?_thumbnail_id=273). This is not about awareness, awareness of being aware, awareness of self, awareness of others, awareness of others being aware, awareness of others being aware of themselves or us, e.t.c. or any other higher level type of consciousness.

Another caveat is that I will be going over multiple accounts on the metaphysics of consciousness, ordered from most socially acceptable to least socially acceptable (among analytic philosophers). That order is: Physicalism, Dualism, Panpsychism, Cosmopsychism, with a final stop at Idealism and Theism. I think it's worth taking some of the less socially acceptable one's seriously, consensus can sometimes shift quickly with just someone taking such an idea seriously and arguing for it well. At the same time, there is a lot of good evidence for physicalism, so if anyone is for it then that's not a problem for me.

## Brief overview of Formal Phenomenology and Natural Laws

While I highly recommend looking into my earlier article [formal phenomenology](https://thephilosophyaddict.wordpress.com/?p=244&preview=true&_thumbnail_id=273) for context, I will do a brief overview here. I take it that phenomenology is formalizable into set theory with no information loss. This is because every moment of experience $latex E_k\in E$ can be expressed as a set containing the visual space, auditory space, olfactory space etc. which in turn contain sets that describe each atomic phenomena. Example of atomic phenomena include pixels in the visual space $latex \{x,y,RED\}$ or pitch-loudness pairs in auditory space $latex \{fr,dB\}$ etc. Subsets of visual space $latex V$ is a visual region, for instance some green area $latex G\subset V$.

Now for what's new in this article. One's experience of the world is not static, but changes ‘over time’. Time in this context is to be thought of as a function that inputs experience at time $latex t$ and outputs a new experience at time $latex t+1$. So we will form a "natural law", specifically a "mental law" with the following:

Definition: Let $latex T :E \rightarrow E$ be the time function which inputs experience sets and outputs experience sets.

Considering our thoroughgoing empiricism, $latex T$ is not necessarily the "reality itself", or some such thing. Time could be mysterious, emergent e.t.c, however, change in phenomenal experience is a change that can be modelled empirically. For example, if we take $latex E_t\in E$ to be your (as in, you reading this) concrete current experience at some timepoint $latex t$, we can take note of a single microphenomenal point on the visual field, take $latex v_t\in V_t\in E_{t}$. We can then see that the color changes as $latex v_{t+1}\neq v_t$. We can model it using such a function.

Example:  
Let $latex E_0=\{\{blue,1\},\{red,2\}\}$ be an experience with one blue pixel to the left and one red pixel to the right and nothing else (in a one-coordinate system)

![](https://thephilosophyaddict.files.wordpress.com/2024/01/image.png?w=362)

  
Fig: What it is like to be $latex E_0$

Then we define $latex T(\{blue, x\}) = \{red, x\}$ and $latex T(\{red, x\}) = \{blue, x\}$. Using our definition we get:

$latex T(E_0)=T(\{\{blue,1\},\{red,2\}\})$  
$latex =\{T(\{blue,1\}), T(\{red,2\})\}$  
$latex =\{\{red,1\},\{blue,2\}\}$  
$latex =E_1$

So the phenomenology has now changed into

![](https://thephilosophyaddict.files.wordpress.com/2024/01/image-1.png?w=355)

Which tells us that the subject is now experiencing the red to the left and blue to the right. As can easily be seen, this process will continue indefinitely, as $latex E_2=T(T(E_0))$ etc. As an exercise you can see what $latex E_3$ will be.

With this basic example in mind, imagine if something like this was applied to a subject of human-level complexity, with a large quantity and variety of qualia. Trying to formulate any kind of natural law as described above however seems very difficult. So we will only approximate it.

So what are some ways of approximating it? Let $latex P, Q$ be phenomenal properties. Then we could say $latex \forall x P(x)\rightarrow Q(x)$ which indicates a law-like statement (universality) maybe that every time x has experienced red in region A, it experiences green in region B. This law is obviously false in our world, but it's a way they could be formulated for some possible world. These laws could then maybe be extended to be necessary, not merely contingent given some notion of natural law.

Of course, laws can look more complicated then that, but we will begin with the simple view that laws are universal generalizations. Notice for instance, that differential equations have such a structure, which are ubiquitous in physics and other sciences. For simplicity we take the Humean approach, in that laws are only universal generalizations of the form $latex \forall x P(x)\rightarrow Q(x)$ and not $latex \square \forall x P(x)\rightarrow Q(x)$.

Of course, there can be some strange examples of mental laws. For example, maybe everyone would have a green bar at the top of their visual fields, until the word "apple" is uttered, in which case it changes to blue and after 30 seconds it goes back to being green. This is a plausible mental law, though obviously not true in our world.

It's worth noting about [Donald Davidson anomalous monism](https://plato.stanford.edu/entries/anomalous-monism/) where he criticizes the idea of mental laws, in favor of "anomalous" "free willed" actions with causal impact. We will assume this view to be false for the sake of simplicity, but might be explored in the future.

## Supervenience Physicalism

Now for how the theory can be applied to the metaphysics of consciousness, beginning with with physicalism. Physicalism is at the moment [the most popular account of the metaphysics of consciousness](https://survey2020.philpeople.org/survey/results/4874). This viewpoint, in the context of consciousness, more or less states that the mind is physical. How exactly the mind is physical is hotly debated. The viewpoint I will overview here is supervenience physicalism, also known as non-reductive physicalism.

Definition: A Supervenes on B iff there cannot be an A change without a B change. That is to say, let A and B be property clusters, then for any $latex a\in A$ then for any object $latex x$ such that $latex a(x)$ must have some $latex b(x)$ for $latex b\in B$.

In the context of mind, we state that the mind supervenes on the physical, in that any phenomenal change must be accompanied by a corresponding physical change. It would never be the case that you can have the same physical configuration and have two different phenomenal experiences. So using our future experimental methods, we can test the supervenience hypothesis. Test subject $latex E$ gets the experience machine headset put on. Let experience at time 1 be only red  
$latex E_1 = \{\{x,y,RED\}:\forall x, \forall y x<X\wedge y<Y\}$

Then we let the physical be some neural configuration $latex C_1$. We can now test supervenience by seeing if $latex E_2$ can be different without a neural configuration change. A single instance of $latex E_1 \neq E_2$ and $latex C_1 = C_2$ disproves the supervenience thesis.

## Property Dualism and Psycho-Physical laws

We may now consider property dualism. It's a type of dualism where objects can have both mental and physical properties, and that there's neither a supervenience nor reduction relation between them in either direction. We can have for example, physical property $latex P$ and mental property $latex M$ such that there exists laws that states:

(i) $latex \forall xP(x)\rightarrow M(x)$  
(ii) $latex \forall xM(x)\rightarrow P(x)$

Here are some potential examples:

(i*) "All K-neuron activations implies the experience of red"

(ii*) "All feelings of action a implies a change in H-neurons"

Technical Note: Given classical implication truth tables, they may still experience red without K-neuron activation and a change in H-neurons can still occur without feelings of actions. This is fine, since such changes are likely multiple realizable.

Assume property dualism is true, and that there exists physical-to-physical laws and mental-to-mental laws. If, in addition, only laws of type (i) exists, then epiphenomenalism is true. If both (i) and (ii) exists, then interactionism is true. If neither exists, then parallelism is true. If only (ii) exists then the world would be very interactive.

One case against dualism is to claim that only physical laws actually exist, only linking physical predicates (for example, "All electrons at rest have (approximate) mass 9*10^-31" or "All photons follow a space-time geodesic") while there doesn't seem to be any example's of psycho-physical laws (or mental laws for that matter).

But this can be solved with our experimental method. With such future technology, one could (if they exist) try to falsify and confirm such laws. Atleast some generalization from how certain properties of some physical substrate (such as the brain) are always, no exception, correlated with some mental property.

## Panpsychism and the Combination Problem

Panpsychism is the view that everything is conscious to some extent, even if very minimal. One problem for panpsychism (specifically constitutive panpsychism) is the notion of combination laws, that is to say, how does atomic consciousness combine into a unified consciousness?

So first we can define an atomic consciousness in formal phenomenology as a singleton set. We can then allow various combinations of consciousness as unions of sets, for instance taking a red pixel and a blue pixel which together generate an consciousness that sees a red pixel to the left of a blue pixel.

So universal generalizations might not work anymore. Instead we create a set theoretic formalism.

For two experiences $latex E_a$ and $latex E_b$ we get the combination $latex E_a\cup E_b$

$latex Pc(E_a,E_b)\leftrightarrow Mc(E_a\cup E_B)$

The experience machine could combine with individuals to generate new experiences for testing these laws. For instance, if we're still humans, then we might bridge the connection using something that combines two brains. In the far future, we might be able to experiment much more freely with digitized minds, or even with brain-computer interfaces.

## Cosmopsychism and the Separation problem

Just like how panpsychism had the problem of combination laws, so cosmopsychism has the problem of separation laws.

While a word like "cosmopsychism" may in some people (not me) invoke feelings of spiritualism or new age stuff, it can in fact be entirely an scientific concept that has no implications on how to live life or treat others. But if it gives you strong aesthetic experiences, then go ahead and have them, they can be interesting. However no matter how beautiful they are, beauty is not epistemically justificatory.

So now for some examples of cosmopsychism. According to some interpretation of quantum mechanics, the whole universe is one entire one quantum state of entangled particles. If the entire universe is one quantum state, then it is not factorizable into its component parts (Schaffer, 2010)

$latex \Psi_{universe} \neq \Psi_1\otimes\Psi_2\otimes\dots\Psi_n$

If consciousness is supervenient on these states, then it would be interesting to know how quantum states separate into individuals.

Another example, in Quantum Field Theory (QFT) there exists multiple particle interaction fields that stretches across the universe. If consciousness is for some reason or another related to these states, how are regions $latex R_1$ and $latex R_2$ divided up between different conscious agents?

Another theory is bernado kastrups analytic idealism where he proposes that the universe has dissociative identity disorder. I will not go over it here, but it's an interesting example nevertheless.

However there are some problems when it comes to our experimental setup. What is panpsychist combination laws can be merely rewritten into cosmopsychist separation laws? If this is the case, then both theories might be empirically equivalent, unless their respective theories are richer in other ways than just combination/separation laws.

## Idealism and Theism

It's worth going over some accounts on the metaphysics of consciousness I don't think this machine can help falsify. One idea is idealism, that their are no physical objects or laws, or the more moderate thesis that mental objects and mental laws are more fundamental or ground physical objects and laws. Whether or not this is falsifiable is something I'm uncertain off, but it's worth mentioning.

Theism is also an option, where God is the most fundamental and grounds everything else, mind and physics alike. This is similar to idealism in that minds ground the physical, but in this case it's only one mind with very special properties such as omniscience and omnipotence etc. How falsifiable or reasonable this is, is a discussion for a future blog post.

## Conclusion

So in conclusion, we will in the future be able to build machines that can test laws regarding mental combination, and as such we're currently unable to figure out what is true. As a consequence, studying consciousness to much is a bad idea right now. Instead, one should focus on minimizing existential risk such that humanity (and post-humanity) can survive and flourish such that they will be able to figure this out in the future.