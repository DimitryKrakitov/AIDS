
import sys
from filereader import *
from cnfWriter import *
from testing import renai_circulation
#from kafka import *
from kafka3 import *

if len(sys.argv) != 2:
    print("Not the right amount of arguments.")
    exit(-1)


data = filereader(sys.argv[1])
cnf_clauses = []
cnf_to_prove = []
full_counter = 0
for line in data[0:-1]:# For each line in the text file
    full_counter += 1
    tup = eval(line)

    ############### DEBUGGING ##########
    '''print(tup)
    print("elem 1: " + str(tup[0]))
    if len(tup) > 1:
        print("elem 2: " + str(tup[1]))
        if len(tup) > 2:
            print("elem 3: " + str(tup[2]))'''

    ####################################
    print("\0")
    print("LINE: " + line)

    try:

        cnf_clauses.extend(renai_circulation(tup)) # Process the line (recursive)
    #new_tup = renai_circulation_teste(tup, full_counter) # Process the line (recursive)
    except:
        print("Invalid sentence at line ", full_counter)

    '''while isinstance(new_tup, tuple) and new_tup[0] == 'and':
    
    if isinstance(new_tup, tuple) and new_tup[0] == 'and':
        # new_tup = ands(new_tup)

        print("New Lines formed (probably from equivalence)")
        print("     line ", full_counter, "(1/2): ", str(new_tup[1]))
        new_line.append(renai_circulation_teste(new_tup[1]))
        print("     line ", full_counter, "(2/2): ", str(new_tup[2]))
        new_line.append(renai_circulation_teste(new_tup[2]))'''

#cnf_clauses.append(new_tup)

try:

    cnf_to_prove.extend(renai_circulation(negation(eval(data[-1]))))  # Process the line (recursive)
# new_tup = renai_circulation_teste(tup, full_counter) # Process the line (recursive)
except:
    print("Invalid clause to prove, line: ", (full_counter + 1))

output_file(metamorfose(cnf_clauses), metamorfose(cnf_to_prove))

