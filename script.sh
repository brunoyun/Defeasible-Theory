#!/bin/bash

 # for s in 25000 50000 75000 100000
 # do
 # java -jar def-generator.jar -p $s T > Examples/Chains/Strict/b$s.txt
 # java -jar def-generator.jar -p $s F > Examples/Chains/Defeasible/b$s.txt
 # java -jar def-generator.jar -c $s T > Examples/Cycles/Strict/b$s.txt
 # java -jar def-generator.jar -c $s F > Examples/Cycles/Defeasible/b$s.txt
 # done

# for s in 8 9 10
# do
# java -jar def-generator.jar -t 3 $s F > Examples/Trees/b$s-3.txt
# done

for s in 10 11 12 13 14 15 20 1000 5000 10000 30000
do
java -jar def-generator.jar -l $s F > Examples/Levels/Normal/b$s.txt
done

# for s in 10 1000 5000 10000 30000
# do
# java -jar def-generator.jar -l $s T > Examples/Levels/Superiority/b$s.txt
# done
#
# for s in 3 4 5 6 7
# do
#   java -jar def-generator.jar -m $s > Examples/Teams/b$s.txt
# done
