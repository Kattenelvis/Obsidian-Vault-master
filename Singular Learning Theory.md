[(10) Singular Learning Theory - Seminar 1 - What is learning? - YouTube](https://www.youtube.com/watch?v=QZG40ZY5TeU)


Def: Learning is the acquisition of knowledge and skill through experience

We consider and agent in an environment making measurments of a computable process $Q$. Learning is a process of an agent selecting a model for $Q$. A model is an algorithm, which is 'true' if it reproduces (the distribution of) measurments from $Q$.  

The "computable" is generally about the processes in the environment being computable (generating information only with computable functions). It may be impossible to "learn" something uncomputable, but this is controversial.

The possible models are parametrized on a space $W$. Learning is a dynamical process on $W$, and the points of $W$ are models, the goal of learning being to find the true model.

Traversing the space of parameter values, for example two values $x$ and $y$, with a function $f(x,y)$ which determines the parameters for some probability distribution, then there are different values of $x$ and $y$ which generates the same values for $f(x,y)$. This might form a line or some other kind of surface on $R^2=W$. So there's not an injection form parameters to models (called degenerancy I think?).

Energy is defined to be the the measure of distance between $Q$ and one's estimate $Q^*$. Energy minimization is learning. 
![[Pasted image 20230618162351.png]]

On the first of the lecture notes, it says "Both a model and a prior are fictional candidates, because uncertainty is unknown". Seems like a highly philosophical statement.  