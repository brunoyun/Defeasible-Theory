from backwards_chainer import generate_AF as generate_AFB
from forwards_chainer import generate_AF as generate_AFF
from abstract import in_preferred_conc,grounded
from parser import read_file
from atom import Atom
import sys

rules=read_file(sys.argv[1])
atom=Atom.from_string(sys.argv[2])
af=generate_AFB(atom,rules)
af2=generate_AFF(rules)
print("baf: ",af)
print("faf: ",af2)
print()
print("af-af2: ", af[0]-af2[0])
print("af2-af: ", af2[0]-af[0])
print("------args----------")
for i in af2[0]:
  print(i)
print("------args 2--------")
for i in af[0]:
        print(i)
print(len(af[0]),len(af2[0]))
print()
print("backwards: ",in_preferred_conc(af[0],af[1],atom))
print("backwards: ",in_preferred_conc(af[0],af[1],atom.neg()))
print("backwards g:",grounded(af[0],af[1]))
print("forwards: ",in_preferred_conc(af2[0],af2[1],atom))
print("forwards: ",in_preferred_conc(af2[0],af2[1],atom.neg()))
print("forwards g:",grounded(af2[0],af2[1]))
