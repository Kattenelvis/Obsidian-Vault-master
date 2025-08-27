

Notes


Main issue: A lot of stuff a lot is noit sufficiently well explained

General structure is ok


Lucas-Penrose
Target audience: Other bachelors arguments
Not experts
Spell out more or not. 
Repeating myself

F not A is substituted by not provable predicate

Implies any AI is a Turing machine
reject that argument.



Chinese room

Not fleshing out the argument
Detail on the argument is exactly what is he arguing against. 
Arbitrary to throw out terms
Couple paragraphs fleshing it out

Jargon that's hard for the uninitiated to know what it means
for instance: GOFAI, Sub-symbolic processing
The main point still stands. 
Minor changes, twin earth response with minor changes (they are not perfect twins one has h2o one has xyz)



What is the frame problem
Boston Dynamics explain what that is
Write more on the book



Mathematical AI
AIXI too much jargon



Amplification premise amplivative argument
AI_0 = AI

Let k be a number between 1 to infinity
AI+ and then AI++

Should've been more clear that AI+ is at the top of humans, AI++ vastly greater than humans


Grammar a bit confusing "an infinite subpremises"
But maybe not explained well
Sorites but uncontroversial at other places
It's not the fact that it's an infinite number of premises that's the issue, it's that it takes a intelligent a stop.
Remove subpremises




Drew McDermott
extendibility premise P=NP also not explained
Explain that out well aswell


Always keep in mind what I'm trying to do with the paper
Loosing track of where the argument is actually going
Hold the readers hand, why are we talking about this.


Start a new section, take time to explain how the argument is relevant, why am I talking about it.
Not exctly clear cut when its needed
Keep readers attention why is this important why is this relevant.





# Meeting 2



General feedback



What's missing big picture-ish: 

Some problems that not sufficiently explained. Present but don't explain it sufficiently or detail. 


Covering a bit too much. Too many positions and arguments. This guy said this etc.

There's very little 'me' work, critical engagement. Even in the discussion there's just my positions laid out, not arguments.


Pick a narrower set and spend more time on those positions. More time critically engaging. 



Focus on where I have my own original contribution.

What do I think are the most convincing and what do I have the most interesting responses to. Demonstrate that I understand the issue and have unique things to say about it. 




Introduction: Basically fine
Syllogism: only two premises


2 line page 5 . Working definition of a machine. Early.


No idea what I'm talking about the large number of arguments.



General issue: Introduce stuff that I don't. Explain too few things.



Elaborate on Chalmers counter-argument to those arguments.




Reformulate last part of Chinese room 

Perfectly well to LLMs working. Kinds of operations is similar mechanically the LLMs. More substantial discussion.

Reformulating it for LLMs




Frame Problem not enough explanation.
Avicenna Last man.


Explaining the problem
Entertaining the reader


Embodied used is getting the case. 



Maybe cut out Lucas-Penrose. 
Cut Chaos Theory
Cut our Rice's Theorem

Expand no free lunch.



Reformulate the list of AIXI, Gödel machines, NARS so it's not like the reader knows it. This has this quality, see these references.

No need for long explanations but make it clear to the reader that one doesn't have to go back and read an earlier section.



Quipp with the argument:

What is Artificial here when it's evolutionarily done
goal oriented and simulated on a computer.
Difference between I and AI.
Working with lab equipment? AI+ just in a computer?
Saying something about definitions.



References 


Clarify LLM. 
Is the data set as big


RAG, Agentic AI etc same thing as with NARS, AIXI



Amplification paragraph anaphoric pronoun. 


McDermott also posits against extendible method no verb in this sentence


P=NP no one knows what this menas. Not enough. Whole 4.1.1 too little explication


Argument after argument not enough explication. Lack focus.




Discussion

Not a separate section? 


Interview points in my paper. It's hard when the paper style is going over all these premises and arguments



Discussion should be more focused on more general issues general conclusions. 

I can quipp in. "One way to enhance Putnams argument is blah blah blah"

More of my own observations and critical engagements. Not just long expositions. 



Try to avoid just saying I have a conviction. 
"All those arguments are unsound... as I have argued in earlier sections!" 


In general saying "I think that" STOP reconsider whether you want to say that. No one cares what anyone says. 


Sit down and consider sections to take out (Gödel). The most interesting one's where I can contribute. Feel confident non-experts would understand it. Have I made enough novel contributions. Structured better. 








Rice's Theorem states that any non-trivial syntactic property of an algorithm cannot be known without running the algorithm itself. It has to be figured out at runtime. 


The No Free Lunch Theorem in deep learning states that certain algorithms are good in some ways, but worse than other algorithms in others, thus no general intelligence could be built.





\subsubsection{Drew McDermott response}
McDermott posits that the argument premise 2 is unnecessary and unsupported. An empirically adequate argument would only require a finite growth up to AI++. But this merely requires a mild rework of the argument itself, and is not a counter-argument.

McDermott also posits an general argument against extendable methods. Computation and Neural Networks with only one hidden neural layer. This demonstrates a kind of outdated argument, since the deep-learning revolution happened just a few years later where deep-neural networks took off with a very large number of layers deep. 

McDermott posits an unproved theorem that extension or self-amplification if and only if $P=NP$ is true. To oversimplify: the set of "easy" computational problems is identical to the set of "easy and hard" problems. It seems the idea is that if self-amplification is $NP$-hard, then one can never bring forth a rapidly growing algorithm for improving said capacity. \citep{mc-dermott} 


