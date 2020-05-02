#!/usr/bin/python3

import random
import statistics
import sys

def find_bad_clauses(CLAUSES, assignment):
    bad_clauses = []
    for i in range(len(CLAUSES)):
        is_bad = True
        for var in CLAUSES[i]:
            if var * assignment[abs(var)] > 0:
                is_bad = False
                break
        if is_bad:
            bad_clauses.append(i)
    return bad_clauses

xx, xx, NUM_VARS, NUM_CLAUSES = map(str, input().split(" "))
NUM_VARS = int(NUM_VARS)
NUM_CLAUSES = int(NUM_CLAUSES)

CLAUSES = [list(map(int, input().split(" ")))[:-1] for i in range(NUM_CLAUSES)]
VARS = [1 for i in range(NUM_VARS + 1)]

RESAMPLE = [0 for i in range(NUM_CLAUSES)]

assignment = [random.choice([-1, 1]) for i in range(NUM_VARS+1)]
iterations = 1
bad_clauses = find_bad_clauses(CLAUSES, assignment)
while (len(bad_clauses) > 0):
    bad_clause = random.choice(bad_clauses)
    RESAMPLE[bad_clause] += 1
    for var in CLAUSES[bad_clause]:
        assignment[abs(var)] = random.choice([-1, 1])
    bad_clauses = find_bad_clauses(CLAUSES, assignment)
    iterations += 1

sys.stdout.write(str(iterations) + " ")
#print("DONE! Iterations: " + str(iterations))
#print("Max: " + str(max(RESAMPLE)) + ", Min: " + str(min(RESAMPLE)) + ", MEDIAN: " + str(statistics.median(RESAMPLE)))
#print(RESAMPLE)
#print("Solution: " + str([assignment[i]*i for i in range(1, NUM_VARS+1)]))