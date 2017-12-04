from filereader import *
from convFunctions import negation
import sys
from literalyPrinters import *

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

for angola in independencia[0:-1]:
    if len(angola) == 1:#if sentence is just literal, add to arguments
        Jail.append(angola)
    else:
        portugal.append(angola)#if not literal (sentence) add to portugal


#portugal = independencia.copy()
print("Portugal in the Begining: " + str(portugal))
#while portugal:
for Nigga in Jail:#cycle through arguments we know are true, till we find one still in unused sentences
    print("")
    print("     Jail is now: " + str(Jail))
    #print(printer(Jail))
    print("Who's this Nigga?")
    print(Nigga)
    print("  Portugal is now: " + str(portugal))
    #print(printer(Jail))
    for thisNephew in portugal:
        print("thisNephew is :" + str(thisNephew))
        print("is " + negation(str(Nigga)) + " in " + str(thisNephew))
        if negation(str(Nigga)) in thisNephew:#if a negated element is found in the disjunction, then the other side is true and added to the "knowledge"
            print("Yes my dudes")
            anotha_one = thisNephew #the sentence
            anotha_one.remove(negation(Nigga))#choose the other side of the disjunction, the "new truth"
            if negation(anotha_one[0]) in Jail: #if the negation of this truth was already in "the knowledge", we have a contradiction, and we prove the resolution "True"
                print("True")
                exit()
            if anotha_one[0] not in Jail:
                Jail.append(anotha_one)#if it's a new Truth, add to the "knowledge"
            portugal.remove(thisNephew)
            break
        else:
            print("Nope my dudes")
#talvez seja possivel que no fim fiquem só sentences perdidas no portugal que n "provam" nada e nunca foram usadas e assim
#  ficamos num ciclo infinito
print("False")
exit()