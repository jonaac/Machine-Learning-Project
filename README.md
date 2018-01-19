# Machine Learning Research Project

The use of machine learning techniques to build autonomous agents/systems is becoming more widespread as designing agents by hand is costly.  Moreover, agents often operate in stochastic domains where it may be difficult to identify effective policies/strategies.  However, the increasing use of machine learning techniques (e.g., reinforcement learning, neural nets and deep learning, genetic programming) to build agents has given rise to widespread concerns over whether such systems are safe to deploy.  One reason for this is that some scenarios that threaten safety may be very infrequent and it is hard to ensure that the training set includes enough of these to ensure that safety-preserving behaviors are learned. Another reason is that many machine learning techniques construct their own representations of the domain (e.g., deep learning) and it is hard to ensure that these representations carry the necessary information to ensure safety, and that the resulting policies/strategies are safe. 

Outside of the Machine Learning field, in the area of Formal Methods, there has been a lot of work on techniques to ensure that computer systems satisfy given specifications, including safety.  One relevant line of work addresses verification and synthesis of reactive systems.  Another line of work is concerned with supervision of discrete event systems to ensure that they satisfy a given supervision specification.  There is a lot of interest in exploiting such techniques to ensure safety of machine learning-based systems.

This research project has two main objectives: 
1. To research the literature on the safety of systems built using machine learning techniques
2. To build a test-bed for experimenting with agents that include machine learning-derived components and techniques for ensuring that they are safe.

With respect to the latter objective, the test-bed should include one or more domains that are easy to describe, stochastic, where it is straightforward to specify performance and safety specifications/objectives, and where effective policies/strategies can be learned. In some domain variants, foresight/look-ahead should be necessary to ensure that safety is preserved. 

For example, a domain might involve a planetary robot that moves around in a grid world collecting mineral ore and avoiding falling into craters. The probability of finding ore might depend on the features of the location.  

An implementation of the test-bed and simulated domain(s) should be developed as part of the project.  The implementation should support at least one machine learning algorithm, perhaps a form of reinforcement learning, and it should be possible to run it to obtain policies/strategies.  Some safety properties of interest should be formalized, and some techniques to ensure that they hold should be identified.
