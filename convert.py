
import sys
from filereader import *
from convFunctions import *
from cnfWriter import *

if len(sys.argv) != 2:
    print("Not the right amount of arguments.")
    exit(-1)


data = filereader(sys.argv[1])
output = []
full_counter = 0
for line in data:# For each line in the text file
    full_counter += 1
    tup = eval(line)
    exp = tup[0]
    '''print(tup)
    print("elem 1: " + tup[0])
    print("elem 2: " + tup[1])
    print("elem 3: " + tup[2])'''
    if len(tup) == 3:
        if exp == "<=>":
            output.extend(equivalence(tup[1],tup[2]))
        elif exp == "=>":
            output.append(implication(tup[1], tup[2]))
        elif exp == "or":
            output.append(disjunction(tup[1],tup[2]))
        elif exp == "and":
            output.extend(conjunction(tup[1],tup[2]))
        else:
            print("Invalid expression  at line: ", full_counter)
    elif len(tup) == 2:
        if exp == "not":
            output.append(negation(tup[1]))
        else:
            print("Invalid expression  at line: ", full_counter)
    elif len(tup) == 1:
        output.append("'" + exp + "'")
    else:
        print("Invalid expression  at line: ", full_counter)

print(output)
output_file(output)

