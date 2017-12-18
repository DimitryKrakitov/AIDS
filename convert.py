
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

    ############### DEBUGGING ##########
    '''print(tup)
    print("elem 1: " + str(tup[0]))
    if len(tup) > 1:
        print("elem 2: " + str(tup[1]))
        if len(tup) > 2:
            print("elem 3: " + str(tup[2]))'''


    ####################################
    if len(tup) == 3:
        if exp == "<=>":
            linha = equivalence(tup[1],tup[2])
            output.extend(linha)

        elif exp == "=>":
            linha = implication(tup[1], tup[2])
            output.append(linha)
        elif exp == "or":
            output.append(disjunction(tup[1],tup[2]))
        elif exp == "and":
            output.extend(conjunction(tup[1],tup[2]))
        else:
            print("Invalid expression  at line: ", full_counter)
    elif len(tup) == 2:
        if exp == "not":
            output.append(negation(str(tup[1])))
        else:
            print("Invalid expression  at line: ", full_counter)
    elif len(tup) == 1:
        output.append("'" + exp + "'")
    else:
        print("Invalid expression  at line: ", full_counter)

    if linha ==


#print(output)
output_file(output)

