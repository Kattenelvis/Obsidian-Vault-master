
[Memetic algorithm - Wikipedia](https://en.wikipedia.org/wiki/Memetic_algorithm)


Baldwinian evolutionary algorithms, Lamarckian EAs, cultural algorithms, or genetic local search.


   **Procedure** Memetic Algorithm
   **Initialize:** Generate an initial population, evaluate the individuals and assign a quality value to them;
   **while** Stopping conditions are not satisfied **do**
       _Evolve_ a new population using stochastic search operators.
       _Evaluate_ all individuals in the population and assign a quality value to them.
       _Select_ the subset of individuals, Ωil![{\displaystyle \Omega _{il}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/69f3721bfdbe134b91e89acfa6c774931c892f41), that should undergo the individual improvement procedure.
       **for** each individual in Ωil![{\displaystyle \Omega _{il}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/69f3721bfdbe134b91e89acfa6c774931c892f41) **do**
           _Perform_ individual learning using meme(s) with frequency or probability of fil![{\displaystyle f_{il}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/5bcb6b7b25d416f0bfc501273503a89e41d1e10a), with an intensity of til![{\displaystyle t_{il}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/b28ba76c20eb6f9e8ef2548b4f472b6dc9ff3a91).
           _Proceed_ with Lamarckian or Baldwinian learning.
       **end for**
   **end while**


![[Pasted image 20250208213031.png]]

> ###   
2nd generation

[[edit](https://en.wikipedia.org/w/index.php?title=Memetic_algorithm&action=edit&section=5 "Edit section: 2nd generation")]

Multi-meme,[[10]](https://en.wikipedia.org/wiki/Memetic_algorithm#cite_note-krasnogor1999cga-10) [hyper-heuristic](https://en.wikipedia.org/wiki/Hyper-heuristic "Hyper-heuristic")[[11]](https://en.wikipedia.org/wiki/Memetic_algorithm#cite_note-kendall2002cfa-11)[[12]](https://en.wikipedia.org/wiki/Memetic_algorithm#cite_note-burke2013-12) and meta-Lamarckian MA[[13]](https://en.wikipedia.org/wiki/Memetic_algorithm#cite_note-ong2004mll-13)[[14]](https://en.wikipedia.org/wiki/Memetic_algorithm#cite_note-:0-14) are referred to as second generation MA exhibiting the principles of memetic transmission and selection in their design. In Multi-meme MA, the memetic material is encoded as part of the [genotype](https://en.wikipedia.org/wiki/Genotype "Genotype"). Subsequently, the decoded meme of each respective individual/[chromosome](https://en.wikipedia.org/wiki/Chromosome "Chromosome") is then used to perform a local refinement. The memetic material is then transmitted through a simple inheritance mechanism from parent to offspring(s). On the other hand, in hyper-heuristic and meta-Lamarckian MA, the pool of candidate memes considered will compete, based on their past merits in generating local improvements through a reward mechanism, deciding on which meme to be selected to proceed for future local refinements. Memes with a higher reward have a greater chance of continuing to be used. For a review on second generation MA; i.e., MA considering multiple individual learning methods within an evolutionary system, the reader is referred to.[[15]](https://en.wikipedia.org/wiki/Memetic_algorithm#cite_note-ong2006cam-15)





> ### 3rd generation

[[edit](https://en.wikipedia.org/w/index.php?title=Memetic_algorithm&action=edit&section=6 "Edit section: 3rd generation")]

Co-evolution[[16]](https://en.wikipedia.org/wiki/Memetic_algorithm#cite_note-smith2007cma-16) and self-generating MAs[[17]](https://en.wikipedia.org/wiki/Memetic_algorithm#cite_note-krasnogor2002ttm-17) may be regarded as 3rd generation MA where all three principles satisfying the definitions of a basic evolving system have been considered. In contrast to 2nd generation MA which assumes that the memes to be used are known a priori, 3rd generation MA utilizes a rule-based local search to supplement candidate solutions within the evolutionary system, thus capturing regularly repeated features or patterns in the problem space.