from copy import deepcopy
from atom import Atom
from rule import Rule
from argument import Argument,generate_defeats
import itertools

def generate_arguments(p,ruleset,seen):
  """Given a ruleset and a proposition, uses backwards chaining to create all arguments for the proposition."""
  arguments=set()
  if p in seen:
          return set()
  valid_rules=filter(lambda x: x.con==p,ruleset) 
  for r in valid_rules:
          added=False
          args_for_pre={}
          for pre in r.pre:
                  args_for_pre[pre]=generate_arguments(pre,ruleset,seen.union([p]))

          prod=itertools.product(*[a for (_,a) in args_for_pre.items()])
          for sa in prod:
                  added=True
                  a=Argument(r,set(sa))
                  for sub in sa:
                          a.subarguments=a.subarguments.union(sub.subarguments)
                  arguments.add(a)
  return arguments                        


def generate_AF(p,ruleset):
  """Generates the abstract AF given the ruleset. Note that the appropriate pref relationship is invoked via the argument file."""
  finished=False
  argsOld=set()

  #there is a hack going on here; we generate arguments, and then iterate through to generate rebutters and undercutters in multiple iterations as needed.
  while not finished:
    t=argsOld.union(generate_arguments(p,ruleset,set()))
    args=deepcopy(t)
    for a in t:
          args=args.union(a.subarguments)
    t=deepcopy(args)
    for a in t:
      args=args.union(generate_arguments(a.toprule.con.neg(),ruleset,set()))
      args=args.union(generate_arguments(Atom(True,a.toprule.name),ruleset,set()))
    if args==argsOld:
       finished=True
    else:
       argsOld=args
      
  #still better to generate attacks with arguments
  attacks=generate_defeats(args)
  return (args,attacks)
