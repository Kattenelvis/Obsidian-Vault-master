Humlegårdens choice to resurface a playground comes with a great opportunity to maximize benefits, and ensure the health and safety for the next generation. In this report we go over multiple optimization criterions for selecting an optimal playground flooring such as fall risk, toxicity, accessibility and cost. Our conclusion is that while wood chips are a little bit more expensive, it's the best compromise for minimizing risks and toxicity while keeping costs relatively low, compared to other flooring types. While somewhat less accessible than some other alternatives, compressed wood chips can be used for accessibility purposes. 

The next few section will dive into attributes of different playground flooring types, such as fall risk, toxicity, accessibility and cost. The section after that will utilize multi-criteria optimization to construct a linear utility function to calculate optimal flooring, and a reflection if the results are reasonable. 

# Fall Risk 

One of the more important risks to consider is fall risk. Many children are hospitalized every year for fall injuries on playgrounds. Flooring can do a great deal of alleviating this suffering and burden on the healthcare system. 

There is a lower risk of damage with loose-fill materials, which include wood fibers, wood chips, sand, pea gravel and rubber mulch. Unitary materials contribute to a larger degree of risk, such as rubber and artificial grass. Being injured is about About 2.28 times more impact absorbing[1].

According to a study, concrete has a 6x injury risk compared to sand. [5] And since sand already has bad protection, I think we don't even need to include concrete as an option. As one study shows [2], the fall risk can be considered as following:

| Flooring          | Fall Risk |
| ----------------- | --------- |
| Wood Chips        | 1         |
| Sand              | 3         |
| Pea Gravel        | 3         |
| Bonded EWP        | 2         |
| Artificial Grass  | 2         |
| Rubber tiles      | 2         |
| Loose-fill rubber | 1         |

# Toxicity

Toxicity at playgrounds could have bad health effects, both short and long term, for children and other vulnerable populations. Children, the main user of playgrounds, have underdeveloped organs, with immature detoxification mechanisms. 

One article[2] divided them up into four classes of toxicity. Deep green, light green, yellow and orange. I will be using this scoring mechanism to quantify toxicity rates, although its worth noting that toxins and chemicals are different and can have different effects. 

The light green class is merely used for woodchips untested for CCA and sand untested for crystalline silica dust. We will as thus assume for the rest of the article that wood chips are tested for CCA and that sand is tested for crystalline silica dust. We will also assume that woodchips are provided with proper drainage, to prevent possible mold growth (the increased cost of proper drainage will be account for in the cost section). 

| Flooring          | Hazard Risk |
| ----------------- | ----------- |
| Wood Chips        | 1           |
| Sand              | 1           |
| Pea Gravel        | 1           |
| Bonded EWP        | 3           |
| Artificial Grass  | 4           |
| Rubber tiles      | 4           |
| Loose-fill rubber | 4           |

# Accessibility

Accessibility, especially from a Rawlsian perspective, shows how disabled and the elderly can be in playgrounds. 

The firmness and stability of materials are important considerations for accessibility in playground surfacing materials. The firmness is important. So while Loose-fill decreases risk for most children, it makes it worse for children with mobility impairments. A compromise could be to have accessible playgrounds, or that a section of the playground is accessible, with another ground layer and likely also with alternative, accessible playground amenities as well.[3]

The alternative may be stabilized engineered wood fiber. This will enable better accessibility, while keeping some of its other properties. [6]

# Heat

Many children also get damaged from heat related incidents. Just like with toxicity, children are also more vulnerable than average to heat related injuries. Some ground surfaces, but also some installations, can reach a very high temperature. Among the highest in this category, Rubber ranks among the highest for heat. Shade and the color of the surface can of course counteract this. Rubber matting can also get very hot.

# Cost

Cost of construction and maintenance are important factors to consider. A municipality has a limited budget to spend on playground material, especially if this proposal will be reused for future playgrounds who also require groundwork. One article[2] includes the following table of costs:

| Material                                       | Construction Cost | Running Cost |
| ---------------------------------------------- | ----------------- | ------------ |
| Engineered Wood Fiber (Woodchips / Bark Mulch) | $10,100           | $75/year     |
| Sand                                           | $3,000            | $120/year    |
| Pea Gravel                                     | $5,000            | $333/year    |
| Artificial Grass                               | $38,000           |              |
| Unitary Rubber (PIP)                           | $50,000           |              |
| Rubber Mulch                                   | $23,000           | $533/year    |

 We will consider the running costs negligible. Take artificial grass as the cheapest option without costly upkeep. It would take $\$10100 - \$75x = 38000\rightarrow x = 372$ years for the artificial grass to pay for itself, compared to woodchips. We can predict that the current flooring, let alone the playground itself, is unlikely to be around for 372 years. Hence, we will neglect running costs from the calculations.
# Multi-Criteria prioritization

As has been shown in previous sections, there are a large number of variables to take into consideration. Let's narrow it down to three important variables to take into consideration, such that we can in the next section further those variables into a utility function. 

Reasons for prioritizing the minimizing of risks of accidents can be justified from consequentialist moral theories. Taking the option that minimizes the risk of accident also minimizes expected suffering. A lower number of accidents also leads to less spending on healthcare, which can get more expensive for society as a whole, so we can spend that money elsewhere. From a deontological one can consider children moral persons and deserving of welfare. Reasons can also be justified on contractualist grounds, for instance Rawls may argue that, under a vale of ignorance, we'd considering doing what is good for those agents using an egalitarian rule, hence prioritizing the worst off in society (specifically children, but also disabled children). Applying say, leximin, we'd optimize for those with high injury risk before considering other factors.

