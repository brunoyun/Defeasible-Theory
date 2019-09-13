Acknowledgements
==================

* This generator is inspired from the Haskell defeasible generator of Maher et al. (Efficient Defeasible Reasoning Systems)

Content
==================

This repository contains:

* An executable JAR containing the generator tool.

* A set of generated examples.

Description
==================

In order to launch the def-generator.jar, you can proceed by launching the terminal, moving to directory and use: 

    * java -jar def-generator.jar [parameters]
    


Tools parameters
==================

The generator tool can generate different types of defeasible theories. The several parameters are:

* [-p] [length] [T/F]: Creates a chain of size [length]. If the third parameter is [T], the chain is composed of strict rules. If it is [F], the chain is composed of defeasible rules.

* [-c] [length] [T/F]: Creates a cycle of size [length]. If the third parameter is [T], the chain is composed of strict rules. If it is [F], the cycle is composed of defeasible rules.

* [-l] [size] [T/F]: Creates a cascade of [size] disputed conclusions. If the third parameter is [T], some rules have superior priorities. If it is [F], all the rules have equal priorities.

* [-t] [branching] [depth] [T/F]: Creates a [branching]-branching tree of depth [depth]. If the fourth parameter is [T], the tree is composed of strict rules. If it is [F], the tree is composed of defeasible rules.

* [-m] [size]: Creates a defeasible theory where every literal is disputed.


Tools parameters
==================

To generate a chain of size 3 composed of defeasible rules, use:

    * java -jar def-generator.jar -p 3 F
    

Contacts
==================

In order to contact me, send me an email at: yun@lirmm.fr
