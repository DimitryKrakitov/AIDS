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

Jail = []#"literals" we "know" are true - the knowledge
Jail.append(independencia[-1])

portugal = []
#portugal.extend(x for x in independencia if len(x) > 1)

for angola in independencia[1:-1]:
    if len(angola) == 1:#if sentence is just literal, add to arguments
        Jail.append(angola)
    else:
        portugal.append(angola)#if not literal (sentence) add to portugal


portugal = independencia.copy()
while portugal:
    for Nigga in Jail:#cycle through arguments we know are true, till we find one still in unused sentences
        for thisNephew in portugal:
            if negation(Nigga) in thisNephew:#if a negated element is found in the disjunction, then the other side is true and added to the "knowledge"
                anotha_one = thisNephew #the sentence
                anotha_one.remove(negation(Nigga))#choose the other side of the disjunction, the "new truth"
                if negation(anotha_one[0]) in Jail: #if the negation of this truth was already in "the knowledge", we have a contradiction, and we prove the resolution "True"
                    print("True")
                    exit()
                if anotha_one[0] not in Jail:
                    Jail.append(anotha_one)#if it's a new Truth, add to the "knowledge"
                portugal.remove(thisNephew)
                break
#talvez seja possivel que no fim fiquem só sentences perdidas no portugal que n "provam" nada e nunca foram usadas e assim
#  ficamos num ciclo infinito
print("False")
exit()