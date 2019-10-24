import timeit

code_to_test = """

from forwards_chainer import generate_AF as generate_AFF
from parser import read_file
from atom import Atom
import sys

rules=read_file(sys.argv[1])
af2=generate_AFF(rules)
print("arguments: ",len(af2[0]))

nbdef = 0
for i in af2[1][0]:
    nbdef+= len(af2[1][0][i])

print("defeats: ",nbdef)

"""

elapsed_time = timeit.timeit(code_to_test, number=1)/1
print("time elapsed:", elapsed_time)
