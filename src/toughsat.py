#!/usr/bin/python3

import sys
import random

if len(sys.argv) < 4:
    print("usage: python toughsat.py <literals per clause> <no. of variables> <no. of clauses>")
    sys.exit()

k = int(sys.argv[1])
n = int(sys.argv[2])
m = int(sys.argv[3])

if k == 0 or n == 0 or m == 0:
    print("usage: python toughsat.py <literals per clause> <no. of variables> <no. of clauses>")
    sys.exit()

vars = []
for i in range(1, n+1):
    vars.append(i)

F = []
for i in range(m):
    rand_vars = random.sample(vars, k)
    clause = []
    for var in rand_vars:
        if random.randint(0, 1) == 0:
            clause.append(str(var))
        else:
            clause.append("-" + str(var))
    F.append(" ".join(clause))

print("p cnf " + str(n) + " " + str(m))
print(" 0\n".join(F) + " 0\n")
