from filereader import *
from provFunctions import simplify, resolve, contained, remove_duplicates, simplify_4

import sys

if len(sys.argv) != 2:
    print("Not the right amount of arguments.")
    exit(-1)

data = filereader(sys.argv[1])

provelist = []
cnfStatements = []


for line in data:
    for s in ["\n", " ", "'", "[", "]", "(", ")", "not,"]:
        if s != "not,":
            line = line.replace(s, "")
        else:
            line = line.replace(s, "-")
    cnfStatements.append(line.split(","))


clauses = simplify(cnfStatements)

clauses = sorted(clauses, key=len)

if not clauses:
    print("FALSE")
    exit(-2)

new = []
while 1:
    for i in range(len(clauses)):
        for j in range(len(clauses)):
            if i < j:
                resolvent, resolved = resolve(clauses[i], clauses[j])

                if resolved and not resolvent:
                    print("TRUE")
                    exit(1)
                elif resolved and resolvent:
                    new.append(resolvent)

    new = simplify_4(new)
    new = remove_duplicates(new)
    if contained(new, clauses):  # We are not "learning" anything new...
        print("FALSE")
        exit(-1)

    clauses.extend(new)

    clauses = remove_duplicates(clauses)
    clauses = sorted(clauses, key=len)

    clauses = simplify(clauses)
