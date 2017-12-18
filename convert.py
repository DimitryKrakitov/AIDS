
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
    print("LINE: " + line)
    output.extend(line_processor(tup, exp, full_counter)) # Process the line (recursive)


#print(output)
output_file(output)

