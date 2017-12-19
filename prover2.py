from filereader import *
from provFunctions import negation_in


import sys
from literalyPrinters import *

if len(sys.argv) != 2:
    print("Not the right amount of arguments.")
    exit(-1)

data = filereader(sys.argv[1])

provelist = []
cnfStatements = []
for line in data:# For each line in the text file
    cnfStatements.append(line)

provelist.append(data[len(data)-1]) # alpha is already negated

for prove in provelist:
    prove = eval(prove)
    #print("PROVE: ", prove)
    for clause in cnfStatements:
        clause = eval(clause)
        #print("CLAUSE: ", clause)
        add_kb = negation_in(prove, clause)
        #print("ADD_KB: ", add_kb)
        if(add_kb==1):
            print("THEOREM PROVED: TRUE")
            exit(1)
        if(add_kb):
            cnfStatements.extend(add_kb)
            provelist.extend(add_kb)
            #print(cnfStatements)

print("THEOREM NOT PROVED: FALSE")
exit(0)
