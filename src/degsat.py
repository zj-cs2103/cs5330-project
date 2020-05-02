#!/usr/bin/python3

import sys
import random

if len(sys.argv) < 5:
    print("usage: python degsat.py <dependence deg> <no. of variables> <no. of clauses> <clause length>")
    sys.exit()

DEP_DEG = int(sys.argv[1])
NUM_VARS = int(sys.argv[2])
NUM_CLAUSES = int(sys.argv[3])
MAX_CLAUSE_LEN = int(sys.argv[4])

CLAUSES = [set() for i in range(NUM_CLAUSES)]
CLAUSE_DEP = [set() for i in range(NUM_CLAUSES)]
VAR_DEP = [set() for i in range(NUM_VARS)]

AVAIL_VARS = [i for i in range(NUM_VARS)]
AVAIL_CLAUSES = [i for i in range(NUM_CLAUSES)]

# set iterations limit
MAX_ITERATIONS = 10000000000000

iterations = 0
while (len(AVAIL_CLAUSES) > 0 and len(AVAIL_VARS) > 0 and iterations < MAX_ITERATIONS):
    iterations += 1
    
    clause = random.choice(AVAIL_CLAUSES)
    var = random.choice(AVAIL_VARS)
    
    # if this clause already contains this var, reroll
    if (var in CLAUSES[clause]):
        continue
    
    # if adding this var causes the deg requirement to be violated, reroll
    if (len(CLAUSE_DEP[clause].union(VAR_DEP[var])) > DEP_DEG):
        continue
    
    # add this var to the clause
    CLAUSES[clause].add(var)
    
    # update the dependencies of all clauses
    # also find max dep over all clauses of this var
    for dep_clause in VAR_DEP[var]:
        CLAUSE_DEP[clause].add(dep_clause)
        CLAUSE_DEP[dep_clause].add(clause)
    
    # add this clause to the var
    VAR_DEP[var].add(clause)
    
    # if this clause is full, remove this clause from the available clauses
    if len(CLAUSES[clause]) == MAX_CLAUSE_LEN:
        AVAIL_CLAUSES.remove(clause)
        
    # remove all variables in clauses with max dependency
    for i in range(NUM_CLAUSES):
        if (len(CLAUSE_DEP[i]) == DEP_DEG):
            try:
                AVAIL_CLAUSES.remove(i)
            except:
                pass
            for var in CLAUSES[i]:
                try:    
                    AVAIL_VARS.remove(var)
                except:
                    pass
    
# randomly negate some of the variables
for i in range(len(CLAUSES)):
    elems = list(CLAUSES[i])
    for j in range(len(elems)):
        multiplier = random.choice([-1, 1])
        elems[j] += 1 # minisat requires 1-indexed vars
        elems[j] *= multiplier
    # pad the clause if the length of this clause is not enough
    if (len(elems) > 0):
        for j in range(MAX_CLAUSE_LEN - len(elems)):
            elems.append(elems[-1])
    CLAUSES[i] = elems
        
# output
for clause in CLAUSES:
    if len(clause) == 0:
        NUM_CLAUSES -= 1

print("p cnf " + str(NUM_VARS) + " " + str(NUM_CLAUSES))
empty = 0
for clause in CLAUSES:
    if len(clause) == 0:
        empty += 1
    else:    
        clause = [str(elem) for elem in clause]
        print(" ".join(clause) + " 0")

sys.stderr.write(str(empty)+"\n")