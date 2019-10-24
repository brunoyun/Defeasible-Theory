from copy import deepcopy

#Contains functions to deal with abstract argumentation frameworks

def __in_preferred(args,att,p,label):
  """Internal function to compute whether a single argument p is in for some AF (arg,att) with a predefined set of labels."""
  if label.get(p)=="in":
          return True
  (attacks,attackers_of)=att
  l=deepcopy(label)
  l[p]="in"
  for a in attackers_of.get(p,set()):
          if not __out_preferred(args,att,a,l):
                  return False
  return True

def __out_preferred(args,att,p,label):
  """Internal function to compute whether a single argument p is out for some AF (arg,att) with a predefined set of labels."""
  if label.get(p)=="in":
          return False
  (attacks,attackers_of)=att
  l=deepcopy(label)
  l[p]="out"
  for a in attackers_of[p]:
          if __in_preferred(args,att,a,l):
                  return True
  return False

def in_preferred(args,att,a):
  """Used to compute whether argument a is labelled in."""
  return __in_preferred(args,att,a,{})

def in_preferred_conc(args,att,p):
  """used to determine whether a proposition p which is a conclusion of an argument is in."""
  for a in filter(lambda x: x.toprule.con==p,args):
          if in_preferred(args,att,a):
                  return True
  return False

def grounded(args,att,admis=set()):
  """Used to compute the grounded extension of an AF."""
  (attacks,attackers_of)=att
  newadmisset=deepcopy(admis)
  for n in args:
    nIn=True
    for a in attackers_of[n]:
      defendedFromA=False
      for b in attackers_of[a]:
         if b in admis:
            defendedFromA=True
            break
      if not defendedFromA:
         nIn=False
         break
    if nIn:
      newadmisset.add(n)
  if len(newadmisset)==len(admis):
      return newadmisset
  else:
      return grounded(args,att,newadmisset)
