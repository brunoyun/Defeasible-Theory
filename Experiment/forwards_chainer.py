from atom import Atom
from rule import Rule
from argument import Argument,generate_defeats
import itertools

def generate_arguments(ruleset,existing_arguments=set()):
  finished=False
  while not finished:
      finished=True
      for r in ruleset:
          applicable_rule=True
          arg_for_p={}
          for p in r.pre:
              arg_for_p[p]=set(filter(lambda x: x.toprule.con==p,existing_arguments))
              if len(arg_for_p[p])==0:
                  applicable_rule=False
                  break
          #so now we have a rule and a map arg_for_p for all its premises (assuming applicable_rule is True)
          if not applicable_rule:
              continue
          arglist=set(itertools.product(*[a for (_,a) in arg_for_p.items()]))

#          if len(arglist)==0:
#              newArg=make_single_argument(set(),r)
#              print("na: ",newArg)
#              if newArg not in existing_arguments:
#                  finished=False
#                  existing_arguments.add(newArg)

          for a in arglist:
              newArg=make_single_argument(a,r)
              if newArg!=set() and newArg not in existing_arguments:
                  finished=False
                  existing_arguments.add(newArg)
  return existing_arguments

def generate_AF(ruleset):
  """Generates an AF from a ruleset using forward chaining."""
  args=generate_arguments(ruleset)
  return (args,generate_defeats(args))


def make_single_argument(arg_tuple,toprule):
  """given a set of possible ways to create an argument, creates an argument from one of them. Note that there is a modification over the standard def - a rule is only allowed to be used once in an argument."""
  subargs=set([i for i in arg_tuple])
  for i in arg_tuple:
	  subargs=subargs.union(i.subarguments)
  if len(set(filter(lambda x:x.toprule==toprule,subargs)))>0: #remove this bit to allow a rule to be used more than once in an argument.
          return set()
  return Argument(toprule,subargs)
