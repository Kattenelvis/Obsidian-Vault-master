![](https://thephilosophyaddict.files.wordpress.com/2023/11/image-2.png?w=573)

## Introduction

In this post I will give the outline of the mathematical structure of phenomenal consciousness by showing how phenomenal space can be modelled by set theory. We will go over simplified modells of sight, hearing, touch and smell. I will finish with more speculative thoughts on the classes of different minds in phenomenal space, aswell as a list on possible future ways this theory can be applied.

## Formal Phenomenology

The idea that sets can be used to model phenomenal experience is not entirely new, as IIT already has done that [with visual space](https://www.mdpi.com/1099-4300/21/12/1160) aswell as the book on [the geometry of visual space](https://www.routledge.com/The-Geometries-of-Visual-Space/Wagner/p/book/9780805852530). Other examples include that smell [has a hyperbolic](https://www.science.org/doi/10.1126/sciadv.aaq1458) structure which we will cover later. Likewise with the well known fact of logarithmic loudness. As will be explained later, the exact set theoretic structure on phenomenology is up to the science process to figure out, not individual introspection, as it can often get things wrong. But we can do a basic approximation of it.

We will begin with formalizing visual space as it is the most easy to visualize and demonstrate (except for blind people). We can, for now, assume that visual space V is merely composed of a cartesian two-dimensional grid where every point has a hue-value and brightness-value. According to the book on non-linearities in visual space, this isn't the case, but it is a temporary simplification. In colors for philosophers, there are arguments put forth that there can be multiple colors in the same region aswell, I will be ignoring that for now. The theory is in principle capable of incorporating such complications. A three dimensional space for hue might be more appropriate to not leave out certain colors such as cyan and magenta. But we keep things simple for now.

We can then start translating sentences written in phenomenal language into a language of sets.

In Set-construction notation:

$latex V=\{v:v\in[0, X]\times [0, Y] \times [0, B] \times [0, H] \times [0, S] \}&s=2$

This gives us points such as

$latex \{4,4,0.5,0.3, 0.9\}&s=2$

Which means that the point at position (4,4), has a brightness of 0.5 (say, 50%) and a hue of 0.3, which if we take a hue of 0 as red, then 0.3 would be some kind of orangy-yellow on the hue wheel that's almost fully saturated. The numbers X, Y, B, H and S all represent their respective maximum values.

We can then take subsets, and get what Ayer would've called a "sense-datum".

$latex SD\subset V&s=2$

Which would be a certain region in visual space. An example of this might be, only points in the left side of visual space. Let v(x) be a function which accesses its x value:

$latex SD=\{v\in V| v(x) < 50 \}&s=2$

We can formalize the auditory system in a similar way as the following, again taking some simplifying assumptions by not considering the logarithmic nature of it. Just as we formalized visual points as a position-hue-brightness-saturation squad, we will formalize auditory points as loudness-pitch pairs, with a binary symbol as to whether it is from the left or from the right.

$latex A=\{a:a\in[0, D]\times [0, P] \times \{L,R\}\}&s=2$

So for instance, a 1000hz sine-wave in the left audio channel (left ear) at a human-speech level loudness of 70db would be

$latex a_1 = \{70,1000,L\}&s=2$

Now for touch. Assume there is a subset of a human touch-space, a subset of Euclidean 3D space. So if we let H be a subset of Euclidean 3D space. Then the touch phenomena is a subset of that T subset H.

Given empirical evidence that there exists only a finite number of touch-receptors, once can formalize it instead as a subset of a discrete vector space such as

$latex T\subseteq H\subset\mathbb{Z}^3&s=2$.

Lastly, the hyperbolic nature of olfactory phenomenology will be explored. The primitive notion will be atomic smells, that are structures in sets like this:

$latex \{\{\{p,q\}, \{r, s\}\},\{\{w,z\},\{f,g\}\}&s=2$

In set theory, it would look something like the following (picture taken from the paper on hyperbolic smells)

![](https://thephilosophyaddict.files.wordpress.com/2023/11/image-3.png?w=373)

## Putting it all together

To borrow terminology from constitutive panpsychism, we can now refer to microphenomena in the following way:  
$latex v\in V&s=2$  
$latex a\in A&s=2$  
$latex t\in T&s=2$  
$latex s\in S&s=2$

We can also define an entire phenomenal field as

$latex E = \{V\times A \times T\times S \}&s=2$

Which makes E the space of all possible experiences. We will call E _experiential space_. We can then index other experiences, such as say, some random rabbit, as

$latex E_{rabbit}\in E&s=2$

We mark "The" experience that's currently happening right now to YOU reading this as E@ where the "@" symbol is inspired by the "actual world" in possible worlds semantics. What E@ refers to changes over time.

## Conclusion and ideas

In future blog posts, I will write about some potential consequences of this theory, extensions, and possibly corrections. I will also eventually generate a rough approximation of what a human experiences, that is to say, explore the subspace of experiential space where humans are. I may later go outside of it, into animals, plants, alien, robots and post-human experiential space. Future posts will also be about more interesting topics that can be generated from this theory, such as various experimental methods for testing consciousness, formalizing the science of phenomenology (including an analysis of emotional, cognitive, algedonic and religious phenomenology, as seen in the book "The Varieties of Consciousness"), helping with the science of consciousness (such as IIT or competing theories such as Global Workspace theory e.t.c) and the metaphysics of consciousness (such as Physicalism, maybe there is a set theoretic structure for how a bat is like?) and so on.

A big idea I have already worked on a lot is formulating a language of phenomenology, including how to generate sentences and give them meaning/truth values using Tarski's recursive truth definition. That includes what you see in the picture. What is the meaning and truth value of "If A is blue then A* is blue".

![](https://thephilosophyaddict.files.wordpress.com/2023/11/image.png?w=359)

This allows one to construct propositions that will be true, even under radical skepticism, such as being in a simulation, brain in a vat, being deceived by a demon e.t.c. So it's sort of an anti-skeptical argument in that sense.

I also think formalizing philosophy of mind to become more rigorous and mathematical is important. I believe that there's a lack of application of mathematical logic into philosophy of mind that's specifically about experience. When it comes to cognitive systems, folk psychology, computational theory of mind e.t.c. there is some, but not for phenomenology itself.

However what does exist for phenomenology itself are a few branches of science, notably scientific phenomenology (perhaps [neural correlates with phenomena](https://en.wikipedia.org/wiki/Neural_correlates_of_consciousness)) and [heterophenomenology](https://en.wikipedia.org/wiki/Heterophenomenology) (how experiences differ between humans such as color blindness, inverse qualia, gender identity, aphantasia, hyperphantasia e.t.c.). And it would be nice to be able to formalize these areas more.

Another potential change is generalizing on how series of experiences as they change over time, so one can model melodies with the theory. Something Brentano put a lot of thought into.

Alot of these potential uses of the theory will be laid out in future blog posts. Or perhaps I will show why it doesn't work for some of them, that might still be interesting. Anyways, thanks, please comment if you have any feedback!