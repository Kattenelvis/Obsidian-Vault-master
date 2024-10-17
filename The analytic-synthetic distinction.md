2. Morton White, Nelson Goodman, Quine, and Hempel are probably the most famous names when it comes to the analytic synthetic distinction debate




Kuro:

"2.   
    @Youv / Philip okay, so there's been a variety of formal explications of the analytic-synthetic distinction (logic of analytic implication, meaning postulates, analytic proofs, etc.) that I can't/won't exhaust here, but I will pretty much (generously) use the notion of analytic proofs from structural proof theory. This is in fact one of the strongest logical notions of analyticity that are available (e.g. logics of analytic implication are strongly sociative and don't even validate vIntro!) and includes a lot of stuff, including basically all of (base) FOL provided that we stick to sequent calculus (unfortunately some desired properties for classical logic aren't invariant under proof system, unlike intuitionistic logic, i.e. classical logic loses the subformula property in ND). There is one stronger notion of analyticity, being Carnapian meaning postulates, but I'll explain why we won't/can't use this after I expand on why I'm deferring to the notion of analytic proofs
    
3. _[_07:39_]_
    
    One common characterization behind analyticity, since Kant, is conceptual containment, so that examining the characteristics of the components of a sentence (ideally, we're expanding the formula or cashing out _definitions_ of its components) allow us to apprehend whether it's true or not. This generates two constraints (i) the conceptual apparatus needed to judge the formula is what occurs in it, nothing external (ii) the process is computable, i.e. the function that carries this out is a computable function (such that the truth value of analytic truths can be apprehended by pure reasoning over the meanings/definitions of the terms that occur: reasoning may take arbitrarily long but finite time). Formally, we can explicate conceptual containment with the subformula property (which guarantees our cut free proofs of sequents only have formulas that contain the connectives that are in that sequent, and the rules about those connectives we will say are just their definitions / conceptually contained in their occurences), and we get (ii) for free as long as we have a real proof system (an effective one) because at bare minimum we have proof search. FO classical logic (presented as a sequent system) will be analytic in this sense, at least for its empty theory, as well as some more stuff like only theories with monadic predicates that I don't remember (better ask Farnir?).
    
4. _[_07:39_]_
    
    on the other hand, basically all the FO theories that are strong enough for maths aren't, including PA, ZF, ZFC, etc (all of which don't have cut elim) nor would be any HOLs, type theories or whatever other logicist systems capable of carrying out maths as Godel results would apply to it, it'd be undecidable and not specifiable by analytic proof, and in this case this isn't just an artifact of the formalism for analyticity we're using but something that deeply resonates with the original concept of analyticity, since analyticity implies that a formula should be decidable by pure reason, e.g. its meaning should yield a proof of it, using concepts internal to it, or a proof of its negation, after some finite amount of time
    
5. _[_07:40_]_
    
    as for why not Carnapian meaning postulates... well, they're good for regimenting the truths intended to be analytic and making sure the logic, in that theory, doesn't do anything weird (i.e. find countermodels to them, fail to enforce their intended consequences), but that's really all their purpose is. They're not even a candidate for an explanation of what analyticity is because the way logic itself is set up (or I guess model theory) can't tell apart stipulations from assertions, and if you say, I'll just ignore this and regiment the structure of nat lang analytic truths as meaning postulates, the issue is, that will be interpreted the same way by your logic as other regimentations of nat lang assertions of the same structure that, instead of govern the meaning of a term in your theory, assert an "established truth" (i.e. govern the modal structure of a scientific theory by having a natural law as an axiom or something), so in principle if Carnapian meaning postulates demarcate what is and isn't analytic then either everything is analytic or nothing is (that said don't get me wrong I love meaning postulates, I just don't think they're good for this purpose)
    
6. _[_07:42_]_
    
    @g1 a lot of this ties into why the Leibniz "everything is analytic, but 'synthetic' facts are analytic given infinite time / mind of God' is genius, btw. the guy was like several centuries ahead of his time
    
    ![👌](https://discord.com/assets/f8ad564299b641dfc32a.svg)
    
    1
    
7. ![](https://cdn.discordapp.com/avatars/915361777397694545/53c5e0df9ab61f51e554cbb08c2cea40.webp?size=20)@Kūro, IBE Opposer
    
    he's completely right about literally everything he said"