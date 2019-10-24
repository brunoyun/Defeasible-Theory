class Rule:
  def __init__(self,pre,con,strict,priority,name):
    self.pre=pre
    self.con=con
    self.strict=strict
    self.name=name
    self.priority=priority

  def __repr__(self):
    s="=>"
    if self.strict:
            s="->"
    p=""
    if self.pre!=set():
            for pr in self.pre:
                    p=p+", "+str(pr)
    return ""+p+" "+s+"  "+str(self.con)

  def __hash__(self):
    s=0
    for p in self.pre:
      s+=hash(p)
    return hash((s,self.con,self.strict,self.name))

  def __eq__(self,other):
    if self.__class__!=type(other):
      return False
    if (self.pre-other.pre)!=set() and (other.pre-self.pre)!=set():
      return False
    return self.con == other.con and self.strict==other.strict and self.name==other.name

  def contrapositives(self):
    cp=set()
    for p in self.pre:
      np=deep_copy(self.pre)
      np.remove(p)
      np.add(self.con.neg())
      cp.add(Rule(np,p.neg(),self.strict,None))

    return cp  