Worth nothing that some argue minor accidents are nothing to worry about, and might even be a negative to overminimize the risks for mild, non-permanent injuries. For mathematical simplicity I will take it that reducing accident risk is always good, and I will still put negative value to all risks. But it's worth noting that a small enough risk could have diminishing returns for a more advanced calculation. 

Minimizing toxicity can be justified on the same grounds as minimizing fall risk. For instance, toxicity is also something which most negatively impact the worse off individuals. If we consider egalitarian or leximin rule again, we can notice that toxicity will be of a larger importance. 

While minimizing heat risk is also important, and have similar reasons to be considered as the previous two factors, it is not the case that, since it can be sufficiently mitigated with shade and the right kind of color aswell as not being as dangerous as the other two, especially in a colder place like Sweden, I will not consider it for the utility function. 

Some may consider optimizing for employment good. However, it's more efficient to minimize this. You can easily go into the broken glass fallacy. Just because glass repairers get work, it doesn't necessarily yield anything worthwhile for society. Minimizing maintenance costs also allows for long term sustainability even if any government would cut funding. And if no funding is cut, we can put it somewhere else. 

More importantly, the up-front costs have been shown to be vastly greater than maintenance costs. As such, we will primarily be concerned with up-front costs. 

So in conclusion, the three most important values we'll pick out is fall risk, toxicity and cost. 
# Constructing the utility function

In this section we develop the multi-criteria utility function for evaluating the 3 factors deemed the most important in the last section. We take it that the aggregated utility function will be a sum of the utilities of the components. 

To construct it, let's first identify the worst realizations of the three values, which are as following:

| Utility Type | Realization       | Amount |
| ------------ | ----------------- | ------ |
| Cost         | Unitary Rubber    | $50000 |
| Fall Risk    | Rubber tiles      | 3      |
| Toxicity     | Loose fill Rubber | 4      |

We take it that the utility achieved by the worst realizations sum up to 0, as follows:

$v(c_0, r_0, t_0) = v_C(c_0)+v_R(r_0)+v_T(t_0)=0$

Where we take $v$ to be the aggregated utility function, $v_C$ to be the utility function for costs, $v_R$ to be the utility function for fall risks, and $v_T$ to be the utility function for toxicity. 

Given the table above we get the following worst situation:

$v(50000, 3, 4) = v_C(50000)+v_R(3)+v_T(4)=0$

We then do an equivalence comparison based on a difference. I will take it that, as argued before, children's health and safety are worth a lot of money. Only if we save as much as $40000 will we consider a higher level risk or toxicity. As such I consider the following equivalences:

$(\$10000, high, 4) \sim (\$50000, medium, 4) \sim (\$50000, high, 3)$

From that one can calculate the individual utility functions using the general formula:
$$v_C(x) = \frac{c_0 - x}{c_0-c_1}$$
As such we get these utility functions:

$v_C(x)=\frac{50000-x}{40000}$
$v_R(x)={3-x}$
$v_T(x)=4-x$

The following table demonstrate the calculations fully for each flooring we're taking into consideration:

| Material         | Cost  | Cost Utility | Fall Risk | Fall Risk Utility | Toxicity Class | Toxicity Utility | Total Utility |
| ---------------- | ----- | ------------ | --------- | ----------------- | -------------- | ---------------- | ------------- |
| Unitary Rubber   | 50000 | 0            | 2         | 1                 | 4              | 0                | 1             |
| Artificial Grass | 38000 | 0.3          | 2         | 1                 | 4              | 0                | 1.3           |
| Rubber Mulch     | 23000 | 0.675        | 1         | 2                 | 4              | 0                | 2.675         |
| Wood chips       | 10100 | 0.9975       | 1         | 2                 | 1              | 3                | 5.9975        |
| Pea Gravel       | 5000  | 1.125        | 3         | 0                 | 1              | 3                | 4.125         |
| Sand             | 3000  | 1.175        | 3         | 0                 | 1              | 3                | 4.175         |

# Conclusion

Wood chips have the highest utility score in our calculations. This makes sense, for it has many good benefits that protect children, while not being too expensive. It is crucial that the wood chips are tested for VCC and that proper drainage is established to prevent mold growth. For accessibility, stabilized engineered wood fiber can be used. With that in place, it's really the best option, and I advocate for Humlegården to use wood chips for their reflooring of their playground. 

# Literature

[1] Chalmers et. al. Height and surfacing as risk factors for injury in falls from playground equipment: a case-control study. 1996. https://pmc.ncbi.nlm.nih.gov/articles/PMC1067669/pdf/injprev00006-0018.pdf

[2]  Playground Surfacing Choosing Safer Materials for Children's Health and the Environment, 2018.

[3]  Use of two test methods to ensure accurate surface firmness and stability measurements for accessibility, 2016. https://www.tandfonline.com/doi/full/10.1080/17483107.2017.1328618

[5] The effect of surface and season on playground injury rates - PMC, 2012 https://pmc.ncbi.nlm.nih.gov/articles/PMC3496349/

[6]  Stabilized Engineered Wood Fiber for Accessible Trails - American Trails https://www.americantrails.org/resources/stabilized-engineered-wood-fiber-for-accessible-trails



