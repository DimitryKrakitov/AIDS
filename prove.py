from filereader import *
from convFunctions import negation
import sys


if len(sys.argv) != 2:
    print("Not the right amount of arguments.")
    exit(-1)

data = filereader(sys.argv[1])

independencia = []
for line in data:# For each line in the text file

    independencia.append(eval(line))

args = []#"literals" we "know" are true - the knowledge
args.append(independencia[-1])

portugal = []
#portugal.extend(x for x in independencia if len(x) > 1)

for angola in independencia[1:-1]:
    if len(angola) == 1:#if sentence is just literal, add to arguments
        args.append(angola)
    else:
        portugal.append(angola)#if not literal (sentence) add to portugal


portugal = independencia.copy()
while portugal:
    for item in args:#cycle through arguments we know are true, till we find one still in unused sentences
        for thisNephew in portugal:
            if negation(item) in thisNephew:#if a negated element is found in the disjunction, then the other side is true and added to the "knowledge"
                another = thisNephew #the sentence
                another.remove(negation(item))#choose the other side of the disjunction, the "new truth"
                if negation(another[0]) in args: #if the negation of this truth was already in "the knowledge", we have a contradiction, and we prove the resolution "True"
                    print("True")
                    exit()
                if another[0] not in args:
                    args.append(another)#if it's a new Truth, add to the "knowledge"
                portugal.remove(thisNephew)
                break
#talvez seja possivel que no fim fiquem só sentences perdidas no portugal que n "provam" nada e nunca foram usadas e assim
#  ficamos num ciclo infinito
print("False")
exit()