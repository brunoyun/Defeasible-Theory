import re

class Atom:
  """Class used to encode propositional atoms."""
  def __init__(self,negated,literal):
    self.negated=negated
    self.literal=literal

  def neg(self):
    return Atom(not self.negated,self.literal)

  def con(self,atom):
    return self.literal==other.literal and (self.negated and other.negated) == False

  def __hash__(self):
    return hash((self.negated,self.literal))

  def __eq__(self,other):
    return type(self)==type(other) and self.negated==other.negated and self.literal==other.literal

  def __repr__(self):
    if self.negated:
      return "!"+self.literal
    else:
      return self.literal

  @classmethod
  def from_string(cls,s):
    """A primitive parser. Given a string, creates an atom where ! denotes negation."""      
    neg=False
    if s.startswith("!"):
      neg=True
    p=re.sub('^[!]','',s)
    return Atom(neg,p)