Lastly let's consider the amplification premise. I want to point out that Bringsjords argument can perhaps be shown as wrongly posited by considering that instead of having to move up in the hierarchy, systems can output systems within their own part of the hierarchy that performs better at some tasks. I think that there can exists Turing machines such that some of them approximate maximum intelligence by Hutter's definition (AIXI). In such a way that Turing machines outside this group could produce as output, atleast in principle. So we go from subset to subset such that their intelligence increases, like so: $M_{LLM}\to M_{LLM+}\to ... \to M_{\approx AIXI}$ 







A potential limiting factor for a singularity is that we're close to our limits. Even if we optimizes computation to be as optimally configured as possible by the laws of physics, that would at most give us a speed explosion, not an intelligence explosion. \citep{hutter-explode} A speed increase is not necessarily an intelligence increase, especially if one is waiting for long-term feedback signals from the environment for some actions. 




humans might close to being at maximum intelligence. For instance, if we have a function $I$ which maps agents to their level of intelligence, where $I$ has a co-domain on the range of rational numbers between 0 and 1, where $I(\text{Human})=1-\epsilon$ for a small number $\epsilon$. This would prevent any kind of intelligence explosion, as it wouldn't even improve by one order of magnitude from humans before stagnating. However, Chalmers argues that there are generally few reasons to believe we're so close to maximum intelligence. \citep{chalmersSingularity} In earth's history we recently evolved from primates and it might be foolish to assume that we've reached the pinnacle of intelligence in such a short period of time of rapid growth in intelligence. 




Chalmers in a later article asks if LLMs are conscious, and takes one potential definition of that to be human level reasoning, which current LLMs don't have, but which such model's may have. Other concepts like "global workspaces" and "recurrent neural networks" may also be important for reaching human level intelligence/consciousness. \citep{chalmers-llm-conscious} But consciousness doesn't matter.






So what is the overall assessment over Chalmers argument? 

Let's first consider the equivalence premise. While there are a considerable number of arguments posited against the idea that the human mind is a machine that will eventually be built, none of them are completely devastating for the argument. 

The extension premise is important for any such system which does in fact reach AI level. AI to AI+ might be doable even with just brain emulations if we use them to form a super-human collective on intelligences by automating all of science. As such, even brain emulations are extendible, hence covers the extension premise. 

Lastly the amplification premise, regarding whether AI+ systems can produce better copies of itself, and thus enter a feedback loop until it's orders of magnitude more intelligent than humans. 





In this way, one can argue that the recursive steps Chalmers theorized are happening even with the step from less-than-human AI to AI, and from this we might theorize that amplification could happen from AI to AI+ too.






# Notes 3


No large scale substantial changes

Few things to change around

Longer conclusion than 7 lines. A couple pages. Going over things I have said that I have contributed.


It's a little unclear when or what I am contributing. 

My argument against this is...


More of a Survey of an ongoing discussion. More in-line with a traditional thesis such as strengthen the thesis or violating a premise. 

If not, the conclusion might be a longer conclusion on why concluding one way or the other is hard to do. 

Also to remind the reader what the contribution is. 


In the context of what I'm doing (chalmers singularity argument) it might not be important to include section 6 and 6.1



Introduction page 2 the idea of a technological singularity dates back to Von Neumann. Need references. Standard reference practice.



2.1.2 End this section by saying less symbolic and increasingly 
Dreyfus Argument is also applicable to LLMs etc



page 18 "perhaps if it is goal directed LLM0 --> LLMaixi". 
'There are reasons to believe' what exactly are those reasons and are those good reasons? More places like this not just this section



page 19
distinction levels "in fact there's a general theorem" need to change it (below not above). Need references to the theorem. What axioms does it follow from. 


Even on the conditiion falsified Turing level hypercomputation. Remove Gödel. Also introducing terminology.


Never really explain what a hypercomputation is.


A paragraph loosing track where I'm talking. Orchestrated microtubles. Removing it entirely. 


if humans are anything .... my arguments. Flag it as my argument. Emil's own contribution. Mention this kinda stuff in the conclusion.


Need some references on "this idea has been Critices". Gardner isn't well liked. Provide evidence for the claims.
"At the end of the section as such intelligence doesn't need to be a linear functions. Some subsets" not understanding the point I'm trying to make. 
Make the point more clear, further argument that Chalmers manages it. Here it seems we're getting something else. 
Rework the section a little bit.
Suppose for argument that Gardner is right. Then someone could say Chalmers argument is wrong. Let's pretend we're not talking about intelligence, but instead some narrower intelligence. In the end this is just as bad. Make this point clearer.


22 takeoff scenarios
Boström equation. Explain the equation. Why are these numbers? It's a bit bizare. Explain specifically what I mean by recalcitrance. 


25 the flynn effect. Explain and give a source


Doom section. Limited time. What works best. 


Something in boxing in AI++ 


Most important thing: Conclusion gets longer. Map out my contributions. The tentative conclusion we can draw based on arguments blah blah blah. 
What is the overarching question
Abstract: In this essay the premises will be explain defended criticized. But ultimately want some answer to the question.

Crucially important: Provide reasons for it. 




Friday but not super late. 14:00 latest
24 hours before. 

Rewrite the conclusion. 


