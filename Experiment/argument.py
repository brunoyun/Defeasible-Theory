from atom import Atom

class Argument:
  """Class describing ASPIC- like arguments made up of toprules, subarguments and whether the rule is strict/defeasible"""
  def __init__(self,toprule,subarguments):
    self.toprule=toprule
    self.subarguments=subarguments

  def strict(self):
    return toprule.strict and all([sa.strict for sa in self.subarguments])


  def defrules(self):
    """returns the defeasible rules of the argument."""
    r=set()
    if not strict:
            r.add(toprule)
    for s in self.subarguments:
            r=r.union(s.defrules)
    return r


  def __eq__(self,other):
    return self.__class__==other.__class__ and self.toprule==other.toprule and self.subarguments==other.subarguments

  def __hash__(self):
    s=0
    for sa in self.subarguments:
            s+=hash(sa)
    return hash(self.toprule)+s

  def __repr__(self):
    o="[("
    for sa in self.subarguments:
            o+=str(sa)+", "
    o+=")"+str(self.toprule)
    s=self.toprule.priority
    for sa in self.subarguments:
            if sa.toprule.priority<s:
                    s=sa.toprule.priority
    return o+" "+str(s)+"]"


  def conc(self):
    return self.toprule.con
##############################################################

def generate_defeats(args):
  """generates the defeats within a set of arguments. Uses the function weaker for preferences."""
  att={}
  attacker_of={}
  for a in args:
          att[a]=set()
          for b in args:
                  if attacker_of.get(b)==None:
                          attacker_of[b]=set()
                  if attacks(a,b) and weaker(b,a):
                          att[a].add(b)
                          attacker_of[b].add(a)
  return att,attacker_of

def weaker(b,a): #change to reflect whatever rule
  """a placeholder to call whetever type of pref function is used"""
  return weakerll(b,a)

def weakerll(b,a):
    """Is b weaker than a according to last link"""
    if b.toprule.strict:
        return False
    if a.toprule.strict:
        return True
    return b.toprule.priority<=a.toprule.priority

def weakerwd(b,a):
  """Is b weaker than a according to weakest link democratic? Democratic means there is one argument in a that is stronger than everything in b"""
  for x in a.defrules():
    stronger=True
    for y in b.defrules():
      if x.priority<=y.priority:
        stronger=False
        break
    if stronger:
      return True
  return False

def weakerwe(b,a):
  """Is b weaker than a according to weakest link elitist - there is an argument in b that is weaker than all arguments in a"""
  for x in b.defrules():
    weaker=True
    for y in a.defrules():
      if y.priority<x.priority:
        weaker=False
        break
    if weaker:
        return True
  return False


def attacks(a,b): #a attacks b
  """Returns True if a attacks b"""
  if a.toprule.con==b.toprule.con.neg() and not b.toprule.strict: #restricted rebut, remove "and not ..." for unrestricted
          return True
  for s in b.subarguments:
          if a.toprule.con==s.toprule.con.neg() and not s.toprule.strict: #restricted rebut, remove "and not ..." for unrestricted
                  return True
  if a.toprule.con==Atom(False,b.toprule.name).neg():
          return True
  return False
