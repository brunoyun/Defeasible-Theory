import random

NUMRULES=20
NUMPROP=8
PDEFEASIBLE=0.5
PNEG=0.5
MAXRULELEN=5
PUNDERCUTTER=0.1


def generateRule():
  head=set()
  for x in range(0,random.randint(0,MAXRULELEN)): 
    head.add(makeAtom(head))
  if random.random()>PUNDERCUTTER:  
    body=makeAtom(head)
  else:
    body=makeRuleUndercutter()  

  if len(head)>0:
    s=','.join(head)
  else:
    s=''  
  if random.random()<PDEFEASIBLE:
    s+="=>"
  else:
    s+="->"
  s+=body
  return s

def makeAtom(excludelist):
  s=""
  if random.random()<PNEG:
    s+="!"
  invalidC=True
  while invalidC:
    candidate="p"+str(random.randint(0,NUMPROP))
    if candidate not in excludelist and "!"+candidate not in excludelist:
      s+=candidate
      invalidC=False  
  return s

def makeRuleUndercutter():
  return "!r%d"%random.randint(0,NUMRULES)
    

for i in range(0,NUMRULES):
  print("r%d: %s"%(i,generateRule()))
