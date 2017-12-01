from filereader import *
from convFunctions import negation
import sys


if len(sys.argv) != 2:
    print("Not the right amount of arguments.")
    exit(-1)

data = filereader(sys.argv[1])

info = []
for line in data:# For each line in the text file

    info.append(eval(line))

args = []#"literals" we "know" are true - the knowledge
args.append(info[-1])

temp = []
#temp.extend(x for x in info if len(x) > 1)

for angola in info[1:-1]:
    if len(angola) == 1:#if sentence is just literal, add to arguments
        args.append(angola)
    else:
        temp.append(angola)#if not literal (sentence) add to temp


temp = info.copy()
while temp:
    for item in args:#cycle through arguments we know are true, till we find one still in unused sentences
        for elem in temp:
            if negation(item) in elem:#if a negated element is found in the disjunction, then the other side is true and added to the "knowledge"
                another = elem #the sentence
                another.remove(negation(item))#choose the other side of the disjunction, the "new truth"
                if negation(another[0]) in args: #if the negation of this truth was already in "the knowledge", we have a contradiction, and we prove the resolution "True"
                    print("True")
                    exit()
                if another[0] not in args:
                    args.append(another)#if it's a new Truth, add to the "knowledge"
                temp.remove(elem)
                break
#talvez seja possivel que no fim fiquem só sentences perdidas no temp que n "provam" nada e nunca foram usadas e assim
#  ficamos num ciclo infinito
print("False")
exit()