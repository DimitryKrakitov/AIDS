from filereader import *
from convFunctions import negation
import sys
from literalyPrinters import *

if len(sys.argv) != 2:
    print("Not the right amount of arguments.")
    exit(-1)

data = filereader(sys.argv[1])

cnfStatements = []
for line in data:# For each line in the text file

    cnfStatements.append(eval(line))

knowledge = []#"literals" we "know" are true - the knowledge
knowledge.append(cnfStatements[-1])

cnfNonAtomicSentences = []
#cnfNonAtomicSentences.extend(x for x in cnfStatements if len(x) > 1)

for angola in cnfStatements[0:-1]:
    if len(angola) == 1:#if sentence is just literal, add to arguments
        knowledge.append(angola)
    else:
        cnfNonAtomicSentences.append(angola)#if not literal (sentence) add to cnfNonAtomicSentences


#cnfNonAtomicSentences = cnfStatements.copy()
print("cnfNonAtomicSentences in the Begining: " + str(cnfNonAtomicSentences))
#while cnfNonAtomicSentences:
for literal in knowledge:#cycle through arguments we know are true, till we find one still in unused sentences
    print("")
    print("     knowledge is now: " + str(knowledge))
    #print(printer(knowledge))
    print("Who's this literal?")
    print(literal)
    print("  cnfNonAtomicSentences is now: " + str(cnfNonAtomicSentences))
    #print(printer(knowledge))
    for sentence in cnfNonAtomicSentences:
        print("sentence is :" + str(sentence))
        print("is " + negation(str(literal)) + " in " + str(sentence))
        if negation(str(literal)) in sentence:#if a negated element is found in the disjunction, then the other side is true and added to the "knowledge"
            print("Yes my dudes")
            anotha_one = sentence #the sentence
            anotha_one.remove(negation(literal))#choose the other side of the disjunction, the "new truth"
            if negation(anotha_one[0]) in knowledge: #if the negation of this truth was already in "the knowledge", we have a contradiction, and we prove the resolution "True"
                print("True")
                exit()
            if anotha_one[0] not in knowledge:
                knowledge.append(anotha_one)#if it's a new Truth, add to the "knowledge"
            cnfNonAtomicSentences.remove(sentence)
            break
        else:
            print("Nope my dudes")
#talvez seja possivel que no fim fiquem só sentences perdidas no cnfNonAtomicSentences que n "provam" nada e nunca foram usadas e assim
#  ficamos num ciclo infinito
print("False")
exit()