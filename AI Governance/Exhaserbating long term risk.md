[Alignment introduction — AI Safety Fundamentals](https://aisafetyfundamentals.com/alignment-introduction?_gl=1*j9m3x1*_ga*NjY1NjAzOTA0LjE2OTUzODg4MTI.*_ga_8W59C8ZY6T*MTY5NTU1MTAzNy4xLjEuMTY5NTU1MjgxMC4wLjAuMA..)



**A high-stakes race (for advanced AI) can dramatically worsen outcomes by making all parties more willing to cut corners in safety. This risk can be generalized.** Just as a safety-performance tradeoff, in the presence of intense competition, pushes decision-makers to cut corners on safety, so can a tradeoff between any human value and competitive performance incentivize decision makers to sacrifice that value. Contemporary examples of values being eroded by global economic competition could include non-monopolistic markets, privacy, and relative equality. In the long run, competitive dynamics could lead to the proliferation of forms of life (countries, companies, autonomous AIs) which lock-in bad values (2). I refer to this as [value erosion](https://docs.google.com/document/d/1B77VWaXG-u34nSRFKV14pJNHJHHb6sa5zJ08J70CVVA/edit); Nick Bostrom discusses this in [The Future of Human Evolution](https://www.nickbostrom.com/fut/evolution.html) (2004); [Paul Christiano](https://www.alignmentforum.org/posts/HBxe6wdjxK239zajf/what-failure-looks-like) has referred to the rise of “greedy patterns”; Hanson’s Age of Em scenario involves loss of most value that is not adapted to ongoing AI market competition.[6]



"To reduce the risks discussed above, two broad types of work are being pursued – developing technical solutions that enable advanced AI to be directed as its designers intend (i.e., _technical AI alignment research_) and other, nontechnical work geared towards ensuring these technical solutions are developed and implemented where necessary (this nontechnical work falls under the larger umbrella of _AI governance_ [26]).

**Some technical AI alignment research involves working with current AI systems to direct them towards desired goals, with the hope that insights transfer to advanced AI:**

- Advanced AI systems might resemble current AI systems to some degree, so methods for directing current AI systems may yield valuable insights that transfer over to advanced AI.
    
- Research intuitions sometimes transfer between engineering paradigms, so even if advanced AI does not resemble current AI, intuitions gained from directing current AI may still be valuable for directing advanced AI.
    

**Other technical AI alignment research involves more theoretical or abstract work:**

- This research often abstracts away the specifics of how advanced AI may work and instead considers how idealized AI systems with traits such as [goal-directedness](https://www.alignmentforum.org/posts/cfXwr6NC9AqZ9kr8g/literature-review-on-goal-directedness), [embeddedness in their environment](https://www.alignmentforum.org/tag/embedded-agency), and high [optimization power](https://www.alignmentforum.org/posts/Q4hLMDrFd8fbteeZ8/measuring-optimization-power) may be formulated so that they could be directed according to the (hard to specify) wishes of their (future) designers.
    
- These sorts of theoretical abstractions allow for research relevant to AI systems with capabilities far beyond those available today or that operate according to unfamiliar processes.
    

The next two paragraphs list two broad areas of technical AI alignment research – note that I’m listing these areas simply for illustrative purposes, and there are many more areas that I don’t list.

**Understanding the inner workings of current black-box AI systems:**

- Better understanding may enable both designing AI in more intentional ways and checking (before deployment) if systems possess dangerous emergent capabilities. 
    
- Further, good understanding of the internal workings of AI systems may allow for training AI not just based on outward behavior, but also on inner workings, potentially allowing for more easily directing AI systems to adopt or avoid particular internal procedures (e.g., it may be possible to train AI to not be deceptive via feedback on the AI’s internal workings [27]).
    
- [Mechanistic interpretability](https://transformer-circuits.pub/2022/mech-interp-essay/index.html) research involves developing methods to understand inner workings of otherwise black-box AI systems ([example](https://transformer-circuits.pub/2021/framework/index.html)).
    
- [Deep Learning theory](https://deeplearningtheory.com/) research involves investigating why current AI systems develop in the sorts of ways they do, as well as describing underlying dynamics ([example](https://openai.com/blog/deep-double-descent/)).
    

**Developing methods for ensuring the honesty or truthfulness of AI systems:**

- Many cutting-edge AI systems specializing in language generation are [prone](https://arxiv.org/abs/2104.07567) to making factually inaccurate statements, [sometimes](https://arxiv.org/abs/2102.01017) despite the exact same system previously having made a true statement on the same exact factual matter (e.g., the system may answer a factual question inaccurately, despite previously having answered the same question accurately) [28].
    
- Research into [truthful AI](https://www.alignmentforum.org/posts/sdxZdGFtAwHGFGKhg/truthful-and-honest-ai#Truthful_systems) aims for AI systems that avoid making such false claims ([example](https://arxiv.org/abs/2109.07958)), while research in the related field of [honest AI](https://www.alignmentforum.org/posts/5HtDzRAk7ePWsiL2L/open-problems-in-ai-x-risk-pais-5#Honest_AI) seeks AI systems that make claims in line with their learned models of the world ([example](https://arxiv.org/abs/2212.03827)) [29].
    
- Work to direct AI systems to only ever be “honest” or “truthful” may function as [practice](https://www.alignmentforum.org/posts/jWkqACmDes6SoAiyE/truthful-lms-as-a-warm-up-for-aligned-agi) for later work directing advanced AI toward other important-yet-“fuzzy” goals.
    
- Additionally, if we could direct advanced AI to be honest, that alone may reduce risks related to deception, as then the system could not pretend to lack knowledge that it had, nor could it necessarily develop strategic plans hidden from human oversight.
    
- In addition to empirical work on directing current AI systems to be honest/truthful, researchers are pursuing theoretical work on methods to [_elicit latent knowledge_](https://www.alignmentforum.org/posts/rxoBY9CMkqDsHt25t/eliciting-latent-knowledge-elk-distillation-summary) from advanced AI – that is, to read off “knowledge” that the AI has, thereby effectively forcing it to be honest.
    

_See more: our_ [_AI Alignment Curriculum_](https://aisafetyfundamentals.com/ai-alignment-curriculum) _describes several further technical AI alignment research avenues in more detail, as does the paper_ [_Unsolved Problems in ML Safety_](https://arxiv.org/abs/2109.13916) [30].

**On the nontechnical side, several areas of AI governance are relevant for reducing misalignment risks from advanced AI, including work to:**

- Reduce risks of corner-cutting on the development of advanced AI – if advanced AI is constructed in a hurried manner or without proper safety measures, it may be more likely to wind up poorly directed. Worryingly, most software is currently developed in a relatively haphazard way, and the field of AI does not have a particularly strong culture of safety the way some disciplines, like nuclear engineering, do. Some current work to reduce this risk is geared towards reducing a zero-sum “race dynamic” towards advanced AI [31].
    
- Improve institutional decision-making processes (especially on emerging technology) – plausible reforms to improve societal decision-making are obviously too numerous and varied to mention, but broadly speaking, better governmental, international, and corporate decision-making may yield more sensible actions to promote aligned AI systems in the run up to advanced AI.
    

_See more: our_ [_AI Governance Curriculum_](https://aisafetyfundamentals.com/ai-governance-curriculum) _describes further areas for governance and strategy work in more detail._

**Note that technical problems can sometimes take decades to solve, so even if advanced AI is decades away, it’s still reasonable to begin working on developing solutions now.** Current technical AI alignment work is occurring in academic labs (e.g., at [UC Berkeley's CHAI](https://humancompatible.ai/), among many other academic labs), in nonprofits and public benefit corporations (e.g., [Redwood Research](https://www.redwoodresearch.org/) and [Anthropic](https://www.anthropic.com/)), and in industrial labs (e.g., [DeepMind](https://www.alignmentforum.org/posts/nzmCvRvPm4xJuqztv/deepmind-is-hiring-for-the-scalable-alignment-and-alignment) and [OpenAI](https://openai.com/blog/our-approach-to-alignment-research/)). A recent survey of top AI researchers, however, [indicates](https://aiimpacts.org/2022-expert-survey-on-progress-in-ai/) most (69%) think society should prioritize “AI safety research” [32] either “more” or “much more” than currently."