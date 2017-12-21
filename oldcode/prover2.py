from filereader import *
from provFunctions import simplify, resolve, contained, remove_duplicates, simplify_4

import sys
from literalyPrinters import *

if len(sys.argv) != 2:
    print("Not the right amount of arguments.")
    exit(-1)

data = filereader(sys.argv[1])

provelist = []
cnfStatements = []
# for line in data:# For each line in the text file
#    cnfStatements.append(line)

for line in data:
    for s in ["\n", " ", "'", "[", "]", "(", ")", "not,"]:
        if s != "not,":
            line = line.replace(s, "")
        else:
            line = line.replace(s, "-")
    cnfStatements.append(line.split(","))

print("BEFORE SIMPLIFY")
print(cnfStatements)

# provelist.append(data[len(data) - 1])  # alpha is already negated


#### DONT KNOW WHERE alpha is ???
clauses = simplify(cnfStatements)

print("\n")
print("\n")

clauses = sorted(clauses, key=len)  ############ ORDENAR CLAUSES POR TAMANHO

print("CLAUSES SORTED:")
print(clauses)

print("\n")

if not clauses:
    print("SIMPLIFICATION EMPTIED CLAUSES")
    print("FALSE")
    exit(-2)
new = []
x=0
while 1:
    x=x+1
    for i in range(len(clauses)):
        for j in range(len(clauses)):
            if i < j:
                #print("RESOLVE:")
                #print(clauses[i])
                #print("WITH")
                #print(clauses[j])
                resolvent, resolved = resolve(clauses[i], clauses[j])
                #print(resolvent)

                if resolved and not resolvent:
                    print("TRUE")
                    exit(1)
                elif resolved and resolvent:
                    new.append(resolvent)
                    #print("NEW")
                    #print(new)
    #print("CLAUSES")
    #print(clauses)
    new = simplify_4(new)
    new = remove_duplicates(new)
    #print("NEW")
    #print(new)
    if contained(new, clauses):  # We are not "learning" anything new...
        print("FALSE")
        exit(-1)

    clauses.extend(new)
    #print("BEFORE REMOVAL")
    #print(clauses)
    clauses = remove_duplicates(clauses)
    clauses = sorted(clauses, key=len)
    #print(clauses)
    #print("SIMPLIFY")
    clauses = simplify(clauses)
    #print("SIMPLIFIED:")
    #print(clauses)
    if(x==2):
        #exit(23)
        pass