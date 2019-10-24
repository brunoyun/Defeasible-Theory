from lark import Lark,Transformer
import sys
from rule import Rule
from atom import Atom

grammar = r"""
NEG: "!"
NUMBER: /[0-9_]\w*/
NUMBERSTRING: /[a-zA-Z0-9_]\w*/
STRICT: "->"
DEFEASIBLE: "=>"
COMMENT: /#[^\n]*/

ruleset: (arule)*
arule: NUMBERSTRING ":" prem (STRICT|DEFEASIBLE) atom ["," NUMBER]
prem: [atom ("," atom)*]
conc: atom
priority: NUMBER
atom: NEG? NUMBERSTRING

%import common.WS
%ignore WS
"""

parser=Lark(grammar,start='ruleset')

class MyTransformer(Transformer):
  
  def ruleset(self,args):
    return set(args)

  def arule(self,args):
    priority=0
    name=str(args[0])
    prems=args[1]
    strict=(args[2].type=="STRICT")
    conc=args[3]
    if len(args)>4:
      priority=int(args[4])
    #print(prems,conc,strict,priority,name)
    return Rule(prems,conc,strict,priority,name)

  def atom(self,args):
    if args[0].type=="NEG":
      return Atom(True,str(args[1]))
    else:
      return Atom(False,str(args[0]))

  def prem(self,args):
    return set(args)


def read_file(filename):
  with open(filename,'r') as myfile:
    return MyTransformer().transform(parser.parse(myfile.read()))


