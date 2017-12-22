from filereader import *
from provFunctions import simplify, resolve, contained, remove_duplicates, simplify_4
import sys

if len(sys.argv) != 2:
    print("Not the right amount of arguments.")
    exit(-1)

data = filereader(sys.argv[1])





'''
Where we change the syntax of the clauses to a more convinient one. Every negated literal is rewriten according
to the example:
( ’ not ’ , ’B’ ) ----->  '-B'

'''
cnfStatements = []
for line in data:
    for s in ["\n", " ", "'", "[", "]", "(", ")", "not,"]:
        if s != "not,":
            line = line.replace(s, "")
        else:
            line = line.replace(s, "-")
    cnfStatements.append(line.split(","))

# Before starting the reasoner, all the knowledge base is simplified
# acording to the 4 simplifications mentioned in the report.
# This improves the efficency of the algorithm.
clauses = simplify(cnfStatements)
# All clauses are sorted, giving priority to clauses with less literals:
clauses = sorted(clauses, key=len)

# If after all the simplifications, all the clauses are removed then this means that there is nothing to prove.
# The program returns False meaning that the sentence cannot be proven given the knowledge base provided.
if not clauses:
    print("FALSE")
    exit(-2)


'''
Theorem Solver: Given a knowledge base (clauses) of facts and a sentence to prove (included in clauses),
it returns True or False depending on wether the sentence can be proven or not by the knowledge base.
The Resolution Inference method is used.
'''


def theorem_prover(clauses):  # Knowledge base with sentence to prove
    new = []  # List to store learned clauses (resolvents)
    while 1:
        # For each of Clauses in the Knowledge Base preform a resolution:
        for i in range(len(clauses)):
            for j in range(len(clauses)):
                if i < j:  # This prevents preforming duplicate resolutions (resolve(a,b)=resolve(b,a))
                    # Resolve 2 clauses:
                    resolvent, resolved = resolve(clauses[i], clauses[j])
                    if resolved and not resolvent:  # If a resolution was preformed and the result was the empty clause
                        # The sentence to prove is proven given the knowledge base!
                        print("TRUE")
                        exit(1)
                    elif resolved and resolvent:  # If the resolution was preformed and the resolvent isn't empty clause
                        new.append(resolvent)  # New clause (resolvent) is added to the new list (new knowledge)
        # Remove duplicate literals (simplification 4) from the new clauses if there are any:
        new = simplify_4(new)
        # Remove duplicate clauses (that are equal) from the new list:
        new = remove_duplicates(new)
        # Check if the clauses learned are all contained in the knowledge base, when this happens, the solver reasoner
        # cannot gather additional information meaning the sentence is impossible to proven given the knowledge base.
        if contained(new, clauses):
            print("FALSE")  # We are not "learning" anything new...
            exit(-1)
        # Add the new information to the knowledge base:
        clauses.extend(new)
        # Remove duplicate clauses from the knowledge base:
        clauses = remove_duplicates(clauses)
        # Make all the 4 simplifications to the knowledge base to remove redundancy:
        clauses = simplify(clauses)
        # Sort all the clauses by lenght to prioritize the smaller ones (with less literals):
        clauses = sorted(clauses, key=len)


# Run the reasoner given a knowledge base:
theorem_prover(clauses)
