#!/bin/bash

# for ((s=1000; s<=2000; s+=50))
# do
# java -jar def-generator.jar -p $s T > Examples/Chains/Strict/b$s.txt
# java -jar def-generator.jar -p $s F > Examples/Chains/Defeasible/b$s.txt
# java -jar def-generator.jar -c $s T > Examples/Cycles/Strict/b$s.txt
# java -jar def-generator.jar -c $s F > Examples/Cycles/Defeasible/b$s.txt
# java -jar def-generator.jar -l $s T > Examples/Levels/Priority/b$s.txt
# java -jar def-generator.jar -l $s F > Examples/Levels/No_priority/b$s.txt
# done

for ((s=1; s<=10; s+=1))
do
java -jar def-generator.jar -t 3 $s T > Examples/Trees/Strict/b$s.txt
java -jar def-generator.jar -t 3 $s F > Examples/Trees/Defeasible/b$s.txt
java -jar def-generator.jar -m $s > Examples/Teams/b$s.txt
done
